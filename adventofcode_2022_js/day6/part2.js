//day 6 part 2
const findProcessedChars=(input)=>{
    for(let i = 0; i<input.length;i++){
        let newFourteen = nextFourteen(input,i);//next fourteen character
        let uniqueArray = newFourteen.filter((value, index, array)=>{return array.indexOf(value) === index;});//remove repeating values
        if(uniqueArray.length==14){//if all 14 is unique
            return i+14;
        }
    }
}

const nextFourteen=(input,index)=>{
    let newArray = [];
    for (let i = index ; i<index+14;i++){
        newArray.push(input[i]);
    }
    return newArray;
}

const fs = require('fs');
var puzzleInput = fs.readFileSync('part1_input.txt','utf8');//fetching input from txt file
const characters = puzzleInput.split('');//seperating characters

console.log(findProcessedChars(characters));