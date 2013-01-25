#!/usr/bin/env python
import os, sys

PYCART_DIR = ''.join(['python-', '.'.join(map(str, sys.version_info[:2]))])

try:
   zvirtenv = os.path.join(os.environ['OPENSHIFT_HOMEDIR'], PYCART_DIR,
                           'virtenv', 'bin', 'activate_this.py')
   execfile(zvirtenv, dict(__file__ = zvirtenv) )
except IOError:
   pass


#
# IMPORTANT: Put any additional includes below this line.  If placed above this
# line, it's possible required libraries won't be in your searchable path
# 


#
#  main():
#
if __name__ == '__main__':
   from gevent.pywsgi import WSGIServer
   import imp
   zapp = imp.load_source('application', 'wsgi/application')

   ip   = os.environ['OPENSHIFT_INTERNAL_IP']
   port = 8080
   print 'Starting WSGIServer on %s:%d ... ' % (ip, port)
   WSGIServer((ip, port), zapp.application).serve_forever()

