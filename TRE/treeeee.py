import os
from tree import Tree, Node

def build_tree(path):
    
    root = Tree(os.path.basename(path) or path)

    try:
        for entry in os.scandir(path):
            if entry.is_dir():
                
                child_tree = build_tree(entry.path)
                root.insert_child(child_tree)
            else:
                # Si es archivo, agregar un Node
                file_node = Node(entry.name)
                root.insert_child(file_node)
    except PermissionError:
        pass  # Ignorar carpetas sin permisos

    return root

def print_tree(tree, indent=""):
    print(indent + tree.name)
    for child in tree.get_children():
        if isinstance(child, Tree):
            print_tree(child, indent + "    ")
        else:
            print(indent + "    " + child.name)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Uso: python script.py <path_del_directorio>")
        sys.exit(1)

    path = sys.argv[1]

    if not os.path.exists(path):
        print(f"El path '{path}' no existe.")
        sys.exit(1)

    tree = build_tree(path)
    print_tree(tree)
