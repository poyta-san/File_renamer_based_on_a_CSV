# File_renamer_based_on_a_CSV

FEATURES
The File Name Manipulator app offers two main features:

- Create a CSV list of the file names from the indicated folder and its subfolders.
- Rename files from a selected folder and its subfolders according to the CSV file that contains a list of the old and new names.

HOW TO USE THIS APP

1- Selecting the Folder:
Click on the "Select Path" button to choose the folder from which you want to retrieve the names of all files, including subfolders.

2- Saving the CSV File:
Click on the "Select Destination" button to choose the location where you want to save the CSV file containing the file names.
Enter the desired name for the CSV file and click "Save".

3- Creating the CSV:
Once you have selected the folder and destination, click on the "Create CSV" button.
The app will generate a CSV file that includes the names of all files within the selected folder and its subfolders. The 
first row of the CSV will be ignored.

4- Modifying File Names:
Open the generated CSV file using a spreadsheet application or any suitable software.
In the CSV file, you will find one column: "Antigo Nome" (Old Name) and you should add another column with any name.
Enter the desired new names for the corresponding files in the new column. Ensure each row has the old name (column 1) and new name (column 2).
Save the modified CSV file.
Example CSV:

Antigo Nome;Novo Nome
100010605-01-G-Raquel-frente.jpg;100010 - 605_605.jpg
100010605-02-G-Raquel-costas.jpg;100010 - 605-2.jpg
100010900-03-G-Raquel-frente.jpg;100010 - 900_900.jpg
100010900-04-G-Raquel-costas.jpg;100010 - 900-2.jpg

Note: The separator used in the CSV file is ";" (semicolon).

5- Loading the CSV:
Click on the "Load file" button to choose the modified CSV file containing the old and new names.
The app will load the CSV file, mapping the old names to the new names.

6- Renaming Files:
Once the CSV file is loaded, click on the "Start Renaming" button.
The app will find all files with names matching the entries in the CSV within the selected folder and its subfolders.
Each file's old name will be replaced with the corresponding new name specified in the CSV.
The renaming process may take some time, depending on the number of files.

TIPS

How to Create an Executable (EXE):

1- Installing PyInstaller:
Run the command pip install pyinstaller to install PyInstaller.

2- Creating the EXE:
Run the command pyinstaller --onefile -w replace_file_names.py.
The command will package the "replace_file_names.py" script into a standalone EXE file.
The -w option is used to create a windowed (non-console) application.
Note: Please ensure that you have Python and the required dependencies installed before following the steps mentioned above.

By following these instructions, you can efficiently use the File Name Manipulator app to generate a CSV list of file names and rename files in bulk using a CSV file.