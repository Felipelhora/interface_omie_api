"""
config.py

"""

import os
from flask import Flask
from decouple import config


path_root = os.getcwd()


CONFIG = {
    'omie_call_listar_clientes': config('omie_call_listar_clientes'),
    'omie_call_incluir_clientes': config('omie_call_incluir_clientes'),
    'omie_call_listar_contas_a_receber': config('omie_call_listar_contas_a_receber'),
    'omie_call_incluir_contas_a_receber': config('omie_call_incluir_contas_a_receber'),
    'omie_call_listar_categorias': config('omie_call_listar_categorias'),
    'omie_call_listar_contas_correntes': config('omie_call_listar_contas_correntes'),
    'omie_end_point_clientes': config('omie_end_point_clientes'),
    'omie_end_point_contas_receber': config('omie_end_point_contas_receber'),
    'omie_end_point_categorias': config('omie_end_point_categorias'),
    'omie_end_point_conta_corrente': config('omie_end_point_conta_corrente'),
    'omie_end_point_boletos': config('omie_end_point_boletos'),
    'token_agendup': config('token_agendup', default='ola'),
    'port': config('port', default=5050),
    'version': config('version', default='v1'),
    'host': config('host', default='0.0.0.0'),
}



# Flask variáveis
server = Flask(__name__)