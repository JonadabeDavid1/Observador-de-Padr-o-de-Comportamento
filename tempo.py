import json
from datetime import datetime

# Função para converter uma string de tempo para um objeto datetime.time
def str_to_time(time_str):
    return datetime.strptime(time_str, '%H:%M').time()

# Função para converter um objeto datetime.time para uma string
def time_to_str(time_obj):
    return time_obj.strftime('%H:%M')

# Função para adicionar uma nova entrada de atividade
def add_entry(entries, start_time, end_time, description):
    entry = {
        'start_time': str_to_time(start_time),
        'end_time': str_to_time(end_time),
        'description': description
    }
    entries.append(entry)

# Função para exibir todas as entradas do dia
def display_entries(entries):
    for idx, entry in enumerate(entries):
        print(f"{idx + 1}. Das {entry['start_time']} às {entry['end_time']}, {entry['description']}.")

# Função para editar uma entrada de atividade
def edit_entry(entries, index, start_time, end_time, description):
    entries[index] = {
        'start_time': str_to_time(start_time),
        'end_time': str_to_time(end_time),
        'description': description
    }

# Função para deletar uma entrada de atividade
def delete_entry(entries, index):
    entries.pop(index)

# Função para salvar entradas em um arquivo JSON
def save_entries_to_file(entries, filename):
    with open(filename, 'w') as file:
        json_entries = [
            {
                'start_time': time_to_str(entry['start_time']),
                'end_time': time_to_str(entry['end_time']),
                'description': entry['description']
            }
            for entry in entries
        ]
        json.dump(json_entries, file, indent=4)

# Função para carregar entradas de um arquivo JSON
def load_entries_from_file(filename):
    try:
        with open(filename, 'r') as file:
            json_entries = json.load(file)
            entries = [
                {
                    'start_time': str_to_time(entry['start_time']),
                    'end_time': str_to_time(entry['end_time']),
                    'description': entry['description']
                }
            for entry in json_entries
            ]
            return entries
    except FileNotFoundError:
        return []

# Nome do arquivo para salvar as entradas
filename = 'atividades.json'

# Carregar entradas do arquivo ao iniciar o programa
entries = load_entries_from_file(filename)

# Loop principal para receber entradas do usuário
while True:
    print("\nDigite a opção desejada:")
    print("1. Adicionar nova atividade")
    print("2. Exibir atividades")
    print("3. Editar uma atividade")
    print("4. Deletar uma atividade")
    print("5. Salvar e sair")
    
    option = input("Opção: ")
    
    if option == '1':
        start_time = input("Digite o horário de início (HH:MM): ")
        end_time = input("Digite o horário de término (HH:MM): ")
        description = input("Digite a descrição da atividade: ")
        add_entry(entries, start_time, end_time, description)
        print("Atividade adicionada com sucesso!")
    elif option == '2':
        print("\nAtividades do dia:")
        display_entries(entries)
    elif option == '3':
        display_entries(entries)
        index = int(input("Digite o número da atividade que deseja editar: ")) - 1
        if 0 <= index < len(entries):
            start_time = input("Digite o novo horário de início (HH:MM): ")
            end_time = input("Digite o novo horário de término (HH:MM): ")
            description = input("Digite a nova descrição da atividade: ")
            edit_entry(entries, index, start_time, end_time, description)
            print("Atividade editada com sucesso!")
        else:
            print("Índice inválido.")
    elif option == '4':
        display_entries(entries)
        index = int(input("Digite o número da atividade que deseja deletar: ")) - 1
        if 0 <= index < len(entries):
            delete_entry(entries, index)
            print("Atividade deletada com sucesso!")
        else:
            print("Índice inválido.")
    elif option == '5':
        save_entries_to_file(entries, filename)
        print("Atividades salvas. Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
