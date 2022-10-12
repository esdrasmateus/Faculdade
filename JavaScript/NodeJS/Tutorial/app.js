const path = require("path");

console.log(path.sep);

const filePath = path.join("Python","Exercicios Udemy","S06E02.py");
console.log(filePath);

const base = path.basename(filePath);
console.log(base);

const absolute = path.resolve(__dirname, "/Python","Exercicios Udemy","S06E02.py");
console.log(absolute);