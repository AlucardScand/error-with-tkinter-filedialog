from tkinter import *
from PIL import ImageTk, Image
import os

#otwieranie plików musimy wezwać bibliotekę
from tkinter import filedialog

# Najelpszy sposób narazie na radzenie sobie ze ścieżkami windowsa
os.chdir(os.path.dirname(os.path.abspath(__file__)))
(filepath, filename) = os.path.split(__file__)
d = os.getcwd()

list_of_files = []

for f in os.listdir(d):
    if os.path.isfile(os.path.join(d, f)):
        (sn, et) = os.path.splitext(os.path.join(d, f))
        if et == ".jpg":
            list_of_files.append(f)
print(list_of_files)

# Tkinter

root = Tk()
root.title("Open Files / Dialog Box")
root.iconbitmap("ikona.ico")

# Gwiazda oznacza dowoloność czyli dwie gwiazdki oznaczają, że szukamy każdy plik w tym folderze
root.filename = filename = filedialog.askopenfilename(
    initialdir=d,
    title="Select a File!",
    filetypes=(
        ("jpg files", "*.jpg"),
        ("all files", "*.*")
    )
)
# Autodesk z jakiegoś powodu wpływa na bibliotekę i nie działa, rozwiązanie na necie https://stackoverflow.com/questions/19576586/log4cpluserror-in-python-when-calling-for-tkinter-file-dialog


mainloop()