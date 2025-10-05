# Prediksi Nilai Belajar - Machine Learning Web App

Aplikasi web Flask untuk memprediksi nilai belajar berdasarkan durasi belajar menggunakan model machine learning.

## Fitur

- Prediksi nilai belajar berdasarkan input durasi belajar
- Visualisasi data dengan berbagai grafik dan plot
- Metrik evaluasi model (R² Score dan RMSE)
- Interface yang user-friendly dengan Bootstrap

## Teknologi yang Digunakan

- **Backend**: Flask (Python)
- **Machine Learning**: scikit-learn, pandas, numpy
- **Frontend**: HTML, CSS, Bootstrap 5
- **Visualisasi**: Matplotlib/Seaborn (pre-generated plots)

## Deployment ke Railway

### Langkah-langkah Deployment:

1. **Siapkan Repository Git**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```

2. **Push ke GitHub**
   ```bash
   git remote add origin <your-github-repo-url>
   git push -u origin main
   ```

3. **Deploy ke Railway**
   - Buka [Railway.app](https://railway.app)
   - Login dengan akun GitHub
   - Klik "New Project"
   - Pilih "Deploy from GitHub repo"
   - Pilih repository yang sudah dibuat
   - Railway akan otomatis mendeteksi aplikasi Python dan melakukan deployment

### File Konfigurasi untuk Railway:

- `requirements.txt` - Dependencies Python
- `Procfile` - Web process configuration
- `runtime.txt` - Python version specification
- `app.py` - Main Flask application (sudah dimodifikasi untuk Railway)

### Struktur Project:

```
├── app.py                 # Main Flask application
├── model_score.pkl        # Trained ML model
├── requirements.txt       # Python dependencies
├── Procfile              # Railway configuration
├── runtime.txt           # Python version
├── templates/
│   └── index.html        # Main template
├── static/               # Static files (images)
│   ├── distribusi hours.png
│   ├── distribusi scores.png
│   ├── grafik prediksi.png
│   ├── heatmap korelasi.png
│   ├── residualplot.png
│   └── scarletplot.png
└── README.md             # Documentation
```

## Menjalankan Aplikasi Lokal

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Jalankan Aplikasi**
   ```bash
   python app.py
   ```

3. **Akses Aplikasi**
   - Buka browser dan kunjungi `http://localhost:5000`

## Model Machine Learning

Aplikasi ini menggunakan model machine learning yang sudah di-train untuk memprediksi nilai belajar berdasarkan durasi belajar. Model memiliki:
- **R² Score**: 0.9709 (97.09% variasi data dapat dijelaskan oleh model)
- **RMSE**: 4.12 (Root Mean Square Error)

## Kontribusi

Silakan fork repository ini dan submit pull request untuk perbaikan atau fitur baru.

## Lisensi

MIT License
