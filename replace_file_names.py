import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Progressbar
import csv
import os
import threading

# Define folder_path as a global variable
folder_path = ""
csv_file_path = ""
csv_file_mod_path = ""


def button_clicked(button_number):
    global folder_path, csv_file_path, csv_file_mod_path  # Use the global variables
    if button_number == 1:
        # Select folder path
        folder_path = filedialog.askdirectory()
        print("Selected folder path:", folder_path)
        log_text.insert(tk.END, "Selected folder path: " + folder_path + "\n")
    elif button_number == 2:
        # Select CSV file path
        csv_file_path = filedialog.asksaveasfilename(
            defaultextension=".csv", filetypes=[("CSV Files", "*.csv")]
        )
        print("Selected CSV file path:", csv_file_path)
        log_text.insert(tk.END, "Selected CSV file path: " + csv_file_path + "\n")
    elif button_number == 3:
        if not folder_path:
            print("Please select a folder path.")
            return
        if not csv_file_path:
            print("Please select a CSV file path.")
            return
        # Save file list to CSV
        file_list = get_all_files(folder_path)
        save_file_list_to_csv(file_list, csv_file_path)
        print("File list saved to CSV.")
        log_text.insert(tk.END, "File list saved to CSV.\n")
    elif button_number == 4:
        # Select modified CSV file path
        csv_file_mod_path = filedialog.askopenfilename(
            filetypes=[("CSV Files", "*.csv")]
        )
        print("Selected modified CSV file path:", csv_file_mod_path)
        log_text.insert(
            tk.END, "Selected modified CSV file path: " + csv_file_mod_path + "\n"
        )
    elif button_number == 5:
        if not folder_path:
            print("Please select a folder path.")
            return
        if not csv_file_mod_path:
            print("Please select a modified CSV file path.")
            return
        # Start a new thread to perform file renaming
        threading.Thread(
            target=rename_files_with_progress, args=(csv_file_mod_path, folder_path)
        ).start()


def get_all_files(folder):
    file_list = []
    for root, _, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            file_name = os.path.basename(file_path)
            file_list.append(file_name)
    return file_list


def save_file_list_to_csv(file_list, csv_file):
    with open(csv_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["File Name"])
        for file in file_list:
            writer.writerow([file])


def rename_files(csv_file, root_dir):
    with open(csv_file, "r") as file:
        csv_reader = csv.reader(file, delimiter=";")
        next(csv_reader)  # Skip header row
        for row in csv_reader:
            if len(row) < 2:
                print("Invalid row format, skipping:", row)
                log_text.insert(
                    tk.END, "Invalid row format, skipping: " + str(row) + "\n"
                )
                continue
            old_name = row[0]
            new_name = row[1]
            for root, _, files in os.walk(root_dir):
                for file in files:
                    if file == old_name:
                        old_path = os.path.join(root, file)
                        new_path = os.path.join(root, new_name)
                        os.rename(old_path, new_path)
                        print(f"File '{old_path}' renamed to '{new_path}'")
                        log_text.insert(
                            tk.END,
                            "File '" + old_path + "' renamed to '" + new_path + "'\n",
                        )


def rename_files_with_progress(csv_file, root_dir):
    progress_bar.grid(row=10, column=0, columnspan=2, sticky="we")
    log_text.insert(tk.END, "Searching and renaming...\n")
    progress_bar.start()
    rename_files(csv_file, root_dir)
    progress_bar.stop()
    progress_bar.grid_remove()
    log_text.insert(tk.END, "Process complete!\n")


root = tk.Tk()

# Set the title of the window
root.title("File renamer based on a CSV")

# Create labels
label_blank = tk.Label(root, text="           ")
label_root = tk.Label(root, text="LOCALIZAÇÃO DO CAMINHO DOS ARQUIVOS")
label_1_part = tk.Label(root, text="GERAÇÃO DE LISTA CSV DOS NOMES DOS ARQUIVOS")
label1 = tk.Label(
    root,
    text="Selecione a pasta principal onde será localizado todos os arquivos (e suas subpastas):",
)
label2 = tk.Label(
    root, text="Selecione a pasta onde será salvo a lista de nome dos arquivos:"
)
label3 = tk.Label(
    root,
    text="Criar um arquivo CSV listando todos os nomes dos arquivos de acordo com a pasta informada:",
)
label_2_part = tk.Label(root, text="ALTERAÇÃO DE NOME DOS ARQUIVOS")
label4 = tk.Label(root, text="Localize o arquivo CSV com as alterações desejadas (2 colunas - nome original e novo nome):")
label5 = tk.Label(
    root,
    text="Iniciar renomeação dos arquivos do caminho selecionado conforme lista no CSV:",
)

# Create buttons
button1 = tk.Button(root, text="Selecionar caminho", command=lambda: button_clicked(1))
button2 = tk.Button(root, text="Selecionar destino", command=lambda: button_clicked(2))
button3 = tk.Button(root, text="Criar CSV", command=lambda: button_clicked(3))
button4 = tk.Button(root, text="Carregar arquivo", command=lambda: button_clicked(4))
button5 = tk.Button(root, text="Iniciar renomeação", command=lambda: button_clicked(5))

# Create progress bar
progress_bar = Progressbar(root, mode="indeterminate")

# Create log frame
log_frame = tk.Frame(root, relief=tk.SUNKEN, bd=1)
log_text = tk.Text(log_frame, height=10)
log_scrollbar = tk.Scrollbar(log_frame, command=log_text.yview)
log_text.configure(yscrollcommand=log_scrollbar.set)
log_text.pack(side=tk.LEFT, fill=tk.BOTH)
log_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
log_frame.grid(row=11, column=0, columnspan=2, sticky="w")


# Arrange labels, buttons, and progress bar in a grid layout
label_root.grid(row=0, column=0, sticky="w")
label1.grid(row=1, column=0, sticky="w")
button1.grid(row=1, column=1, sticky="w")
label_blank.grid(row=2, column=0, sticky="w")
label_1_part.grid(row=3, column=0, sticky="w")
label2.grid(row=4, column=0, sticky="w")
button2.grid(row=4, column=1, sticky="w")
label3.grid(row=5, column=0, sticky="w")
button3.grid(row=5, column=1, sticky="w")
label_blank.grid(row=6, column=0, sticky="w")
label_2_part.grid(row=7, column=0, sticky="w")
label4.grid(row=8, column=0, sticky="w")
button4.grid(row=8, column=1, sticky="w")
label5.grid(row=9, column=0, sticky="w")
button5.grid(row=9, column=1, sticky="w")

root.mainloop()
