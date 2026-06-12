import os
from tkinter import filedialog, messagebox

def filesave(text_widget):
    dosya = filedialog.asksaveasfilename(defaultextension="*.ea")
    if dosya:
        with open(dosya, "w", encoding="utf-8") as save:
            content = text_widget.get("1.0", "end-1c")
            save.write(content)
        messagebox.showinfo("Başarılı", f"Dosya kaydedildi: {dosya}")

def openfile(text_widget):
    dosya = filedialog.askopenfilename(filetypes=[("EA dosyaları", "*.ea")])
    if dosya and os.path.exists(dosya):
        with open(dosya, "r", encoding="utf-8") as ac:
            icerigi = ac.read()
            text_widget.delete("1.0", "end")
            text_widget.insert("1.0", icerigi)
        return dosya
    else:
        messagebox.showerror("Hata", "Dosya bulunamadı")

cwd = os.getcwd()

def filedel():
    if os.path.exists(cwd):
        dosya = os.remove(cwd)
        print("Dosya silindi")
    else:
        print("Önce dosyayı açın")