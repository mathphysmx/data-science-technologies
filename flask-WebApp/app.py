# Run this app as follows
# >_ export FLASK_APP = # $env:FLASK_APP = "app"
# >_ python app.py # >_ flask run --host 127.0.0.1 --port 5000

from flask import Flask

app = Flask(__name__)

@app.route("/")
def h():
    return("aaaa")

if __name__ == "__main__":
    app.run()