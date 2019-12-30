let list = ["최지웅", "김효준", "허유나", "박민환"]
function findName(name){

    let index = list.indexOf(name);
    return index
}
console.log(findName("김효준"));
console.log(findName("허유나"));
console.log(findName("박민환"));
console.log(findName("박민"));