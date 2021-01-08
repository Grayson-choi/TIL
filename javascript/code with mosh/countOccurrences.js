const numbers = [1, 2, 3, 4, 5, 6, 1];

const count = countOccurrences(numbers, 1);

console.log(count);

// function countOccurrences(array, findElement) {
//   let count = 0
//   for (let element of array)
//     if (element === findElement){
//       count++;
//     }
//   return count
// }


// function countOccurrences(array, searchElement){
//   return array.reduce((accumulator, current) => {
//     const occurrence = (current === searchElement) ? 1 : 0;
//     return accumulator + occurrence
//   }, 0);
// }

function countOccurrences(array, searchElement){
  return array.reduce((accumulator, current) => {
  const occurrence = (accumulator === searchElement) ? 1 : 0;
  return accumulator + occurrence;  
}, 0);
  
}