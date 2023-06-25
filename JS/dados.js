fetch('a.py') // O caminho para o arquivo JSON
  .then(response => response.json())
  .then(data => {
    // Manipule os dados recebidos aqui
    console.log(data); // Exemplo: exibir os dados no console
    
    // Acessar o elemento da tabela pelo ID
    const table = document.getElementById('dados-table');
    
    // Percorrer os dados e adicionar linhas à tabela
    data.forEach(item => {
      const row = table.insertRow();
      // Adicionar células à linha com os dados desejados
      // Exemplo: item.nome é o valor do campo "nome" do objeto JSON
      const cell1 = row.insertCell();
      cell1.innerHTML = item.nome;
      // Adicione mais células conforme necessário para outros campos
    });
  })
  .catch(error => {
    console.error('Erro:', error);
  });