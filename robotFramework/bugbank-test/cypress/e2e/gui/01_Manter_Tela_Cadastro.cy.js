import telaCadastro from '../../support/pages/telaCadastro';
import mensagens from '../../support/controllers/mensagens';

describe('Fluxo de Cadastro', () => {

  beforeEach(() => {
    telaCadastro.acessarCadastro();
  });

  it('Deve preencher e enviar o cadastro com sucesso', () => {
    cy.fixture('usuario').then((user) => {
      telaCadastro.campoNome().type(user.nome);
      telaCadastro.campoEmail().type(user.email);
      telaCadastro.campoSenha().type(user.senha);
      telaCadastro.toggleAdmin().click();
      telaCadastro.botaoCadastrar().click();
    });
  });

  it('Validacao de email em uso', () => {
    cy.fixture('usuario').then((user) => {
      telaCadastro.campoNome().type(user.nome);
      telaCadastro.campoEmail().type(user.email);
      telaCadastro.campoSenha().type(user.senha);
      telaCadastro.toggleAdmin().click();
      telaCadastro.botaoCadastrar().click();
      cy.contains(mensagens.emailEmUso()).should('be.visible');
    });
  });
});
