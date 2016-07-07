from flask import Flask, request
import commands
import logging

app = Flask(__name__)

logging.basicConfig(filename='flog.txt', level=logging.INFO)


def get_argv(maps, key, default=None):
    if key in maps:
        return maps[key]
    if default is None:
        return 0
    return default


@app.route('/', methods=['GET'])
def main():
    if get_argv(request.args, 'time') == '20160606':
        logging.info(commands.getoutput("cd /root/blog-hugo && git pull"))
        return '1'
    return '0'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
