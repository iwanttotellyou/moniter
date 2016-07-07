from flask import Flask, request

import commands

app = Flask(__name__)


@app.route('/')
def main():
    if "auth" in request.args and request.args['auth'] == 'LJun':
        print commands.getoutput("cd ")
    return 'Hello LJun!'


if __name__ == '__main__':
    app.run(port=8000, debug=True)
