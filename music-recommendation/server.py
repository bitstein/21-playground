import spotipy

# import flask web microframework
from flask import Flask
from flask import request
from flask import abort
from flask import jsonify
from flask import make_response

# import from the 21 Developer Library
from two1.lib.wallet import Wallet
from two1.lib.bitserv.flask import Payment

app = Flask(__name__)
wallet = Wallet()
payment = Payment(app, wallet)
sp = spotipy.Spotify()

@app.route('/related')
# Payment required not allowed because of the Spotify API terms of service
# https://developer.spotify.com/developer-terms-of-use/#section-iv-restrictions
# @payment.required(1000)
def related_artists():
    result = []
    search_name = str(request.args.get('artist'))
    search_results = search_artists(search_name)

    if not search_results:
        abort(404)
    else:
        artist_id = search_results[0]['id']

    related_artists = sp.artist_related_artists(artist_id)

    for rel_art in related_artists['artists']:
        artist_data = {
            'name': rel_art['name'],
            'url': rel_art['external_urls']['spotify']
        }
        result.append(artist_data)

    return jsonify({'related_artists': result})

def search_artists(name):
    results = sp.search(q='artist:' + name, type='artist', limit=1)
    items = results['artists']['items']
    return items

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Artist not found'}), 404)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
