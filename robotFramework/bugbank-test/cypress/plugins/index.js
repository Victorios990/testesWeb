const mysql = require('mysql2');

module.exports = (on, config) => {
  on('task', {
    queryDb(query) {
      const connection = mysql.createConnection({
        host: 'localhost',
        user: 'root',
        password: '',
        database: 'meu_banco'
      });

      return new Promise((resolve, reject) => {
        connection.query(query, (error, results) => {
          if (error) reject(error);
          else resolve(results);
        });
      });
    }
  });
};