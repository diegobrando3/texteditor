# TEXT EDİTÖRÜ
# 430 9ATP A Enes Acar
# Enes Acar Text Editor

Tkinter tabanlı, sade ve kullanışlı bir masaüstü metin editörü.

## Özellikler

- Özelleştirilebilirlik seçenekleri
- Satır numaraları gösterimi
- Kelime sayacı
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
| `F1` | Dosya oluştur |
| `F2` | Dosya aç |
| `F3` | Geçici dosyaya kaydet |
| `F4` | Değişiklikleri kalıcı kaydet (commit) |
| `F5` | Sil menüsünü aç |
| `F6` | Uygulamayı kapat |

## İş Akışı

1. **F1** ile yeni bir dosya oluşturun (sonuna .ea ekleyin).
1. **F2** ile bir dosya açın.
2. Düzenlemelerinizi yapın.
3. **F3** ile değişikliklerinizi geçici bir `.ea` dosyasına kaydedin (isteğe bağlı).
4. **F4** ile değişiklikleri asıl dosyaya kalıcı olarak işleyin.
5. **F5** ile silme seçeneklerini seçin.
6. **F6** ile işiniz bittiğinde utgulamayı kapatın.
## Silme Seçenekleri

**F5** tuşuna basıldığında iki seçenek sunulur:

- **Dosya İçeriğini Sil** — Editördeki metni ve dosyanın içindeki yazıları siler.
- **Dosyayı Sil** — Dosyayı diskten kalıcı olarak siler (onay ister).

## Geçici Dosyalar

Geçici kayıt yapıldığında `temp_*.ea` uzantılı dosyalar çalışma dizininde oluşturulur. Commit işlemi tamamlandığında bu dosyalar otomatik olarak silinir.

## Sırada ekleyeceğim özellikler
-Json dosyası ile stat tablosu???
-Uygulama kapatırken autosave(commit) ve kaydedilmeyenleri kullanıcıya sorarak kaydetme

## ***KNOWN BUGS*** 🔨🔨
Font size değişiklği yapılınca pencere boyutu değişiyor??

**PROJECT ASSISTED BY COPILOT <3**

**CODE FLOW SUGGESTED BY GEMINI <3**

**GLORY TO MUSTAFA E-REPUBLIC**
