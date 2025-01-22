function listarPares(sequenciaNumerica) {
    const listaPares = [];
    for (let i = 0; i < sequenciaNumerica.length; i++) {
        if (sequenciaNumerica[i] % 2 === 0) {
            listaPares.push(sequenciaNumerica[i]);
        }
    }
    return listaPares;
}

let conjunto = [1, 2, 3, 4, 5, 6];
let listaNova = listarPares(conjunto);
console.log(listaNova);
