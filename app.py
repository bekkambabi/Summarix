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

        result = summarizer(
            text,
            max_length=100,
            min_length=30,
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

if __name__ == "__main__":
    app.run(debug=True)