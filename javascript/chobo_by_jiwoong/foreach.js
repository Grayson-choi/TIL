let array = ["지웅","태호","민환","효준"]
let word = "안녕하세요"
array.forEach(function(element){
    element += " 멍청이";
    console.log(element);
});

array.forEach(element => {
    element += " 바보";
    console.log(element);
});



