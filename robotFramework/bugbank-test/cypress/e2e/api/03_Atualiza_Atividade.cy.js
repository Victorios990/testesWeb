describe('API - Atualizar atividade', () => {
  it('Deve atualizar a atividade com ID 3', () => {
    const atividadeAtualizada = {
      id: 0,
      title: 'Atividade Atualizada',
      dueDate: '2025-10-09T17:49:12.090Z',
      completed: true
    };

    cy.request({
      method: 'PUT',
      url: 'https://fakerestapi.azurewebsites.net/api/v1/Activities/3',
      headers: {
        accept: 'text/plain; v=1.0',
        'Content-Type': 'application/json; v=1.0'
      },
      body: atividadeAtualizada,
      failOnStatusCode: false
    }).then((response) => {
      expect(response.status).to.eq(200);
      expect(response.body.title).to.eq(atividadeAtualizada.title);
      expect(response.body.completed).to.be.true;
      expect(response.body.dueDate.startsWith('2025-10-09T17:49:12')).to.be.true;
    });
  });
});