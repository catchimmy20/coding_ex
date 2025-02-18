// 숫자 세개 입력 후 가장 큰 수 출력
let a = Number(prompt("첫번째 수 입력"));
let b = Number(prompt("두번째 수 입력"));
let c = Number(prompt("세번째 수 입력"));
let arr = [a, b, c]

console.log(Math.max(...arr))