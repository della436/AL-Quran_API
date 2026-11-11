from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    surat_list = []
    surat_detail = None
    error = None

    try:
        response = requests.get(
            "https://equran.id/api/v2/surat",
            timeout=15
        )
        response.raise_for_status()
        surat_list = response.json()["data"]

        if request.method == "POST":
            nomor = request.form.get("surat")

            response = requests.get(
                f"https://equran.id/api/v2/surat/{nomor}",
                timeout=15
            )
            response.raise_for_status()
            surat_detail = response.json()["data"]

    except requests.RequestException:
        error = "Data tidak bisa diambil. Periksa koneksi internet."

    return render_template(
        "index.html",
        surat_list=surat_list,
        surat_detail=surat_detail,
        error=error
    )

if __name__ == "__main__":
    app.run(debug=True)