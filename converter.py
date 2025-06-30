import pandas as pd
import sys

if len(sys.argv) != 3:
    print("Usage: python converter.py input_file.xlsx output_file.sql")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

df = pd.read_excel(input_file)

table = input("What is the name of the table in the database?\n")

encoding = input("Enter the encoding type (default is 'utf-8'):\n") or "utf-8"

with open(output_file, "w", encoding=encoding) as f:
    columns = ", ".join([f"`{col}`" for col in df.columns])
    values = []
    for _, row in df.iterrows():
        row_data = []
        for val in row:
            if pd.isna(val) or str(val).strip().upper() == "NULL":
                row_data.append("null")
            elif isinstance(val, float):
                if val.is_integer():
                    row_data.append(str(int(val)))
                else:
                    row_data.append(str(val))
            elif isinstance(val, int):
                row_data.append(str(val))
            else:
                escaped = str(val).replace("'", "''")
                row_data.append(f"'{escaped}'")
        values.append(f"({', '.join(row_data)})")
    values_str = ",\n".join(values)
    f.write(f"INSERT INTO {table} ({columns}) VALUES\n{values_str};\n")

print(f"SQL dump written to {output_file} with encoding {encoding}")
