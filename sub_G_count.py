import xlrd
import numpy as np
import networkx as nx
import scipy.io as sio
import xlwt
from tempfile import TemporaryFile
import matplotlib.pyplot as plt

f = r'C:\Users\Desktop\teamE\DATAA.mat'
data = sio.loadmat(f)
A = data['A']

data=xlrd.open_workbook(r'C:\Users\Desktop\teamE\all_nodes_subgraph.xls')
table=data.sheets()[0]
all_route=[]
row_num=table.nrows
col_num=table.ncols

for i in range(table.nrows):
    every_row=list(filter(None,table.row_values(i)))
    for j in every_row:
        all_route.append(j)
all_route=sorted(all_route)
book = xlwt.Workbook()
sheet1 = book.add_sheet('sheet1')
j=0
have_counted=[]
for r in all_route:
    if r in have_counted:
        pass
    else:
        sheet1.write(j,0,r)
        sheet1.write(j, 1, all_route.count(r))
        j += 1
    have_counted.append(r)

name = "count_point_subG.xls"
book.save(name)
book.save(TemporaryFile())

