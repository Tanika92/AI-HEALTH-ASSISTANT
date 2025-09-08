async function getAdvice() {
    const symptoms = document.getElementById("symptoms").value;
    const responseDiv = document.getElementById("response");
    responseDiv.innerHTML = "⏳ Analyzing...";
    
    const res = await fetch("/advice", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({symptoms: symptoms})
    });
    
    const data = await res.json();
    responseDiv.innerHTML = "💡 " + data.advice;
}
