# ============================================
# NETWORK TOPOLOGY DIAGRAM
# Author: [Ton Prénom]
# Stack: Python, Plotly, Networkx
# ============================================

import plotly.graph_objects as go
import math

# ============================================
# NODES
# ============================================
nodes = {
    'Internet':   (0,    4.5,  '🌐', '#94a3b8'),
    'R1':         (0,    3.5,  '🔴', '#ef4444'),
    'R2':         (3,    2.5,  '🔴', '#ef4444'),
    'SW-CORE':    (0,    2.5,  '🟡', '#f59e0b'),
    'SW1':        (-3,   1.5,  '🔵', '#00d4ff'),
    'SW2':        (-1,   1.5,  '🔵', '#00d4ff'),
    'SW3':        (1,    1.5,  '🔵', '#00d4ff'),
    'SW4':        (3,    1.5,  '🔵', '#00d4ff'),
    'VLAN10\nAdmin':     (-3,   0.5,  '🟢', '#10b981'),
    'VLAN20\nDev':       (-1,   0.5,  '🟢', '#10b981'),
    'VLAN30\nRH':        (1,    0.5,  '🟢', '#10b981'),
    'VLAN40\nDirection': (3,    0.5,  '🟢', '#10b981'),
}

edges = [
    ('Internet', 'R1'),
    ('R1', 'SW-CORE'),
    ('R1', 'R2'),
    ('SW-CORE', 'SW1'),
    ('SW-CORE', 'SW2'),
    ('SW-CORE', 'SW3'),
    ('R2', 'SW4'),
    ('SW1', 'VLAN10\nAdmin'),
    ('SW2', 'VLAN20\nDev'),
    ('SW3', 'VLAN30\nRH'),
    ('SW4', 'VLAN40\nDirection'),
]

edge_x, edge_y = [], []
for src, dst in edges:
    x0, y0, *_ = nodes[src]
    x1, y1, *_ = nodes[dst]
    edge_x += [x0, x1, None]
    edge_y += [y0, y1, None]

node_x     = [v[0] for v in nodes.values()]
node_y     = [v[1] for v in nodes.values()]
node_labels = list(nodes.keys())
node_colors = [v[3] for v in nodes.values()]
node_icons  = [v[2] for v in nodes.values()]

# ============================================
# FIGURE
# ============================================
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=edge_x, y=edge_y,
    mode='lines',
    line=dict(width=2, color='rgba(148,163,184,0.4)'),
    hoverinfo='none'
))

fig.add_trace(go.Scatter(
    x=node_x, y=node_y,
    mode='markers+text',
    marker=dict(size=40, color=node_colors, opacity=0.9,
                line=dict(width=2, color='white')),
    text=[f"{icon}\n{label}" for icon, label in
          zip(node_icons, node_labels)],
    textposition='middle center',
    textfont=dict(size=9, color='white'),
    hovertemplate='<b>%{text}</b><extra></extra>'
))

# Annotations IP
ip_labels = {
    'R1':      '10.0.0.1 / 203.0.113.1',
    'R2':      '10.0.0.6',
    'SW-CORE': '192.168.x.1 (SVI)',
    'SW1':     '192.168.99.11',
}
for node, ip in ip_labels.items():
    x, y, *_ = nodes[node]
    fig.add_annotation(
        x=x, y=y - 0.3,
        text=f"<i>{ip}</i>",
        showarrow=False,
        font=dict(size=8, color='#94a3b8')
    )

fig.update_layout(
    title=dict(
        text='🖧 Infrastructure Réseau — Packet Tracer 2023',
        font=dict(size=22, color='#e2e8f0', family='Inter'),
        x=0.5, xanchor='center'
    ),
    paper_bgcolor='#0a0e1a',
    plot_bgcolor='#0a0e1a',
    font=dict(color='#e2e8f0'),
    height=700,
    showlegend=False,
    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    margin=dict(t=80, b=20, l=20, r=20)
)

fig.write_html("diagrams/topology_diagram.html")
fig.write_image("diagrams/topology_diagram.png", width=1200, height=700, scale=2)
print("✅ Topology diagram exporté !")
