import random
import pandas as pd

# Função para gerar IDs únicos
def generate_id():
    return ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(6))

# Função para gerar nomes fictícios de itens
def generate_item_name():
    return ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(5))

# Categorias de itens
categories = ["Eletrônicos", "Roupas", "Alimentos", "Móveis", "Livros",
              "Jogos", "Beleza", "Esportes", "Automóveis", "Brinquedos",
              "Jardinagem", "Computadores", "Decoração", "Joias", "Animais"]

# Lista para armazenar os dados
data = []

# Criar 400 IDs e nomes de itens
for _ in range(400):
    item_id = generate_id()
    item_name = generate_item_name()
    category = random.choice(categories)
    value = round(random.uniform(30, 3000), 2)

    # Criar 5000 transações
    for _ in range(5000):
        customer_name = f'Cliente-{random.randint(1, 3000)}'
        phone_number = f'({random.randint(100, 999)}) {random.randint(100000, 999999)}'
        email = f'cliente{random.randint(1, 3000)}@exemplo.com'

        data.append([item_id, item_name, category, value, customer_name, phone_number, email])

# Criar um DataFrame com os dados
df = pd.DataFrame(data, columns=['cod ID', 'nome do item', 'categoria', 'valor', 'nome do comprador', 'telefone', 'e-mail'])

# Salvar os dados em um arquivo CSV
df.to_csv('dados.csv', index=False)
