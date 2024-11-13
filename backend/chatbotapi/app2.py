from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

# Replace with your actual API key
GOOGLE_API_KEY = "your-api-key"
genai.configure(api_key=GOOGLE_API_KEY)

class WomensHealthChatbot:
    def __init__(self):
        try:
            # Initialize the model in the constructor
            self.model = genai.GenerativeModel('gemini-pro')
        except Exception as e:
            print(f"Error initializing model: {str(e)}")
            raise e

    def generate_response(self, prompt):
        """Generate response using the AI model with error handling"""
        try:
            if not self.model:
                raise Exception("Model not properly initialized")
            
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"I apologize, but I encountered an error: {str(e)}. Please try rephrasing your question."

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        prompt = data.get("prompt")
        
        if not prompt:
            return jsonify({"error": "No prompt provided"}), 400

        chatbot = WomensHealthChatbot()
        bot_response = chatbot.generate_response(prompt)
        print(bot_response)
        
        return jsonify({"message": bot_response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)