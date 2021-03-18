from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    hits = redis.get('hits').decode('utf-8')
    return '<h1>{}</h1>'.format(hits)

@app.route('/reset')
def reset():
    redis.set('hits', 0)
    return 'reset done!'
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)