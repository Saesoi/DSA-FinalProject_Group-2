import networkx as nx
import matplotlib.pyplot as plt
from flask import Flask, render_template, request

app = Flask(__name__)

# MRT stations and connections (just an example)
stations = {
    "Boni": ["Shaw", "Pioneer"],
    "Shaw": ["Boni", "Mandaluyong", "Ortigas"],
    "Pioneer": ["Boni", "Mandaluyong"],
    "Mandaluyong": ["Shaw", "Pioneer", "Ortigas", "Bonifacio"],
    "Ortigas": ["Shaw", "Mandaluyong", "Santolan"],
    "Santolan": ["Ortigas", "Bonifacio"],
    "Bonifacio": ["Mandaluyong", "Santolan", "Cubao"],
    "Cubao": ["Bonifacio"]
}

# Create a graph
G = nx.Graph()

# Add edges to the graph
for station, connections in stations.items():
    for connection in connections:
        G.add_edge(station, connection)

@app.route('/')
def index():
    return render_template('graph.html')

@app.route('/shortest_path', methods=['POST'])
def shortest_path():
    start = request.form['start']
    end = request.form['end']
    
    try:
        # Calculate the shortest path
        path = nx.shortest_path(G, source=start, target=end)
        return render_template('graph.html', path=path, start=start, end=end)
    except nx.NetworkXNoPath:
        return render_template('graph.html', path=None, start=start, end=end, error="No path found!")

def plot_graph():
    plt.figure(figsize=(8, 6))
    nx.draw(G, with_labels=True, node_color='skyblue', font_size=12, node_size=2000, font_weight='bold')
    plt.savefig('static/mrt_graph.png')  # Save the graph as an image

if __name__ == '__main__':
    plot_graph()  # Plot and save the graph image
    app.run(debug=True, port=5006)  # Run on port 5006
