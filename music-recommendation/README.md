Music Recommendation
====================

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
