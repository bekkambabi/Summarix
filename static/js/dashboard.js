const form = document.getElementById("summaryForm");
const loading = document.getElementById("loading");

// ================= Loading =================

if (form) {

    form.addEventListener("submit", function () {

        loading.style.display = "block";

    });

}

// ================= Copy =================

const copyBtn = document.getElementById("copyBtn");

if (copyBtn) {

    copyBtn.addEventListener("click", function () {

        const text = document.getElementById("summaryText").innerText;

        navigator.clipboard.writeText(text);

        alert("Summary copied!");

    });

}

// ================= Download =================

const downloadBtn = document.getElementById("downloadBtn");

if (downloadBtn) {

    downloadBtn.addEventListener("click", function () {

        const text = document.getElementById("summaryText").innerText;

        const blob = new Blob([text], {
            type: "text/plain"
        });

        const link = document.createElement("a");

        link.href = URL.createObjectURL(blob);

        link.download = "summary.txt";

        link.click();

    });

}

// ================= Word Counter =================

const textInput = document.getElementById("textInput");

const wordCount = document.getElementById("wordCount");

const charCount = document.getElementById("charCount");

if (textInput) {

    textInput.addEventListener("input", () => {

        const text = textInput.value.trim();

        const words = text === ""
            ? 0
            : text.split(/\s+/).length;

        wordCount.innerHTML = "Words : " + words;

        charCount.innerHTML = "Characters : " + text.length;

    });

}

// ================= Clear =================

const clearBtn = document.getElementById("clearSummaryBtn");

if (clearBtn) {

    clearBtn.addEventListener("click", () => {

        window.location.href = "/summarize";

    });

}