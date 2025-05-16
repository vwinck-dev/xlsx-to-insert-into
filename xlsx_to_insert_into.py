import pandas as pd

df = pd.read_excel(input("Enter the path to the Excel file:\n"))

table = input("What is the name of the table in the database?\n")

for i, row in df.iterrows():
    columns = ", ".join([f"`{col}`" for col in df.columns])
    data = ", ".join([f"'{str(val).replace('\'', '\\\'')}'" for val in row])
    print(f"INSERT INTO {table} ({columns}) VALUES ({data});")