const answer = fizzbuzz(7);
console.log(answer);

function fizzbuzz(num) {
  let output;
  if (typeof num !== 'number'){
    return NaN
  }

  if ((num % 3 === 0) && (num % 5 === 0)){
   output = "FizzBuzz"; 
  }else if(num % 5 === 0){
    output = "Buzz"
  }else if (num % 3 === 0){
    output = "Fizz"
  }else{
    output = num;
  }
  return output;

}