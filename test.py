import mysql.connector
import xlrd

book = xlrd.open_workbook("test.xlsx")
sheet = book.sheet_by_name("sheet1")

# FILL IN YOUR CREDS HERE
db = mysql.connector.connect(
    host="",
    user="",
    passwd="",
    database=""
    )

mycursor = db.cursor()

# THIS IS WHAT I USED TO CREATE A TABLE IN MY DB FOR THIS INFO - YOU WILL NEED TO RUN IT ONCE BEFORE ATTEMPTING TO ENTER ANY DATA
# mycursor.execute("CREATE TABLE Statement (transaction_date DATE, post_date DATE, description VARCHAR(50), category VARCHAR(50), type VARCHAR(50), amount smallint)")


query = """INSERT INTO statement (description, category, type, amount) VALUES (%s,%s,%s,%s)"""

#Currently, not properly evaluating dates from Excel. May need a different Excel file opener or a way to manipulate that text.
for r in range(1, sheet.nrows):
    # transaction_date    = sheet.cell(r,0).value
    # post_date           = sheet.cell(r,1).value
    description         = sheet.cell(r,2).value
    category            = sheet.cell(r,3).value
    type                = sheet.cell(r,4).value
    amount              = sheet.cell(r,5).value

    values = (description, category, type, amount)

    mycursor.execute(query, values)

mycursor.close()
db.commit() 