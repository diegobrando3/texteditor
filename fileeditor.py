import os
from tkinter import filedialog, messagebox
def filesave():
    dosya=filedialog.asksaveasfilename(defaultextension="*.ea")
    if dosya:
        with open(dosya, "w", encoding="utf-8")as save:
            save.write
def openfile():
    dosya=filedialog.askopenfilename(filetypes=[("EA dosyaları", "*.ea")])
    if not os._exists(dosya):
        os.path.join("AEditor", "hello.ea")
    with open(dosya, "r", encoding="utf-8") as ac:
        ac.read
        cwd=os.getcwd()
        print(cwd)
        return cwd

def filedel():
    if cwd:
        dosya=os.remove(cwd)
    else:
        print("Önce dosyayı açın")