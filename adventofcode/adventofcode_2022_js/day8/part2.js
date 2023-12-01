const fs = require('fs');
const puzzleInput = fs.readFileSync('input.txt','utf8').split('\n').map(line=>line.trim());//fetching input from txt file

const findScenicScore = (x,y)=>{
    let scenicScore = 1;
    let visibleTrees = 0;
    let maxValue = -1;
    let itsHeight = puzzleInput[y][x];
    for(let i = x+1;i<puzzleInput[y].length;i++){//to right
        if(puzzleInput[y][i]<itsHeight){
            visibleTrees++;
            maxValue = puzzleInput[y][i];
        }else{
            visibleTrees++;
            break;
        }
    }
    scenicScore*=visibleTrees;
    visibleTrees = 0;
    maxValue = -1;
    for(let i = x-1;i>=0;i--){//to left
        if(puzzleInput[y][i]<itsHeight){
            visibleTrees++;
            maxValue = puzzleInput[y][i];
        }else{
            visibleTrees++;
            break;
        }
    }
    scenicScore*=visibleTrees;
    visibleTrees = 0;
    maxValue = -1;
    for(let i = y-1;i>=0;i--){//to top
        if(puzzleInput[i][x]<itsHeight){
            visibleTrees++;
            maxValue = puzzleInput[i][x];
        }else{
            visibleTrees++;
            break;
        }
    }
    scenicScore*=visibleTrees;
    visibleTrees = 0;
    maxValue = -1;
    for(let i = y+1;i<puzzleInput.length;i++){//to bottom
        if(puzzleInput[i][x]<itsHeight){
            visibleTrees++;
            maxValue = puzzleInput[i][x];
        }else{
            visibleTrees++;
            break;
        }
    }
    scenicScore*=visibleTrees;
    return scenicScore;
}

const findHighestScenicScore = (input)=>{
    let highestScenicScore = 0;
    for(let i = 0;i<input.length;i++){//loop for rows
        for (let j = 0;j<input[i].length;j++){//loop for columns
            let newScenicScore = findScenicScore(j,i);
            if(newScenicScore>highestScenicScore){
                highestScenicScore=newScenicScore;
            }
        }
    }
    return highestScenicScore;
}

console.log(findHighestScenicScore(puzzleInput));