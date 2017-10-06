import xlrd
import numpy as np
import xlwt
from tempfile import TemporaryFile


book = xlwt.Workbook()
sheet1 = book.add_sheet('sheet1')

for id,i in enumerate(load_name):
    data=xlrd.open_workbook(i)
    table=data.sheets()[0]
    all_data=[]
    row_num=table.nrows
    col_num=table.ncols

    j=1
    for s in range(table.nrows):
        every_row=table.row_values(s)
        all_data.append(every_row)
    new_all_data=np.array(all_data)
    loca = np.where(new_all_data == np.min(new_all_data))
    sheet1.write(id, 0, np.min(new_all_data))
    all_data_for_choose=new_all_data
    while j<12:

        #all_loc.append([loca[0][0],loca[1][0]])
        change1=np.delete(all_data_for_choose,[loca[0][0],loca[1][0]],0)
        change2=np.delete(change1,[loca[0][0],loca[1][0]],1)
        dis = np.min(change2)
        all_data_for_choose = change2
        loca = np.where(all_data_for_choose == dis)


        sheet1.write(id, j, dis)
        j+=1

name = 'distance.xls'
book.save(name)
book.save(TemporaryFile())


