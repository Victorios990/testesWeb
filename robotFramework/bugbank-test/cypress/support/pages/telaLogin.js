class TelaLogin {
  acessarLogin() {
    cy.visit('https://front.serverest.dev/login');
  }

  preencherCredenciais(email, senha) {
    cy.get('[data-testid="email"]').type(email);
    cy.get('[data-testid="senha"]').type(senha);
  }

  clicarBotaoEntrar() {
    cy.get('[data-testid="entrar"]').click();
  }

  home() {
    return cy.get('[data-testid="home"]');
  }

  listaDeCompras() {
    return cy.get('[data-testid="lista-de-compras"]');
  }

  carrinho() {
    return cy.get('[data-testid="carrinho"]');
  }

  usuarioLogado() {
    return cy.get('[data-testid="usuario-logado"]');
  }

  logout() {
    return cy.get('[data-testid="logout"]');
  }

  validarLoginSucesso() {
    cy.url().should('include', '/home');
    cy.contains('Bem vindo').should('be.visible');
  }

  validarRetornoTelaLogin() {
    cy.url().should('include', '/login');
    cy.contains('Login').should('be.visible');
  }
}

export default new TelaLogin();