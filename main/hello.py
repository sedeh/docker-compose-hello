import os
import requests
from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello():
    response = {os.environ['HOSTNAME']: 'hello from ' + os.environ['CONTAINER_NAME']}
    response.update(requests.get('http://app1:6000/').json())
    response.update(requests.get('http://app2:7000/').json())
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
