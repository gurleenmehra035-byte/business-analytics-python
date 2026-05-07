#GURLEEN 12514824
import matplotlib.pyplot as plt
import networkx as nx

# Create directed graph
G = nx.DiGraph()

# Add nodes
G.add_edges_from([
    ("FinancialStrength", "TotalAssets"),
    ("TAD", "TotalAssets"),
    ("FSxTAD", "TotalAssets")
])

# Position nodes manually
pos = {
    "FinancialStrength": (0, 1),
    "TAD": (0, 0),
    "FSxTAD": (0, -1),
    "TotalAssets": (2, 0)
}

# Draw
plt.figure(figsize=(6, 4))
nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=3500,
    node_color="lightgray",
    font_size=10,
    arrowsize=20
)

plt.title("SEM with TAD as Moderating Variable")
plt.show()