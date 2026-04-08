*** Settings ***
Library    SeleniumLibrary
Resource  ../variables/variables.robot

*** Keywords ***
Abrir o navegador e acessar o site
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Page Contains Element    xpath=//input[@data-testid="email"]    timeout=10s

Fazer login com credenciais válidas
    Input Text    xpath=//input[@data-testid="email"]    ${VALID_USER}
    Input Password    xpath=//input[@data-testid="senha"]    ${VALID_PASS}
    Click Button    xpath=//button[@data-testid="entrar"]
    Wait Until Page Contains    Home    timeout=10s

Validar elementos do menu superior
    Element Should Be Visible    xpath=//a[@data-testid="home"]
    Element Should Be Visible    xpath=//a[@data-testid="lista-de-compras"]
    Element Should Be Visible    xpath=//a[@data-testid="carrinho"]

Adicionar item à lista de compras

    # Digita o código ou nome do produto no campo de busca
    Wait Until Page Contains Element    xpath=//input[@data-testid="pesquisar"]    timeout=10s
    Input Text    xpath=//input[@data-testid="pesquisar"]    Logitech MX Vertical

    # Clica no botão "Pesquisar"
    Click Button    xpath=//button[@data-testid="botaoPesquisar"]

    # Aguarda o produto ser exibido na lista
    Wait Until Page Contains Element    xpath=//button[@data-testid="adicionarNaLista"]    timeout=10s

    # Adiciona o produto encontrado
    Scroll Element Into View    xpath=(//button[@data-testid="adicionarNaLista"])[1]
    Click Button    xpath=(//button[@data-testid="adicionarNaLista"])[1]

    # Aguarda a confirmação de que o produto foi adicionado
    Wait Until Page Contains Element    xpath=//div[@data-testid="shopping-cart-product-name"]    timeout=10s


Validar produto na lista
    Element Should Contain    xpath=//div[@data-testid="shopping-cart-product-name"]    ${PRODUTO_NOME}

Limpar lista de compras
    Click Button    xpath=//button[@data-testid="limparLista"]

Validar carrinho vazio
    Wait Until Page Contains Element    xpath=//p[@data-testid="shopping-cart-empty-message"]    timeout=10s
    Element Should Contain    xpath=//p[@data-testid="shopping-cart-empty-message"]    Seu carrinho está vazio


Fazer logout
    Click Button    xpath=//button[@data-testid="logout"]


Validar retorno à tela de login
    Wait Until Page Contains Element    xpath=//h1[contains(text(), 'Login')]    timeout=10s
    Element Should Contain    xpath=//h1[contains(@class, 'font-robot')]    Login

Fechar o navegador
    Close Browser

