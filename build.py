#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Statik site üretici — burakozbay.com yeniden inşası.
Her sayfa NAV/FOOTER şablonunu paylaşır; içerik PAGES listesinde tanımlıdır.
Çalıştırma: python3 build.py
"""
import os

OUT = os.path.dirname(os.path.abspath(__file__))

NAV_ITEMS = [
    ("index.html", "Ana Sayfa"),
    ("egitimlerimiz.html", "Eğitimlerimiz"),
    ("hakkimda.html", "Hakkımda"),
    ("referanslar.html", "Referanslar"),
    ("blog.html", "Blog"),
    ("egitim-takvimi.html", "Eğitim Takvimi"),
    ("iletisim.html", "İletişim"),
]

TRAININGS = [
    ("etkili-iletisim-teknikleri.html", "Etkili İletişim Teknikleri", "corporate-trainings.jpg"),
    ("etkili-sunum-teknikleri.html", "Etkili Sunum Teknikleri", "sunum-teknikleri.jpg"),
    ("diksiyon.html", "Diksiyon", "diksiyon.jpg"),
    ("beden-dili-egitimi.html", "Beden Dili Eğitimi", "beden-dili.jpg"),
    ("etkili-konusma-teknikleri.html", "Etkili Konuşma Teknikleri", "etkili-konusma.jpg"),
    ("vatandas-ic-musteri-empati.html", "Vatandaş ve İç Müşteri Empati Egzersizleri", "empati.jpg"),
    ("reyon-gorevlisi-egitimi.html", "Reyon Görevlisi Eğitimi - Merchandiser", "reyon-gorevlisi.jpg"),
    ("ekipte-lider-olabilme.html", "Ekipte Lider Olabilme", "lider.jpg"),
]

SITE_DESC = "Kurumların ihtiyaçlarına göre hazırlanan iletişim, diksiyon, beden dili ve sunum teknikleri eğitimleri."

# ---------------------------------------------------------------- shell

def page_shell(title, active_file, body_html, meta_desc=SITE_DESC, cover=None, eyebrow=None, breadcrumb=None):
    nav_links = "\n".join(
        f'<a href="{href}" class="{"active" if href==active_file else ""}">{label}</a>'
        for href, label in NAV_ITEMS
    )
    cover_html = ""
    if cover:
        cover_html = f'''<div class="cover"><img src="images/covers/{cover}" alt="{title}" loading="lazy"
            onerror="this.parentElement.style.background=\'var(--paper-dim)\'; this.remove();"></div>'''
    crumb_html = f'<div class="breadcrumb">{breadcrumb}</div>' if breadcrumb else ""
    eyebrow_html = f'<div class="eyebrow">{eyebrow}</div>' if eyebrow else ""

    return f"""<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — Burak Özbay</title>
<meta name="description" content="{meta_desc}">
<link rel="stylesheet" href="assets/css/style.css">
<link rel="icon" href="data:,">
</head>
<body>
<header class="site-header">
  <div class="wrap">
    <a href="index.html" class="logo">Burak <em>Özbay</em></a>
    <button class="nav-toggle" aria-label="Menü" onclick="document.querySelector('.main-nav').classList.toggle('open')"><span></span></button>
    <nav class="main-nav">
      {nav_links}
      <a href="egitim-basvuru.html" class="nav-cta">Eğitim Başvuru</a>
    </nav>
  </div>
</header>

<main>
{crumb_wrap(crumb_html, eyebrow_html, title, cover_html) if breadcrumb is not None else ""}
{body_html}
</main>

<footer class="site-footer">
  <div class="wrap">
    <div class="cols">
      <div>
        <a href="index.html" class="logo">Burak <em>Özbay</em></a>
        <p style="margin-top:16px">{SITE_DESC}</p>
      </div>
      <div>
        <h5>Eğitimler</h5>
        <a href="egitimlerimiz.html">Kurumsal Eğitimlerimiz</a>
        <a href="diksiyon.html">Diksiyon</a>
        <a href="beden-dili-egitimi.html">Beden Dili Eğitimi</a>
        <a href="etkili-sunum-teknikleri.html">Etkili Sunum Teknikleri</a>
      </div>
      <div>
        <h5>Kurumsal</h5>
        <a href="hakkimda.html">Hakkımda</a>
        <a href="referanslar.html">Referanslar</a>
        <a href="blog.html">Blog</a>
        <a href="iletisim.html">İletişim</a>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© <span id="y"></span> Burak Özbay — Tüm hakları saklıdır.</span>
      <span>burakozbay.com</span>
    </div>
  </div>
