
var toSort = document.getElementById('content_data').children;
let len = 0;

toSort = Array.prototype.slice.call(toSort, 0);
len = toSort.length
console.log(len)

var arr = []; 
for(let i = 0; i < len; i++){
    let price = toSort[i].children[1];
    arr.push([i, price]);
    console.log(price);
}

console.log(arr);