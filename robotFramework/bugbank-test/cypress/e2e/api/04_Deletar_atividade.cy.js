describe('API - Deletar atividade', () => {
  it('Deve deletar a atividade com ID 3', () => {
    cy.request({
      method: 'DELETE',
      url: 'https://fakerestapi.azurewebsites.net/api/v1/Activities/3',
      headers: {
        accept: '*/*'
      },
      failOnStatusCode: false
    }).then((response) => {
      expect(response.status).to.eq(200); 
      expect(response.body).to.be.empty;
    });
  });
});