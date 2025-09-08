from flask import Flask, request, jsonify
import pyttsx3

# ------------------------------
# RESPONSE LOGIC (from response_logic.py)
# ------------------------------
def get_response(symptom_text):
    symptom_text = symptom_text.lower()

    if "fever" in symptom_text and "stomach" in symptom_text:
        return "This may be a stomach infection or viral fever. Avoid spicy food, drink ORS, and rest well."

    if "chest pain" in symptom_text and "breathlessness" in symptom_text:
        return "These could be signs of a cardiac issue or asthma. Please seek medical attention immediately."

    symptom_map = {
        "fever": "You might have a viral infection. Stay hydrated and monitor your temperature.",
        "headache": "It could be a tension headache or migraine. Rest and avoid screen time.",
        "vomiting": "Stay hydrated. Sip ORS or water slowly. If persistent, consult a doctor.",
        "bleeding from mouth": "This may indicate gum injury, infection, or internal bleeding. Please consult a doctor immediately.",
        "rash": "This may be a skin allergy or irritation. Apply a mild antiseptic and avoid scratching.",
        "burn": "Cool the burn under running water. Do not apply ice. Cover with a clean cloth.",
        "injury": "Apply pressure to stop bleeding. Seek immediate medical attention.",
        "chest pain": "This could be serious. Call emergency services immediately."
    }

    matched = [response for key, response in symptom_map.items() if key in symptom_text]
    if matched:
        return " ".join(set(matched))

    return "I'm not sure about that symptom. Please consult a doctor for a proper diagnosis."


# ------------------------------
# TTS FUNCTION (from tts.py)
# ------------------------------
def speak(text):
    print("Assistant:", text)
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 160)
        engine.setProperty('volume', 1.0)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print("Speech error:", e)


# ------------------------------
# FLASK APP
# ------------------------------
app = Flask(__name__)

@app.route("/")
def home():
    return "✅ AI Health Assistant API is running!"

@app.route("/advice", methods=["POST"])
def advice():
    data = request.json
    symptoms = data.get("symptoms", "")
    response = get_response(symptoms)

    # (Optional) Call TTS — comment out if not needed on Render
    # speak(response)

    return jsonify({
        "symptoms": symptoms,
        "advice": response
    })


if __name__ == "__main__":
    # For local development
    app.run(host="0.0.0.0", port=5000, debug=True)
