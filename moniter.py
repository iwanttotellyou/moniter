from flask import Flask, request
import commands

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    if "auth" in request.args and request.args['time'] == '20160606':
        print commands.getoutput("git pull")
        return '1'
    return '0'


if __name__ == '__main__':
    app.run(port=8000, debug=True)
