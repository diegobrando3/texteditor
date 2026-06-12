# TEXT EDİTÖRÜ
# Enes Acar Text Editor

Tkinter tabanlı, sade ve kullanışlı bir masaüstü metin editörü.

## Özellikler

- Satır numaraları gösterimi
- Dosya açma, düzenleme ve kalıcı kaydetme
- Geçici dosyaya kaydetme, temp (commit öncesi taslak)
- Dosya içeriğini veya dosyanın kendisini silme
- Klavye kısayolları ile hızlı kullanım
- Durum çubuğu ile anlık feedback

## Gereksinimler

- Python 3.x
- `tkinter` kütüphanesi (Python ile birlikte gelir, Linux kullanıcıları özel olarak indirmeli.)


## Kullanım

```bash
git clone https://github.com/diegobrando3/texteditor.git
cd texteditor
python main.py
```

## Klavye Kısayolları

| Kısayol | İşlev |
|---------|-------|
| `F1` | Dosya aç |
| `F2` | Geçici dosyaya kaydet |
| `F3` | Değişiklikleri kalıcı kaydet (commit) |
| `F4` | Sil menüsünü aç |
| `F5` | Uygulamayı kapat |

## İş Akışı

1. **F1** ile bir dosya açın.
2. Düzenlemelerinizi yapın.
3. **F2** ile değişikliklerinizi geçici bir `.ea` dosyasına kaydedin (isteğe bağlı).
4. **F3** ile değişiklikleri asıl dosyaya kalıcı olarak işleyin.
5. **F5** ile işiniz bittiğinde
## Sil Seçenekleri

**F4** tuşuna basıldığında iki seçenek sunulur:

- **Dosya İçeriğini Sil** — Editördeki metni temizler, dosyaya dokunmaz.
- **Dosyayı Sil** — Dosyayı diskten kalıcı olarak siler (onay ister).

## Geçici Dosyalar

Geçici kayıt yapıldığında `temp_*.ea` uzantılı dosyalar çalışma dizininde oluşturulur. Commit işlemi tamamlandığında bu dosyalar otomatik olarak silinir.



**README ASSISTED BY CLAUDE <3**

**PROJECT ASSISTED BY COPILOT <3**
