# python 3

class Node:
    def __init__(self, name, priority, left=None, right=None):
        self.name = name
        self.priority = priority
        self.left = left
        self.right = right

    def __str__(self):
        return f'({self.name}, {self.priority})'

class BinaryTree:
    def __init__(self):
        self.root = None

    def _retrive(self, val, is_equal):
        stack = [self.root]
        while len(stack) > 0:
            node = stack.pop()
            if is_equal(node, val):
                return node
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return None

    def _insert(self, node: Node, new_node: Node, is_less):
        if node is None:
            return new_node
        if is_less(node, new_node):
            node.left = self._insert(node.left, new_node, is_less)
        else:
            node.right = self._insert(node.right, new_node, is_less)
        return node
    
    def toList(self):
        stack = [self.root]
        allNodes = []
        while len(stack) > 0:
            node = stack.pop()
            allNodes.append(node)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return allNodes    

    def pop_greatest(self):
        if self.root is None:
            return None
        if self.root.right is None:
            node = self.root
            self.root = node.left
            return node
        return self._pop_g(self.root)
    
    def pop_smallest(self):
        if self.root is None:
            return None
        if self.root.left is None:
            node = self.root
            self.root = node.right
            return node
        return self._pop_s(self.root)
    
    def _pop_g(self, node):
        if node.right.right is None:
            rnode = node.right
            if node.right.left:
                node.right = node.right.left
            else:
                node.right = None
            return rnode
        return self._pop_g(node.right)

    def _pop_s(self, node):
        if node.left.left is None:
            rnode = node.left
            if node.left.right:
                node.left = node.left.right
            else:
                node.left = None
            return rnode
        return self._pop_s(node.left)

    def _find_greatest(self, node: Node):
        if node.right is None:
            return node
        return self._find_greatest(node.right)

    def _find_smallest(self, node: Node):
        if node.left is None:
            return node
        return self._find_smallest(node.left)


class Tarefas(BinaryTree):
    def inserir(self, name, relevance):
        novo_no = Node(name, relevance)
        self.root = self._insert(self.root, novo_no, self.menor_prioridade)

    def buscar_por_nome(self, name):
        return self._retrive(name, self.nome_igual)

    def encontrar_mais_prioritario(self):
        if self.root is None:
            return None
        return self._find_greatest(self.root)

    def imprimir_ordem_prioridade(self):
        self._imprimir_ordem_prioridade(self.root)

    def _imprimir_ordem_prioridade(self, node):
        if node is not None:
            self._imprimir_ordem_prioridade(node.left)
            print(f"{node}")
            self._imprimir_ordem_prioridade(node.right)

    @staticmethod
    def nome_igual(node: Node, name: str):
        return node.name == name

    @staticmethod
    def menor_prioridade(no: Node, outro_no: Node):
        return outro_no.priority < no.priority 

    @staticmethod
    def ordenacao_lexica(no: Node, outro_no: Node):
        return outro_no.name < no.name    
    

class FilaDesenbarque(BinaryTree):
    class Carga(Node):
        def __init__(self, name, peso, volume, left=None, right=None):
            priority = 0

            if volume > 0:
                priority = volume**3 + (peso/volume)**2
            self.caracteristicas = {'peso_T' : peso, 
                                   'volume_m3' : volume}
            super().__init__(name, priority, left, right)
        
    _tamanho_fila = 0

    def inserir(self, nome, peso, volume):
        novo_no = self.Carga(nome, peso, volume)
        self.root = self._insert(self.root, novo_no, self.maior_peso)
        self._tamanho_fila += 1

    def executa_carga(self):
        self._tamanho_fila -= 1
        greatest = self.pop_greatest()
        return greatest
    
    def totais_carga(self):
        nodes = self.toList()
        totais = {'Peso_total' : 0,
                  'Volume_total' : 0}
        for n in nodes:
            totais['Peso_total'] += n.caracteristicas['peso_T']
            totais['Volume_total'] += n.caracteristicas['volume_m3']
        return totais

    @staticmethod
    def maior_peso(no: Carga, outro_no: Carga):
        return  no.caracteristicas['peso_T'] > outro_no.caracteristicas['peso_T']

    @property
    def tamanho_fila(self):
        return self._tamanho_fila
    

if __name__ == '__main__':
#############  Afazeres   ################
    print('-/-'*10,' Afazeres ', '-/-'*10)
    afazeres = Tarefas()
    afazeres.inserir("Estudar Algebra", 50)
    afazeres.inserir("Estudar Programação", 82)
    afazeres.inserir("Assistir partida de peteca", 55)
    afazeres.inserir("Lista 1 de programação", 40)
    afazeres.inserir("Lista 2 de programação", 75)
    afazeres.inserir("Lista 3 de programação", 80)
    afazeres.inserir("Estudar Calculo 2", 95)

    print(afazeres.buscar_por_nome("Lista 3 de programação")) 
# Saída: (Lista 3 de programaçã, 80)
    print(afazeres.encontrar_mais_prioritario())
# Saída: (Estudar Calculo 2, 95)

    afazeres.imprimir_ordem_prioridade()
# Saída:
# (Lista 1 de programaçã0, 40)
# (Estudar Algebra, 50)
# (Assistir partida de peteca, 55)
# (Lista 2 de programação, 75)
# (Lista 3 de programação, 80)
# (Estudar Programação, 82)
# (Estudar Calculo 2, 95)


#############  Cargas   ################
    print()
    print('-/-'*10,' Cargas ', '-/-'*10)
    cargas = FilaDesenbarque()

    cargas.inserir('Margarina', 50.457, 5.15 )
    cargas.inserir('Cereal', 15.025, 166.94 )
    cargas.inserir('Xarope de milho', 100.235, 67.01 )
    cargas.inserir('Cebolinha Seca', 10.363, 345.56 )
    cargas.inserir('Cimento', 73.507 , 49.08 )

    print(cargas.totais_carga())
# Saída: {'Peso_total': 249.58700000000002, 'Volume_total': 633.74}

    while cargas.tamanho_fila > 0:
        print(cargas.executa_carga().name, 
              ' descarregado!  -> Fila restante = ', 
               cargas.tamanho_fila)
# Saída:
# Xarope de milho  descarregado!  -> Fila restante =  4
# Cimento  descarregado!  -> Fila restante =  3
# Margarina  descarregado!  -> Fila restante =  2
# Cereal  descarregado!  -> Fila restante =  1
# Cebolinha Seca  descarregado!  -> Fila restante =  0