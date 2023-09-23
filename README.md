# API de Controle de Disciplinas e Tarefas

Esta API foi desenvolvida para explorar as técnicas relacionadas a APIs. Ela menciona vários endpoints e métodos, como POST, GET, PUT, PATCH, DELETE e GET, que permitem realizar consultas, exclusões e atualizações em alunos, tarefas e disciplinas presentes no sistema.
## Modelos de Dados

- **Aluno:** Representa um aluno com os campos nome e email.
- **Disciplina:** Representa uma disciplina com os campos nome e descrição.
- **Tarefa:** Representa uma tarefa com os campos título, descrição, data, estado (completo), associação a alunos (alunosTarefas) e associação a disciplinas (disciplinasTarefas).

## Configurando do Ambiente

Para configurar o ambiente, siga as etapas abaixo no terminal:

1. Clone este repositório: `git clone <URL do repositório>`.
2. Crie um ambiente virtual: `python -m venv .env`.
3. Ative o ambiente virtual: `source .env/bin/activate` (Linux/macOS) ou `.env\Scripts\activate` (Windows).
4. Instale as dependências: `pip install -r requirements.txt`.
5. Para executar a aplicação: `python manage.py runserver`.

## EndPoints da API

### Consulta de Alunos:

- `/api/alunos/` (método GET): Retorna a lista de todos os alunos.

### Criação de um Aluno:

- `/api/alunos/` (método POST): Permite a criação de um novo aluno.

### Detalhes do Aluno:

- `/api/alunos/<id>/` (método GET): Retorna detalhes específicos de um aluno com base no ID.

### Atualização de um Aluno:

- `/api/alunos/<id>/` (método PUT): Permite a atualização dos detalhes de um aluno específico com base no ID.

### Exclusão de um Aluno:

- `/api/alunos/<id>/` (método DELETE): Permite a exclusão de um aluno específico com base no ID. Todas as tarefas associadas a esse aluno serão excluídas ou desassociadas.

### Busca de todas as tarefas de um determinado aluno:

- `/api/alunos/<id>/tarefas` (método GET): Permite a busca de todas as tarefas de um único aluno.

(Os URLs permanecem os mesmos para disciplinas e tarefas, apenas com a alteração da palavra "alunos" por "disciplinas" ou "tarefas").

## Exemplos de Testes

### Alunos:

- {
- "nome": "Vinicius de Morais",
- "email": "viniciusmoraaais@gmail.com"
- }

### Disciplinas:
- {
- "nome": "Geografia",
- "descricao": "Estudos geográficos sobre o mundo"
- }
### Tarefas:
- { 
- "titulo": "Estudo sobre planícies",
- "descrição":"Avaliação sobre como são e como se comportam as planícies do nosso terreno"
- "data": "2023-10-24"
- "estado": false,
- "aluno: 1
- "disciplina: [1]
- }
