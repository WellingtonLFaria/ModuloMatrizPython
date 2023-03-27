class Matriz:
    """Classe com funções que permitem criar matrizes e mostrá-las na tela de maneira fácil.
    """
    def __init__(self, linhas:int, colunas:int, preencher:str='-', valores:list=None):
        """Cria o objeto e cria a matriz.

        Args:
            linhas (int): Quantidade de linhas da matriz.
            colunas (int): Quantidade de colunas da matriz.
            preencher (str, optional): Caso não informe os valores que deseja adicionar na matriz, ela será preenchida com esse argumento. Defaults to '-'.
            valores (list, optional): Os valores de cada elemento da matriz OBS: A quantidade de valores tem que ser igual a linhas * colunas se não a matriz será preenchida com o argumento preencher. Defaults to None.
        """
        self.matriz = []
        self.linhas = linhas
        self.colunas = colunas
        self.valores = valores
        if valores != None:
            if len(valores) == linhas * colunas:
                c=0
                for a in range(0, linhas):
                    self.matriz.append([])
                    for b in range(0, colunas):
                        self.matriz[a].append(valores[c])
                        c+=1
            else:
                for a in range(0, linhas):
                    self.matriz.append([])
                    for b in range(0, colunas):
                        self.matriz[a].append(preencher)
        else:
            for a in range(0, linhas):
                self.matriz.append([])
                for b in range(0, colunas):
                    self.matriz[a].append(preencher)
    

    def informações(self):
        """Retorna a matriz, valores da matriz, linhas e colunas. OBS: Se valores da matriz forem None os valores não foram informados na criação da matriz.
        """
        return self.matriz, self.valores, self.linhas, self.colunas


    def mostrar_matriz(self):
        """Mostra a matriz de maneira amigável na tela.
        """
        maiorvalor =  len(str(self.matriz[0][0]))
        for linha in self.matriz:
            for coluna in linha:
                if len(str(coluna)) > len(str(maiorvalor)):
                    maiorvalor = coluna

        
        print(f'{"Matriz":=^80}')
        for linha in self.matriz:
            for coluna in linha:
                print(f'{coluna:^{len(str(maiorvalor))+2}}', end=" ")
            print()
    

    def limpar_valores_da_matriz(self, preencher='-'):
        """Limpa os valores da matriz e preenche com o argumento preencher informado.

        Args:
            preencher (Any, optional): Informe com o que deseja preencher os campos vazios da matriz. Defaults to '-'.
        """
        for linha in self.matriz:
            linha.clear()
            for c in range(0, self.colunas):
                linha.append(preencher)
        self.atualizar_valores()


    def adicionar_linha(self, preencher='-'):
        """Adiciona uma nova linha a matriz.

        Args:
            preencher (Any, optional): Valor que ocupará as novas linhas e colunas da matriz. Defaults to '-'.
        """
        self.linhas += 1
        nova_linha = []
        for a in range(0, self.colunas):
            nova_linha.append(preencher)
        self.matriz.append(nova_linha)
        self.atualizar_valores()


    def remover_linha(self, index:int):
        """Remove a linha desejada da matriz.

        Args:
            index (int): Índice da linha que deseja remover.
        """
        self.linhas -= 1
        self.matriz.pop(index)
        self.atualizar_valores()


    def adicionar_coluna(self, preencher='-'):
        """Adiciona uma nova coluna a matriz.

        Args:
            preencher (Any, optional): Valor que ocupará as novas linhas e colunas da matriz. Defaults to '-'.
        """
        self.colunas += 1
        for linha in self.matriz:
            linha.append(preencher)
        self.atualizar_valores()

    
    def remover_coluna(self, index:int):
        """Remove a coluna desejada da matriz.

        Args:
            index (int): Índice da coluna que deseja remover.
        """
        self.colunas -= 1
        for linha in self.matriz:
            linha.pop(index)
        self.atualizar_valores()
    

    def alterar_valores(self, valores:list, preencher='-'):
        """Altera os valores da matriz pelos novos valores informados.

        Args:
            valores (list): Lista contendos os novos valores da matriz.
            preencher (str, optional): Caso a lista de valores seja menor que a quantidade de elementos necessários para completar a matriz, será usado este argumento para definir os valores de preenchimento de espaços pendentes. Defaults to '-'.
        """
        for linha in self.matriz:
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
        for linha in self.matriz:
            for b in range(0, self.colunas):
                linha.append(self.valores[c])
                c+=1
    

    def atualizar_valores(self):
        """Atualiza a variável de valores do Objeto.
        """
        self.valores = []
        for linha in self.matriz:
            for coluna in linha:
                self.valores.append(coluna)