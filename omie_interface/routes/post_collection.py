"""
    POST COLLECTION
    Recebe os dados para cadastrar uma venda
"""
from flask import request, jsonify
import json
from omie_interface.config import server, CONFIG
from omie_interface.middleware.auth import auth
from omie_interface.middleware.check_paramters import check_parameter_post_contas_a_receber
from omie_interface.services.PostCollectionServices import PostCollectionServices


route ='/api/{}/cobranca'.format(CONFIG['version'])


@server.route(route, methods=['POST'])
def post_cobranca():

    status = check_parameter_post_contas_a_receber(request.json)
    if status['status'] != True:
        return jsonify(status), 400
    if auth(request.json['token_agendup']) != True:
        return jsonify({}),401
    answer_ = PostCollectionServices().post_collection_services(request.json)
    print (answer_)
    if answer_['status'] == True:
        return jsonify(answer_), 200
    else:
        return jsonify(answer_), 500
