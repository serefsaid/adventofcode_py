const fs = require('fs');
const puzzleInput = fs.readFileSync('input.txt','utf8').split('\n').map(line=>line.trim());//fetching input from txt file

const checkVisible = (x,y)=>{
    let blockerTree = 0;//if there is a higher tree that makes it invisible increase this counter
    for(let i = x+1;i<puzzleInput[y].length;i++){//from right
        if(puzzleInput[y][i]>=puzzleInput[y][x]){
            blockerTree++;break;
        }
    }
    for(let i = 0;i<x;i++){//from left
        if(puzzleInput[y][i]>=puzzleInput[y][x]){
            blockerTree++;break;
        }
    }
    for(let i = 0;i<y;i++){//from top
        if(puzzleInput[i][x]>=puzzleInput[y][x]){
            blockerTree++;break;
        }
    }
    for(let i = y+1;i<puzzleInput.length;i++){//from bottom
        if(puzzleInput[i][x]>=puzzleInput[y][x]){
            blockerTree++;break;
        }
    }
    return blockerTree<4;//check if invisible angle is less than 4 (visible)
}

const findVisibleTrees = (input)=>{
    let visibleTrees = 0;
    for(let i = 0;i<input.length;i++){//loop for rows
        for (let j = 0;j<input[i].length;j++){//loop for columns
            if(checkVisible(j,i)){
                visibleTrees++;
            }
        }
    }
    return visibleTrees;
}

console.log(findVisibleTrees(puzzleInput));