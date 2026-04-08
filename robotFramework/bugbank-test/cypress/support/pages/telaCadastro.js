class TelaCadastro {
  acessarCadastro() {
    cy.visit('https://front.serverest.dev/cadastrarusuarios');
  }

  campoNome() {
    return cy.get('[data-testid="nome"]');
  }

  campoEmail() {
    return cy.get('[data-testid="email"]');
  }

  campoSenha() {
    return cy.get('[data-testid="password"]');
  }

  toggleAdmin() {
    return cy.get('[data-testid="checkbox"]');
  }

  botaoCadastrar() {
    return cy.get('[data-testid="cadastrar"]');
  }

  botaoEntrar() {
    return cy.get('[data-testid="entrar"]');
  }

  preencherFormulario({ nome, email, senha, administrador }) {
    this.campoNome().clear().type(nome);
    this.campoEmail().clear().type(email);
    this.campoSenha().clear().type(senha);
    if (administrador) {
      this.campoAdministrador().check({ force: true });
    }
  }

  cadastrar() {
    this.botaoCadastrar().click();
  }

  entrar() {
    this.botaoEntrar().click();
  }
}

export default new TelaCadastro();