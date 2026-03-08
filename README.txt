RENDER UYGULAMALARINI ÇALIŞTIRMA - ÇÖZÜM DOKÜMANI
=====================================================

SORUN:
------
- Render Free Tier sadece 2 custom domain destekliyor
- 15 uygulama var, hepsi için custom domain MÜMKÜN DEĞİL
- Cloudflare Worker API token'ı Worker yetkisine sahip değil

ÇÖZÜMLER:
---------

### ÇÖZÜM 1: Direct .onrender.com URLs (ŞİMDİ ÇALIŞIR) ✓

Keep-alive scripti direct Render URLlerini kullanacak:
- https://doviz-app.onrender.com/
- https://video-app-pqii.onrender.com/
- https://metal-app-ocvv.onrender.com/
- vb.

Avantajlar:
+ Hemen çalışır, ekstra kurulum gerektirmez
+ Keep-alive script tüm uygulamaları uyanık tutar
+ Bedava, limitasyon yok

Dezavantajlar:
- Custom domain yok (uzun .onrender.com URLs)
- Branding yok

**NASIL KULLANILIR:**
1. GCP VM'ye SSH ile bağlan: https://console.cloud.google.com/compute/instances
2. Şu komutları çalıştır:

```bash
cd /home/aytekozdemir
git clone https://github.com/AYTEKKSK/render-keepalive.git temp-repo || (cd temp-repo && git pull)
cp temp-repo/keepalive_direct.py keepalive.py
sudo systemctl restart keepalive
sudo systemctl status keepalive
```

3. Test et:
```bash
sudo journalctl -u keepalive -f
```


### ÇÖZÜM 2: Cloudflare Worker + Custom Domains (TAM ÇÖZÜM) ✓

Custom domain'ler için Cloudflare Worker kullan:
- https://metal.articnc.online/ ✓
- https://hava.articnc.online/ ✓
- https://doviz.articnc.online/ ✓
- vb.

Avantajlar:
+ Kısa, güzel URLs
+ Custom branding
+ Tüm subdomainler çalışır

Dezavantajlar:
- Manuel Cloudflare Worker kurulumu gerekir (tek seferlik)

**NASIL KURULUR:**
Detaylı talimatlar için: `WORKER_KURULUM.txt` dosyasına bak

KISA ÖZET:
1. https://dash.cloudflare.com → Workers & Pages
2. Create Worker → İsim ver (articnc-router)
3. Edit code → `cloudflare-worker.js` içeriğini yapıştır
4. Save and Deploy
5. Settings → Triggers → Her subdomain için route ekle:
   - metal.articnc.online/*
   - hava.articnc.online/*
   - doviz.articnc.online/*
   - ... (15 tane)


DOSYALAR:
---------
✓ cloudflare-worker.js - Worker kodu (hazır)
✓ WORKER_KURULUM.txt - Detaylı kurulum talimatları
✓ keepalive_direct.py - Direct URLs için keep-alive script
✓ keepalive.py - Custom domains için keep-alive script
✓ deploy_worker.py - Worker API deployment (token yetkisi yok, çalışmıyor)


MEVCUT DURUM:
-------------
✓ 15 Render servisi aktif ve çalışıyor
✓ GCP VM (e2-micro) çalışıyor, keepalive servisi aktif
✓ Cloudflare DNS kayıtları eklendi (15 CNAME)
✓ DNS kayıtları proxied=true (Worker için hazır)
✓ GitHub repo güncellendi

EKSIKLER:
---------
⚠️ Cloudflare Worker manuel kurulumu gerekiyor (API token yetkisi yok)
⚠️ GCP VM'deki keepalive.py dosyası güncellenmeli

TAVSİYE:
--------
1. HIZLI: keepalive_direct.py kullan (5 dk) → .onrender.com URLs
2. TAM: Worker kur (30 dk) → custom domains

Her iki durumda da uygulamalar çalışacak!
