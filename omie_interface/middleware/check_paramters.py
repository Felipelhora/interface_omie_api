


def __check_main_paramters(parameters:dict) ->dict:
    if 'token_agendup' not in parameters.keys():
        return {"message": "parametro ausente -> token_agendup","status": False}
    if 'app_key' not in parameters.keys():
        return {"message": "parametro ausente -> app_key","status": False}
    if 'app_secret' not in parameters.keys():
        return { "message": "parametro ausente -> app_secret","status": False}
    return {"status": True}


def check_parameter_post_contas_a_receber(parameters:dict) -> dict:
    main_answer = __check_main_paramters(parameters=parameters)
    if main_answer['status'] != True:
        return main_answer
    if 'cpf_cliente' not in parameters.keys():
        return {"message": "parametro ausente -> cpf_cliente","status": False}
    if 'codigo_cliente_integracao_id_cliente_agendup' not in parameters.keys():
        return {"message": "parametro ausente -> codigo_cliente_integracao_id_cliente_agendup","status": False}
    if 'codigo_lancamento_integracao_id_venda_agendup' not in parameters.keys():
        return {"message": "parametro ausente -> codigo_lancamento_integracao_id_venda_agendup","status": False}
    if 'razao_social_nome' not in parameters.keys():
        return {"message": "parametro ausente -> razao_social_nome","status": False}
    if 'codigo_categoria' not in parameters.keys():
        return {"message": "parametro ausente -> codigo_categoria","status": False}
    if 'id_conta_corrente' not in parameters.keys():
        return {"message": "parametro ausente -> id_conta_corrente","status": False}
    if 'value' not in parameters.keys():
        return {"message": "parametro ausente -> value","status": False}
    if 'data_vencimento' not in parameters.keys():
        return {"message": "parametro ausente -> data_vencimento","status": False}
    else:
        return {"status": True}


def check_parameter_get_bank_accounts(parameters:dict) -> dict:
    return __check_main_paramters(parameters=parameters)


def check_parameter_get_categories(parameters:dict) -> dict:
    return __check_main_paramters(parameters=parameters)