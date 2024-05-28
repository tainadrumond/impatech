import matplotlib.pyplot as plt
import numpy as np

def generate_points_graph(x: list, y: list, nameX: str, nameY: str, graphTitle: str):
    '''
    input:
        x: list of floats for the horizontal axis
        y: list of floats for the vertical axis
        nameX: str for the name of the horizontal axis
        nameY: str for the name of the vertical axis
        graphTitle: str for the name of the graph
    output:
        displays the graph for the input info
    '''
    plt.plot(x, y)
    plt.grid(True)

    plt.xlabel(nameX)
    plt.ylabel(nameY)

    plt.title(graphTitle)

    plt.show()

def generate_multiple_points_graph(graphs_config: list, graph_title: str, label_x: str):
    '''
    input:
        graphs_config: array with the dictionary configuration of the
        to be shown on the same image
            - keys expected in the dictionary:
                x: list of floats for the horizontal axis
                y: list of floats for the vertical axis
                name_x: str for the name of the horizontal axis
                name_y: str for the name of the vertical axis
    output:
        displays the graph for the input info
    '''
    number_of_graphs = len(graphs_config)
    # figure, graphs = plt.subplots(number_of_graphs)
    
    for i in range(number_of_graphs):
        graph_config = graphs_config[i]
        plt.plot(graph_config['x'], graph_config['y'], label=graph_config['label'])
        # graphs[i].plot(graph_config['x'], graph_config['y'])

        # graphs[i].set_xlabel(graph_config['name_x'])
        # graphs[i].set_ylabel(graph_config['name_y'])

    plt.grid(True)
    plt.title(graph_title)
    plt.xlabel(label_x)
    plt.legend()

    plt.tight_layout()
    plt.show()

def generate_polynomial_graph(coeficients: list,  nameX: str, nameY: str, graphTitle: str, x_zero):
    x = np.linspace(0.45, 0, 600)
    y = np.polyval(coeficients, (x + x_zero))
    generate_points_graph(x, y, nameX, nameY, graphTitle)
    
    
