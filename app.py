from flask import Flask, render_template, request, jsonify
from textblob import TextBlob


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']
    blob = TextBlob(text)
    sentiment = "Positive" if blob.sentiment.polarity > 0 else "Negative" if blob.sentiment.polarity < 0 else "Neutral"
    return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    app.run(debug=True, port=8000)

