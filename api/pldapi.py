#!/usr/bin/env python3

from flask import request
from flask_api import FlaskAPI

app = FlaskAPI(__name__)


@app.route("/", methods=['GET',])
def hello_world():
    return {'request data': request.data, }


if __name__ == "__main__":
    app.run(debug=True,
            host='0.0.0.0',
            port=8050)

