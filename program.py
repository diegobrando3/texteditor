#FONT SİZE BÜYÜTÜNCE PENCERE BÜYÜYOR

import os
import tempfile
import tkinter as tk
from tkinter import messagebox, colorchooser, simpledialog
import fileeditor

root = tk.Tk()
root.title("Enes Acar Text Editor")
#KENDİ MONİTÖRÜME GÖRE YAPTIM SİZ DEĞİŞTİREBİLİRSİNİZ!
root.geometry("1920x1080")
#root.resizable(False, False)
menu_bar = tk.Menu(root)
settings_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Ayarlar", menu=settings_menu)
root.config(menu=menu_bar)


anlik_dosya = None
gecici_dosya = None

# Text ve line numbers için frame
text_frame = tk.Frame(root)
text_frame.pack(fill="both", expand=True)
#text_frame.pack_propagate(False)


# Line numbers widget
line_numbers = tk.Text(text_frame, width=5, padx=5, bg="#E8E8E8", fg="#999999", font=("Arial", 12), state="disabled")
line_numbers.pack(side="left", fill="y")

textsize=12
text = tk.Text(text_frame, font=("Arial", textsize))
text.pack(side="left", fill="both", expand=True)

status_frame = tk.Frame(root)
status_frame.pack(side="bottom", fill="x")
status_label = tk.Label(status_frame, text="Açık dosya yok", anchor="w")
kelime_sayac = tk.Label(status_frame, text="Kelime: 0", anchor="center")
status_label.pack(side="left", fill="x", expand=True)
kelime_sayac.pack(side="left")

# Varsayılan font ayarları
current_font_family = "Arial"
current_font_size = 12

def arkaplan():
    color = colorchooser.askcolor(title="Arka plan rengi seç")
    if color and color[1]:
        text.config(bg=color[1])
        durum(f"Arka plan rengi ayarlandı: {color[1]}")

def yazi_renk():
    color = colorchooser.askcolor(title="Yazı rengi seç")
    if color and color[1]:
        text.config(fg=color[1])
        durum(f"Yazı rengi ayarlandı: {color[1]}")

def update_line_numbers(event=None):
    """kaçıncı satırdayızx"""
    lines = text.get("1.0", "end-1c").split("\n")
    line_count = len(lines)
    line_numbers.config(state="normal")
    line_numbers.delete("1.0", "end")
    for i in range(1, line_count + 1):
        line_numbers.insert("end", f"{i}\n")    
    
    line_numbers.config(state="disabled")
    update_word_count()

def update_word_count():
    content=text.get("1.0", "end").strip() #end-1c kullanacaktım ama zaten strip boşlukları temizliyor
    count=0
    count = len(content.split())#liste yapam liste içini sayam
    kelime_sayac.config(text=f"Kelime: {count}")

def set_font_size(size):
    global current_font_size
    current_font_size = size
    text.config(font=(current_font_family, current_font_size), wrap="none")  # wrap="none" ekle
    line_numbers.config(font=(current_font_family, current_font_size))
    update_line_numbers()
    durum(f"Yazı boyutu ayarlandı: {size} pt")

def choose_font_size_dialog():
    size = simpledialog.askinteger("Yazı Boyutu", "Yeni yazı boyutu (pt):", initialvalue=current_font_size, minvalue=6, maxvalue=72)
    if size:
        set_font_size(size)

menu_bar = tk.Menu(root)
font_menus = tk.Menu(menu_bar, tearoff=0)
settings_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Ayarlar", menu=settings_menu)
settings_menu.add_command(label="Arkaplan rengi", command=arkaplan)
settings_menu.add_command(label="Yazı rengi", command=yazi_renk)
settings_menu.add_cascade(label="Font Ayarla", menu=font_menus)
font_menus.add_command(label="Elle Gir", command=choose_font_size_dialog)
font_menus.add_command(label="Font size buglı!")
font_menus.add_separator()
font_menus.add_command(label="10 pt", command=lambda: set_font_size(10))
font_menus.add_command(label="14 pt", command=lambda: set_font_size(14))
font_menus.add_command(label="18 pt", command=lambda: set_font_size(18))
font_menus.add_command(label="22 pt", command=lambda: set_font_size(22))
font_menus.add_command(label="26 pt", command=lambda: set_font_size(26))
root.config(menu=menu_bar)

