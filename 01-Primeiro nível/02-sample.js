let administrador = true;

function verificarAdmin(usuario) {
    if (administrador && usuario.isAdmin) {
        console.log("Acesso permitido ao administrador.");
    } else {
        console.log("Acesso negado.");
    }
}

const user = { nome: "João", isAdmin: true };
verificarAdmin(user);
