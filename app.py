from flask import Flask
app = Flask(__name__)

@app.route('/health-check')
def health_check():
    return 'API is working'