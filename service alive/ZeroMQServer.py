# stdlib
import logging

# zmq
import zmq

context = zmq.Context()
socket = context.socket(zmq.PULL)
socket.bind('tcp://127.0.0.1:35101')

logging.basicConfig(level=logging.DEBUG)

while True:
    msg = socket.recv_json()
    logging.debug('Got message:[{}]'.format(msg))
