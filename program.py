import os
import tempfile
import tkinter as tk
from tkinter import messagebox
import fileeditor

root = tk.Tk()
root.title("Enes Acar Text Editor")
root.geometry("1920x1080")

active_file = None
temp_file = None

# Text ve line numbers için frame
text_frame = tk.Frame(root)
text_frame.pack(fill="both", expand=True)

# Line numbers widget
line_numbers = tk.Text(text_frame, width=5, padx=5, bg="#E8E8E8", fg="#999999", font=("Arial", 12), state="disabled")
line_numbers.pack(side="left", fill="y")

text = tk.Text(text_frame, font=("Arial", 12))
text.pack(side="left", fill="both", expand=True)

status_label = tk.Label(root, text="Açık dosya yok", anchor="w")

def update_line_numbers(event=None):
    """kaçıncı satırdayızx"""
    lines = text.get("1.0", "end-1c").split("\n")
    line_count = len(lines)
    line_numbers.config(state="normal")
    line_numbers.delete("1.0", "end")
    for i in range(1, line_count + 1):
        line_numbers.insert("end", f"{i}\n")
    
    line_numbers.config(state="disabled")

def durum(message):
    status_label.config(text=message)

def yeni_dosya_command():
    global active_file, temp_file
    dosya = fileeditor.newfile(text)
    if dosya:
        active_file = dosya
        temp_file = None
        durum(f"Yeni dosya oluşturuldu: {os.path.basename(active_file)}")
    else:
        durum("Yeni dosya oluşturulamadı")

def ac_command():
    global active_file, temp_file
    dosya = fileeditor.openfile(text)
    if dosya:
        active_file = dosya
        temp_file = None
        durum(f"Açılan dosya: {os.path.basename(active_file)}")
    else:
        durum("Dosya açılmadı")

def ekle_command():
    global temp_file
    if not active_file:
        messagebox.showwarning("Uyarı", "Önce bir dosya açın.")
        return
    content = text.get("1.0", "end-1c")
    if not content:
        messagebox.showwarning("Uyarı", "Yazı alanı boş.")
        return
    if not temp_file or not os.path.exists(temp_file):
        temp_handle = tempfile.NamedTemporaryFile(delete=False, suffix=".ea", prefix="temp_", dir=os.getcwd())
        temp_file = temp_handle.name
        temp_handle.close()
    with open(temp_file, "w", encoding="utf-8") as temp:
        temp.write(content)

    durum(f"Geçici dosyaya yazıldı: {os.path.basename(temp_file)}")
    messagebox.showinfo("Geçici Kaydedildi", f"Değişiklikler geçici dosyaya kaydedildi:\n{temp_file}")

def commit_command():
    global temp_file
    if not active_file:
        messagebox.showwarning("Uyarı", "Önce bir dosya açın.")
        return
    content = text.get("1.0", "end-1c")
    with open(active_file, "w", encoding="utf-8") as real_file:
        real_file.write(content)
    if temp_file and os.path.exists(temp_file):
        os.remove(temp_file)
        temp_file = None
    durum(f"Commit yapıldı: {os.path.basename(active_file)}")
    messagebox.showinfo("Commit Tamamlandı", f"Değişiklikler kalıcı olarak kaydedildi:{active_file}")

def sil_command():
    global active_file, temp_file
    if not active_file:
        messagebox.showwarning("Uyarı", "Önce bir dosya açın.")
        return
    
    # Seçim penceresini oluştur
    sil_window = tk.Toplevel(root)
    sil_window.title("Sil")
    sil_window.geometry("400x150")
    sil_window.resizable(False, False)
    
    # Başlık etiketi
    baslik = tk.Label(sil_window, text="Ne yapmak istiyorsunuz?", font=("Arial", 12, "bold"))
    baslik.pack(pady=10)
    
    # Tab gibi butonlar için frame
    tab_frame = tk.Frame(sil_window)
    tab_frame.pack(pady=10)
    
    def delete_content():
        text.delete("1.0", "end")
        durum("Dosya içeriği silindi")
        sil_window.destroy()
    
    def delete_file():
        global active_file, temp_file
        if messagebox.askyesno("Onay", f"'{os.path.basename(active_file)}' dosyasını kalıcı olarak silmek istediğinizden emin misiniz?"):
            try:
                os.remove(active_file)
                text.delete("1.0", "end")
                active_file = None
                temp_file = None
                durum("Dosya silindi")
                messagebox.showinfo("Başarılı", "Dosya kalıcı olarak silindi.")
                sil_window.destroy()
            except Exception as e:
                messagebox.showerror("Hata", f"Dosya silinemedi: {e}")
    
    # Tab butonları
    btn_icerik = tk.Button(
        tab_frame, 
        text="Dosya İçeriğini Sil", 
        command=delete_content,
        width=20,
        bg="#FFE4E1",
        activebackground="#FFB6C1"
    )
    btn_icerik.pack(side="left", padx=5)
    
    btn_dosya = tk.Button(
        tab_frame, 
        text="Dosyayı Sil", 
        command=delete_file,
        width=20,
        bg="#FFE4E1",
        activebackground="#FFB6C1"
    )
    btn_dosya.pack(side="left", padx=5)
    
    # İptal butonu
    iptal_btn = tk.Button(
        sil_window,
        text="İptal",
        command=sil_window.destroy,
        width=20
    )
    iptal_btn.pack(pady=10)


dugmecubugu = tk.Frame(root)
yeni_dosya = tk.Button(dugmecubugu, text="Yeni Dosya (F1)", command=yeni_dosya_command)
ac = tk.Button(dugmecubugu, text="Dosya Aç (F2)", command=ac_command)
ekle = tk.Button(dugmecubugu, text="Ekle (F3)", command=ekle_command)
commit = tk.Button(dugmecubugu, text="Değişiklikleri kaydet (F4)", command=commit_command)
sil = tk.Button(dugmecubugu, text="Sil (F5)", command=sil_command)
kapat = tk.Button(dugmecubugu, text="Kapat (F6)", command=root.quit)

text.pack(fill="both", expand=False)
status_label.pack(side="bottom", fill="x")
yeni_dosya.pack(side="left", padx=5, pady=5)
ac.pack(side="left", padx=5, pady=5)
ekle.pack(side="left", padx=5, pady=5)
commit.pack(side="left", padx=5, pady=5)
sil.pack(side="left", padx=5, pady=5)
kapat.pack(side="left", padx=5, pady=5)

dugmecubugu.pack(side="bottom", fill="x")

# Line numbers'ı güncelle
update_line_numbers()
text.bind("<KeyRelease>", update_line_numbers)

# Keyboard kısayolları
root.bind("<F1>", lambda event: yeni_dosya_command())
root.bind("<F2>", lambda event: ac_command())
root.bind("<F3>", lambda event: ekle_command())
root.bind("<F4>", lambda event: commit_command())
root.bind("<F5>", lambda event: sil_command())
root.bind("<F6>", lambda event: root.quit())

root.mainloop()