class Tabela:
    """Classe com funções que permitem criar tabelas e mostrá-las na tela de maneira fácil.
    """
    def __init__(self, linhas:int, colunas:int, preencher:str='', valores:list=None):
        """Cria o objeto e cria a tabela.

        Args:
            linhas (int): Quantidade de linhas da tabela.
            colunas (int): Quantidade de colunas da tabela.
            preencher (str, optional): Caso não informe os valores que deseja adicionar na tabela, ela será preenchida com esse argumento. Defaults to ''.
            valores (list, optional): Os valores de cada elemento da tabela OBS: A quantidade de valores tem que ser igual a linhas * colunas se não a tabela será preenchida com o argumento preencher. Defaults to None.
        """
        self.tabela = []
        self.linhas = linhas
        self.colunas = colunas
        if valores != None:
            if len(valores) == linhas * colunas:
                c=0
                for a in range(0, linhas):
                    self.tabela.append([])
                    for b in range(0, colunas):
                        self.tabela[a].append(valores[c])
                        c+=1
            else:
                for a in range(0, linhas):
                    self.tabela.append([])
                    for b in range(0, colunas):
                        self.tabela[a].append(preencher)
        else:
            for a in range(0, linhas):
                self.tabela.append([])
                for b in range(0, colunas):
                    self.tabela[a].append(preencher)
    

    def mostrar_tabela(self):
        """Mostra a tabela de maneira amigável na tela.
        """
        c = 0 
        for linha in self.tabela:
            c += 1
            print(f'{c:<{len(str(self.linhas))}}:{linha}')