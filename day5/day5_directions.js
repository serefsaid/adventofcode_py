let txt= document.getElementById('p').innerHTML;
let directions = txt.split('\n');
directions = directions.map(function(x){return x.split(' ');});//converted every direction line to arrays
directions = directions.map(function(x){
    x.splice(0,1);
    x.splice(1,1);
    x.splice(2,1);
    return x;
});//removed move,to and from texts
directions = directions.map(function(x){return x.map(function(y){return parseInt(y)});});//parsed text elements to integer