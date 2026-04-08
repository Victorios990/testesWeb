# Testes Automatizados - BugBank

Este projeto contém testes automatizados usando Robot Framework para o site https://bugbank.netlify.app.

## Estrutura

- `resources/keywords.robot`: Keywords reutilizáveis
- `tests/login_tests.robot`: Casos de teste de login
- `variables/variables.robot`: Variáveis globais
- `results/`: Relatórios de execução

## Executando os testes

Use o comando abaixo para executar os testes:

robot -d results tests/login_tests.robot
