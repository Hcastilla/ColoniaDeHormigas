let nodes = ["a", "b", "c", "d", "f", "g", "h", "k"]
let edges = []
function rand()
{
  return Math.floor(Math.random() * 7) + 0  
}
for (var i=0; i<100; i++){
    let a = nodes[rand()]
    let b = nodes[rand()]
    while(a == b)
    {
      b = nodes[rand()]
    }
  
    o = {
        "start":a,
        "end":b,
        "cost":rand() * rand() + 10
    }
    let s = false;
    for(var j = 0; j < edges.length -1; j++)
    {
      if(edges[j].start == a && edges[j].end == b){
        s = true
      }
    }
    if(!s){
      edges.push(o)
    }
}
console.log(JSON.stringify(edges))