from os import path
import openpyxl


async def file_read(data):
    try:
        file_path = path.join(path.dirname(__file__), "person.xlsx")
        wb = openpyxl.load_workbook(file_path)
        sheet = wb.active
        for row in data:
            sheet.append(row)
        wb.save(file_path)
        return True
    except Exception as err:
        print(err)
