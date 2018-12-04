from flask import Flask
from redis import Redis


app = Flask(__name__)
redis = Redis(host='redis', port=6379)


@app.route('/')
def stats():
    redis.incr('hits')
    return 'This app has been viewed %s time(s).' % redis.get('hits')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
