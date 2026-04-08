describe('API - Buscar atividade por ID', () => {
  it('Deve retornar os dados da atividade com ID 2', () => {
    cy.request({
      method: 'GET',
      url: 'https://fakerestapi.azurewebsites.net/api/v1/Activities/30',
      headers: {
        accept: 'text/plain; v=1.0'
      }
    }).then((response) => {
      expect(response.status).to.eq(200);
      expect(response.body).to.have.property('id', 30);
      expect(response.body).to.have.property('title', 'Activity 30');
      expect(response.body).to.have.property('completed', true);
    });
  });
});

describe('API - Buscar atividade inexistente', () => {
    
  it('Deve retornar erro 404 ao buscar atividade com ID 31', () => {
    cy.request({
      method: 'GET',
      url: 'https://fakerestapi.azurewebsites.net/api/v1/Activities/31',
      headers: {
        accept: 'text/plain; v=1.0'
      },
      failOnStatusCode: false 
    }).then((response) => {
      expect(response.status).to.eq(404);
      expect(response.body).to.have.property('title');
      expect(response.body.title).to.include('Not Found');
    });
  });
});