// 2. 인생은 리액션이 중요합니다. 숫자를 입력받으면 박수를 치는 함수를 작성하세요.
// 예:
// n = 1 -> "박"
// n = 2 -> "박수" 
// n = 3 -> "박수박"
// n = 4 -> "박수박수"
// n = 5 -> "박수박수박"
// n = 6 -> "박수박수박수"
// i = 0 -> i % 2 === 0 이니까 "박"
// i = 1 -> i % 2 !== 0 이니까 "수"

function solution(n){
    let result = '';
    for(let i = 0; i < n; i++){
        if(i % 2 === 0){
            result += '박'
        }else{
            result += '수'
        }
    }
    return result
}

function solution2(n){
    let result = "박수";
    result = result.repeat(n).substring(0,n);
    return result
}


console.log(solution(10));
console.log(solution(8));
console.log(solution(1));

console.log(solution2(10));
console.log(solution2(8));
console.log(solution2(1));
