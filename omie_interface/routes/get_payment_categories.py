"""
    POST COLLECTION
    Recebe os dados para cadastrar uma venda
"""
from flask import request, jsonify
import json
from omie_interface.config import server, CONFIG
from omie_interface.middleware.check_paramters import check_parameter_get_categories
from omie_interface.middleware.auth import auth
from omie_interface.services.GetPaymentCategoriesServices import GetPaymentCategoriesServices


route ='/api/{}/categorias'.format(CONFIG['version'])


@server.route(route, methods=['POST'])
def get_payment_categories():

    status = check_parameter_get_categories(request.json)
    if status['status'] != True:
        return jsonify(status), 400
    if auth(request.json['token_agendup']) != True:
        return jsonify({}),401
    answer = GetPaymentCategoriesServices().get_payment_categories(request.json)
    if answer['status'] == True:
        return jsonify(answer), 200
    else:
        return jsonify(answer), 500
    
