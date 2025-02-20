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
            return 

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

    def search(self, key: str) -> list[int]:
        positions = []
        if self.front == -1 or self.front > self.rear:
            return positions
        for i in range(self.front, self.rear + 1):
            if self.elements[i] == key:
                positions.append(i)
        return positions

import cProfile
import pstats

n = n = 500000  # Tamaño base reducido para pruebas rápidas
  # Tamaño base (ajustable)
sizes = [n, 2*n, 3*n, 4*n, 5*n]
elementos = ['a', 'b', 'c']

for i, size in enumerate(sizes):
    print(f"\n{'='*50}\nPerfilando cola {i+1} (Tamaño: {size})")
    
    # Crear y poblar cola
    queue = LinearQueue(size)
    
    # Perfilado de Enqueue
    pr_enqueue = cProfile.Profile()
    pr_enqueue.enable()
    for j in range(size):
        queue.enqueue(elementos[j % 3])
    pr_enqueue.disable()
    
    # Perfilado de Search (elemento no existente)
    pr_search = cProfile.Profile()
    pr_search.enable()
    queue.search('x')  # 'x' no existe en la cola
    pr_search.disable()
    
    # Perfilado de Dequeue (vaciar toda la cola)
    pr_dequeue = cProfile.Profile()
    pr_dequeue.enable()
    while queue.front != -1 and queue.front <= queue.rear:
        queue.dequeue()
    pr_dequeue.disable()
    
    # Reportes
    stats_enqueue = pstats.Stats(pr_enqueue)
    stats_search = pstats.Stats(pr_search)
    stats_dequeue = pstats.Stats(pr_dequeue)
    
    print("\n[Enqueue]")
    stats_enqueue.strip_dirs().sort_stats('cumulative').print_stats(3)
    print(f"Tiempo total enqueue: {stats_enqueue.total_tt:.4f} s")
    
    print("\n[Search]")
    stats_search.strip_dirs().sort_stats('cumulative').print_stats(3)
    print(f"Tiempo total search: {stats_search.total_tt:.6f} s")
    
    print("\n[Dequeue]")
    stats_dequeue.strip_dirs().sort_stats('cumulative').print_stats(3)
    print(f"Tiempo total dequeue: {stats_dequeue.total_tt:.4f} s")
    
    # Métricas adicionales
    print(f"\nResumen:")
    print(f"- Enqueue: {stats_enqueue.total_tt/size*1e6:.2f} µs/elemento")
    print(f"- Dequeue: {stats_dequeue.total_tt/size*1e6:.2f} µs/elemento")
    print(f"- Search: {stats_search.total_tt*1e6:.2f} µs")