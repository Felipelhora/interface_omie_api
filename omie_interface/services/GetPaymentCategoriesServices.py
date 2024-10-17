from omie_interface.services.RequestOmie import RequestOmie
from omie_interface.config import CONFIG


class GetPaymentCategoriesServices:
    def __init__(self) -> None:
        self.answer = {}

    def __dto_payment_categories(self, list_categories:dict):
        categories_dto = {}
        list_temp = []
        try:
            for account in list_categories['categoria_cadastro']:
                categories_dto_temp = {}
                try:
                    categories_dto_temp['codigo'] = account['codigo']
                    categories_dto_temp['descricao'] = account['descricao']
                    categories_dto_temp['descricao_padrao'] = account['descricao_padrao']
                    list_temp.append(categories_dto_temp)
                except:
                    pass
            categories_dto['status'] = True
            categories_dto['message'] = list_temp
            del list_temp
            del categories_dto_temp
            return categories_dto
        except Exception as erro:
            categories_dto['status'] = False
            categories_dto['message'] = str(erro).replace('"', '')
            return categories_dto


    def get_payment_categories(self, params:dict):
        with RequestOmie(params) as answer:
            # recuparar as contas correntes cadastradas
            categories = answer.get_payment_categories(url=CONFIG['omie_end_point_categorias'])
            # filtra com a DTO
            if categories['status'] == True:
                return self.__dto_payment_categories(list_categories=categories)
            else:
                return categories
            
            


            


        

    
    


