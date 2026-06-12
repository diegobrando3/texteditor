import tkinter as tk
import os
import tempfile
import fileeditor
gecici=None
aktif=None

root= tk.Tk()
root.title("Enes Acar Text Editor")
root.geometry("600x400")
text = None  # Global text widget

def ekle_command():
    if text:
        fileeditor.filesave(text)

def ac_command():
    if text:
        fileeditor.openfile(text)

ekle=tk.Button(root, text="Ekle", command=ekle_command)
ac=tk.Button(root, text="Yeni Aç", command=ac_command)
sil=tk.Button(root, text="Sil")

def editoru_ac():

    # Ana menü butonlarını kaldır
    ekle.pack_forget()
    ac.pack_forget()
    sil.pack_forget()

    # Yazı alanı
    global text
    text = tk.Text(root, font=("Arial", 12))
    text.pack(fill="both", expand=False)

    # Alt araç çubuğu
    toolbar = tk.Frame(root)
    toolbar.pack(side="bottom", fill="x")

    kaydet = tk.Button(toolbar, text="Kaydet", command=ekle_command)
    kaydet.pack(side="left", padx=5, pady=5)

    sil_btn = tk.Button(toolbar, text="Sil")
    sil_btn.pack(side="left", padx=5, pady=5)

    kapat = tk.Button(toolbar, text="Kapat")
    kapat.pack(side="left", padx=5, pady=5)


# Editörü başlat
editoru_ac()
ekle.pack(pady=20)
ac.pack(pady=20)
sil.pack(pady=20)

root.mainloop()