let array = ["지웅","효준","유나","민환"];
//             0   ,  1   ,  2   ,   3
// console.log(array[2]);

console.log(array + " 바보");

for (let i = 0; i < array.length; i++) {
    console.log(array[i] + " 바보");
    console.log(array);
}

array.forEach(element => {
    element + " 멍청이";
});

array.forEach(function(element){
    element += " 멍청이";
    console.log(element);
});