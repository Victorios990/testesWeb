# Testes Automatizados - Serverest & FakeRestAPI

Este projeto contém testes automatizados usando Robot Framework (GUI e API) e Cypress (GUI e API).

- **GUI**: [https://front.serverest.dev](https://front.serverest.dev)
- **API**: [https://fakerestapi.azurewebsites.net](https://fakerestapi.azurewebsites.net)

## Estrutura

```
BUGBANK-TEST/
│
├── gui/                         # Testes de interface (Robot Framework + Selenium)
│   ├── resources/
│   │   └── keywords.robot
│   ├── variables/
│   │   └── variables.robot      # URL, browser, credenciais
│   └── tests/
│       └── login_tests.robot
│
├── api/                         # Testes de API (Robot Framework + RequestsLibrary)
│   ├── resources/
│   │   └── api_keywords.robot
│   ├── variables/
│   │   └── api_variables.robot  # BASE_URL, endpoint, session
│   └── tests/
│       └── activities_api_tests.robot
│
├── cypress/                     # Testes Cypress (GUI + API)
│   ├── e2e/
│   │   ├── api/                 # CRUD de atividades
│   │   └── gui/                 # Cadastro e login
│   ├── fixtures/
│   ├── support/
│   └── cypress.config.js
│
├── results/                     # Relatórios gerados pelo Robot Framework
└── requirements.txt
```

## Pré-requisitos

### Python / Robot Framework

```bash
pip install -r requirements.txt
```

> O ChromeDriver é baixado automaticamente pelo webdriver-manager.
> Caso não esteja instalado: `pip install webdriver-manager`

### Node.js / Cypress

```bash
npm install
```

## Executando os testes

> Execute todos os comandos abaixo a partir da pasta `robotFramework/bugbank-test/`:
> ```bash
> cd robotFramework/bugbank-test
> ```

### Robot Framework — GUI (Selenium + Chrome)

```bash
robot -d results gui/tests/login_tests.robot
```

### Robot Framework — API (RequestsLibrary)

```bash
robot -d results api/tests/activities_api_tests.robot
```

### Robot Framework — Todos os testes

```bash
robot -d results gui/tests/ api/tests/
```

### Cypress — Headless (todos)

```bash
npx cypress run
```

### Cypress — Somente API

```bash
npx cypress run --spec "cypress/e2e/api/**"
```

### Cypress — Somente GUI

```bash
npx cypress run --spec "cypress/e2e/gui/**"
```

### Cypress — Interface interativa

```bash
npx cypress open
```

## Relatórios

Após rodar os testes com Robot Framework, os relatórios ficam em `results/`:

- `results/report.html` — resumo dos testes
- `results/log.html` — log detalhado com screenshots

## Observações

- O usuário de teste do Serverest deve estar cadastrado como **não-administrador**.
  As credenciais estão em `gui/variables/variables.robot`.
- A API base URL está configurada em `api/variables/api_variables.robot`.
