
import os
import xlrd


def fileHandler(path:str):
    """
    path: Path of the excel file
    """
    book = xlrd.open_workbook(path)
    excel = book.sheet_by_index(0)
    col = excel.ncols
    row = excel.nrows
    for i in range(0, row):
        alp = excel.cell_value(0, i)
        a = alp.lower
        if (a != "name") or (a!="usn" or (a!="sem") or (a!="gender") or (a!="marks1") or (a!="marks2") or (a!="marks3")):
            return False
    i, j = 0, 0
    data = []
    for i in range(1,row):
        for j in range(1, col):
            data[i-1][j-1] = excel.cell_value(i, j) # (row, col) -> row: --, col: |
    
    try:
        os.remove(path)
    except:
        pass

    return data


