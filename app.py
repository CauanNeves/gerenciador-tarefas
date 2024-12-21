from database import DataBase
from colorama import Fore, Style, init
from tabulate import tabulate
from datetime import datetime
from time import sleep
import sqlite3
import os
from database import DataBase

# Caminho para o banco de dados
db_path = os.path.join(os.getcwd(), 'database_tasks.db')
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

#Resetando a cor do prompt 
init(autoreset=True)

#----------Funções secundárias --------------
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
    cursor.execute('INSERT INTO tasks (task, creation_dt, previous_dt) VALUES (?, ?, ?)', (task, date, previous_date))
    
    ask_commit()

#Marcando tarefa como conluída
def task_completed(id):
    if validate_id(0):
        print(Fore.RED + '\nId selecionado não é válido.')
        sleep(1)
        return
    cursor= connection.cursor()
    cursor.execute('UPDATE tasks SET status = ? WHERE id= ?', (1, id))
    ask_commit()

#Remover tarefa
def del_task(id):
    if validate_id(id) == 0:
        print(Fore.RED + '\nId selecionado não é válido.')
        sleep(1)
        return
    
    cursor.execute('DELETE FROM tasks WHERE id= ?', (id,))
    
    ask_commit()

#Executando    
if __name__ == '__main__':
    show_datas()
    add_task()