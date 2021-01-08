
function PhoneNumberChecker(phonenumber){
   if (phonenumber.substring(0,3)=="010" && phonenumber.length == 11){
        return "올바른 전화번호가 맞습니다."
   }
   else{
       return "올바른 전화번호가 아닙니다."
   }
}

console.log(PhoneNumberChecker("01078721234"))
console.log(PhoneNumberChecker("11111111111"))
console.log(PhoneNumberChecker("0123456789"))

function FoodfightRecord( foodList ){
    var record = 0;
    for ( var i = 0; i < foodlist.length; i++ ){
    record += i
}
    return record
}  
console.log(FoodfightRecord([ 5, 3, 2, 4, 1, 3 ]));
console.log(FoodfightRecord([ 3, 4, 6, 1, 2, 5 ]));
console.log(FoodfightRecord([ 9, 6, 5, 1, 1, 1 ]));