import requests
import time

# Subdomain listenizi buraya ekleyin
urls = [
    "https://metal.articnc.online/",
    "https://video.articnc.online/",
    "https://doviz.articnc.online/",
    "https://ceviri.articnc.online/",
    "https://haberler.articnc.online/",
    "https://imsakiye.articnc.online/",
    "https://namaz.articnc.online/",
    "https://ocr_analiz.articnc.online/",
    "https://yapay_zeka.articnc.online/",
    "https://yemek.articnc.online/",
    "https://gorsel.articnc.online/",
    "https://dosya_analizi.articnc.online/",
    "https://donusturucu.articnc.online/",
    "https://muzik.articnc.online/",
    "https://hava_durumu.articnc.online/"
]

while True:
    for url in urls:
        try:
            r = requests.get(url, timeout=10)
            print(f"{url} - {r.status_code}")
        except Exception as e:
            print(f"{url} - ERROR: {e}")
    # 10 dakika bekle
    time.sleep(600)
