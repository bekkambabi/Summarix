from flask import Flask, render_template, request
from transformers import pipeline
from deep_translator import GoogleTranslator
import PyPDF2

app = Flask(__name__)

summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

# Temporary storage (we'll improve this later)
latest_summary = ""
original_words = 0
summary_words = 0
compression = 0


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
# Text Summarizer
# -----------------------
@app.route("/summarize", methods=["GET", "POST"])
def summarize():

    global latest_summary
    global original_words
    global summary_words
    global compression

    summary = ""

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

        latest_summary = summary

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


# -----------------------
# Translation
# -----------------------
@app.route("/translate", methods=["POST"])
def translate():

    global latest_summary
    global original_words
    global summary_words
    global compression

    language = request.form.get("language")

    language_map = {
        "English": "en",
        "Telugu": "te",
        "Hindi": "hi",
        "Tamil": "ta",
        "Kannada": "kn",
        "Malayalam": "ml"
    }

    if language == "English":
        translated_summary = latest_summary

    else:

        translated_summary = GoogleTranslator(
            source="auto",
            target=language_map[language]
        ).translate(latest_summary)

    return render_template(
        "summarize.html",
        summary=translated_summary,
        original_words=original_words,
        summary_words=len(translated_summary.split()),
        compression=compression
    )


# -----------------------
# Future Pages
# -----------------------
@app.route("/pdf", methods=["GET", "POST"])
def pdf():

    summary = ""
    original_words = 0
    summary_words = 0
    compression = 0

    if request.method == "POST":

        pdf_file = request.files["pdf"]

        pdf_reader = PyPDF2.PdfReader(pdf_file)

        text = ""

        for page in pdf_reader.pages:

            extracted = page.extract_text()

            if extracted:
                text += extracted + "\n"

        if text.strip():

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
        "pdf.html",
        summary=summary,
        original_words=original_words,
        summary_words=summary_words,
        compression=compression
    )


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