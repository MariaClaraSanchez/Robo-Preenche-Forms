from pydoc import plain
from controllers.acessar_site import Site 
from controllers.extrair_dados import Planilha

def start():
    site = Site()
    dados = Planilha()

    
    site.acessar_forms(dados.extrai_dados())
if __name__ == '__main__':
    start()