#!/usr/bin/env python3

# Change this to the IP address of your 21 Bitcoin Computer.
# You can find this with `sudo hostname --ip-address`
SERVER_IP_ADDRESS='127.0.0.1'

# Import methods from the 21 Bitcoin Library
from two1.commands.config import Config
from two1.lib.wallet import Wallet
from two1.lib.bitrequests import BitTransferRequests

# Configure your Bitcoin wallet.
username = Config().username
wallet = Wallet()
requests = BitTransferRequests(wallet, username)

# Send text to the endpoint
def send_artist(text):
    # tell the user what text they're sending
    print('You sent {0}'.format(text))

    # 402 endpoint URL and request
    artist_url = 'http://' + SERVER_IP_ADDRESS + ':5000/related?artist={0}'
    related_artists = requests.get(url=artist_url.format(text))

    # save the received audio file to disk
    print(related_artists.text)

# Read the text to speechify from the CLI
if __name__ == '__main__':
    from sys import argv
    send_artist(argv[1])
