import tkinter as tk
import os
import tempfile
import fileeditor
gecici=None
aktif=None

root= tk.Tk()
root.title("Enes Acar Text Editor")
root.geometry("600x400")
bas=tk.Button(root, text="Ekle", command=fileeditor.filesave)
ac=tk.Button(root, text="Aç", command=fileeditor.openfile)
sil=tk.Button(root, text="Sil", command=fileeditor.filedel)
bas.pack(pady=20)
ac.pack(pady=20)
sil.pack(pady=20)
root.mainloop()