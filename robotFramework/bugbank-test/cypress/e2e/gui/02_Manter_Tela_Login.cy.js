import telaLogin from '../../support/pages/telaLogin';

describe('Fluxo de Login e Logout', () => {
  beforeEach(() => {
    telaLogin.acessarLogin();
    telaLogin.preencherCredenciais('victor.laurentino90@gmail.com', 'agnes123456');
    telaLogin.clicarBotaoEntrar();
  });

  it('Deve validar elementos do menu superior', () => {
    telaLogin.home().should('be.visible').and('contain', 'Home');
    telaLogin.listaDeCompras().should('be.visible').and('contain', 'Lista de Compras');
    telaLogin.carrinho().should('be.visible').and('contain', 'Carrinho');
  });

  it('Deve realizar logout e retornar à tela de login', () => {
    telaLogin.logout().click();
    telaLogin.validarRetornoTelaLogin();
  });
});