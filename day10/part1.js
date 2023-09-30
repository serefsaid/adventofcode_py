const fs = require('fs');
//var puzzleInput = fs.readFileSync('input.txt','utf8').split('\n').map(line => line.trim()).map(line =>line.split(' '));//fetching input from txt file
var puzzleInput = fs.readFileSync('input.txt','utf8').split(/[\n\s]+/);//fetching input from txt file
const findSum = (indexesForSum)=>{
    let xValue = 1;
    let result = 0;//sum of choosen indexes
    for(let i = 0;i<=Math.max(...indexesForSum);i++){
        let index = i;
        if(i>=puzzleInput.length){//to reset index
            index=i-puzzleInput.length;
        }

        //console.log(parseInt(puzzleInput[index]));
        if(Number.isInteger(parseInt(puzzleInput[index]))){
            xValue += parseInt(parseInt(puzzleInput[index]));
        }
        if(indexesForSum.includes(i)){
            result+=xValue*i;
            console.log(result,xValue*i,xValue,i);
        }
    }
    return result;
}

console.log(findSum([20,60,100,140,180,220]));