import pygsheets
from pygsheets.datarange import DataRange
import webcolors as colors

# -- connect to google 
client = pygsheets.authorize(service_file='nicolasgsheets-servicefile.json')

# -- get the spreadsheet
spreadsheet_id = '1uxM0qPz6htYM_pF7JQ2-Qwp72tc1WHF5iTsWYKkzUEk'
spreadsheet = client.open_by_key(spreadsheet_id)

# -- get the working sheet
sheet = spreadsheet.worksheet_by_title('Dashboard')

# -- working sheet info
print(f'WorkSheet : {sheet.title}  size: ({sheet.rows}x{sheet.cols})')

# -- update values in wks
sheet.update_value('A1', '20')
sheet.update_value('B1', '30')
sheet.update_value('C1', '=A1+B1')

# -- setting validaton on a cell
sheet.set_data_validation(start="C2", end="C2", condition_type='ONE_OF_LIST', condition_values=['One', 'Two'], showCustomUi='True')

# -- change cell color
cellB6 = sheet.cell('B6')
c1, c2, c3 = colors.hex_to_rgb("#4285f4")
cellB6.color = (c1/255, c2/255, c3/255, 0.9) # color is a tuple (red, green, blue, alpha) of float values

# -- change row color
row10 = DataRange(f'A10', 'Z10', worksheet=sheet) # or row10 = sheet.get_row(10, returnas = "range")
row10.apply_format(cellB6)

# -- formating column text