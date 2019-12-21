// 홀수만 출력하고 싶다면?
// 1,     2,           3,       4, 5,
//    continue;
//     실행안함
for (let i = 1; i < 10; i++) {
    if (i % 5 == 0){
        continue;     
    }else{
        console.log(i);
    }
    
}



let array = ["지웅","태호","유나","민환"]

// for (let index = 0; index < array.length; index++) {
//     console.log(array[index]);
    
// }

// for (const key in array) {
//     console.log(array[key]);
// }

// for (const iterator of array) {
//     console.log(iterator);
// }

array.forEach(function(element){
    element += " 멍청이";
    console.log(element);
    console.log(array);
});

array.forEach(element => {
    element += " 바보";
    console.log(element);
    console.log(array);
});