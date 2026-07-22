const pdfInput = document.getElementById("pdfFile");
const fileName = document.getElementById("fileName");

if (pdfInput) {

    pdfInput.addEventListener("change", function () {

        if (this.files.length > 0) {

            fileName.textContent = this.files[0].name;

        } else {

            fileName.textContent = "No file selected";

        }

    });

}