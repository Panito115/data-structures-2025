import time

class CircularQueue:
    def __init__(self, size: int):
        self.max = size
        self.elements = [None] * size
        self.front = -1
        self.rear = -1

    def __repr__(self) -> str:
        return f'Queue: {self.elements} | F: {self.front} | R: {self.rear}'

    def enqueue(self, val: str) -> None:
        if (self.front == 0 and self.rear == self.max - 1) or (self.rear == self.front - 1):
            print('Queue overflow...')
            return None 
    
        if self.front == -1 and self.rear == -1:
            self.front = 0
            self.rear = 0
        elif self.rear == self.max - 1 and self.front != 0:
            self.rear = 0
        else:
            self.rear += 1

        self.elements[self.rear] = val
        
    def dequeue(self) -> str:
        if self.front == -1:
            print('Queue Underflow...')
            return None

        val = self.elements[self.front]
        self.elements[self.front] = None

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            if self.front == self.max - 1:
                self.front = 0
            else:
                self.front += 1

        return val

n = 11525000  # Tamaño base definido como 25 millones
elementos = ['A', 'B', 'C', 'D', 'E']

# Crear las 5 colas con tamaños n, 2n, ..., 5n
colas = [
    CircularQueue(n * 1),  
    CircularQueue(n * 2),  
    CircularQueue(n * 3),  
    CircularQueue(n * 4),  
    CircularQueue(n * 5)   
]

for indice, cola in enumerate(colas):
    tamaño = cola.max
    print(f"Poblando cola {indice + 1} (tamaño {tamaño})...")
    inicio = time.time()
    
    for i in range(tamaño):
        valor = elementos[i % 5]  # Ciclo A, B, C, D, E
        cola.enqueue(valor)
    
    tiempo_transcurrido = time.time() - inicio
    print(f"Cola {indice + 1} poblada en {tiempo_transcurrido:.2f} segundos\n")
