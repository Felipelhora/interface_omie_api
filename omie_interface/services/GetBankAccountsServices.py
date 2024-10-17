from omie_interface.services.RequestOmie import RequestOmie
from omie_interface.config import CONFIG


class GetBankAccountsServices:
    def __init__(self) -> None:
        self.answer = {}

    def __dto_bank_accounts(self, list_accoounts:dict):
        accounts_dto = {}
        list_temp = []
        try:
            for account in list_accoounts['ListarContasCorrentes']:
                account_dto_temp = {}
                try:
                    if account['inativo'] == "S":
                        pass
                    elif account['bloqueado'] == "S":
                        pass
                    else:
                        account_dto_temp['nCodCC'] = account['nCodCC']
                        account_dto_temp['descricao'] = account['descricao']
                        list_temp.append(account_dto_temp)
                except:
                    pass
            accounts_dto['status'] = True
            accounts_dto['message'] = list_temp
            del list_temp
            del account_dto_temp
            return accounts_dto
        except Exception as erro:
            accounts_dto['status'] = False
            accounts_dto['message'] = str(erro).replace('"', '')
            return accounts_dto


    def get_bank_accounts(self, params:dict):
        with RequestOmie(params) as answer:
            # recuparar as contas correntes cadastradas
            account = answer.get_bank_accounts(url=CONFIG['omie_end_point_conta_corrente'])
            # filtra com a DTO
            if account['status'] == True:
                return self.__dto_bank_accounts(account)
            else:
                return account
            
            


            


        

    
    


