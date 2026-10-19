# Maaş Tahmin Uygulaması (MLOps / Streamlit Deployment)

Aday deneyimi, yazılı sınav puanı ve mülakat puanına göre teklif edilecek maaşı tahmin eden bir
doğrusal regresyon modeli ve bu modeli uçtan uca kullanıma açan bir Streamlit web uygulaması.

Amaç yalnızca modeli eğitmek değil; **eğitilmiş modeli serileştirip (pickle) bağımsız bir uygulamadan
servis etmek** — yani basit bir MLOps/model-dağıtım akışını uçtan uca kurmaktı.

## Akış

1. `maas_tahmini_model.ipynb` — `hiring.csv` verisiyle veri temizliği (metinsel deneyim değerlerinin
   sayısallaştırılması, eksik değer doldurma) ve `LinearRegression` modelinin eğitilmesi, `maas.pkl`
   olarak diske kaydedilmesi.
2. `app.py` — kaydedilen modeli yükleyip Streamlit arayüzünden tecrübe/sınav/mülakat puanlarını alarak
   anlık maaş tahmini sunan web uygulaması.

## Kullanılan Teknolojiler

`python`, `pandas`, `scikit-learn`, `streamlit`, `pickle`

## Çalıştırma

```bash
pip install -r requirements.txt

# 1) Modeli eğit (maas.pkl üretir) — depoda hazır haliyle de mevcuttur
jupyter notebook maas_tahmini_model.ipynb

# 2) Streamlit uygulamasını başlat
streamlit run app.py
```
