from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

# -----------------------
# Home Page
# -----------------------
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/choose")
def choose():
    return render_template("choose.html")

# -----------------------
# Summarizer Page
# -----------------------
@app.route("/summarize", methods=["GET", "POST"])
def summarize():

    summary = ""
    original_words = 0
    summary_words = 0
    compression = 0

    if request.method == "POST":

        text = request.form["text"]

        original_words = len(text.split())

        length = request.form.get("length")

        if length == "short":
            max_len = 60
            min_len = 20

        elif length == "medium":
            max_len = 120
            min_len = 40

        else:
            max_len = 200
            min_len = 80

        result = summarizer(
            text,
            max_length=max_len,
            min_length=min_len,
            do_sample=False
        )

        summary = result[0]["summary_text"]

        summary_words = len(summary.split())

        compression = round(
            ((original_words - summary_words) / original_words) * 100,
            1
        )

    return render_template(
        "summarize.html",
        summary=summary,
        original_words=original_words,
        summary_words=summary_words,
        compression=compression
    )



@app.route("/pdf")
def pdf():
    return "<h1>PDF Summarizer Coming Soon</h1>"


@app.route("/website")
def website():
    return "<h1>Website Summarizer Coming Soon</h1>"


@app.route("/youtube")
def youtube():
    return "<h1>YouTube Summarizer Coming Soon</h1>"


@app.route("/audio")
def audio():
    return "<h1>Audio Summarizer Coming Soon</h1>"

if __name__ == "__main__":
    app.run(debug=True)