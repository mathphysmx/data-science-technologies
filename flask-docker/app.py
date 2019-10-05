# http://containertutorials.com/docker-compose/flask-simple-app.html

# Run this as
# >_ docker run --name fd -d -p 3000:5000 flaskdocker
# and go to your browser (Chrome for instance) localhost:3000/

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flask Dockerized'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')