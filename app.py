from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "Hey there! Hello from  Cookies Cutter"
if __name__ == '__main__':
    app.run(debug=True)
