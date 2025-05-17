# 3. Cree una estructura de objetos que asemeje un Binary Tree.
#     1. Debe incluir un método para hacer `print` de toda la estructura.
#     2. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`.

class Node():
    data: str
    def __init__(self,data,pointer1=None,pointer2=None):
        self.data=data
        self.pointer1=pointer1
        self.pointer2=pointer2

class BinaryTree:
    root: Node
    def __init__(self,root):
        self.root=root

    def print_structure(self,node):
        if node is None:
            return
        print(node.data)
        self.print_structure(node.pointer1)
        self.print_structure(node.pointer2) #Had to use recursive function to solve this. 


#               A
#            /     \
#          B         C
#        /   \     /   \
#      D      E   F     G
#     / \    / \  / \   / \
#    H  I   J  K L  M  N   O
    
# Nodes (level 4)
h = Node("H")
i = Node("I")
j = Node("J")
k = Node("K")
l = Node("L")
m = Node("M")
n = Node("N")
o = Node("O")

# Luego los nodos del nivel 3
d = Node("D", h, i)
e = Node("E", j, k)
f = Node("F", l, m)
g = Node("G", n, o)

# Nivel 2
b = Node("B", d, e)
c = Node("C", f, g)

# Nivel 1 (raíz)
a = Node("A", b, c)

# Crear el árbol
arbol = BinaryTree(a)

# Ejecutar recorrido
arbol.print_structure(arbol.root)
