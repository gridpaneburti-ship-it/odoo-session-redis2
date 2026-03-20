import os

# 1. Configurar el entorno ANTES de cargar el código del módulo
os.environ.setdefault('ODOO_SESSION_REDIS', '1')
os.environ.setdefault('ODOO_SESSION_REDIS_HOST', 'odoo-redis')
os.environ.setdefault('ODOO_SESSION_REDIS_PORT', '6379')

# 2. Ahora sí, cargar el resto del módulo que leerá esas variables
from . import http
from . import session
