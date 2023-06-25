
function MensageError(){
    Swal.fire({
        icon: "error",
        title: "Opa!",
        text: "Ops! Parece que alguma informação fornecida está incorreta.",
        confirmButtonText: "OK",
      });
}

function MensageSucess(){
    Swal.fire({
        icon: "success",
        title: "Olá!",
        text: "Seja Bem-Vindo.",
        confirmButtonText: "OK",  
    }).then(() => {
      window.location.href = "index.html";
      });
}

const teste = document.getElementById("formId");
teste.addEventListener('submit', (event) => {
event.preventDefault();

    
fetch("../php/a.php", {
    method: "POST",
    header: {"Content-Type":"application/json"},
    body: new FormData(teste)
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Erro no servidor: " + response.status);
      }
      return response.json();
    })
    .then((data) => {
        console.log(data);
        if (data.status === "error") {
        MensageError();
      } else if (data.status === "sucess") {
        MensageSucess(data.status);
      } else {
        throw new Error("Dados não reconhecidos: ");
      }
    })
    .catch((error) => {
        MensageError("Erro na requisição: " + error.message);
    })
    .finally(() => { 
    })});