def durum(message):
    status_label.config(text=message)

def yeni_dosya_command():
    global anlik_dosya, gecici_dosya
    dosya = fileeditor.newfile(text)
    if dosya:
        anlik_dosya = dosya
        gecici_dosya = None
        durum(f"Yeni dosya oluşturuldu: {os.path.basename(anlik_dosya)}")
    else:
        durum("Yeni dosya oluşturulamadı")

def ac_command():
    global anlik_dosya, gecici_dosya
    dosya = fileeditor.openfile(text)
    if dosya:
        anlik_dosya = dosya
        gecici_dosya = None
        durum(f"Açılan dosya: {os.path.basename(anlik_dosya)}")
    else:
        durum("Dosya açılmadı")

def ekle_command():
    global gecici_dosya
    if not anlik_dosya:
        messagebox.showwarning("Uyarı", "Önce bir dosya açın.")
        return
    content = text.get("1.0", "end-1c")
    if not content:
        messagebox.showwarning("Uyarı", "Yazı alanı boş.")
        return
    if not gecici_dosya or not os.path.exists(gecici_dosya):
        temp_handle = tempfile.NamedTemporaryFile(delete=False, suffix=".ea", prefix="temp_", dir=os.getcwd())
        gecici_dosya = temp_handle.name
        temp_handle.close()
    with open(gecici_dosya, "w", encoding="utf-8") as temp:
        temp.write(content)

    durum(f"Geçici dosyaya yazıldı: {os.path.basename(gecici_dosya)}")
    messagebox.showinfo("Geçici Kaydedildi", f"Değişiklikler geçici dosyaya kaydedildi:\n{gecici_dosya}")

def commit_command():
    global gecici_dosya
    if not anlik_dosya:
        messagebox.showwarning("Uyarı", "Önce bir dosya açın.")
        return
    content = text.get("1.0", "end-1c")
    with open(anlik_dosya, "w", encoding="utf-8") as real_file:
        real_file.write(content)
    if gecici_dosya and os.path.exists(gecici_dosya):
        os.remove(gecici_dosya)
        gecici_dosya = None
    durum(f"Commit yapıldı: {os.path.basename(anlik_dosya)}")
    messagebox.showinfo("Commit Tamamlandı", f"Değişiklikler kalıcı olarak kaydedildi:{anlik_dosya}")

def sil_command():
    global anlik_dosya, gecici_dosya
    if not anlik_dosya:
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
        global anlik_dosya, gecici_dosya
        if messagebox.askyesno("Onay", f"'{os.path.basename(anlik_dosya)}' dosyasını kalıcı olarak silmek istediğinizden emin misiniz?"):
            try:
                os.remove(anlik_dosya)
                text.delete("1.0", "end")
                anlik_dosya = None
                gecici_dosya = None
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
yeni_dosya = tk.Button(dugmecubugu, text="Dosya oluştur (F1)", command=yeni_dosya_command)
ac = tk.Button(dugmecubugu, text="Dosya Aç (F2)", command=ac_command)
ekle = tk.Button(dugmecubugu, text="Ekle (F3)", command=ekle_command)
commit = tk.Button(dugmecubugu, text="Değişiklikleri kaydet (F4)", command=commit_command)
sil = tk.Button(dugmecubugu, text="Sil (F5)", command=sil_command)
kapat = tk.Button(dugmecubugu, text="Kapat (F6)", command=root.quit)

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
update_word_count()
text.bind("<KeyRelease>", update_line_numbers)
# Keyboard kısayol
root.bind("<F1>", lambda event: yeni_dosya_command())
root.bind("<F2>", lambda event: ac_command())
root.bind("<F3>", lambda event: ekle_command())
root.bind("<F4>", lambda event: commit_command())
root.bind("<F5>", lambda event: sil_command())
root.bind("<F6>", lambda event: root.quit())

root.mainloop()