#!/usr/bin/env python
import stomp
import time
import logging
import sys
import random

logging.basicConfig()

class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('received an error %s' % message)
    def on_message(self, headers, message):
        for k,v in headers.iteritems():
            print('header: key %s , value %s' %(k,v))
        print('received message\n %s'% message)


dest='/topic/manager'
conn=stomp.Connection([('localhost',61613)])
print('set up Connection')
conn.set_listener('somename',MyListener())
print('Set up listener')

conn.start()
print('started connection')

conn.connect(wait=True)
print('connected')
conn.subscribe(destination=dest, ack='auto')
print('subscribed')


