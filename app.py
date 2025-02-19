from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load GPT-2 Model
generator = pipeline("text-generation", model="gpt2")

@app.route("/generate", methods=["POST"])
def generate_text():
    data = request.get_json()
    prompt = data.get("prompt", "Hello, world!")
    max_length = data.get("max_length", 50)

    result = generator(prompt, max_length=max_length, num_return_sequences=1)
    return jsonify(result[0])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
  
