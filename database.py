import sqlite3
import os
from datetime import datetime

class DataBase:
    def __init__(self, db_path):
        self.db_path = db_path
    
    def add(self, task, previous_date):
        # Conectando ao banco de dados
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
        
            # Criando a tabela
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS tasks(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    task TEXT NOT NULL,
                    creation_dt TEXT NOT NULL,
                    previous_dt TEXT,
                    status BOOLEAN DEFAULT 0
                );
            ''')