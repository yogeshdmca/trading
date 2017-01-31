import os
import sys
sys.path.insert(0, os.path.abspath('..'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trading.settings')

from django.conf import settings
from ws4redis.uwsgi_runserver import uWSGIWebsocketServer

import gevent.monkey
gevent.monkey.patch_thread()

from ws4redis.uwsgi_runserver import uWSGIWebsocketServer
application = uWSGIWebsocketServer()
