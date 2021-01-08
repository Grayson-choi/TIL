function is_palindrome(str){
    let len = str.length;
        for (let i = 0; i < len/2; i++) {
            if (str[i] !== str[len - 1 - i]) {
                return false;
            }
        }
    return true;
}

console.log(is_palindrome("토마토"));
console.log(is_palindrome("기러기"));
console.log(is_palindrome("hello"));
console.log(is_palindrome("ㅁㅁㅁㅁ"));
console.log(is_palindrome("kayak"));
console.log(is_palindrome("최지웅"));