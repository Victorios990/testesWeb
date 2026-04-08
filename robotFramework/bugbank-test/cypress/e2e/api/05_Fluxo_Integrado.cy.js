describe('API - Fluxo integrado com ID fixo', () => {
  const atividadeId = 30;

  it('Deve criar uma nova atividade com ID fixo', () => {
    const novaAtividade = {
      id: atividadeId,
      title: 'Atividade Fluxo',
      dueDate: new Date().toISOString(),
      completed: false
    };

    cy.request({
      method: 'POST',
      url: 'https://fakerestapi.azurewebsites.net/api/v1/Activities',
      headers: {
        accept: 'text/plain; v=1.0',
        'Content-Type': 'application/json; v=1.0'
      },
      body: novaAtividade
    }).then((response) => {
      expect(response.status).to.eq(200);
      expect(response.body.id).to.eq(atividadeId);
    });
  });

  it('Deve buscar a atividade criada', () => {
    cy.request({
      method: 'GET',
      url: `https://fakerestapi.azurewebsites.net/api/v1/Activities/${atividadeId}`,
      headers: {
        accept: 'text/plain; v=1.0'
      }
    }).then((response) => {
      expect(response.status).to.eq(200);
      expect(response.body.id).to.eq(atividadeId);
    });
  });

  it('Deve atualizar a atividade', () => {
    const atividadeAtualizada = {
      id: atividadeId,
      title: 'Atividade Atualizada',
      dueDate: new Date().toISOString(),
      completed: true
    };

    cy.request({
      method: 'PUT',
      url: `https://fakerestapi.azurewebsites.net/api/v1/Activities/${atividadeId}`,
      headers: {
        accept: 'text/plain; v=1.0',
        'Content-Type': 'application/json; v=1.0'
      },
      body: atividadeAtualizada
    }).then((response) => {
      expect(response.status).to.eq(200);
      expect(response.body.title).to.eq('Atividade Atualizada');
    });
  });

  it('Deve deletar a atividade', () => {
    cy.request({
      method: 'DELETE',
      url: `https://fakerestapi.azurewebsites.net/api/v1/Activities/${atividadeId}`,
      headers: {
        accept: '*/*'
      }
    }).then((response) => {
      expect(response.status).to.eq(200);
    });
  });
});