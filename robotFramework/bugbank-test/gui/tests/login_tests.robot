*** Settings ***
Documentation     Testes no Serverest - Login, busca, carrinho, logout
Library           SeleniumLibrary
Resource          ../resources/keywords.robot

*** Test Cases ***
Testes no Serverest
    Abrir o navegador e acessar o site
    Fazer login com credenciais válidas
    Page Should Contain  Home
    Validar elementos do menu superior
    Adicionar item à lista de compras
    Validar produto na lista
    Limpar lista de compras
    Validar carrinho vazio
    Fazer logout
    Validar retorno à tela de login
    Fechar o navegador
