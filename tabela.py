class Tabela:
    """Classe com funções que permitem criar tabelas e mostrá-las na tela de maneira fácil.
    """
    def __init__(self, linhas:int, colunas:int, preencher:str='-', valores:list=None):
        """Cria o objeto e cria a tabela.

        Args:
            linhas (int): Quantidade de linhas da tabela.
            colunas (int): Quantidade de colunas da tabela.
            preencher (str, optional): Caso não informe os valores que deseja adicionar na tabela, ela será preenchida com esse argumento. Defaults to '-'.
            valores (list, optional): Os valores de cada elemento da tabela OBS: A quantidade de valores tem que ser igual a linhas * colunas se não a tabela será preenchida com o argumento preencher. Defaults to None.
        """
        self.tabela = []
        self.linhas = linhas
        self.colunas = colunas
        self.valores = valores
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
    

    def informações(self):
        """Retorna a tabela, valores da tabela, linhas e colunas. OBS: Se valores da tabela forem None os valores não foram informados na criação da tabela.
        """
        return self.tabela, self.valores, self.linhas, self.colunas


    def mostrar_tabela(self):
        """Mostra a tabela de maneira amigável na tela.
        """
        maiorvalor =  len(str(self.tabela[0][0]))
        for linha in self.tabela:
            for coluna in linha:
                if len(str(coluna)) > len(str(maiorvalor)):
                    maiorvalor = coluna

        
        print(f'{"TABELA":=^80}')
        for linha in self.tabela:
            for coluna in linha:
                print(f'{coluna:^{len(str(maiorvalor))+2}}', end=" ")
            print()
    

    def limpar_valores_da_tabela(self, preencher='-'):
        """Limpa os valores da tabela e preenche com o argumento preencher informado.

        Args:
            preencher (Any, optional): Informe com o que deseja preencher os campos vazios da tabela. Defaults to '-'.
        """
        for linha in self.tabela:
            linha.clear()
            for c in range(0, self.colunas):
                linha.append(preencher)
        self.atualizar_valores()


    def adicionar_linha(self, preencher='-'):
        """Adiciona uma nova linha a tabela.

        Args:
            preencher (Any, optional): Valor que ocupará as novas linhas e colunas da tabela. Defaults to '-'.
        """
        self.linhas += 1
        nova_linha = []
        for a in range(0, self.colunas):
            nova_linha.append(preencher)
        self.tabela.append(nova_linha)
        self.atualizar_valores()


    def remover_linha(self, index:int):
        """Remove a linha desejada da tabela.

        Args:
            index (int): Índice da linha que deseja remover.
        """
        self.linhas -= 1
        self.tabela.pop(index)
        self.atualizar_valores()


    def adicionar_coluna(self, preencher='-'):
        """Adiciona uma nova coluna a tabela.

        Args:
            preencher (Any, optional): Valor que ocupará as novas linhas e colunas da tabela. Defaults to '-'.
        """
        self.colunas += 1
        for linha in self.tabela:
            linha.append(preencher)
        self.atualizar_valores()

    
    def remover_coluna(self, index:int):
        """Remove a coluna desejada da tabela.

        Args:
            index (int): Índice da coluna que deseja remover.
        """
        self.colunas -= 1
        for linha in self.tabela:
            linha.pop(index)
        self.atualizar_valores()
    

    def alterar_valores(self, valores:list, preencher='-'):
        """Altera os valores da tabela pelos novos valores informados.

        Args:
            valores (list): Lista contendos os novos valores da tabela.
            preencher (str, optional): Caso a lista de valores seja menor que a quantidade de elementos necessários para completar a tabela, será usado este argumento para definir os valores de preenchimento de espaços pendentes. Defaults to '-'.
        """
        for linha in self.tabela:
            linha.clear()
        
        if len(valores) == self.linhas * self.colunas:
            pass
        elif len(valores) > self.linhas * self.colunas:
            diferença = len(valores) - self.linhas * self.colunas
            for a in range(0, diferença):
                valores.pop()
        elif len(valores) < self.linhas * self.colunas:
            diferença = self.linhas * self.colunas - len(valores)
            for a in range(0, diferença):
                valores.append(preencher)
        
        self.valores = valores

        c=0
        for linha in self.tabela:
            for b in range(0, self.colunas):
                linha.append(self.valores[c])
                c+=1
    

    def atualizar_valores(self):
        """Atualiza a variável de valores do Objeto.
        """
        self.valores = []
        for linha in self.tabela:
            for coluna in linha:
                self.valores.append(coluna)