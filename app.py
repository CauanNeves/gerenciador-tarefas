from colorama import Fore, Style, init
from tabulate import tabulate
from datetime import datetime
from time import sleep
import sqlite3
import os


# Caminho para o banco de dados
db_path = os.path.join(os.getcwd(), 'database_tasks.db')
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

#Resetando a cor do prompt 
init(autoreset=True)

#-------------------Funções secundárias ------------------------
#Obtendo confirmação para salvar a alteração
def ask_commit():
    show_datas()
    confirm= input(Fore.GREEN + 'Salvar? (s/n)').upper()
    while confirm not in ['S', 'N']:
        print(Fore.RED + 'Por favor, responda com "s" para sim ou "n" para não.')
        confirm= input(Fore.GREEN + 'Salvar? (s/n)').upper()
    
    if confirm == 'S':
        connection.commit()
        print(Fore.GREEN + 'Alterações salvas com sucesso.')
        sleep(1)
    else:
        connection.rollback()
        print(Fore.GREEN + 'Alterações Descartadas')

#Validando se o Id existe na tabela
def validate_id(id):
    cursor.execute('SELECT EXISTS(SELECT 1 FROM tasks WHERE id=?)', (id,))
    return cursor.fetchone()[0]



#------------------Funções principas----------------
# Visualizar tarefas
def show_datas():
    cursor.execute('SELECT id, task, previous_dt, status FROM tasks')
    datas = cursor.fetchall()
    
    table = [['Id', 'Tarefa', 'Data para finalizar', 'Status']]
    for row in datas:
        table.append(list(row))
        
    print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

#Adicionar Tarefas
def add_task():
    show_datas()
    task= input('Tarefa:\n')
    while True:
        try:
            previous_dt= input('Data para finalização da tarefa (dd-mm-yyyy):\n')
            previous_date = datetime.strptime(previous_dt, '%d-%m-%Y')
            if previous_date < datetime.now():
                print(Fore.RED + 'A data para finalização da tarefa não pode ser anterior ao dia de hoje')
            else:
                break
        except:
            print(Fore.RED + 'Formato de data inválido. Use o formato dd-mm-yyyy.')
            
    date = datetime.now().strftime('%d-%m-%Y')       
    cursor.execute('INSERT INTO tasks (task, creation_dt, previous_dt) VALUES (?, ?, ?)', (task, date, previous_dt))
    
    ask_commit()

#Marcando tarefa como conluída
def task_completed():
    show_datas()
    ids= input(Fore.CYAN + 'Informe o id da tarefa que já foi concluída (caso seja mais de uma separe apenas com um espaço):\n').split()
    for id in ids:
        if validate_id(0):
            print(Fore.RED + '\nId selecionado não é válido.')
            sleep(1)
            return
        cursor.execute('UPDATE tasks SET status = ? WHERE id= ?', (1, id))
    ask_commit()

#Remover tarefa
def del_task():
    show_datas()
    ids= input(Fore.CYAN + 'Informe o id da tarefa (caso seja mais de uma separe apenas com um espaço):\n').split()
    for id in ids:
        if validate_id(id) == 0:
            print(Fore.RED + '\nId selecionado não é válido.')
            sleep(1)
            return
        cursor.execute('DELETE FROM tasks WHERE id= ?', (id,))    
    ask_commit()

#-------------------Funções do Prompt------------------------
def navbar():
    #Exibe a barra de navegação no terminal.
    print(f"{Fore.CYAN + Style.BRIGHT + '=' * 110}\n{Fore.GREEN + Style.BRIGHT + 'Tarefas'.center(110)}\n{Fore.CYAN + Style.BRIGHT + '=' * 110}")
    
def prompt_cls():
    #limpa o terminal
    os.system('cls' if os.name== 'nt' else 'clear')

def main_menu():
    prompt_cls()
    navbar()
    show_datas()
    print(Fore.CYAN + 'Opções:\n' + Fore.WHITE + ' 0. Adicionar nova tarefa\n 1. Marcar tarefa como concluída\n 2. Remover tarefa\n 3. Informações\n 4. Sair')
    to_do= input(Fore.CYAN + 'Informe o número da opção que deseja:\n')
    return to_do

class Task:
    def main():
        try:
            while True:
                
                to_do= main_menu()
                while to_do not in ['0', '1', '2', '3', '4']:
                    print(Fore.RED + 'O número da opção informada não consta no programa.')
                    sleep(1)
                    to_do = main_menu()
                
                if to_do == '0':
                    prompt_cls()
                    navbar()
                    add_task()
                
                elif to_do == '1':
                    prompt_cls()
                    navbar()
                    task_completed()
                
                elif to_do == '2':
                    prompt_cls()
                    navbar()
                    del_task()
                    
                elif to_do == '3':
                    prompt_cls()
                    print(Fore.YELLOW + '''
Este programa foi desenvolvido por Cauan Silva das Neves.
Redes e meios de comunicação:
 Github: https://github.com/CauanNeves
 LinkedIn: https://www.linkedin.com/in/cauan-neves-65916a228/
                          ''')
                    input(Fore.CYAN + 'Precione enter para continuar...')
                    
                elif to_do == '4':
                    break
                    
        finally:
            connection.close()
    
#Executando    
if __name__ == '__main__':
    app= Task
    app.main()