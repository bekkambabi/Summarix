const form = document.getElementById("summaryForm");
const loading = document.getElementById("loading");

if(form){

    form.addEventListener("submit",function(){

        loading.style.display="block";

    });

}

const copyBtn=document.getElementById("copyBtn");

if(copyBtn){

    copyBtn.addEventListener("click",function(){

        const text=document.getElementById("summaryText").innerText;

        navigator.clipboard.writeText(text);

        alert("Summary copied!");

    });

}

const downloadBtn=document.getElementById("downloadBtn");

if(downloadBtn){

    downloadBtn.addEventListener("click",function(){

        const text=document.getElementById("summaryText").innerText;

        const blob=new Blob([text],{type:"text/plain"});

        const link=document.createElement("a");

        link.href=URL.createObjectURL(blob);

        link.download="summary.txt";

        link.click();

    });

const textInput=document.getElementById("textInput");

const wordCount=document.getElementById("wordCount");

const charCount=document.getElementById("charCount");

textInput.addEventListener("input",()=>{

    const text=textInput.value.trim();

    const words=text===""
        ?0
        :text.split(/\s+/).length;

    wordCount.innerHTML="Words : "+words;

    charCount.innerHTML="Characters : "+text.length;

});

const clearBtn=document.getElementById("clearBtn");

clearBtn.addEventListener("click",()=>{

    textInput.value="";

    wordCount.innerHTML="Words : 0";

    charCount.innerHTML="Characters : 0";

});

}