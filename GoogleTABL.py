#NEZABYD PRO FAIL JSON (service_account.json) ПЕРЕИМЕНОВАННЫЙ
import gspread
sa = gspread.service_account(filename="service_account.json")

sh = sa.open("StudentsTest")

wks = sh.worksheet("list1")

#stroki
print('Rows: ', wks.row_count)
#stolbchi
print('Cols: ', wks.col_count)


#polychit znach yicheyki     ili
print(wks.acell('A4').value)
print(wks.cell(4, 1))


#obnovit yicheyky
wks.update('A4', 'yzii')

#ydalenie stroki
wks.delete_rows(3)

