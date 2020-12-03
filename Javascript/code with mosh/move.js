const numbers = [1, 2, 3, 4];

const output = move(numbers, 0, 2);

console.log(output);

function move(array, index, offset) {
  const position = index + offset;
  if (position >= array.length) {
    console.errorr('Invalid offset');
    return;
  }

  const output = [...array]; // 인자로 받은 array 복사
  const element = output.splice(index, 1)[0]; // 지정된 arrray 삭제
  output.splice(position, 0, element);
  return output;
}