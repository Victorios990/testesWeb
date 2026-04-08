*** Settings ***
Library    RequestsLibrary

*** Variables ***
${SESSION}     fake_api

*** Keywords ***
Criar sessão da API
    Create Session    ${SESSION}    ${BASE_URL}

Fazer requisição GET em Activities
    ${headers}=    Create Dictionary    accept=application/json
    ${response}=    GET On Session    ${SESSION}    ${ENDPOINT}    headers=${headers}
    Set Suite Variable    ${response}

Validar status code 200
    Should Be Equal As Integers    ${response.status_code}    200

Validar que a lista de atividades não está vazia
    ${json}=    Set Variable    ${response.json()}
    Should Be True    len($json) > 0    A lista de atividades está vazia