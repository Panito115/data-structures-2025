class LinearQueue:
    def __init__(self, size: int):
        self.max = size
        self.elements = [None] * size
        self.front = -1
        self.rear = -1

    def __repr__(self) -> str:
        return f'Queue: {self.elements} | F: {self.front} | R: {self.rear}'

    def enqueue(self, val: str) -> None:
        if self.rear == self.max - 1:
            print('Queue overflow...')
            return None 

        if self.front == -1 and self.rear == -1:
            self.front = 0
            self.rear = 0
        else: 
            self.rear += 1

        self.elements[self.rear] = val

    def dequeue(self) -> str:
        if self.front == -1 or self.front > self.rear:
            print('Queue underflow...')
            return None
        
        val = self.elements[self.front]
        self.elements[self.front] = None
        self.front += 1

        return val

import time

n = 5500000  # Tamaño base
sizes = [n, 2*n, 3*n, 4*n, 5*n]  # Lista de tamaños
elementos = ['a', 'b', 'c']  # Elementos a insertar cíclicamente

for i, size in enumerate(sizes):
    # Crear cola con el tamaño correspondiente
    queue = LinearQueue(size)
    
    # Medir tiempo de inserción
    start_time = time.time()
    
    for j in range(size):
        # Seleccionar elemento cíclico (a -> b -> c -> a -> ...)
        elemento = elementos[j % 3]
        queue.enqueue(elemento)
    
    end_time = time.time()
    
    # Mostrar resultados
    print(f"\nCola {i+1} (Tamaño: {size})")
    print(f"Tiempo total: {end_time - start_time:.4f} segundos")
    print(f"Tiempo por elemento: {(end_time - start_time)/size * 1e6:.4f} microsegundos")