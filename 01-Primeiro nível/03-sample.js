const data1 = "2024-01-01";
const data2 = "2024-01-10";

function calcDif(d1, d2) {
    const diferencaMs = new Date(d2) - new Date(d1);
    const diferencaSegs = diferencaMs / 1000;
    const diferencaMins = diferencaSegs / 60;
    const diferencaHoras = diferencaMins / 60;
    const diferencaDias = diferencaHoras / 24;
    return diferencaDias
}

const result = calcDif(data1, data2);
console.log(result);
