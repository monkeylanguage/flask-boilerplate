from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'youbetterchanegthisasap'

@app.route('/', methods=['GET', 'POST'])
def index():

    return jsonify(status="1")
