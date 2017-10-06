import plotly
import plotly.graph_objs as go
import plotly.plotly as py
import networkx as nx
import h5py
import matplotlib.pyplot as plt
from random import randint
import scipy.io as sio
import numpy as np

f = r'C:\Users\Desktop\teamE\DATAA.mat'
data = sio.loadmat(f)
A = data['A']

G = nx.MultiGraph()
# for i in range(3):
# G.add_node(i)
for i in range(len(A)):
    for j in range(i, len(A)):
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

Dn_for_J=[]
X=[]
Y=[]
for k in range(8,68):
    all_dis = []
    for l in range(0,2):
        distance = nx.dijkstra_path_length(G, source=k, target=l)
        all_dis.append(distance)
    D_number=all_dis.index(min(all_dis))+1
    F=pos[k]
    X.append(F[0])
    Y.append(F[1])
    Dn_for_J.append(D_number)


plotly.tools.set_credentials_file(username='tjzxh', api_key='r2F9Tbql2xiZLWzFLRJ6')
trace1 = go.Scatter(
    x=X,
    y=Y,
    mode='markers',
    marker=dict(
        size='16',
        color = Dn_for_J, #set color equal to a variable
        colorscale='Viridis',
        showscale=True
    )
)
data = [trace1]

py.iplot(data, filename='zone_number')