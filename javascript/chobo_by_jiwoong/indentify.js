// 조건문을 이용하여
// 나이를 입력하면
// 7세 이하면 유아입니다.
// 13세 이하면 초등학생입니다.
// 19세 이하면 청소년 입니다.
// 20 ~ 65세이면 어른입니다.
// 65세 이상이면 노인입니다.를 출력하는 프로그램을 만드세요.

let age = 32;
if(7 >= age){
    console.log("유아입니다.")
}else if(age <= 13){
    console.log("초등학생입니다.")
}else if(age <= 19){
    console.log("청소년입니다.")
}else if(age <= 65){
    console.log("어른입니다.")
}else{
    console.log("노인입니다.")
}