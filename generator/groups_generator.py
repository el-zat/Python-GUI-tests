from comtypes.client import CreateObject
import os.path


n = 5
f = "fixture/groups.xlsx"

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

xl = CreateObject("Excel.Application")
xl.Visible = 1
wb = xl.Workbooks.Add()
for i in range(n):
    xl.Range["A%s" % (i+1)].Value[()] = "group %s" % i
wb.SaveAs(os.path.join(file))
xl.Quit()



