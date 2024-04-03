# CRUD de Usuários | FLASK

Esta é uma parte do projeto em Flask que implementa operações CRUD (Create, Read, Update, Delete) em uma entidade de usuário.

## Funcionalidades Implementadas

1. **Página Inicial**: Página inicial que exibe um formulário de login/cadastro.
2. **Cadastro de Usuário**: Funcionalidade para cadastrar novos usuários no sistema.
3. **Listagem de Usuários**: Página que lista todos os usuários cadastrados.
4. **Atualização de Senha**: Permite que os usuários atualizem suas senhas.
5. **Exclusão de Usuário**: Permite que os usuários sejam excluídos do sistema.

## Estrutura de Pastas

- `app.py`: Arquivo principal do aplicativo Flask com as rotas e funcionalidades implementadas.
- `connection.py`: Arquivo com funções para interagir com o banco de dados (criar, ler, atualizar, deletar usuários).
- `templates/`: Pasta que contém os arquivos HTML das páginas do aplicativo.
  - `index.html`: Página inicial com o formulário de login/cadastro.
  - `usuarios.html`: Página para listar os usuários cadastrados.
- `static/`: Pasta que contém os arquivos estáticos do aplicativo, como CSS, JavaScript, etc.
  - `css/`: Pasta que contém os arquivos CSS para estilizar as páginas HTML.

## Como Executar o Projeto

1. Certifique-se de ter o Python e o Flask instalados em seu sistema.
2. Clone este repositório em sua máquina local.
3. Navegue até o diretório do projeto.
4. Execute o comando `python app.py` para iniciar o servidor Flask.
5. Acesse o aplicativo em seu navegador em `http://localhost:5000`.

## Próximos Passos

- Implementar autenticação de usuários.
- Melhorar a estilização das páginas.
- Adicionar funcionalidades adicionais conforme necessário.

Este é um projeto em andamento e será atualizado conforme novas funcionalidades forem implementadas.
