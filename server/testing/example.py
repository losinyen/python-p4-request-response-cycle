from app import app
from flask import request # type: ignore

request_context = app.test_request_context()
request_context.push()


if __name__ == '__main__':
    app.run(port=5555, debug=True)