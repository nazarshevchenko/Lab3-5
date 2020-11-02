

function fun1(){
    
    var toSort = document.querySelector('.content_data').children;
    let len = 0;

    toSort = Array.prototype.slice.call(toSort, 0);
    len = toSort.length

    var arr = []; 
    for(let i = 0; i < len; i++){
        let price = +toSort[i].children[1].textContent;
        arr.push([i, price]);
    }


    var sorted = []
    while (arr.length > 1){

        var min = 0;
        for(var i = 0; i < (arr.length); i++){
            if(arr[i][1] < arr[min][1]){
                min = i;
            }
        }
        sorted.push(arr[min]);
        arr.splice(min, 1);
    }
    sorted.push(arr[0]);
    console.log(sorted[0][0])
    console.log(toSort[2])

    var box2 = document.querySelector(".content_data");
    for(var i = 0; i < len; i++){
        box2.appendChild(toSort[sorted[i][0]]);
    }
}


function search(){
    console.log("Pressed")
}
