const response = await fetch("http://localhost:5000/predict", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify(data)
});

const result = await response.json();
resultDiv.innerText = `🏆 Predicted Winner: ${result.prediction}`;
console.log("Sending data:", data);
console.log("Received result:", result);
