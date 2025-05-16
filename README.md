# XLSX to MySQL Dump Converter

This project is a Python-based tool designed to convert data from an Excel file (`.xlsx`) into a MySQL dump file. The generated dump file can be used to populate a MySQL database with the data from the Excel spreadsheet.

## Features

- Parse `.xlsx` files and extract data.
- Generate MySQL-compatible dump files.
- Easy-to-use and customizable.

## Requirements

- Python 3.x
- Required Python libraries (install via `pip`):
    - `pandas`
    - `sys`

## Installation

1. Clone this repository:
     ```
     git clone https://github.com/vwinck-dev/xlsx-to-insert-into.git
     cd xlsx-to-insert-into
     ```

## Usage

1. Place your `.xlsx` file in the project directory.
2. Run the script:
     ```
     python converter.py input_file_name.xlsx output_file_name_example.sql
     ```
3. The generated MySQL dump file will be saved as `output_file_name_example.sql`.

## Contributing

Feel free to fork this repository and submit pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
