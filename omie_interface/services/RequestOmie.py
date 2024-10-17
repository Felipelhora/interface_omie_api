import requests
import json
from omie_interface.config import CONFIG



class RequestOmie:

    def __init__(self, paramans:dict):
        self.payload = {
                            "app_key": paramans['app_key'],
                            "app_secret": paramans['app_secret'],
                        }

        self.headers = {'Content-Type': 'application/json'}

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __log_request(self, method: str, url: str, payload: dict):
        print("Request Method:", method)
        print("Request URL:", url)
        print("Request Payload:", json.dumps(payload, indent=4))


    def post_client(self, url:str, paramans:dict):
        new_payload = self.payload
        new_payload["call"] = CONFIG['omie_call_incluir_clientes']
        new_payload["param"] = [
                                    {
                                        "codigo_cliente_integracao": paramans['codigo_cliente_integracao_id_cliente_agendup'],
                                        "razao_social": paramans['razao_social_nome'],
                                        "cnpj_cpf": paramans['cpf_cliente']
                                    }
        ]

        return self.__send_requisition(payload=new_payload, url=url)


    def get_clientes(self, url:str, paramans:dict):
        new_payload = self.payload
        new_payload["call"] = CONFIG['omie_call_listar_clientes']
        new_payload["param"] = [
                                    {
                                        "clientesFiltro": 
                                                        {
                                                                "cnpj_cpf": paramans['cpf_cliente']
                                                        }
                                    }
                                ]
        return self.__send_requisition(payload=new_payload, url=url)
    


    def get_bank_accounts(self, url:str):
        new_payload = self.payload
        new_payload["call"] = CONFIG['omie_call_listar_contas_correntes']
        new_payload["param"] = [
                                {
                                    "pagina": 1,
                                    "registros_por_pagina": 100,
                                    "apenas_importado_api": "N"
                                }
                                ]
        return self.__send_requisition(payload=new_payload, url=url)
    


    def get_payment_categories(self, url:str):
        new_payload = self.payload
        new_payload["call"] = CONFIG['omie_call_listar_categorias']
        new_payload["param"] = [
                                  {
                                    "pagina": 1,
                                    "registros_por_pagina": 50
                                  }
                                ]
        return self.__send_requisition(payload=new_payload, url=url)
    
    
    def post_lancamentos(self, url:str, paramans:dict, cod_cliente:int):
        new_payload = self.payload
        new_payload["call"] = CONFIG['omie_call_incluir_contas_a_receber']
        new_payload["param"] = [
                                    {
                                        "codigo_lancamento_integracao": str(paramans['codigo_lancamento_integracao_id_venda_agendup']),
                                        "codigo_cliente_fornecedor": cod_cliente,
                                        "data_vencimento": paramans['data_vencimento'],
                                        "valor_documento": paramans['value'],
                                        "codigo_categoria": paramans['codigo_categoria'],
                                        "data_previsao": paramans['data_vencimento'],
                                        "id_conta_corrente": paramans['id_conta_corrente']
                                    }
                                ]
        return self.__send_requisition(payload=new_payload, url=url)


    def __send_requisition(self, payload:dict, url:str):
        try:
            answer = requests.request("POST", url, headers=self.headers, data=json.dumps(payload, indent=4))
            decoded_string = answer.content.decode('utf-8')
            try:
                answer = json.loads(decoded_string)
                answer['status'] = True
                del decoded_string
            except json.JSONDecodeError:
                new_answer = {}
                new_answer['status'] = False
                new_answer['message'] = answer
                return {"status": False, "message": "Não foi possível converter a resposta em JSON"}
            else:
                if "faultstring" in answer.keys():
                    answer_wrong = {}
                    answer_wrong['status'] = False
                    answer_wrong['message'] = answer
                    return answer_wrong
                else:
                    answer['status'] = True
                    return answer 
        except Exception as error:
            return {"status": False, "message": str(error).replace('"', '')}



