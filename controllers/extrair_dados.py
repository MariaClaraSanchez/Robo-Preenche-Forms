from openpyxl import load_workbook

class Planilha:
    def __init__(self) -> None:    
        
        self.caminho_arquivo = "DadosFormulario.xlsx"
        self.planilha = load_workbook(filename=self.caminho_arquivo)

        #Seleciona a sheet que tem as informações a serem passadas para o formulario on-line
        self.sheet = self.planilha['Dados']

    def extrai_dados(self) -> dict:

        dados = {}
        for linha in range(2, len(self.sheet['A']) + 1):
            
            nome = self.sheet['A%s' % linha].value
            email = self.sheet['B%s' % linha].value
            telefone = self.sheet['C%s' % linha].value
            sexo = self.sheet['D%s' % linha].value
            sobre = self.sheet['E%s' % linha].value
            
            dados.update({nome:{
                'email': email,
                'telefone': telefone,
                'sexo': sexo,
                'sobre':sobre
            }})
            
        return dados
            
