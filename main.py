"""
main.py
"""

from omie_interface.routes import post_collection
from omie_interface.routes import get_bank_accounts
from omie_interface.routes import get_payment_categories

from omie_interface.config import server
from omie_interface.config import CONFIG
from flask_cors import CORS


cors = CORS()
cors.init_app(server, resource={r"/api/*": {"origins": "*"}})

application = server

if __name__ == '__main__':
    server.run(debug=False, host=CONFIG['host'], port=CONFIG['port'])
