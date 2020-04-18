let list = ["최지웅", "김효준", "허유나", "박민환"]
function findName(name){

    let index = list.indexOf(name);
    // let index = list.indexOf("김효준");
    return index
}
console.log(findName("김효준")+ "번째에 있습니다.");
console.log(findName("허유나")+ "번째에 있습니다.");
console.log(findName("박민환")+ "번째에 있습니다.");
console.log(findName("박민")+ "번째에 있습니다.");






