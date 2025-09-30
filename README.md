Fraud Mini Project

Bu proje Kaggle’dan aldığım bir veri seti ile sigorta dolandırıcılıgı (fraud detection) üzerine temel veri analizi ve görsellestirme çalışmasıdır.
data/ → Veri seti (worksheet.xlsx)

Proje klasörünü ve alt klasörleri hazırladım
Sanal ortam oluşturdum (python3 -m venv venv)
Gerekli kütüphaneleri yükledim (pandas, matplotlib, seaborn, openpyxl, jupyter)
Excel dosyasını Pythona yükledim

Grafiklerle veri analizini yaptım ve outputs/ klasörüne kaydettim:
Yaş dağılımı → age_distribution.png
Toplam talep miktarı → total_claim_amount_distribution.png
Fraud rapor sayıları → fraud_reported_counts.png
Olay şiddeti dağılımı → incident_severity_distribution.png
Eyaletlere göre poliçe sayısı → policies_per_state.png
Cinsiyete göre dolandırıcılık → fraud_by_gender.png
Eğitim seviyesine göre dolandırıcılık → fraud_by_education.png
