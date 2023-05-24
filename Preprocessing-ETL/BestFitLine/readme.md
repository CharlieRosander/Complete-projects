# Program README

This program is designed to import a CSV file, create arrays from the data, perform calculations using the Gauss elimination and least squares methods, and plot the data along with the best-fit line.

## Requirements
- Python 3.x
- numpy library
- pandas library
- matplotlib library

## Installation
1. Make sure you have Python 3.x installed on your system.
2. Install the required libraries by running the following commands:
   ```
   pip install numpy
   pip install pandas
   pip install matplotlib
   ```

## Usage
1. Place the CSV file you want to import in the same directory as the program file.
2. Open the program file in a text editor or integrated development environment (IDE).
3. Customize the program as needed by modifying the following sections:
   - Importing the CSV file:
     ```python
     RawData.import_csv("your_file.csv")
     ```
   - Creating arrays:
     ```python
     RawData.create_arrays(df_x, df_y)
     ```
   - Performing calculations:
     ```python
     Calculations.prepare_arrays(x, y)
     Calculations.gauss_and_least_square()
     ```
   - Plotting the graph:
     ```python
     create_graph(x_raw, y_raw, k, m)
     ```
4. Save the program file.
5. Run the program by executing the following command in your terminal or command prompt:
   ```
   python program_file.py
   ```
6. The program will perform the necessary calculations and display the best-fit line equation (K and m values) in the console.
7. A graph will be plotted showing the data points and the best-fit line.

Note: Make sure that the data in the CSV file is formatted correctly and matches the expected input format.

## Credits
This program was created by Charlie Rosander.