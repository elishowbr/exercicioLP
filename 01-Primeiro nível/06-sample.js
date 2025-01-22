const nomeUsuario = "Pedro";
const idadeUsuario = 25;
const online = true;

function displayUser(nome, idade, on) {
    if (on) {
        console.log(nome + " tem " + idade + " anos e está ativo.");
    } else {
        console.log(nome + " está inativo.");
    }
}

displayUser(nomeUsuario, idadeUsuario, online);
