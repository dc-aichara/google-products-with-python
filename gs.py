"""
Python can be used to automate Google Sheets.  Read Medium article for detailed information:
https://medium.com/@dc.aichara/play-with-google-spreadsheets-with-python-301dd4ee36eb

Before you start
1. Install pygsheets python package
2. Obtain OAuth2 credentials from Google Developers Console for google spreadsheet api and drive api
   and save the file as client_secret.json in same directory as project
"""

import pygsheets

gc = pygsheets.authorize()
# Use customized credentials
gc = pygsheets.authorize(custom_credentials=my_credentials)
# For the first time, it will may produce as a link to authorize


#  Open spreadsheet

# 1. Open spreadsheet by name
sh = gc.open('google spreadsheet name') # open spreadsheet

# 2. Open spreadsheet by key
sh = gc.open_by_key('spreadsheet_key')

# 3. Open spredhseet by link
sh.open_by_link('spreadsheet link)

# Open worksheet

wk1 = sh[0] Open first worksheet of spreadsheet
# Or
wk1 = sh.sheet1 # sheet1 is name of first worksheet

""" First worksheet has index 0, second has index 1, so on. 
Instead of index, you can use worksheet name. 
"""

# Get spreadsheet title

sh.id     # Returns id of spreadsheet

# Get spreadsheet id

sh.title      # Returns title of spreadsheet

# Get spreadsheet url

sh.url     # Returns url of spreadsheet

# Check last update

sh.updated  # Returns date and time of last update

# Delete spreadsheet

sh.delete() # Delete spreadsheet

# Get worksheets info

sh.worksheets() # Return information of worksheets

# Share spreadsheet

sh.share('example@gmail.com', role='commenter', type='user', emailMessage='Here is the spreadsheet we talked about!')
sh.share('', role='reader', type='anyone') # Make public

# Remove permissions

sh.remove_permission('example@gmail.com', permission_id=None)
# You can specify permission id

# Add new worksheet

sh.add_worksheet('sheet3',rows=250, cols=20)

# Delete worksheet

sh.del_worksheet('sheet3')

#                               Playing around Worksheet
#  Open a worksheet

wk1 = sh.sheet1 or wk1 =sh[0] # Open first worksheet


# Get title, id, and url of worksheet

wk1.title       # Returns title of worksheet
wk1.id          # Returns id of worksheet
wk1.url         # Returns url of worksheet

# Get rows and cols count

wk1.rows # returns number of rows
wk1.cols # returns number of columns

# Get cell object and cell value

wk1.cell((row_number,col_number))       # Returns cell object
wk1.cell((row_number,col_number)).value # Returns cell value as string

#Get value/values/records

wk1.get_value('A1')        # Returns A1’s value
wk1.get_value('A1', 'B2')  # Returns list of values
wk1.get_all_values()       # Returns list of all values in worksheet
wk1.get_all_records()      # Returns a list of dictionaries

# Update value/values

wk1.update_value('A8', '40')  # Updates A8 with 40
or
wk1.update_value('A8','=A6+A7',True)#Updates A8 with sum of A6 and A7
wk1.update_values('A8', [['G',40]]) # Updates values in 8th starting from A8

# Get rows or columns

wk1.get_row(row_number)   # Returns a list of all values in a row
wk1.get_col(col_number)   # Returns a list of all values in a column

# Add/delete rows and columns

wk1.add_rows(n)     # Add  n rows to worksheet at end
wk1.add_cols(n)     # Add n columns to worksheet at end
wk1.delete_rows(n)  # Delete last n rows of worksheet
wk1.delete_rows(n)  # Delete last n columns of worksheet

# Insert rows and columns

wk1.insert_rows(row =1, number = 2) # inserts 2 new rows after 1st row
wk1.insert_rows(row =1, number = 1, values =['AA', 40]) # insert 1 new row and insert values in same row
wk1.insert_cols(col =6, number = 2) # inserts 2 new columns after 6th column
wk1.insert_rows(col=6, number = 1, values =['AA', 40]) # insert a new column and insert values in same column

# Update row and column

wk1.update_row(row_index, values, col_offset =0) # Updates values in a row from 1st column
# Example: >>> wk1.update_row(9, ['H', 45, 178, 81])

wk1.update_col(col_index, values, row_offset=0)  # Updates values in a column from 1st row
#Example:  >>> wk1.update_col(9, [78, 45, 178, 81])

# Adjust width of column and height of row

wk1.adjust_column_width(start=0, end=3, pixel_size=50) # Updates column size to 50 pixel
wk1.adjust_row_height(1,10, pixel_size=50) # Updates row height to 50 pixel

# Resize and clear worksheet

wk1.clear('A9')     # Clear all values starting from A9
wk1.clear('A9:D10') # Clear values in grid range A9 to D10
wks.resize(num_rows, num_cols)  # Resize to given dimension

# Add pandas DataFrame to worksheet

wk1.set_dataframe(df, 'A9')#Inserts df in worksheet starting from A9
# Note: set copy_head =False  if you don't want to add first row of df

# Get worksheet values as pandas DataFrame

wk1.get_as_df() # Returns a pandas DataFrame of worksheet
# Note: You can specify start and end to get specific range data

Add chart to worksheet

wk1.add_chart(('A1', 'A6'), [('B1', 'B6')], 'Age Chart')

