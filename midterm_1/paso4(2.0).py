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

import cProfile
import pstats

n = 500000  # Tamaño base reducido para pruebas rápidas
sizes = [n, 2*n, 3*n, 4*n, 5*n]
elementos = ['a', 'b', 'c']

for i, size in enumerate(sizes):
    queue = LinearQueue(size)
    
    # Configurar el profiler
    profiler = cProfile.Profile()
    profiler.enable()
    
    # Poblar la cola
    for j in range(size):
        elemento = elementos[j % 3]
        queue.enqueue(elemento)
    
    profiler.disable()
    
    # Generar reporte
    stats = pstats.Stats(profiler)
    stats.strip_dirs()
    
    print(f"\n{'='*50}\nAnálisis para cola {i+1} (Tamaño: {size})")
    stats.sort_stats('cumulative').print_stats(5)  # Top 5 funciones
    
    # Métricas adicionales
    total_time = stats.total_tt
    print(f"Resumen:")
    print(f"- Tiempo total: {total_time:.4f} segundos")
    print(f"- Tiempo por elemento: {total_time / size * 1e6:.2f} µs")
