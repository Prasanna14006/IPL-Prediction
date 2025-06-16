from flask import Flask, request, jsonify, send_file
import joblib
import os
app = Flask(__name__)
# ✅ Load model using raw string or forward slashes
model = joblib.load(r'E:\internship chainsys\EM\xgboost_ipl_winner_model.pkl')
teams = {
    "CSK": 0, "MI": 1, "RCB": 2, "KKR": 3, "RR": 4,
    "DC": 5, "PBKS": 6, "SRH": 7, "GT": 8, "LSG": 9
}
venues = {
    "Chennai": 0, "Mumbai": 1, "Bangalore": 2, "Kolkata": 3,
    "Jaipur": 4, "Delhi": 5, "Mohali": 6, "Hyderabad": 7,
    "Ahmedabad": 8, "Lucknow": 9
}
decisions = {"bat": 0, "field": 1}
# ✅ Serve HTML file properly using send_file
@app.route('/')
def serve_home():
    return send_file(r'E:\internship chainsys\EM\index.html')
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    try:
        features = [
            teams[data['team1']],
            teams[data['team2']],
            venues[data['venue']],
            teams[data['toss_winner']],
            decisions[data['toss_decision']],
            1
        ]
        prediction = model.predict([features])[0]
        winner = list(teams.keys())[list(teams.values()).index(prediction)]
        return jsonify({'prediction': winner})
    except Exception as e:
        return jsonify({'error': str(e)}), 400
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)