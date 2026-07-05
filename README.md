# burakozbay.com — Yeni Site (Statik HTML)

Bu klasör, eski Weebly sitenizin yerine geçecek, tamamen sizin sahip olduğunuz
statik bir site. Hiçbir aylık ücret gerektirmez (Cloudflare Pages ücretsiz).

## Klasör yapısı

```
index.html, egitimlerimiz.html, ... → sayfalar (build.py tarafından üretildi)
assets/css/style.css                → tüm görsel tasarım
images/covers/                      → her eğitim sayfasının kapak görseli
images/gallery/                     → "Fotoğraflar" sayfasındaki galeri görselleri
images/logos/                       → "Referanslar" sayfasındaki kurum logoları
docs/                                → indirilebilir PDF kataloglar
build.py                             → sayfaları yeniden üretmek için (opsiyonel)
```

## 1. Eksik görselleri ekleyin

Derlediğiniz görselleri aşağıdaki **tam dosya adlarıyla** ilgili klasöre koyun
(isimler otomatik eşleşir, başka bir şey yapmanıza gerek yok):

**`images/covers/`**
- corporate-trainings.jpg *(Etkili İletişim Teknikleri)*
- sunum-teknikleri.jpg
- diksiyon.jpg
- beden-dili.jpg
- etkili-konusma.jpg
- empati.jpg
- reyon-gorevlisi.jpg
- lider.jpg
- hakkimda.jpg

**`images/gallery/`** (her biri `-1.jpg`, `-2.jpg` şeklinde numaralı)
- as-ecza-1.jpg … as-ecza-3.jpg
- gursel-turizm-1.jpg … gursel-turizm-3.jpg
- dsi-1.jpg … dsi-7.jpg
- edirne-1.jpg … edirne-6.jpg
- emniyet-1.jpg … emniyet-6.jpg
- ibb-1.jpg … ibb-6.jpg

Bir görsel eksik olsa bile site bozulmaz — o alan otomatik olarak boş/nötr
görünür, hata vermez.

**Logolar** için `referanslar.html` dosyasını açıp `.ph` yazan kutucuklardan
birini bulun (örn. `<div class="ph">Yapı Kredi<br>Bankası</div>`) ve şununla
değiştirin:
```html
<div class="ph"><img src="images/logos/yapikredi.png" alt="Yapı Kredi"></div>
```

## 2. İletişim formlarını aktif edin (Web3Forms — ücretsiz)

Weebly'nin form barındırma özelliği burada yok; bunun yerine ücretsiz
**Web3Forms** kullanıyoruz (e-postalar doğrudan size düşer, sunucu gerekmez).

1. https://web3forms.com adresine gidip e-postanızla ücretsiz bir "Access Key" alın
2. Şu dosyalarda geçen `YOUR-WEB3FORMS-KEY` yazısını kendi anahtarınızla değiştirin:
   - `iletisim.html`
   - `egitim-basvuru.html`
   - `egitimlerimiz.html`
   - her eğitim sayfası (`diksiyon.html`, `beden-dili-egitimi.html`, vb.)

(Metin düzenleyicinizde "Tüm Dosyalarda Bul-Değiştir" ile tek seferde yapabilirsiniz.)

## 3. GitHub'a yükleyin

1. github.com → **New repository** → isim: `burakozbay-site` (veya istediğiniz)
2. **Public** veya **Private** — ikisi de Cloudflare Pages ile çalışır
3. "uploading an existing file" linkine tıklayıp bu klasördeki **tüm dosya ve
   klasörleri** sürükleyip bırakın (images/ klasörünü de dahil edin)
4. "Commit changes" ile kaydedin

## 4. Cloudflare Pages'e bağlayın

1. Cloudflare panelinde sol menüden **Workers & Pages** → **Create** → **Pages** → **Connect to Git**
2. Az önce oluşturduğunuz GitHub reposunu seçin
3. Build ayarları: **Framework preset: None**, Build command: *boş bırakın*, Build output directory: `/`
4. **Save and Deploy**

Birkaç dakika içinde siteniz `xxxx.pages.dev` adresinde yayında olacak.

## 5. Kendi domaininizi bağlayın

Cloudflare Pages projenizin içinde **Custom domains** sekmesine gidip
`burakozbay.com` ve `www.burakozbay.com` ekleyin — domain zaten Cloudflare'de
olduğu için tek tıkla otomatik bağlanır, ekstra DNS ayarı gerekmez.

## Notlar

- Blog yazılarının tam metinleri şu an yer tutucu (placeholder) — orijinal
  metinler `blog_post.csv` içinde mevcut, isterseniz birlikte işleriz.
- Eğitim Takvimi sayfasındaki 2019 tarihli örnekler güncel değil, güncel
  tarihlerle değiştirilmeli ya da kaldırılmalı.
- Prezi gömme linkleriniz varsa, ilgili eğitim sayfasına
  `<iframe src="PREZI-LINKINIZ" ...></iframe>` şeklinde ekleyebiliriz —
  linki verdiğinizde yerleştiririm.