</footer>
<script>document.getElementById('y').textContent = new Date().getFullYear();</script>
</body>
</html>"""

def crumb_wrap(crumb_html, eyebrow_html, title, cover_html):
    return f'''<div class="page-hero">
    <div class="wrap">
      {crumb_html}
      {eyebrow_html}
      <h1>{title}</h1>
      {cover_html}
    </div>
  </div>'''

def syllabus(items):
    lis = "\n".join(
        f'<li><span class="num">{i:02d}</span><span>{item}</span></li>'
        for i, item in enumerate(items, 1)
    )
    return f'<ul class="syllabus">{lis}</ul>'

def training_body(nicin, icerik, cover):
    return f'''<div class="wrap">
  <div class="two-col" style="padding-bottom:60px">
    <div class="content-block">
      <h2>Niçin ve Neden?</h2>
      <p>{nicin}</p>
      <h2 style="margin-top:36px">Eğitim İçeriği</h2>
      {syllabus(icerik)}
      <p style="margin-top:30px">Eğitim sonrasında katılımcılara eğitim notları verilecektir. Grup ile birlikte uygulamalı çalışmalardır.</p>
    </div>
    <aside>
      <form class="card-form" action="https://api.web3forms.com/submit" method="POST">
        <input type="hidden" name="access_key" value="YOUR-WEB3FORMS-KEY">
        <input type="hidden" name="subject" value="Eğitim Talebi — {'{{TITLE}}'}">
        <div class="field"><label>Ad Soyad</label><input type="text" name="name" required></div>
        <div class="field"><label>E-posta</label><input type="email" name="email" required></div>
        <div class="field"><label>Telefon</label><input type="tel" name="phone"></div>
        <div class="field"><label>Mesajınız</label><textarea name="message" placeholder="Kurumunuz ve katılımcı sayısı hakkında kısa bilgi"></textarea></div>
        <button class="btn voice" type="submit">Teklif İsteyin</button>
      </form>
      <p class="form-note">Bilgileriniz yalnızca size dönüş yapmak için kullanılır.</p>
    </aside>
  </div>
</div>'''

# ---------------------------------------------------------------- PAGES

pages = {}

# ---------- index.html ----------
training_grid = "\n".join(
    f'''<a href="{href}" class="training-card">
      <span class="idx">{i:02d}</span>
      <h3>{label}</h3>
      <span class="go">İncele →</span>
    </a>''' for i, (href, label, _cov) in enumerate(TRAININGS, 1)
)

pages["index.html"] = page_shell(
    "Kurumsal İletişim ve Diksiyon Eğitimleri", "index.html",
    breadcrumb=None,
    meta_desc=SITE_DESC,
    body_html=f'''
  <section class="split-hero">
    <div class="split-hero__media">
      <img src="images/hero/hero.jpg" alt="Burak Özbay eğitim veriyor" loading="eager"
        onerror="this.parentElement.classList.add('split-hero__media--empty'); this.remove();">
    </div>
    <div class="split-hero__text">
      <div>
        <div class="eyebrow">İletişim · Diksiyon · Beden Dili</div>
        <h1>Söylediğiniz kadar, <span class="accent">nasıl</span> söylediğiniz de önemli.</h1>
        <div class="waveform" aria-hidden="true">
          <span></span><span></span><span></span><span></span><span></span><span></span>
          <span></span><span></span><span></span><span></span><span></span><span></span>
        </div>
        <p class="lead">Kurumlara ve bireylere iletişimin, diksiyonun ve beden dilinin gücünü öğretiyorum. 2004'ten bu yana kamu kurumları ve özel şirketlerle çalışıyorum — TV sunuculuğu ve yönetmenlik geçmişimden gelen bir bakış açısıyla.</p>
        <div style="display:flex; gap:12px; flex-wrap:wrap">
          <a href="egitim-basvuru.html" class="btn voice">Eğitim Başvurusu Yapın</a>
          <a href="#egitimler" class="btn outline">Eğitimleri İnceleyin</a>
        </div>
      </div>
    </div>
  </section>

  <section id="hakkimda-ozet" class="tint">
    <div class="wrap two-col">
      <div>
        <div class="eyebrow">Hakkımda</div>
        <h2 style="font-family:var(--serif); font-size:30px; margin:16px 0 18px">Kamera önünden eğitim salonuna</h2>
        <p style="color:var(--ink-soft)">1999'dan bu yana televizyon sunuculuğu, yönetmenlik ve editörlük yaptım (TRT, Star TV, Kanal D, ATV, TV8...). 2004'ten beri bu deneyimi kurumsal eğitimlere taşıyorum — diksiyon, beden dili ve etkili iletişim üzerine.</p>
        <a href="hakkimda.html" class="btn outline" style="margin-top:14px">Devamını okuyun →</a>
      </div>
      <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px">
        <div style="padding:22px; background:var(--paper); border:1px solid var(--line)">
          <div class="eyebrow" style="margin-bottom:8px">20+</div>
          <p style="margin:0; font-size:14px; color:var(--ink-soft)">yıllık medya ve iletişim deneyimi</p>
        </div>
        <div style="padding:22px; background:var(--paper); border:1px solid var(--line)">
          <div class="eyebrow" style="margin-bottom:8px">2004'ten beri</div>
          <p style="margin:0; font-size:14px; color:var(--ink-soft)">kurumsal eğitimler veriyorum</p>
        </div>
        <div style="padding:22px; background:var(--paper); border:1px solid var(--line)">
          <div class="eyebrow" style="margin-bottom:8px">8</div>
          <p style="margin:0; font-size:14px; color:var(--ink-soft)">farklı kurumsal eğitim başlığı</p>
        </div>
        <div style="padding:22px; background:var(--paper); border:1px solid var(--line)">
          <div class="eyebrow" style="margin-bottom:8px">Kamu + Özel</div>
          <p style="margin:0; font-size:14px; color:var(--ink-soft)">sektör, geniş kurum yelpazesi</p>
        </div>
      </div>
    </div>
  </section>

  <section id="egitimler">
    <div class="wrap">
      <div class="section-head">
        <div class="eyebrow">Kurumsal Eğitimlerimiz</div>
        <h2>Ekibinizin iletişim becerilerini birlikte geliştirelim</h2>
      </div>
    </div>
    <div class="wrap">
      <div class="grid-trainings">{training_grid}</div>
    </div>
  </section>

  <section id="referanslar" class="dark">
    <div class="wrap">
      <div class="eyebrow">Birlikte Çalıştığımız Kurumlar</div>
      <h2 style="font-family:var(--serif); font-size:28px; margin:16px 0 30px; color:var(--paper)">Referanslar</h2>
      <div class="logo-row">
        <div class="ph" style="background:#2b2820; color:#B8B0A2; border:1px solid var(--line-dark)">Yapı Kredi<br>Bankası</div>
        <div class="ph" style="background:#2b2820; color:#B8B0A2; border:1px solid var(--line-dark)">İstanbul Emniyet<br>Müdürlüğü</div>
        <div class="ph" style="background:#2b2820; color:#B8B0A2; border:1px solid var(--line-dark)">İstanbul Büyükşehir<br>Belediyesi</div>
        <div class="ph" style="background:#2b2820; color:#B8B0A2; border:1px solid var(--line-dark)">Devlet Su<br>İşleri</div>
        <div class="ph" style="background:#2b2820; color:#B8B0A2; border:1px solid var(--line-dark)">As Ecza<br>Deposu</div>
        <div class="ph" style="background:#2b2820; color:#B8B0A2; border:1px solid var(--line-dark)">Gürsel<br>Turizm</div>
      </div>
      <a href="fotograflar.html" class="btn outline" style="margin-top:30px; border-color:#5b5647; color:var(--paper)">Eğitim Fotoğraflarını Görün →</a>
    </div>
  </section>

  <section id="podcast">
    <div class="wrap two-col">
      <div>
        <div class="eyebrow">Yakında</div>
        <h2 style="font-family:var(--serif); font-size:30px; margin:16px 0 18px">Podcast yolda</h2>
        <p style="color:var(--ink-soft)">İletişim, diksiyon, beden dili ve sunum sanatı üzerine sohbetler yapacağım bir podcast üzerinde çalışıyorum. Yayınlandığında ilk siz haberdar olun.</p>
      </div>
      <form class="card-form" action="https://api.web3forms.com/submit" method="POST">
        <input type="hidden" name="access_key" value="YOUR-WEB3FORMS-KEY">
        <input type="hidden" name="subject" value="Podcast Bildirim Listesi">
        <div class="field"><label>E-posta</label><input type="email" name="email" required placeholder="ornek@eposta.com"></div>
        <button class="btn voice" type="submit">Haberdar Olmak İstiyorum</button>
      </form>
    </div>
  </section>

  <section id="blog" class="tint">
    <div class="wrap">
      <div class="section-head">
        <div class="eyebrow">Blog</div>
        <h2>Son yazılar</h2>
      </div>
      <div class="post-list">
        <a class="post-row" href="blog.html">
          <span class="date">24.01.2018</span>
          <div><h3>İletişim eğitimi neden gerekli?</h3><p>Kurum içi motivasyon, verim ve iş tatmini üzerinde iletişimin etkisi.</p></div>
        </a>
        <a class="post-row" href="blog.html">
          <span class="date">16.01.2018</span>
          <div><h3>Konuşma hızının nedenleri</h3><p>Hızlı ya da yavaş konuşmanın altında yatan nedenler üzerine.</p></div>
        </a>
      </div>
    </div>
  </section>

  <section id="iletisim" class="dark" style="text-align:center; padding:90px 0">
    <div class="wrap">
      <div class="eyebrow" style="justify-content:center">Birlikte Çalışalım</div>
      <h2 style="font-family:var(--serif); font-weight:600; font-size:clamp(28px,4vw,44px); color:var(--paper); margin:16px 0 28px; max-width:22ch; margin-left:auto; margin-right:auto">Kurumunuz için bir eğitim mi planlıyorsunuz?</h2>
      <a href="egitim-basvuru.html" class="btn voice">Eğitim Başvurusu Yapın</a>
      <a href="iletisim.html" class="btn outline" style="border-color:#5b5647; color:var(--paper)">İletişime Geçin</a>
    </div>
  </section>
''')

# ---------- eğitimlerimiz ----------
egitimlerimiz_list = "\n".join(
    f'<li><span class="num">{i:02d}</span><a href="{href}" style="text-decoration:none;color:inherit;font-weight:600">{label}</a></li>'
    for i, (href, label, _c) in enumerate(TRAININGS, 1)
)
pages["egitimlerimiz.html"] = page_shell(
    "Eğitimlerimiz", "egitimlerimiz.html",
    breadcrumb='<a href="index.html">Ana Sayfa</a> / Eğitimlerimiz',
    eyebrow="Kurumsal &amp; Bireysel",
    body_html=f'''
  <section>
    <div class="wrap two-col">
      <div class="content-block">
        <h2>Kurumsal Eğitimlerimiz</h2>
        <p>Şirket içi ekiplere, kamu kurumlarına ve mağaza personeline yönelik, uygulamalı ve kurum ihtiyacına göre revize edilebilen sekiz eğitim başlığı.</p>
        <ul class="syllabus">{egitimlerimiz_list}</ul>
        <h2 style="margin-top:40px">Bireysel Eğitimlerimiz</h2>
        <p>Diksiyon, Beden Dili Kullanımı, Sunum Teknikleri, İletişim Teknikleri ve Empati konularında bireysel eğitim de veriyoruz.</p>
        <div class="pdf-list">
          <a href="docs/egitim-katalogu-2019.pdf">📄 Eğitim Kataloğu 2019</a>
          <a href="docs/egitim-katalogu-2013.pdf">📄 Eğitim Kataloğu 2013</a>
        </div>
      </div>
      <aside>
        <form class="card-form" action="https://api.web3forms.com/submit" method="POST">
          <input type="hidden" name="access_key" value="YOUR-WEB3FORMS-KEY">
          <div class="field"><label>Ad Soyad</label><input type="text" name="name" required></div>
          <div class="field"><label>E-posta</label><input type="email" name="email" required></div>
          <div class="field"><label>Mesajınız</label><textarea name="message"></textarea></div>
          <button class="btn voice" type="submit">Bilgi İsteyin</button>
        </form>
      </aside>
    </div>
  </section>
''')

# ---------- training subpages ----------
TRAINING_CONTENT = {
    "etkili-iletisim-teknikleri.html": dict(
        nicin="İş dünyasında iç ve dış müşterilerle sorunlarınızı azaltmak veya rakiplerinizden bir adım önde olmak istiyorsanız, önceliklerinizden biri iletişim teknikleri üzerine kendinizi yenilemenizdir. Bu eğitimin amacı, profesyonel hayatınızda ilişkilerinizi doğru yönlendirmenizi, başarılı ve mutlu bir iş hayatına kavuşmanızı sağlamaktır.",
        icerik=["Doğru Diksiyon ile ilgili bilgi", "Doğru nefes kullanımı", "Nefes egzersizleri",
                "Harf kullanımı ve konuşma sorunlarının tespiti", "Sözcük ve cümle kullanımı",
                "Konuşmada duraklar ve vurgular", "Boğumlanma ve bükümlülük",
                "Genel anlatım bozukluklarının paylaşılması", "Okuma ve konuşma egzersizleri"],
    ),
    "etkili-sunum-teknikleri.html": dict(
        nicin="Günümüzde pek çok çalışan üstüne, astına, çalışma arkadaşlarına ya da müşterilerine karşı tanıtım ya da benzeri amaçlarla sunum yapmak durumunda kalmaktadır. Bu eğitim dinleyicileri etkilemenin ve ikna etmenin yollarını göstererek etkili bir sunuş için gereken bilgileri pratikler eşliğinde öğrenmeyi amaçlamaktadır.",
        icerik=["Sunum içeriği", "Sunum öncesi hazırlıklar", "Sunum araçlarının kullanımı",
                "Sunum içeriğinin hazırlanması", "Sunumu hikayelendirme", "Türkçenin doğru kullanımı",
                "İtiraz ve soru karşılama", "Heyecan ile başa çıkabilme", "Beden dilinin doğru kullanımı",
                "Kapanış teknikleri"],
    ),
    "diksiyon.html": dict(
        nicin="Bu eğitimin amacı katılımcıların günlük iletişim becerilerinde yaşadıkları ve farkında olmadıkları sorunları belirleyebilmek, unutulan bazı konuşma kurallarını hatırlatmak, daha sağlıklı iletişim kurabilmelerini sağlamaktır.",
        icerik=["Doğru diksiyon ile ilgili kısa bilgi", "Doğru nefes kullanımı", "Nefes egzersizleri",
                "Alfabeye yeniden bakış", "Harf kullanımı ve konuşma sorunlarının tespiti",
                "Sözcük ve cümle kullanımı", "Konuşmada duraklar ve vurgular", "Boğumlanma ve bükümlülük",
                "Genel anlatım bozukluklarının paylaşılması", "Okuma ve konuşma egzersizleri"],
    ),
    "beden-dili-egitimi.html": dict(
        nicin="Bu eğitimin amacı katılımcıların günlük iletişim becerilerinde beden dillerini daha aktif, doğru biçimde kullanabilmelerini ve sözel olmayan işaret ve hareketlerin bilincine varılmasını sağlamaktır.",
        icerik=["Beden dili iletişimi ile ilgili temel bilgi", "Beden dili öğeleri", "Bölgeler ve kullanımı",
                "Bakışlar ve duruşlar", "İş hayatında bedenin kullanımı", "Yalana farklı bakış açısı",
                "Katılımcılarla egzersizler"],
    ),
    "etkili-konusma-teknikleri.html": dict(
        nicin="Doğru bir diksiyon ile topluluk karşısında, anlaşılır ve kendine güvenir bir şekilde konuşma yapabilmeniz için hazırlanmış bir eğitimdir. Grup ile birlikte uygulamalı çalışmalardır.",
        icerik=["Doğru diksiyon", "Nefes egzersizleri", "Konuşmada duraklar ve vurgular",
                "Boğumlanma ve bükümlülük", "Genel anlatım bozuklukları", "Bedenin kullanımı",
                "Okuma ve konuşma egzersizleri"],
    ),
    "vatandas-ic-musteri-empati.html": dict(
        nicin="Bu eğitimin amacı katılımcıların günlük iletişimde anlama ve iletişimi yönetebilme becerilerini ilerletebilmelerini sağlamaktır. Bedenin verdiği mesajlarla karşıdaki kişiyle daha sağlıklı iletişim kurabilmelerini sağlamaktır.",
        icerik=["Empati ve sempati", "Benlik analizi", "İletişimde olduğunu tanıma",
                "Yalan ve anlaşılma halleri", "Renklerin dili", "Çatışma ve çözümleri", "İkna"],
    ),
    "reyon-gorevlisi-egitimi.html": dict(
        nicin="Bu eğitimin amacı, katılımcıların modern perakendecilikte günlük iletişimlerini değiştirme, müşteri bazlı yaklaşımlarını sağlamaktır. Bu eğitim sayesinde katılımcılar müşteri ile iletişimlerini arttırırken takım olma yolunda ciddi adımlar atacaklar.",
        icerik=["Merchandising nedir", "Modern perakendecilik", "İletişim hataları", "Empati",
                "Müşteri kimdir ve ne ister?", "Takım olabilmek", "Mağaza uygulamaları", "Çatışma ve çözümleri"],
    ),
    "ekipte-lider-olabilme.html": dict(
        nicin="Bu eğitimin amacı, katılımcıların özeleştiri yaparak lider ve takım olabilmenin farkındalığını arttırmaktır. Bu sayede aklın, tekniğin ve duygusal zekanın içinde bulunduğu bir eğitimle katılımcılar içindeki doğru enerjiye ulaşacaktır.",
        icerik=["Özeleştiri ve farkındalık", "Lider ve takım olabilme", "Duygusal zeka",
                "Grup uygulamaları"],
    ),
}

for href, label, cover in TRAININGS:
    data = TRAINING_CONTENT[href]
    pages[href] = page_shell(
        label, href,
        breadcrumb=f'<a href="index.html">Ana Sayfa</a> / <a href="egitimlerimiz.html">Eğitimlerimiz</a> / {label}',
        eyebrow="Kurumsal Eğitim",
        cover=cover,
        meta_desc=SITE_DESC,
        body_html=training_body(data["nicin"], data["icerik"], cover).replace("{{TITLE}}", label)
    )

# ---------- hakkımda ----------
pages["hakkimda.html"] = page_shell(
    "Hakkımda", "hakkimda.html",
    breadcrumb='<a href="index.html">Ana Sayfa</a> / Hakkımda',
    eyebrow="Burak Özbay",
    cover="hakkimda.jpg",
    body_html='''
  <section>
    <div class="wrap content-block">
      <p>1975 İstanbul doğumluyum. Cumhuriyet Lisesi ve Anadolu Üniversitesi Kamu Yönetimi mezunuyum.</p>
      <ul class="syllabus">
        <li><span class="num">97</span><span><strong>1997–1999:</strong> Garanti Bankası AGF Sigorta, pazarlama / müşteri temsilcisi.</span></li>
        <li><span class="num">99</span><span><strong>1999–2006:</strong> Bayrak Radyo Televizyon Kurumu — sunucu, yönetmen, programcı. TRT Eğitim Dairesi'nin Kıbrıs'taki diksiyon ve sunum eğitimlerine katıldım. Türk Hava Kurumu için 2 yıllık bir TV programı hazırladım. "Eğitime Farklı Bakış" programını yönettim.</span></li>
        <li><span class="num">06</span><span><strong>2006–2009:</strong> İstanbul'da Rumeli Televizyonu'nu kurdum, genel müdürlüğünü yaptım. "Seçime Doğru" ve "Meclise Doğru" programlarını hazırladım.</span></li>
        <li><span class="num">09</span><span><strong>2009–2011:</strong> Saha Pazarlama ve Organizasyon Şirketi'nde proje uzmanı olarak çalıştım.</span></li>
        <li><span class="num">+</span><span>TRT, Star TV, Kanal D, NOW, ATV ve TV8 gibi kanallarda yönetmenlik ve editörlük yaptım (Ben Bilmem Eşim Bilir, Çarkıfelek, Karavan, Big Brother, Utopia, Doya Doya Moda, Zahide Yetiş ile Yeniden Başlasak).</span></li>
        <li><span class="num">04</span><span><strong>2004'ten beri</strong> kurumsal eğitim planları hazırlayıp sunuyorum.</span></li>
      </ul>
      <div class="two-col" style="margin-top:20px">
        <div>
          <h2>Vizyon</h2>
          <p>Uzmanlık alanlarımla firmalarda gerçekleştirdiğim çalışmalarla akılda kalan, kendi tarzını ortaya koyabilen bir yapıya sahip olmak.</p>
        </div>
        <div>
          <h2>Misyon</h2>
          <p>Hızlı hareket eden, sürekliliği olan, gelişimi devam eden, yenilikleri uygulayan bir yapıda hareket etmek.</p>
        </div>
      </div>
    </div>
  </section>
''')

# ---------- referanslar ----------
pages["referanslar.html"] = page_shell(
    "Referanslar", "referanslar.html",
    breadcrumb='<a href="index.html">Ana Sayfa</a> / Referanslar',
    eyebrow="Birlikte Çalıştığımız Kurumlar",
    body_html='''
  <section>
    <div class="wrap">
      <div class="logo-row">
        <div class="ph">Yapı Kredi<br>Bankası</div>
        <div class="ph">İstanbul Emniyet<br>Müdürlüğü</div>
        <div class="ph">İstanbul Büyükşehir<br>Belediyesi</div>
        <div class="ph">Devlet Su<br>İşleri</div>
        <div class="ph">As Ecza<br>Deposu</div>
        <div class="ph">Gürsel<br>Turizm</div>
      </div>
      <p style="margin-top:34px; color:var(--ink-soft)">Logo görsellerini eklemek için <code>images/logos/</code> klasörüne dosyaları koyup <code>referanslar.html</code> içindeki <code>.ph</code> kutularını <code>&lt;img&gt;</code> ile değiştirin.</p>
      <a href="fotograflar.html" class="btn outline" style="margin-top:10px">Eğitim Fotoğraflarını Görün →</a>
    </div>
  </section>
''')

# ---------- fotoğraflar ----------
GALLERY_GROUPS = [
    ("As Ecza Deposu'nda eğitimdeyiz", 3, "as-ecza"),
    ("Gürsel Turizm'de eğitimdeyiz", 3, "gursel-turizm"),
    ("Devlet Su İşleri'nde eğitimdeydik", 7, "dsi"),
    ("Yaratıcı Çocuklar Derneği — Edirne Güzel Sanatlar Lisesi", 6, "edirne"),
    ("İstanbul Emniyet Müdürlüğü'nde eğitimdeydik", 6, "emniyet"),
    ("İstanbul Büyükşehir Belediyesi'nde eğitimdeydik", 6, "ibb"),
]
gallery_html = ""
for title, count, slug in GALLERY_GROUPS:
    thumbs = "\n".join(
        f'<div class="ph"><img src="images/gallery/{slug}-{i}.jpg" alt="{title}" loading="lazy" '
        f'onerror="this.parentElement.textContent=\'{slug}-{i}.jpg\'"></div>'
        for i in range(1, count+1)
    )
    gallery_html += f'<div class="gallery-group"><h3>{title}</h3><div class="gallery-grid">{thumbs}</div></div>\n'

pages["fotograflar.html"] = page_shell(
    "Fotoğraflar", "referanslar.html",
    breadcrumb='<a href="index.html">Ana Sayfa</a> / <a href="referanslar.html">Referanslar</a> / Fotoğraflar',
    eyebrow="Eğitimlerden Kareler",
    body_html=f'<section><div class="wrap">{gallery_html}</div></section>'
)

# ---------- blog ----------
BLOG_POSTS = [
    ("konusmada-lelestirme-hatasi.html", "Konuşmada 'Leleştirme' Hatası", "13.09.2018",
     "Günlük konuşmada sıkça yapılan, kelimelerin sonundaki seslerin yutulması ya da gereksiz uzatılmasıyla oluşan 'leleştirme' hatası ve bunun önüne geçmenin yolları üzerine kısa bir not."),
    ("iletisim-egitimi-neden-gerekli.html", "İletişim Eğitimi Neden Gerekli?", "24.01.2018",
     "Kurum içi motivasyon, çalışan verimliliği ve iş tatmini üzerinde sağlıklı iletişimin etkisi; iletişim eksikliğinin kurumlara maliyeti üzerine bir değerlendirme."),
    ("konusma-hizinin-nedenleri.html", "Konuşma Hızının Nedenleri", "16.01.2018",
     "Kimi insanlar neden çok hızlı, kimileri neden çok yavaş konuşur? Nörolojik, bölgesel ve kişisel geçmişe dayalı nedenleriyle konuşma hızı üzerine bir inceleme."),
]

blog_rows = "\n".join(
    f'''<a class="post-row" href="{slug}">
      <span class="date">{date}</span>
      <div><h3>{title}</h3><p>{excerpt}</p></div>
    </a>''' for slug, title, date, excerpt in BLOG_POSTS
)
pages["blog.html"] = page_shell(
    "Blog", "blog.html",
    breadcrumb='<a href="index.html">Ana Sayfa</a> / Blog',
    eyebrow="Yazılar",
    body_html=f'<section><div class="wrap"><div class="post-list">{blog_rows}</div></div></section>'
)

for slug, title, date, excerpt in BLOG_POSTS:
    pages[slug] = page_shell(
        title, "blog.html",
        breadcrumb=f'<a href="index.html">Ana Sayfa</a> / <a href="blog.html">Blog</a> / {title}',
        eyebrow=f"Yazı · {date}",
        body_html=f'''<section><div class="wrap content-block">
          <p>{excerpt}</p>
          <p style="margin-top:20px; padding:16px; background:var(--paper-dim); border-left:3px solid var(--voice); font-size:14px">
          Bu yazının tam metni eski Weebly sitesinden aktarılacak — CSV içindeki <code>blog_post.csv</code> dosyasında
          orijinal içerik mevcut, isterseniz bir sonraki adımda birebir işleyelim.</p>
          <a href="blog.html" class="btn outline" style="margin-top:10px">← Tüm Yazılar</a>
        </div></section>'''
    )

# ---------- iletişim ----------
pages["iletisim.html"] = page_shell(
    "İletişim", "iletisim.html",
    breadcrumb='<a href="index.html">Ana Sayfa</a> / İletişim',
    eyebrow="Bize Ulaşın",
    body_html='''
  <section>
    <div class="wrap two-col">
      <div class="content-block">
        <h2>Sorularınız mı var?</h2>
        <p>Kurumunuz için eğitim planlamak, teklif almak ya da genel bir soru sormak için formu doldurabilir, ya da sosyal medya hesaplarımızdan ulaşabilirsiniz.</p>
        <div style="margin-top:24px; display:flex; gap:16px; flex-wrap:wrap">
          <a href="https://facebook.com/burak.ozbay.12" class="btn outline">Facebook</a>
          <a href="https://twitter.com/BurakOzbay7" class="btn outline">Twitter</a>
          <a href="https://instagram.com/ozburakbay" class="btn outline">Instagram</a>
          <a href="https://linkedin.com/in/burak-özbay-0091374a" class="btn outline">LinkedIn</a>
        </div>
      </div>
      <form class="card-form" action="https://api.web3forms.com/submit" method="POST">
        <input type="hidden" name="access_key" value="YOUR-WEB3FORMS-KEY">
        <div class="field"><label>Ad</label><input type="text" name="name" required></div>
        <div class="field"><label>E-posta</label><input type="email" name="email" required></div>
        <div class="field"><label>Yorumunuz</label><textarea name="message" required></textarea></div>
        <button class="btn voice" type="submit">Gönder</button>
        <p class="form-note">Form gönderimleri Web3Forms üzerinden doğrudan e-postanıza düşer — kurulum notu için README dosyasına bakın.</p>
      </form>
    </div>
  </section>
''')

# ---------- eğitim takvimi ----------
pages["egitim-takvimi.html"] = page_shell(
    "Eğitim Takvimi", "egitim-takvimi.html",
    breadcrumb='<a href="index.html">Ana Sayfa</a> / Eğitim Takvimi',
    eyebrow="Yaklaşan Eğitimler",
    body_html='''
  <section>
    <div class="wrap">
      <div style="padding:14px 18px; background:var(--paper-dim); border-left:3px solid var(--voice); margin-bottom:30px; font-size:14px">
        Bu sayfadaki eski (2019) tarihli eğitimler örnek olarak bırakıldı — yeni tarihlerle güncellenmesi gerekiyor.
      </div>
      <div class="timeline">
        <div class="row"><span class="d">16 Şub 2019</span><div><h4>Diksiyon Semineri</h4><span class="meta">1 gün · maks. 20 katılımcı</span></div><span class="tag">Örnek</span></div>
        <div class="row"><span class="d">23 Şub 2019</span><div><h4>Beden Dili Eğitimi</h4><span class="meta">1 gün · maks. 20 katılımcı</span></div><span class="tag">Örnek</span></div>
        <div class="row"><span class="d">24 Şub 2019</span><div><h4>Sunum Teknikleri Eğitimi</h4><span class="meta">2 gün · maks. 15 katılımcı</span></div><span class="tag">Örnek</span></div>
      </div>
      <a href="egitim-basvuru.html" class="btn voice" style="margin-top:34px">Eğitim Başvurusu Yapın</a>
    </div>
  </section>
''')

# ---------- eğitim başvuru ----------
pages["egitim-basvuru.html"] = page_shell(
    "Eğitim Başvuru", "egitim-takvimi.html",
    breadcrumb='<a href="index.html">Ana Sayfa</a> / <a href="egitim-takvimi.html">Eğitim Takvimi</a> / Eğitim Başvuru',
    eyebrow="Bireysel Eğitim Başvuru Formu",
    body_html='''
  <section>
    <div class="wrap" style="max-width:640px">
      <form class="card-form" action="https://api.web3forms.com/submit" method="POST">
        <input type="hidden" name="access_key" value="YOUR-WEB3FORMS-KEY">
        <div class="field"><label>Ad Soyad</label><input type="text" name="name" required></div>
        <div class="field"><label>E-posta</label><input type="email" name="email" required></div>
        <div class="field"><label>Telefon</label><input type="tel" name="phone" required></div>
        <div class="field">
          <label>Eğitim Konusu</label>
          <select name="egitim_konusu">
            <option>Diksiyon</option>
            <option>Beden Dili</option>
            <option>Etkili İletişim</option>
            <option>Sunum Teknikleri</option>
          </select>
        </div>
        <div class="field" style="display:flex; align-items:center; gap:10px">
          <input type="checkbox" name="pazarlama_izni" style="width:auto" id="izin">
          <label for="izin" style="margin:0; font-weight:400">Pazarlama ve bilgilendirme e-postaları almak istiyorum</label>
        </div>
        <button class="btn voice" type="submit">Başvuruyu Gönder</button>
      </form>
    </div>
  </section>
''')

# ---------------------------------------------------------------- write

for filename, html in pages.items():
    with open(os.path.join(OUT, filename), "w", encoding="utf-8") as f:
        f.write(html)

print(f"{len(pages)} sayfa oluşturuldu.")
