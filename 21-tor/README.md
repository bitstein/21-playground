21-Tor
======

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
