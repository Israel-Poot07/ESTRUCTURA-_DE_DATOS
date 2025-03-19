class Node:
    def __init__(self, info):
        self.info = info  # Valor del nodo
        self.next = None  # Apunta al siguiente nodo en la lista

class Queue:
    def __init__(self):
        self.front = None  # Primer nodo (cabeza)
        self.rear = None   # Último nodo (final)
        self.size = 0   # Tamaño de la cola

    def is_empty(self):
        return self.front is None  # Si `front` es None, la cola está vacía

    def enqueue(self, info):
        new_node = Node(info)  # Creamos un nuevo nodo con el valor proporcionado
        if self.rear is None:
            # Si la cola está vacía, ambos, `front` y `rear` apuntan al nuevo nodo
            self.front = self.rear = new_node
        else:
            # Si la cola no está vacía, el nodo `rear` apunta al nuevo nodo
            self.rear.next = new_node
            self.rear = new_node  # Actualizamos `rear` para que apunte al nuevo nodo
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("La cola está vacía")
        temp = self.front  # Guardamos el primer nodo
        self.front = self.front.next  # `front` ahora apunta al siguiente nodo
        if self.front is None:
            self.rear = None  # Si la cola se queda vacía, `rear` también debe ser None
        self.size -= 1
        return temp.info  # Devolvemos el valor del nodo eliminado
    
    def dequeue_at_position(self, position):
        if position < 0 or position >= self.size:
            raise Exception("Posición fuera de los límites de la cola")

        current = self.front
        previous = None
        index = 0

        # Si el nodo a eliminar es el primero (front)
        if position == 0:
            return self.dequeue()  # Usamos el método dequeue normal para eliminar el primero

        # Recorremos la cola hasta la posición deseada
        while current and index < position:
            previous = current
            current = current.next
            index += 1

        # Si encontramos el nodo a eliminar
        if current:
            previous.next = current.next
            if current == self.rear:
                self.rear = previous  # Si el nodo a eliminar es el último, actualizamos `rear`
            self.size -= 1
            return current.info  # Devolvemos el valor del nodo eliminado
        else:
            raise Exception("Nodo no encontrado en la posición especificada")

    def peek(self):
        if self.is_empty():
            raise Exception("La cola está vacía")
        return self.front.info  # Devolvemos el valor del nodo al frente de la cola

    def get_size(self):
        return self.size  # Retorna el tamaño de la cola

    def display(self):
        current = self.front
        elements = []
        while current:
            elements.append(current.info)  # Añadimos el valor de cada nodo a la lista
            current = current.next  # Pasamos al siguiente nodo
        print(" -> ".join(map(str, elements)))  # Mostramos los valores de la cola


if __name__ == "__main__":
    cola = Queue()

    # Añadir elementos a la cola
    cola.enqueue(10)
    cola.enqueue(20)
    cola.enqueue(30)
    cola.enqueue(40)

    # Mostrar los elementos antes de eliminar
    print("Elementos en la cola:")
    cola.display()  # Salida: 10 -> 20 -> 30 -> 40

    # Eliminar el nodo en la posición 2 (el valor 30)
    print("Elemento eliminado en posición 2:", cola.dequeue_at_position(3))  # Salida: 30

    # Mostrar los elementos después de eliminar
    print("Elementos después de eliminar en la posición 2:")
    cola.display()  # Salida: 10 -> 20 -> 40
