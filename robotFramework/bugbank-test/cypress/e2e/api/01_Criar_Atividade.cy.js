describe('API - Criar atividade', () => {

  it('Deve criar uma nova atividade com sucesso', () => {
    const atividade = {
      id: 30,
      title: 'Atividade de Teste',
      dueDate: new Date().toISOString(),
      completed: true
    };

    cy.request({
      method: 'POST',
      url: 'https://fakerestapi.azurewebsites.net/api/v1/Activities',
      headers: {
        accept: 'text/plain; v=1.0',
        'Content-Type': 'application/json; v=1.0'
      },
      body: atividade,
      failOnStatusCode: false
    }).then((response) => {
      expect(response.status).to.eq(200);
      expect(response.body).to.have.property('id');
      expect(response.body.title).to.eq(atividade.title);
      expect(response.body.completed).to.be.true;
    });
  });
});