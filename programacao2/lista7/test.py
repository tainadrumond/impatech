import unittest
from collections import deque, defaultdict
import matplotlib.pyplot as plt
import networkx as nx

def calculate_distances(points) -> dict[tuple[int, int], float]:
    '''
    Calculate the distances between each point of the given list
    '''
    distances: dict[tuple[int, int], float] = dict()
    
    for i, pi in enumerate(points):
        for j in range(i+1, len(points)):
            pj = points[j]
            if pi[0] == pj[0] and pi[1] == pj[1]:
                continue
            edge = (pi, pj)
            distance = ((pi[0] - pj[0])**2 + (pi[1] - pj[1])**2)**(1/2)
            distances[edge] = distance
    return distances

def nodes_are_connected(node1, node2, adj_list):
    '''
    Bfs to check if two nodes are connected
    '''
    queue = deque([node1])
    visited = set([node1])
    
    while len(queue) != 0:
        node = queue.popleft()
        
        for neighbor in adj_list[node]:
            if neighbor == node2:
                return True
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return False
        
        
def minimum_spanning_tree(points: list[tuple]):
    '''
    Calculate minimum spanning tree for the given list of points
    '''
    # Remover pontos duplicados
    points = list(set(points))

    adj_list: dict[tuple, list[tuple]] = defaultdict(list)
    distances = calculate_distances(points)
    edges_ordered_by_distance = sorted(distances.items(), key=lambda item: item[1])

    for edge, distance in edges_ordered_by_distance:
        node1, node2 = edge
        if not nodes_are_connected(node1, node2, adj_list):
            adj_list[node1].append(node2)
            adj_list[node2].append(node1)

    return adj_list


class TestMinimumSpanningTree(unittest.TestCase):

    def assert_graph_equal(self, graph1, graph2):
        self.assertEqual(len(graph1), len(graph2))
        for key in graph1:
            self.assertIn(key, graph2)
            # Comparando as listas de arestas de forma não ordenada
            self.assertEqual(set(graph1[key]), set(graph2[key]))

    def test_case_1(self):
        points = [(0, 0), (1, 0), (0, 1)]
        expected_mst = {
            (0, 0): [(1, 0), (0, 1)],
            (1, 0): [(0, 0)],
            (0, 1): [(0, 0)],
        }
        mst = minimum_spanning_tree(points)
        self.assert_graph_equal(mst, expected_mst)

    def test_case_2(self):
        points = [(0, 0), (1, 0), (0, 1), (-1, 0), (0, -1)]
        expected_mst = {
            (0, 0): [(1, 0), (0, 1), (-1, 0), (0, -1)],
            (1, 0): [(0, 0)],
            (0, 1): [(0, 0)],
            (-1, 0): [(0, 0)],
            (0, -1): [(0, 0)],
        }
        mst = minimum_spanning_tree(points)
        self.assert_graph_equal(mst, expected_mst)

    def test_case_3(self):
        points = [(0, 0), (0, 0), (0, 0)]
        expected_mst = {}
        mst = minimum_spanning_tree(points)
        self.assert_graph_equal(mst, expected_mst)

    def test_case_4(self):
        points = [(0, 0), (1, 0), (0, 1), (1, 1)]
        expected_mst = {
            (0, 0): [(1, 0), (0, 1)],
            (1, 0): [(0, 0), (1, 1)],
            (0, 1): [(0, 0), (1, 1)],
            (1, 1): [(1, 0), (0, 1)],
        }
        mst = minimum_spanning_tree(points)
        self.assert_graph_equal(mst, expected_mst)

    def test_case_5(self):
        points = [(0, 0), (2, 0), (0, 2), (2, 2), (3, 3)]
        expected_mst = {
            (0, 0): [(2, 0), (0, 2)],
            (2, 0): [(0, 0), (2, 2)],
            (0, 2): [(0, 0), (2, 2)],
            (2, 2): [(2, 0), (0, 2), (3, 3)],
            (3, 3): [(2, 2)],
        }
        mst = minimum_spanning_tree(points)
        self.assert_graph_equal(mst, expected_mst)


def plot_mst(points, mst):
    G = nx.Graph()
    for point in points:
        G.add_node(point)
    for node1, neighbors in mst.items():
        for node2 in neighbors:
            G.add_edge(node1, node2)
    
    pos = {node: node for node in points}  # Organizar os pontos para a plotagem
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_weight="bold", edge_color="gray")
    plt.show()

def test_plot_case_1():
    points = [(0, 0), (1, 0), (0, 1)]
    mst = minimum_spanning_tree(points)
    plot_mst(points, mst)

def test_plot_case_2():
    points = [(0, 0), (1, 0), (0, 1), (-1, 0), (0, -1)]
    mst = minimum_spanning_tree(points)
    plot_mst(points, mst)

def test_plot_case_3():
    points = [(0, 0), (0, 0), (0, 0)]
    mst = minimum_spanning_tree(points)
    plot_mst(points, mst)

def test_plot_case_4():
    points = [(0, 0), (1, 0), (0, 1), (1, 1)]
    mst = minimum_spanning_tree(points)
    plot_mst(points, mst)

def test_plot_case_5():
    points = [(0, 0), (2, 0), (0, 2), (2, 2), (3, 3)]
    mst = minimum_spanning_tree(points)
    plot_mst(points, mst)

# Chamar as funções para visualizar os casos de teste
if __name__ == '__main__':
    unittest.main()  # Executa os testes unitários
    test_plot_case_1()
    test_plot_case_2()
    test_plot_case_3()
    test_plot_case_4()
    test_plot_case_5()
