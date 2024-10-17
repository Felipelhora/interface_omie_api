from omie_interface.services.RequestOmie import RequestOmie
from omie_interface.config import CONFIG


class PostCollectionServices:
    def __init__(self) -> None:
        self.codigo_cliente_omie = ''

    def criar_cliente(self, params):
        with RequestOmie(params) as save_client:
            client_new = save_client.post_client(paramans=params, url=CONFIG['omie_end_point_clientes'])
            return client_new

    def post_collection_services(self, params:dict):
        with RequestOmie(params) as answer:
            # return answer.post_lancamentos(paramans=params, url=CONFIG['omie_end_point_contas_receber'], cod_cliente=self.codigo_cliente_omie)
            #tenta recuparar os dados do cliente
            client = answer.get_clientes(paramans=params, url=CONFIG['omie_end_point_clientes'])
            # caso seja negatico ele tentea criar o usuario
            if client['status'] == False:
                answer_post_client = self.criar_cliente(params=params)
                # caso não consiga criar retorna o erro
                if answer_post_client['status'] == False:
                    return answer_post_client
                # criado ele salva o código do cliente na variável da classe
                else:
                    self.codigo_cliente_omie = answer_post_client['codigo_cliente_omie']
            else:
                #recuperado o id do ele salvo na variável da classe
                self.codigo_cliente_omie = client['clientes_cadastro'][0]['codigo_cliente_omie']
            return answer.post_lancamentos(paramans=params, url=CONFIG['omie_end_point_contas_receber'], cod_cliente=self.codigo_cliente_omie)
            


            


        

    
    


