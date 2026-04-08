# Testes Automatizados - BugBank

Este projeto contém testes automatizados usando Robot Framework para o site https://bugbank.netlify.app.

## Estrutura

BUGBANK-TEST/
│
├── gui/                         # Testes de interface (Robot Framework + Selenium)
│   ├── resources/
│   │   └── keywords.robot
│   ├── variables/
│   │   └── variables.robot
│   └── tests/
│       └── login_tests.robot
│
├── api/                         # Testes de API (Robot Framework + RequestsLibrary)
│   ├── resources/
│   │   └── api_keywords.robot
│   ├── variables/
│   │   └── api_variables.robot
│   └── tests/
│       └── activities_api_tests.robot
│
├── results/                     # Relatórios e logs
│
├── cypress/                     # (futuramente) testes Cypress
│   ├── e2e/
│   ├── fixtures/
│   ├── support/
│   └── cypress.config.js
│
└── requirements.txt  

## Executando os testes

Use o comando abaixo para executar os testes:

GUI com RobotFramework

robot -d results gui/tests/login_tests.robot

API com RobotFramework

robot -d results api/tests/activities_api_tests.robot

Cypress em headless

npx cypress run
