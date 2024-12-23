# 📝 Gerenciador de Tarefas com SQLite e Python

Este é um aplicativo simples de gerenciamento de tarefas desenvolvido em **Python**, utilizando **SQLite** para armazenamento de dados, **Colorama** para cores no terminal e **Tabulate** para formatação de tabelas.

---

## 🚀 Funcionalidades

- 📋 **Listar Tarefas:** Visualize todas as tarefas em formato de tabela.
- ➕ **Adicionar Tarefas:** Adicione novas tarefas com uma data de conclusão.
- ✅ **Marcar Tarefa como Concluída:** Atualize o status de uma tarefa.
- 🗑️ **Remover Tarefas:** Exclua tarefas pelo ID.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **SQLite3** (banco de dados local)
- **Colorama** (cores no terminal)
- **Tabulate** (formatação de tabelas)

---

## 📦 Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/CauanNeves/gerenciador-tarefas.git
   ```
2. Acesse a pasta do projeto:
   ```bash
   cd seurepositorio
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute o programa:
   ```bash
   python app.py
   ```

---

## 📊 Estrutura do Banco de Dados

A tabela `tasks` possui a seguinte estrutura:

- `id` (INTEGER, PRIMARY KEY)
- `task` (TEXT, descrição da tarefa)
- `creation_dt` (TEXT, data de criação)
- `previous_dt` (TEXT, data de conclusão)
- `status` (INTEGER, 0 - pendente, 1 - concluída)

---

## 🤝 Contribuição

Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias.

1. Faça um fork do projeto.
2. Crie uma nova branch:
   ```bash
   git checkout -b feature/nova-funcionalidade
   ```
3. Envie suas alterações:
   ```bash
   git commit -m 'Adiciona nova funcionalidade'
   ```
4. Faça o push para a branch:
   ```bash
   git push origin feature/nova-funcionalidade
   ```
5. Abra um Pull Request.


---

Desenvolvido por **Cauan Silva das Neves**  
🔗 [GitHub](https://github.com/CauanNeves) | [LinkedIn](https://www.linkedin.com/in/cauan-neves-65916a228/)

---

⚡ *Gerencie suas tarefas com eficiência!*

