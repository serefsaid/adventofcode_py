const fs = require('fs');
//var puzzleInput = fs.readFileSync('input.txt','utf8').split('\n').map(line => line.trim()).map(line =>line.split(' '));//fetching input from txt file
var puzzleInput = fs.readFileSync('input.txt','utf8').split(/[\n\s]+/);//fetching input from txt file
puzzleInput.unshift(null);//to set 0 index null
const findSum = (indexesForSum)=>{
    let xValue = 1;
    let result = 0;//sum of choosen indexes
    for(let i = 1;i<=Math.max(...indexesForSum);i++){
        if(indexesForSum.includes(i)){//to find sum of signal strengths
            result+=xValue*i;
        }
        
        if(Number.isInteger(parseInt(puzzleInput[i]))){//to find new xValue
            xValue += parseInt(puzzleInput[i]);
        }
    }
    return result;
}
console.log(findSum([20,60,100,140,180,220]));