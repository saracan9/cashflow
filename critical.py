import networkx as nx
import matplotlib.pyplot as plt

# Yardımcı: float karşılaştırma
def is_close(a, b, tol=1e-6):
    return abs(a - b) < tol

# Görevler ve süreler
edges = [
    ("A", "B", 4),
    ("B", "C", 5),
    ("C", "D", 2),
    ("D", "K", 3),
    ("K", "E", 7),
    ("B", "F", 5),
    ("F", "G", 4),
    ("G", "H", 5),
    ("H", "E", 4),
    ("F", "I", 8),
    ("G", "J", 3),
    ("J", "L", 2),
    ("L", "E", 2)
]

# Ağı oluştur
G = nx.DiGraph()
for u, v, w in edges:
    G.add_edge(u, v, weight=w)

# FORWARD PASS (ES, EF)
topo_order = list(nx.topological_sort(G))
ES = {n: 0 for n in topo_order}
EF = {}
for u in topo_order:
    for v in G.successors(u):
        ES[v] = max(ES[v], ES[u] + G[u][v]['weight'])
for u in topo_order:
    EF[u] = ES[u] + max([G[u][v]['weight'] for v in G.successors(u)] or [0])

# BACKWARD PASS (LF, LS)
max_ef = max(EF.values())
LF = {n: max_ef for n in reversed(topo_order)}
LS = {}
for u in reversed(topo_order):
    for v in G.successors(u):
        LF[u] = min(LF[u], LF[v] - G[u][v]["weight"])
for u in topo_order:
    LS[u] = LF[u] - max([G[u][v]['weight'] for v in G.successors(u)] or [0])

# Kenar slack hesaplayarak kritik kenarlar belirle
critical_edges = []
for u, v in G.edges():
    dur = G[u][v]["weight"]
    slack = LS[v] - ES[u] - dur
    if is_close(slack, 0):
        critical_edges.append((u, v))

# POZİSYONLAR ve çizim
pos = nx.shell_layout(G)
plt.figure(figsize=(15, 8))

# Düğümler (sadece harf)
nx.draw_networkx_nodes(G, pos, node_color="mediumpurple", node_size=2000)
nx.draw_networkx_labels(G, pos, labels={n: n for n in G.nodes()}, font_size=11, font_color="white", font_weight="bold")

# Kenarlar ve renk
edge_colors = ["red" if (u, v) in critical_edges else "black" for u, v in G.edges()]
nx.draw_networkx_edges(G, pos, edge_color=edge_colors, width=2.5, arrows=True)

# Kenar etiketleri: ES/EF üstte, LS/LF altta
for u, v in G.edges():
    x1, y1 = pos[u]
    x2, y2 = pos[v]
    xm, ym = (x1 + x2) / 2, (y1 + y2) / 2

    # ÜSTTE: ES, EF
    plt.text(xm, ym + 0.06, f"ES:{ES[u]} EF:{EF[u]}", fontsize=8, ha="center", color="navy")

    # ALTA: LS, LF
    plt.text(xm, ym - 0.06, f"LS:{LS[u]} LF:{LF[u]}", fontsize=8, ha="center", color="darkgreen")

# Kenar süreleri (süre)
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

plt.title("📌 Critical Path with ES/EF (top) and LS/LF (bottom)", fontsize=14)
plt.axis("off")
plt.tight_layout()
plt.show()
