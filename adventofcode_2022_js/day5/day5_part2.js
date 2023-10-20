const directionsFile = require('./day5_directions');
let directions = directionsFile.directions;

let arrayx = ['B','V','W','T','Q','N','H','D'];
let arrayx1 = ['B','W','D'];
let arrayx2 = ['C','J','W','Q','S','T'];
let arrayx3 = ['P','T','Z','N','R','J','F'];
let arrayx4 = ['T','S','M','J','V','P','G'];
let arrayx5 = ['N','T','F','W','B'];
let arrayx6 = ['N','V','H','F','Q','D','L','B'];
let arrayx7 = ['R','F','P','H'];
let arrayx8 = ['H','P','N','L','B','M','S','Z'];
let arrayxs = [arrayx,arrayx1,arrayx2,arrayx3,arrayx4,arrayx5,arrayx6,arrayx7,arrayx8];
for(let r = 0 ; r<directions.length ; r++){//transfering elements
    let moveQuantity =directions[r][0];
    let toAddArrayx = arrayxs[directions[r][1]-1].splice(0,moveQuantity);//spliced first ${x} elements
    while(toAdd = toAddArrayx.pop()){//added elements to target array one by one
        arrayxs[directions[r][2]-1].unshift(toAdd);
    }
}
let resultText1 = '';
for(let p=0 ; p<arrayxs.length ; p++){//adding top elements of each stack to a text
    resultText1 += arrayxs[p][0];
}
console.log('answer of part 2 : '+resultText1);//result (BNTZFPMMW)