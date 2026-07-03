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

    if request.method == "POST":

        text = request.form["text"]

        result = summarizer(
            text,
            max_length=100,
            min_length=30,
            do_sample=False
        )

        summary = result[0]["summary_text"]

    return render_template(
        "summarize.html",
        summary=summary
    )


if __name__ == "__main__":
    app.run(debug=True)