import xlrd


def read_excel(name):
    ExcelFile = xlrd.open_workbook('team-roster.xlsx')
    sheet1 = ExcelFile.sheet_by_index(0)
    cols = sheet1.col_values(0)
    counter = 0
    for names in iter(cols):
        if name == names:
            data = sheet1.row_values(counter)
            print(data)
        else:
            counter += 1


if __name__ == '__main__':
    name = input('请输入姓名(例如Tom, Rust): ')
    read_excel(name)

import os


# path1 = os.path.dirname(os.getcwd())
# print(path1)
# wb = xlrd.open_workbook(filename="./xlrd.xlsx")