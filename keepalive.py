import requests
import time

urls = [
    "https://metal.articnc.online/",
    "https://video.articnc.online/",
    "https://doviz.articnc.online/",
    "https://ceviri.articnc.online/",
    "https://haberler.articnc.online/",
    "https://imsakiye.articnc.online/",
    "https://namaz.articnc.online/",
    "https://ocr.articnc.online/",
    "https://yapay.articnc.online/",
    "https://yemek.articnc.online/",
    "https://gorsel.articnc.online/",
    "https://dosya.articnc.online/",
    "https://donusturucu.articnc.online/",
    "https://muzik.articnc.online/",
    "https://hava.articnc.online/"
]

while True:
    for url in urls:
        try:
            r = requests.get(url, timeout=10)
            print(f"{url} - {r.status_code}", flush=True)
        except Exception as e:
            print(f"{url} - ERROR: {e}", flush=True)
    time.sleep(600)
