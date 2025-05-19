from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Je suis toujours allumé, même si ton PC est éteint !"

app.run(host='0.0.0.0', port=10000)
