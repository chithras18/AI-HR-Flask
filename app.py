from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

genai.configure(api_key="Your api key")

MODEL_NAME = "models/gemini-2.5-flash"
model = genai.GenerativeModel(MODEL_NAME)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_msg = data["message"]

        response = model.generate_content(user_msg)

        return jsonify({
            "reply": response.text
        })

    except Exception as e:
        return jsonify({
            "reply": f"HR Error: {str(e)}"
        })

@app.route("/submit_leave", methods=["POST"])
def submit_leave():
    data = request.get_json()
    name = data.get("name")
    emp_id = data.get("id")
    from_date = data.get("from_date")
    to_date = data.get("to_date")
    reason = data.get("reason")
    
    if not all([name, emp_id, from_date, to_date, reason]):
        return jsonify({"message": "Please fill all fields."})

    msg = f"""
💼 Leave Request Submitted! 💼
-----------------------------
Employee Name: {name}
Employee ID: {emp_id}
From: {from_date}
To: {to_date}
Reason: {reason}
-----------------------------
Your leave request has been recorded.
"""
    return jsonify({"message": msg})

if __name__ == "__main__":
    app.run(debug=True)
