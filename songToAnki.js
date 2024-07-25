var {x, y, translatedX} = require("./songGraph.json");

// console.log(x)

const fs = require("fs")

function toCSV() {
    return(
        x.map((word, index) => {
    return(`<${word} : ${translatedX[index]}`)
}).join("\n"))
}

// console.log(toCSV())

fs.writeFile("8Kambarys-Save.txt", 
    toCSV(),
    (er)=> {console.log(er)}
)
