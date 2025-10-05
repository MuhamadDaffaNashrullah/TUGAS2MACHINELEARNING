from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd
import os

app = Flask(__name__)

# Load model
model = joblib.load("model_score.pkl")

# Nilai R2 dan RMSE dari hasil training model
R2_SCORE = 0.9708871356050831  # Nilai aktual dari notebook
RMSE_SCORE = 4.124008274830024  # Nilai aktual dari notebook

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    duration_input = None
    
    if request.method == "POST":
        try:
            # Ambil input durasi belajar dari form
            duration_input = float(request.form.get("Hours"))
            
            # Prediksi nilai belajar menggunakan model
            # Model di-train dengan DataFrame, jadi kita perlu menggunakan DataFrame dengan nama kolom
            input_data = pd.DataFrame([[duration_input]], columns=['Hours'])
            prediction = model.predict(input_data)[0]
            prediction = round(prediction, 2)
            
        except (ValueError, TypeError):
            prediction = "Error: Masukkan angka yang valid"
    
    return render_template(
        "index.html",
        prediction=prediction,
        duration=duration_input,
        r2=R2_SCORE,
        rmse=RMSE_SCORE
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)