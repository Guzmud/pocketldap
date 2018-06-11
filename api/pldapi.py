#!/usr/bin/env python3

from apistar import App, Route


def hello_world():
    return {'text': 'Hello, world!'}


routes = [
    Route('/', method='GET', handler=hello_world),
]

app = App(routes=routes)

if __name__ == "__main__":
    app.serve(debug=True,
              host='0.0.0.0',
              port=8050)

