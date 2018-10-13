
#----------------------------------------------------#
#-                                                  -#
#-                Bogdan Polvanov                   -#
#-                 Project Euler                    -#
#-                    Task_26                       -#
#-                                                  -#
#----------------------------------------------------#

import time
import xlrd
from openpyxl import Workbook
from openpyxl import load_workbook

start = time.time()
#-------------------- working space ---------------------


book = xlrd.open_workbook("proper.xlsx")

first_sheet = book.sheet_by_index(0)

for n in range(1,524):
    stan = first_sheet.row_values(n)# відкриваємо кожний рядок book
    if stan[0] == 'd->a'and stan[1] == '1->2':
        print(stan)
    if stan[0] == 'n->c'and stan[1] == '0->1':
        print(stan)
    if stan[0] == 'G->C' and stan[1] == '1->1':
        print(stan)
    if stan[0] == 'R->C' and stan[1] == '0->1':
        print(stan)
        





    

#-------------------    end    ---------------------
end = time.time()
print('time work - ',end - start)



