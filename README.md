# AI Health Assistant API

This project provides a simple health assistant API using Flask. 
It can take user symptoms and return first-aid style advice. 
Optionally, it includes text-to-speech (TTS) with `pyttsx3`.

---

## 🚀 Features
- Accepts symptoms via REST API (`/advice` endpoint)
- Returns advice messages based on rule-based logic
- Text-to-speech (optional, disabled on server)
- Deployable on [Render](https://render.com)

---

## 📦 Installation (Local Development)

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/ai-health-assistant.git
   cd ai-health-assistant
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate    # Windows

   pip install -r requirements.txt
   ```

3. Run the app locally:
   ```bash
   python app.py
   ```

   Visit: [http://localhost:5000](http://localhost:5000)

---

## 🌐 Deployment on Render

1. Push this project to **GitHub**.
2. Log in to [Render](https://render.com/) and click **New Web Service**.
3. Connect your GitHub repo.
4. Set environment to **Python 3.10+**.
5. Add a **Start Command**:
   ```bash
   gunicorn app:app
   ```
6. Click **Deploy**.

After deployment, your API will be available at:
```
https://your-app.onrender.com
```

---

## 📡 Example Usage

Send a POST request with symptoms:

```bash
curl -X POST https://your-app.onrender.com/advice \
     -H "Content-Type: application/json" \
     -d '{"symptoms": "I have fever and stomach pain"}'
```

Response:
```json
{
  "symptoms": "I have fever and stomach pain",
  "advice": "This may be a stomach infection or viral fever. Avoid spicy food, drink ORS, and rest well."
}
```

---

## 🛠 Requirements
See [requirements(1).txt](requirements.txt).

---

## ⚠️ Disclaimer
This project is for **educational/demo purposes only**.  
It is **not a substitute for professional medical advice**.
