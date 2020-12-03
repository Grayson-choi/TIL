const readPermission = 4;
const writePermission = 2;
const excutePermission = 1;

let myPermission = 0
myPermission = myPermission | readPermission | writePermission

console.log(myPermission); // 실행 결과는 6

let message = (myPermission & readPermission) ? 'Yes': 'no';

console.log(message);
