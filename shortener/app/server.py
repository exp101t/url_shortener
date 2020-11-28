from flask import Flask, redirect, render_template, request
from redis import Redis

from config import BASE, PROTO, REDIS_HOST, REDIS_PORT
from helpers import rand_str, validate_url

app = Flask(__name__)
_redis = Redis(host=REDIS_HOST, port=REDIS_PORT)


@app.route('/go/<string:shorten>', methods=['GET'])
def do_redirect(shorten: str):
    full_url = _redis.get(shorten)

    if full_url is None:
        return 'URL is not valid', 400

    return redirect(full_url.decode(), code=301)


@app.route('/shorten', methods=['POST'])
def shorten_url():
    body = request.get_json()

    if not isinstance(body, dict) or 'url' not in body:
        return {'ok': False, 'reason': 'Invalid body'}, 400

    if not validate_url(body['url']):
        return {'ok': False, 'reason': 'Malformed URL'}, 400

    suffix = rand_str(5)
    short_url = '{proto}://{base}/go/{suffix}'.format(
        proto=PROTO, base=BASE, suffix=suffix
    )

    _redis.set(suffix, body['url'])

    return {'ok': True, 'url': short_url}


@app.route('/')
def get_index_page():
    return render_template('index.html',
                           proto=PROTO,
                           base=BASE)


if __name__ == '__main__':
    app.run(debug=True)
