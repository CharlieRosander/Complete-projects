# Program README

This program is designed to read a CSV file, preprocess the data, normalize specified columns, and save the modified data to a new CSV file. It utilizes the pandas library for data manipulation and processing.

## Requirements
- Python 3.x
- pandas library

## Installation
1. Make sure you have Python 3.x installed on your system.
2. Install the pandas library by running the following command:
   ```
   pip install pandas
   ```

## Usage
1. Place the CSV file you want to process in the same directory as the program file.
2. Open the program file in a text editor or integrated development environment (IDE).
3. Modify the following line to specify the name of your CSV file:
   ```python
   csv = Data("Automobile_data.csv")
   ```
4. Customize the data preprocessing and normalization settings as needed by modifying the `Data.data_preprocess()` and `Data.set_columns()` methods.
5. Save the program file.
6. Run the program by executing the following command in your terminal or command prompt:
   ```
   python program_file.py
   ```
7. Follow the instructions displayed in the console.
   - If any NaN values are present in the data, you will be shown the columns containing NaN values.
   - You can choose to show the number of NaN values, drop rows with NaN values, or replace NaN values with zero.
   - The program will display the columns that will be normalized.
   - The selected columns will be normalized using the min-max normalization technique.
   - You will be prompted to enter a name for the new CSV file to save the processed data.
8. Once the program finishes executing, you will find the processed data saved as a new CSV file in the same directory as the program file.

Note: Make sure that the column names in the CSV file are correctly interpreted as intended. The program assumes that columns with names containing "index," "idx," or "ix" are not intended to be normalized and skips them.

## Credits
This program was written by Charlie Rosander.