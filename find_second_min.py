import xlrd
import numpy as np
import xlwt
from tempfile import TemporaryFile


book = xlwt.Workbook()
sheet1 = book.add_sheet('sheet1')

data=xlrd.open_workbook(r'C:\Users\Desktop\teamE\D1_route.xlsx')
table=data.sheets()[0]
all_data=[]
row_num=table.nrows
col_num=table.ncols

all_loc=[]

for i in range(table.nrows):
    every_row=table.row_values(i)
    all_data.append(every_row)
new_all_data=np.array(all_data)

data_try=new_all_data.flatten()
data_try1=sorted(data_try)

for l in range(len(data_try1)):
    j = 1
    order_min=data_try1[l]
    loca=np.where(new_all_data==order_min)
    all_data_for_choose=new_all_data
    sheet1.write(l, 0, order_min)
    while j<12:

        #all_loc.append([loca[0][0],loca[1][0]])
        change1=np.delete(all_data_for_choose,[loca[0][0],loca[1][0]],0)
        change2=np.delete(change1,[loca[0][0],loca[1][0]],1)
        dis = np.min(change2)
        all_data_for_choose = change2
        loca = np.where(all_data_for_choose == dis)


        sheet1.write(l, j, dis)
        j+=1

name = "find_route_sensitivity_D1.xls"
book.save(name)
book.save(TemporaryFile())


