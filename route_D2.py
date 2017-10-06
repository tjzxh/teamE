import xlrd
import numpy as np
import networkx as nx
import scipy.io as sio
import xlwt
from tempfile import TemporaryFile

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

Z1=xlrd.open_workbook(r'C:\Users\小卉\Desktop\teamE\Z_D2.xlsx')
table1=Z1.sheets()[0]

data=xlrd.open_workbook(r'C:\Users\Desktop\teamE\D2_route.xlsx')
table=data.sheets()[0]
all_data=[]
row_num=table.nrows
col_num=table.ncols
j=0
all_loc=[]
for i in range(table.nrows):
    every_row=table.row_values(i)
    all_data.append(every_row)

new_all_data=np.array(all_data)
loca=np.where(new_all_data==np.min(new_all_data))
loca_for_route=loca
all_loc.append([loca_for_route[0][0],loca_for_route[1][0]])
all_data_for_choose=new_all_data

while j<11:


    change1=np.delete(all_data_for_choose,[loca[0][0],loca[1][0]],0)
    change2=np.delete(change1,[loca[0][0],loca[1][0]],1)
    dis = np.min(change2)
    all_data_for_choose = change2
    loca = np.where(all_data_for_choose == dis)
    loca_for_route=np.where(new_all_data==dis)
    #all_loc.append([loca[0][0], loca[1][0]])
    all_loc.append([loca_for_route[0][0],loca_for_route[1][0]])
    j+=1
#print(all_loc)
all_route=[]
standard_id=[8,9,10,11,12,13,14,15,16,17,18,19,20,31,32,33,34,35,36,37,51,52,53,54,55,56,57,58,59,60,62,63]
for k in all_loc:
    id0=k[0]
    id1=k[1]
    z_id=table1.cell(id0,id1).value
    every_route=[1,standard_id[id0],z_id+1,standard_id[id1]]#for D2,standard number is 1
    path0 = nx.dijkstra_path(G, source=every_route[0], target=every_route[1])
    path1=nx.dijkstra_path(G,source=every_route[1],target=every_route[2])
    path2=nx.dijkstra_path(G,source=every_route[2],target=every_route[3])
    node_route=path0+path1[1:len(path1)-1]+path2
    node_route=np.array(node_route)
    comple_route=list(node_route.flatten())
    all_route.append(comple_route)
print(all_route)

name=['D1','D2','Z01','Z02','Z03','Z04','Z05','Z06','F01','F02','F03','F04','F05','F06','F07','F08','F09','F10','F11','F12','F13','F14','F15','F16','F17','F18','F19','F20','F21','F22','F23','F24','F25','F26','F27','F28','F29','F30','F31','F32','F33','F34','F35','F36','F37','F38','F39','F40','F41','F42','F43','F44','F45','F46','F47','F48','F49','F50','F51','F52','F53','F54','F55','F56','F57','F58','F59','F60','J01','J02','J03','J04','J05','J06','J07','J08','J09','J10','J11','J12','J13','J14','J15','J16','J17','J18','J19','J20','J21','J22','J23','J24','J25','J26','J27','J28','J29','J30','J31','J32','J33','J34','J35','J36','J37','J38','J39','J40','J41','J42','J43','J44','J45','J46','J47','J48','J49','J50','J51','J52','J53','J54','J55','J56','J57','J58','J59','J60','J61','J62'
]

book = xlwt.Workbook()
sheet1 = book.add_sheet('sheet1')

for s,r in enumerate(all_route):
    for i,d in enumerate(r):
        sheet1.write(s, i, d)

name = "node_D2.xls"
book.save(name)
book.save(TemporaryFile())




