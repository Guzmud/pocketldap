#!/usr/bin/env python3

import hug


@hug.cli()
@hug.local()
@hug.get()
def hello_world():
    return {'text': 'Hello, world!'}

