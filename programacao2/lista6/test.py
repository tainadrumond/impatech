# EXERCÍCIO 1
from lista import Graph, Vertex, bfs
def test_bfs():
    # Test Case 1: Basic graph with two connected vertices
    v1 = Vertex(1)
    v2 = Vertex(2)
    graph1 = Graph({v1: [v2], v2: []})
    assert bfs(graph1, v1) == [v1, v2]

    # Test Case 2: Graph with isolated vertex
    v3 = Vertex(3)
    graph2 = Graph({v1: [v2], v2: [], v3: []})
    assert bfs(graph2, v1) == [v1, v2]

    # Test Case 3: Graph with cycle
    v4 = Vertex(4)
    graph3 = Graph({v1: [v2], v2: [v1, v4], v4: [v2]})
    assert bfs(graph3, v1) == [v1, v2, v4]

    # Test Case 4: Larger graph with branching
    v5 = Vertex(5)
    v6 = Vertex(6)
    graph4 = Graph({v1: [v2, v3], v2: [v4], v3: [v5], v4: [v6], v5: [v6], v6: []})
    assert bfs(graph4, v1) == [v1, v2, v3, v4, v5, v6]

    # Test Case 5: Graph where all vertices are isolated
    graph5 = Graph({v1: [], v2: [], v3: []})
    assert bfs(graph5, v1) == [v1]

    print("All test cases passed!")

# Run tests
test_bfs()

# EXERCÍCIO 2
from lista import busca_propriedade
def test_busca_propriedade():
    # Test Case 1: Value found in a connected graph
    v1 = Vertex(1)
    v2 = Vertex(2)
    v3 = Vertex(3)
    v4 = Vertex(4)
    graph1 = Graph({v1: [v2, v3], v2: [v4], v3: [], v4: []})
    assert busca_propriedade(graph1, 4) == v4

    # Test Case 2: Value not found in the graph
    assert busca_propriedade(graph1, 5) is None

    # Test Case 3: Graph with isolated vertex
    v5 = Vertex(5)
    graph2 = Graph({v1: [v2, v3], v2: [v4], v3: [], v4: [], v5: []})
    assert busca_propriedade(graph2, 5) == v5

    # Test Case 4: Graph with a cycle
    v6 = Vertex(6)
    graph3 = Graph({v1: [v2], v2: [v3], v3: [v1, v4], v4: [v6], v6: []})
    assert busca_propriedade(graph3, 6) == v6

    # Test Case 5: Single vertex graph (vertex is the searched value)
    graph4 = Graph({v1: []})
    assert busca_propriedade(graph4, 1) == v1

    # Test Case 6: Single vertex graph (vertex is not the searched value)
    assert busca_propriedade(graph4, 10) is None

    print("All test cases passed!")

# Run tests
test_busca_propriedade()

# EXERCÍCIO 5
from lista import is_there_a_lake

def test_is_there_a_lake():
    # Teste 1: Lago presente no meio do mapa
    map_1 = [
        ['1', '1', '1', '1', '1'],
        ['1', '0', '0', '0', '1'],
        ['1', '0', '1', '0', '1'],
        ['1', '0', '0', '0', '1'],
        ['1', '1', '1', '1', '1']
    ]
    assert is_there_a_lake(map_1) == True, "Erro no Teste 1: Lago deveria estar presente"

    # Teste 2: Nenhum lago (área aberta para a borda)
    map_2 = [
        ['1', '1', '1', '1'],
        ['1', '0', '0', '1'],
        ['1', '0', '0', '0'],
        ['1', '1', '1', '1']
    ]
    assert is_there_a_lake(map_2) == False, "Erro no Teste 2: Nenhum lago deveria estar presente"

    # Teste 3: Múltiplos lagos (apenas um lago central)
    map_3 = [
        ['1', '1', '1', '1', '1', '1'],
        ['1', '0', '1', '0', '1', '1'],
        ['1', '1', '1', '1', '1', '1'],
        ['1', '0', '0', '0', '1', '1'],
        ['1', '1', '1', '1', '1', '1']
    ]
    assert is_there_a_lake(map_3) == True, "Erro no Teste 3: Deveria haver um lago central"

    # Teste 4: Mapa sem lagos (todo preenchido com '1')
    map_4 = [
        ['1', '1', '1'],
        ['1', '1', '1'],
        ['1', '1', '1']
    ]
    assert is_there_a_lake(map_4) == False, "Erro no Teste 4: Nenhum lago deveria estar presente"

    # Teste 5: Mapa sem lagos (todo preenchido com '0')
    map_5 = [
        ['0', '0', '0'],
        ['0', '0', '0'],
        ['0', '0', '0']
    ]
    assert is_there_a_lake(map_5) == False, "Erro no Teste 5: Nenhum lago deveria estar presente"

    # Teste 6: Mapa com lago mínimo de uma célula cercado
    map_6 = [
        ['1', '1', '1'],
        ['1', '0', '1'],
        ['1', '1', '1']
    ]
    assert is_there_a_lake(map_6) == True, "Erro no Teste 6: Lago de uma célula deveria estar presente"

    # Teste 7: Mapa com múltiplos "0" mas sem lagos cercados
    map_7 = [
        ['1', '1', '1', '1', '1'],
        ['1', '0', '1', '0', '1'],
        ['0', '0', '1', '1', '1'],
        ['1', '1', '0', '1', '1'],
        ['1', '1', '1', '1', '1']
    ]
    assert is_there_a_lake(map_7) == True, "Erro no Teste 7: Nenhum lago deveria estar presente"

    print("Todos os testes passaram!")

# Executar os testes
test_is_there_a_lake()

