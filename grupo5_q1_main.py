from grupo5_q1 import Node, insert, search

# Criar a árvore binária de busca
root = None
keys = [20, 8, 22, 4, 12, 10, 14]

# Inserir os valores
for key in keys:
    root = insert(root, key)

# Buscar um valor na árvore
key_to_find = 10
if search(root, key_to_find):
    print(f"Valor {key_to_find} encontrado na árvore.")
else:
    print(f"Valor {key_to_find} não encontrado na árvore.")
