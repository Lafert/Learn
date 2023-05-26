import os
import xlsxwriter
from main import array

def writer(parametrs):
    current_dir = os.getcwd()

    # Создание пути к файлу данных
    file_path = os.path.join(current_dir, 'data.xlsx')

    book = xlsxwriter.Workbook(file_path)
    page = book.add_worksheet('good')

    row = 0
    colum = 0

    page.set_column('A:A', 20)
    page.set_column('B:B', 20)
    page.set_column('C:C', 50)
    page.set_column('D:D', 50)

    for item in parametrs():
        page.write(row, colum, item[0])
        page.write(row, colum+1, item[1])
        page.write(row, colum+2, item[2])
        page.write(row, colum+3, item[3])
        row+=1
    book.close()

writer(array)