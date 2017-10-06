import networkx as nx
import scipy.io as sio
import plotly.plotly as py
import plotly
from plotly.graph_objs import *
import xlrd
import numpy as np
import plotly.graph_objs as go

plotly.tools.set_credentials_file(username='tjzxh', api_key='r2F9Tbql2xiZLWzFLRJ6')

f = r'C:\Users\Desktop\teamE\DATAA.mat'
data = sio.loadmat(f)
A = data['A']

data=xlrd.open_workbook(r'C:\Users\Desktop\teamE\all_nodes_subgraph.xls')
table=data.sheets()[0]
all_route=[]
row_num=table.nrows
col_num=table.ncols

for i in range(table.nrows):
    every_row=table.row_values(i)
    all_route.append(every_row)

G = nx.Graph()
# for i in range(3):
# G.add_node(i)
for i in range(len(A)):
    for j in range(i, len(A)):
        if A[i,j]!=100000:
            G.add_weighted_edges_from([(i, j, A[i, j])])

pos = [(121, 8), (193, 137), (205, 92), (159, 62), (143, 38), (108, 80), (55, 38), (62, 105), (135, 142),
       (127, 143), (124, 129), (115, 130), (105, 130), (108, 145), (90, 145), (72, 142), (60, 139), (70, 121),
       (100, 121), (53, 132), (37, 127), (25, 120), (15, 115), (7, 105), (28, 106), (24, 90), (45, 90), (49, 82),
       (16, 76), (15, 70), (14, 56), (168, 126), (165, 117), (165, 105), (145, 113), (132, 100), (130, 94),
       (130, 80), (110, 100), (114, 90), (95, 90), (95, 77), (106, 63), (86, 75), (72, 70), (74, 60), (79, 53),
       (68, 46), (46, 20), (59, 15), (77, 5), (240, 127), (240, 107), (230, 100), (220, 98), (158, 77), (176, 75),
       (206, 77), (184, 62), (215, 62), (227, 64), (206, 46), (231, 49), (232, 37), (148, 15), (170, 17), (201, 22),
       (224, 20), (237, 137), (232, 127), (204, 119), (188, 100), (168, 94), (143, 74), (117, 67), (122, 48),
       (108, 38), (102, 23), (99, 3), (170, 145), (150, 133), (140, 120), (105, 108), (85, 92), (63, 73), (53, 57),
       (37, 41), (18, 37), (130, 135), (110, 139), (93, 138), (66, 132), (86, 122), (49, 123), (18, 108), (37, 91),
       (44, 74), (24, 75), (23, 57), (175, 132), (175, 115), (155, 105), (140, 105), (137, 87), (106, 94),
       (102, 72), (77, 79), (83, 65), (58, 47), (93, 45), (33, 29), (58, 24), (80, 30), (80, 13), (234, 118),
       (220, 110), (168, 83), (193, 78), (149, 68), (143, 55), (195, 60), (164, 50), (183, 50), (221, 54),
       (165, 40), (178, 33), (196, 39), (226, 43), (160, 18), (214, 23)]

edge_trace = Scatter(
    x=[],
    y=[],
    line=Line(width=0.5,color='#888'),
    hoverinfo='none',
    mode='lines')

for edge in G.edges():
    point0=pos[edge[0]]
    point1=pos[edge[1]]
    x0=point0[0]
    y0=point0[1]
    x1=point1[0]
    y1=point1[1]
    edge_trace['x'] += [x0, x1, None]
    edge_trace['y'] += [y0, y1, None]

node_trace = Scatter(
    x=[],
    y=[],
    text=[],
    mode='markers',
    hoverinfo='text',
    marker=Marker(
        showscale=True,
        # colorscale options
        # 'Greys' | 'Greens' | 'Bluered' | 'Hot' | 'Picnic' | 'Portland' |
        # Jet' | 'RdBu' | 'Blackbody' | 'Earth' | 'Electric' | 'YIOrRd' | 'YIGnBu'
        colorscale='Electric',
        reversescale=True,
        color=[],
        size=10,
        colorbar=dict(
            thickness=15,
            title='Node Clustering Coefficient',
            xanchor='left',
            titleside='right'
        ),
        line=dict(width=2)))



for i in range(len(pos)):
    point=pos[i]
    x = point[0]
    y = point[1]
    node_trace['x'].append(x)
    node_trace['y'].append(y)
    clust_index = nx.clustering(G)
    for i in clust_index.keys():
        s=clust_index.get(i, 'not exist')
        node_trace['marker']['color'].append(s)


data=Data([edge_trace, node_trace])

py.iplot(data, filename='cluster_G')