from flask import Flask, request, jsonify
import crewai

app = Flask(__name__)
agent = crewai.create_agent("YourAgentName")

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    response = agent.chat(user_input)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
