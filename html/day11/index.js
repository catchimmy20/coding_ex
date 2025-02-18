// alert("js파일 실행!")

/*
    [전역변수가 가진 특이사항]
    호이스팅 - 변수가 먼저 만들어지는 것
    변수가 만들어지는 코드가 아래에 있어도 위에서 변수가 만들어지는 기능
*/

// 변수를 어디서든 쓸 수 있으나 해당 변수가 올바른 값을 가지고 있는지
// 알 수 없음.
//console.log(b); // undefined 
var b = 3; // 값이 부여되는 건 이 시점이기 때문


// const = let + final(상수)
const c = 3; // 변화할 수 없는 값, 호이스팅 불가능
// = 5; // 오류 발생
// index.js:16 Uncaught TypeError: Assignment to constant variable.
//console.log(c);

/**
 * JS의 변수는 자료형이 없기에 자료형을 추측하면서 사용
 * JS 자료형
 *  - 원시 타입
 *      number: 정수 + 실수
 *      string: 
 *          한글자, 여러글자, 문자를 전부 관리
 *          '', "" - 문자열
 *          ``을 사용하면 특수문자 사용 가능
 *          => `${변수}`, `${계산식}`
 *      boolean
 * 
 *  - 오브젝트 타입
 *      array:
 *          배열, 여러 개의 값을 하나로 묶은 것
 *          JS에서는 자료형이 존재하지 않아 
 *          자료형과 상관없이 일렬로 묶어서 인덱싱으로 사용하는 구조
 *          ** 중간에 여러 개의 값을 한번에 [1, 2, 4, 5] 넣을 수 있음!
 *          (배열 - 동일한 자료형을 하나로 묶은 것)
 *          자바의 List<Object>와 비슷
 * 
 *      object: 
 *          객체형 -> 클래스와 다름
            Map<String, Object>와 비슷 키에 값을 대응하는 형태의 자료형
            특이사항
                기본 사용법은 변수명.key로 사용이 가능
                변수명['key']로 문자열 인덱싱도 지원

        function:
            함수형(메서드)
            JS에서는 메서드도 하나의 값이고 자료형임

        class(object)
            자바의 class와 동일
            변수 넣을 수 있고 함수 넣을 수 있다
            중요한점 - 원래 JS는 클래스가 생길 수 없는 구조
            애초부터 프로그래밍 문법의 고도화를 위하기보다 Script 언어로 브라우저에서 자유롭게 사용되기위해 만들어졌기 때문
            그래서 JS의 클래스는 object형의 변형 (그냥 클래스처럼 보이도록 한것) => type은 object로 나온다.
            class 생성 방법
                class 이름 {} - new 이름(); 


 *  - 특수 타입
 *      undefined: 
 *          변수를 처음 만들었을 때, 변수에 아무것도 넣은 적이 없을 때 빈 값을 나타냄
 *      null:
 *          비어있음을 뜻함.
 *          변수가 undefined가 아닌데 비어있을 경우
 *      NaN:
 *          잘못된 숫자를 의미
 *          숫자 연산이 불가능한 경우
 *      Infinity:
 *          무한대, 숫자 연산이 무한대일 경우
 */
// 자바에서 String은 클래스

const input = prompt("입력해봐");
console.log(input);
confirm("메시지"); // true, false 반환

let tmp1 = 'abcd';
let tmp2 = "abcd";
let tmp3 = `abcd ${tmp1} ${3 + 4}`;
let a = 4;
let a1 = true;
let a2 = null;
let b2 = [1, 2, 3, 4, "Hello", '4'];

// object
let d = {
    id:'cat',
    pw:1234
}
console.log(d.id)
console.log(d.pw)


console.log(tmp1);
console.log(tmp2);
console.log(tmp3);
console.log(a1);
console.log(null == undefined); // ?

console.log(b2[0]);
console.log(b2[1]);
console.log(b2[2]);
console.log(b2[4]);

// class 
class Person {
    #name; // 멤버 변수
    // 멤버 메서드 안에서 멤버 변수를 이용할때 this.을 "무조건" 붙여야한다
    // this는 클래스의 this와 다르게 자기 자신을 지칭하지 않고
    // 해당하는 공간을 소유한 객체를 지칭한다
    constructor(a){
        console.log(`생성자 ${a}`);
    }
    show(){
        console.log(this.#name);
    }
    setName(name){
        this.name = name;
    }
    getName(){
        return this.name;
    }
}

class Student extends Person {
    constructor(a){
        super(a);
        //super.show();
    }
}
const value = new Person();
value.name = "Hello!"
console.log(value);
value.show();

const int = 100.12345;
let arr = [1,2,3,4,5]
arr.filter();

