# From https://www.youtube.com/watch?v=UbCWoMf80PY
# To extend this app to Docker, follow http://containertutorials.com/docker-compose/flask-simple-app.html

# First, run the app as follows (In Windows 10)
# >_ $env:FLASK_APP = "app"
# >_ flask run
# OR as
# >_ python app.py

import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'experience':2, 'test_score':9, 'interview_score':6})
print(r.json())


## Save to .json file
# import json
# x = {"experience":2, "test_score":9, "interview_score":6}
# json.dumps(x)

# with open('data.txt', 'w') as outfile:
#     json.dump(x, outfile)

