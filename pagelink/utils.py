import matplotlib.pyplot as plt
import base64
from io import BytesIO

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer,format = 'png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(x,y,gname = 'Graph-x',xlable = 'x-axis',ylable = 'y-axis'):
    plt.switch_backend('AGG')
    plt.figure(figsize=(4,4))
    plt.title(gname)
    plt.plot(x,y)
    plt.xlabel(xlable)
    plt.ylabel(ylable)
    plt.tight_layout()
    graph =  get_graph()
    return graph



def get_histo_plot(x,gname = 'Graph-x',xlable = 'x-axis'):
    plt.switch_backend('AGG')
    plt.figure(figsize=(4,4))
    plt.title(gname)
    plt.hist(x)
    plt.xlabel(xlable)
    plt.tight_layout()
    graph =  get_graph()
    return graph

def get_pie_plot(x,gname = 'Graph-x',xlable = 'x-axis'):
    plt.switch_backend('AGG')
    plt.figure(figsize=(4,4))
    plt.title(gname)
    plt.pie(x)
    plt.xlabel(xlable)
    plt.tight_layout()
    graph =  get_graph()
    return graph
