// abcd -> bc
// abc -> b
// a -> a

// s : “abcde”
// return “c”
// s: “qwer”
// return “we”

// s : “abcde”
// return “c”
// s: “qwer”
// return “we”




function solution(s) {
    let answer = '';
    let middle = parseInt(s.length / 2);
    if(s.length === 0){
        answer = '';
    }
    if(s.length === 1){
        answer = s;
    }
    if(s.length % 2 === 0){
        answer = s.substring(middle-1,middle+1);

    }else{
        answer = s[middle];
    }
    return answer;
}

console.log(solution("a"));
console.log(solution("ab"));
console.log(solution("abc"));
console.log(solution("abcd"));
console.log(solution("abcde"));


