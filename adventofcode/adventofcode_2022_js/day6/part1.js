//day 6 part 1
const findProcessedChars=(input)=>{
    for(let i = 0; i<input.length;i++){
        let newFour = [input[i],input[i+1],input[i+2],input[i+3]];//next four character
        let uniqueArray = newFour.filter((value, index, array)=>{return array.indexOf(value) === index;});//remove repeating values
        if(uniqueArray.length==4){//if all 4 is unique
            return i+4;
        }
    }
}

const fs = require('fs');
var puzzleInput = fs.readFileSync('part1_input.txt','utf8');//fetching input from txt file
const characters = puzzleInput.split('');//seperating characters

console.log(findProcessedChars(characters));