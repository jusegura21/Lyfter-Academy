
# 1. Cree una estructura de objetos que asemeje un Stack.
#     1. Debe incluir los métodos de `push` (para agregar nodos) y `pop` (para quitar nodos).
#     2. Debe incluir un método para hacer `print` de toda la estructura.
#     3. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`.
# 2. Cree una estructura de objetos que asemeje un Double Ended Queue.
#     1. Debe incluir los métodos de `push_left` y `push_right` (para agregar nodos al inicio y al final) y `pop_left` y `pop_right` (para quitar nodos al inicio y al final).
#     2. Debe incluir un método para hacer `print` de toda la estructura.
#     3. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`.

class Node():
    data: str
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class LinkedList:
    head: Node
    def __init__(self,head):
        self.head=head

    def print_structure(self):
        current_node = self.head
        while (current_node is not None):
            print(current_node.data)
            current_node = current_node.next

class Stack(LinkedList):

    def push(self,new_node):
        new_node.next=self.head
        self.head=new_node

    def pop(self):
        node_pop=self.head
        self.head=self.head.next
        return node_pop

class DoubleEndedQueue(LinkedList):

    def push_right(self,new_node):
        new_node.next=self.head
        self.head=new_node

    def push_left(self,new_node):
        current_node=self.head
        while current_node.next is not None:
            current_node=current_node.next
        current_node.next=new_node

    def pop_left(self):
        self.head=self.head.next

    def pop_right(self):
        current_node=self.head
        while current_node.next is not None:
            past_node=current_node
            current_node=current_node.next
        past_node.next=None

fourth_node=Node('4th node')
third_node = Node("3rd node",fourth_node)
second_node = Node("2nd node", third_node)
first_node = Node("1st node", second_node)

#Test Run for STACK
stack=Stack(first_node)#Initialize stack structure
print('Running STACK Test')
stack.print_structure()#print structure
print('-Executing Push-')
stack.push(Node('Nodo Push')) #Push "Push Node"
stack.print_structure() #print result after push
print('-Executing Pop-')
stack.pop() #Pop node
stack.print_structure() #print result after pop
#End of test run
#Test run for DoubleEndQueue
print('Running DoubleEndQueue Test')
doublequeue=DoubleEndedQueue(first_node)
doublequeue.print_structure()
print('-Executing Push Right-')
doublequeue.push_right(Node('PushRight Node'))
doublequeue.print_structure()
print('-Executing Push Left-')
doublequeue.push_left(Node('PushLeft Node'))
doublequeue.print_structure()
print('-Executing Pop Left-')
doublequeue.pop_left()
doublequeue.print_structure()
print('-Executing Pop Right-')
doublequeue.pop_right()
doublequeue.print_structure()