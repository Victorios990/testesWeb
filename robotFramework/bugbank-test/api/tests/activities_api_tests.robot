*** Settings ***
Library    RequestsLibrary
Resource   ../variables/api_variables.robot
Resource   ../resources/api_keywords.robot

*** Test Cases ***
CT001 - Validar retorno da API de atividades
    [Documentation]    Verifica se o endpoint GET /Activities retorna status 200 e lista de atividades
    Criar sessão da API
    Fazer requisição GET em Activities
    Validar status code 200
    Validar que a lista de atividades não está vazia
