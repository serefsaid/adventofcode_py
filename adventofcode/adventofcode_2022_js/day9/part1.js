const fs = require('fs');
var puzzleInput = fs.readFileSync('input.txt','utf8');//fetching input from txt file
puzzleInput = puzzleInput.split('\n');

let currentPosition = {head:[0,0],tail:[0,0]};//x,y

var tailPositions = [JSON.stringify({x:0,y:0})];

const justifyPositions = (input)=>{
    function onlyUnique(value, index, array) {
        return array.indexOf(value) === index;
    }
    
    var unique = input.filter(onlyUnique);
    return unique;
}

const pushPositions = (positions,rotation)=>{
    switch(rotation[0]){
        case 'U':for(let i = 0 ;i<rotation[1];i++){
            positions[1]--;
            tailPositions.push(JSON.stringify({x:positions[0],y:positions[1]}))
        };
        break;
        case 'D':for(let i = 0 ;i<rotation[1];i++){
            positions[1]++;
            tailPositions.push(JSON.stringify({x:positions[0],y:positions[1]}))
        };
        break;
        case 'L':for(let i = 0 ;i<rotation[1];i++){
            positions[0]--;
            tailPositions.push(JSON.stringify({x:positions[0],y:positions[1]}))
        };
        break;
        case 'R':for(let i = 0 ;i<rotation[1];i++){
            positions[0]++;
            tailPositions.push(JSON.stringify({x:positions[0],y:positions[1]}))
        };
        break;
    }
}
const detectSumPosition = (input)=>{
    input = input.map(function(line){return line.split(' ')});
    for (let i = 0 ; i<input.length;i++){
        input[i][1] = parseInt(input[i][1]);
        switch(input[i][0]){
            case 'U':currentPosition.head[1]-=input[i][1];break;
            case 'D':currentPosition.head[1]+=input[i][1];break;
            case 'L':currentPosition.head[0]-=input[i][1];break;
            case 'R':currentPosition.head[0]+=input[i][1];break;
        }
        console.log(currentPosition.tail,input[i]);
        if(!(currentPosition.head[0]==currentPosition.tail[0])&&!(currentPosition.head[1]==currentPosition.tail[1])){//check if not in same row or column
            pushPositions(currentPosition.tail,input[i]);
        }
        //let tail = JSON.stringify({x:currentPosition.tail[0],y:currentPosition.tail[1]});
        //tailPositions.push(tail);
    }
    return justifyPositions(tailPositions);
    //return positions;
}

console.log(detectSumPosition(puzzleInput));