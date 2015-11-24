21 Playground
=============

This repo contains sample applications built on the [21 platform](http://21.co/learn/).

## Music Recommendation

This app lets you send a name of a music artist and receive a list of related artists via the Spotify API.

Example:

```
$ python client.py "duke ellington"
You sent duke ellington
{
  "related_artists": [
    {
      "name": "Count Basie",
      "url": "https://open.spotify.com/artist/2jFZlvIea42ZvcCw4OeEdA"
    },
    {
      "name": "Benny Goodman",
      "url": "https://open.spotify.com/artist/1pBuKaLHJlIlqYxQQaflve"
    },
    {
      "name": "Charlie Parker",
      "url": "https://open.spotify.com/artist/4Ww5mwS7BWYjoZTUIrMHfC"
    },
    {
      "name": "John Coltrane",
      "url": "https://open.spotify.com/artist/2hGh5VOeeqimQFxqXvfCUf"
    },
    {
      "name": "Dizzy Gillespie",
      "url": "https://open.spotify.com/artist/5RzjqfPS0Bu4bUMkyNNDpn"
    },
    {
      "name": "Thelonious Monk",
      "url": "https://open.spotify.com/artist/4PDpGtF16XpqvXxsrFwQnN"
    },
    ...
  ]
}
```

Because of the [Spotify API terms of service](https://developer.spotify.com/developer-terms-of-use/#section-iv-restrictions), the payment required decorator has been disabled.

## 21-Tor

This app lets you establish a 21 API endpoint behind a Tor hidden service. It requires the `stem` library.

`pip install stem` or (in the 21-tor directory) `pip install -r requirements.txt`

Example:

```
$ torsocks curl -I http://hpy73zd5fekkduf2.onion/hello
HTTP/1.0 402 PAYMENT REQUIRED
Price: 1000
Username: bitstein
Bitcoin-Address: 13J8mwKK1KT7sEtCCSFnukL1Cu2hX5kXNo
Bitcoin-Micropayment-Server: http://hpy73zd5fekkduf2.onion/payment
Content-Type: text/plain; charset=utf-8
Content-Length: 16
Server: Werkzeug/0.11.2 Python/3.5.0
Date: Tue, 24 Nov 2015 22:52:40 GMT
```

You may need to change the port number to 9050 or 9051, depending on your Tor proxy.

Note: this is only for demonstrable purposes. Do not use for secure applications as it has not been thoroughly tested.

TODO: Write a client that connects via the socks proxy.
