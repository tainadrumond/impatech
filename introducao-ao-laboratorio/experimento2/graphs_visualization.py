import matplotlib.pyplot as plt

def generate_graph(x: list, y: list, nameX: str, nameY: str, graphTitle: str):
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

    plt.xlabel(nameX)
    plt.ylabel(nameY)

    plt.title(graphTitle)

    plt.show()
    
