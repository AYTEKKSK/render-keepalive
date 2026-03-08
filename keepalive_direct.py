import requests
import time

# Use direct .onrender.com URLs since Render free tier only supports 2 custom domains
urls = [
    "https://metal-app-ocvv.onrender.com/",
    "https://video-app-pqii.onrender.com/",
    "https://doviz-app.onrender.com/",
    "https://ceviri-app.onrender.com/",
    "https://haberler-app.onrender.com/",
    "https://imsakiye-app.onrender.com/",
    "https://namaz-app.onrender.com/",
    "https://ocr-analiz-app.onrender.com/",
    "https://yapay-zeka-app.onrender.com/",
    "https://yemek-app.onrender.com/",
    "https://gorsel-app.onrender.com/",
    "https://dosya-analizi-app.onrender.com/",
    "https://donusturucu-app.onrender.com/",
    "https://muzik-app-7q6u.onrender.com/",
    "https://hava-durumu-app-j89a.onrender.com/"
]

while True:
    for url in urls:
        try:
            r = requests.get(url, timeout=30)
            print(f"{url} - {r.status_code}", flush=True)
        except Exception as e:
            print(f"{url} - ERROR: {e}", flush=True)
    
    # Wait 10 minutes before next round
    time.sleep(600)
