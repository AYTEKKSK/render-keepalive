# Render Keepalive Script

Bu script, Render'daki Flask uygulamalarınızın uykuya geçmesini engellemek için her 10 dakikada bir tüm subdomainlere HTTP isteği gönderir.

## Kullanım

1. Gerekli paketleri yükleyin:
   ```bash
   pip install requests
   ```

2. Scripti başlatın:
   ```bash
   python keepalive.py
   ```

3. Subdomain listenizi `keepalive.py` dosyasında güncelleyebilirsiniz.

## Açıklama
- Script, listedeki tüm URL'lere her 10 dakikada bir GET isteği gönderir.
- Sunucuda arka planda çalıştırabilirsiniz.
- Çıktı olarak her isteğin durumunu terminalde gösterir.

## Not
- Render Free planında bu yöntem uygulamalarınızın uykuya geçmesini engeller.
- Render'ın kullanım şartlarını ihlal etmemeye dikkat edin.
