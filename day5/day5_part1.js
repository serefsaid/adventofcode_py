const directionsFile = require('./day5_directions');
let directions = directionsFile.directions;

let array = ['B','V','W','T','Q','N','H','D'];
let array1 = ['B','W','D'];
let array2 = ['C','J','W','Q','S','T'];
let array3 = ['P','T','Z','N','R','J','F'];
let array4 = ['T','S','M','J','V','P','G'];
let array5 = ['N','T','F','W','B'];
let array6 = ['N','V','H','F','Q','D','L','B'];
let array7 = ['R','F','P','H'];
let array8 = ['H','P','N','L','B','M','S','Z'];
let arrays = [array,array1,array2,array3,array4,array5,array6,array7,array8];

for(let i = 0 ; i<directions.length ; i++){//transfering elements
    let moveQuantity =directions[i][0];
    for(let j=0;j<moveQuantity ; j++){
        let toAdd = arrays[directions[i][1]-1].shift();//remove first element of array (reduce 1 for equalize to index)
        arrays[directions[i][2]-1].unshift(toAdd);//adding to the other array as first element
    }
}
let resultText = '';
for(let q=0 ; q<arrays.length ; q++){//adding top elements of each stack to a text
    resultText += arrays[q][0];
}
console.log('answer of part 1 : '+resultText);//result (PSNRGBTFT)