# microservice.py
from flask import Flask, jsonify, render_template_string, send_from_directory

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Hello Microservice</title>
    <style>
        body { font-family: Inter, Arial, sans-serif; background: #f7f7fa; margin: 0; }
        .container { max-width: 600px; margin: 40px auto; padding: 2rem; background: #fff; border-radius: 12px; box-shadow: 0 2px 12px rgba(0,0,0,0.07); text-align: center; }
        button { padding: 0.75rem 2rem; font-size: 1.2rem; border-radius: 8px; border: none; background: #7702ff; color: #fff; cursor: pointer; margin-bottom: 2rem; }
        h1 { font-size: 2.5rem; color: #7702ff; margin: 1.5rem 0; }
        .ball-container { width: 100%; display: flex; justify-content: center; align-items: flex-end; height: 200px; margin-top: 2rem; }
        .bouncing-ball { width: 50px; height: 50px; background: radial-gradient(circle at 30% 30%, #ff41f8 70%, #7702ff 100%); border-radius: 50%; position: relative; animation: bounce 1s infinite cubic-bezier(.28,.84,.42,1); }
        @keyframes bounce { 0%, 100% { bottom: 0; } 50% { bottom: 120px; } }
    </style>
</head>
<body>
    <div class="container">
        <button onclick="getMessage()">Get Message from Microservice</button>
        <h1 id="message"></h1>
        <div class="ball-container">
            <div class="bouncing-ball"></div>
        </div>
    </div>
    <script>
        function getMessage() {
            fetch('/api/hello')
                .then(res => res.json())
                .then(data => {
                    document.getElementById('message').textContent = data.message;
                });
        }
    </script>
</body>
</html>
'''

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/api/hello')
def hello():
    return jsonify({'message': 'Hello World'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
