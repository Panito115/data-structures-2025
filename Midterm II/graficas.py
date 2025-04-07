import csv
import matplotlib.pyplot as plt

# === Leer datos del CSV ===
archivo_csv = "tiempos_bst.csv"

insert_data = {
    "insert() BST": [],
    "insert() AVL": []
}

search_data = {
    "search() BST": [],
    "search() AVL": []
}

with open(archivo_csv, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row["Operacion"] == "Operacion":
            continue
        op = row["Operacion"]
        cantidad = int(row["Cantidad de Datos"])
        tiempo_promedio = float(row["Tiempo Promedio por Dato (s)"])

        if op in insert_data:
            insert_data[op].append((cantidad, tiempo_promedio))
        elif op in search_data:
            search_data[op].append((cantidad, tiempo_promedio))

# Ordenar los puntos por cantidad
for grupo in (insert_data, search_data):
    for key in grupo:
        grupo[key].sort()

xticks_custom = [1000, 5000, 10000, 15000, 20000, 25000]

# === GRÁFICO 1: insert() promedio ===
plt.figure(figsize=(10, 6))

# BST (lineal)
x_bst = [p[0] for p in insert_data["insert() BST"]]
y_bst = [p[1] for p in insert_data["insert() BST"]]
plt.plot(x_bst, y_bst, marker='o', label="insert() BST")

# AVL (logarítmico)
x_avl = [p[0] for p in insert_data["insert() AVL"]]
y_avl = [p[1] for p in insert_data["insert() AVL"]]
plt.plot(x_avl, y_avl, marker='o', label="insert() AVL (log scale)", linestyle='--')

plt.yscale("log")
plt.title("Tiempo promedio de insert() - BST vs AVL")
plt.xlabel("Cantidad de Datos")
plt.ylabel("Tiempo Promedio por Dato (segundos)")
plt.xticks(xticks_custom)
plt.legend()
plt.grid(True, which="both", linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.savefig("insert_promedio_log_mix.png")
plt.show()

# === GRÁFICO 2: search() promedio ===
plt.figure(figsize=(10, 6))

# BST (lineal)
x_bst = [p[0] for p in search_data["search() BST"]]
y_bst = [p[1] for p in search_data["search() BST"]]
plt.plot(x_bst, y_bst, marker='o', label="search() BST")

# AVL (logarítmico)
x_avl = [p[0] for p in search_data["search() AVL"]]
y_avl = [p[1] for p in search_data["search() AVL"]]
plt.plot(x_avl, y_avl, marker='o', label="search() AVL (log scale)", linestyle='--')

plt.yscale("log")
plt.title("Tiempo promedio de search() - BST vs AVL")
plt.xlabel("Cantidad de Datos")
plt.ylabel("Tiempo Promedio por Dato (segundos)")
plt.xticks(xticks_custom)
plt.legend()
plt.grid(True, which="both", linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.savefig("search_promedio_log_mix.png")
plt.show()
