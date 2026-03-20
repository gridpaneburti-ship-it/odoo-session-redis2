from . import http
from . import session
import os
os.environ['ODOO_SESSION_REDIS'] = '1'
os.environ['ODOO_SESSION_REDIS_HOST'] = 'odoo-redis'
os.environ['ODOO_SESSION_REDIS_PORT'] = '6379'
