from openpyxl import load_workbook

wb2 = load_workbook('QuestDump.xls')

print wb2.get_sheet_names()