import os
import shutil

from stem.control import Controller
from subprocess import call
from uuid import uuid4

from flask import Flask
from flask import request
from flask import send_from_directory

# Import from the 21 Bitcoin Developer Library
from two1.lib.wallet import Wallet
from two1.lib.bitserv.flask import Payment

# Configure the app and wallet
app = Flask(__name__)
wallet = Wallet()
payment = Payment(app, wallet)

# Charge a fixed fee of 1000 satoshis per request to the
# /tts endpoint
@app.route('/hello')
@payment.required(1000)
def hello():
    return "Hello world"


print(' * Connecting to tor')

with Controller.from_port(port=9151) as controller:
  controller.authenticate()

  hidden_service_dir = os.path.join(controller.get_conf('DataDirectory', '/tmp'), 'hello_world')

  print(" * Creating our hidden service in %s" % hidden_service_dir)
  result = controller.create_hidden_service(hidden_service_dir, 80, target_port = 5000)

  if result.hostname:
    print(" * Our service is available at %s, press ctrl+c to quit" % result.hostname)
  else:
    print(" * Unable to determine our service's hostname, probably due to being unable to read the hidden service directory")

  if __name__ == '__main__':
      try:
        app.run()
      finally:
        print(" * Shutting down our hidden service")
        controller.remove_hidden_service(hidden_service_dir)
        shutil.rmtree(hidden_service_dir)
