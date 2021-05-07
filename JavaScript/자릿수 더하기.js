function solution(n) {
    let answer = 0;
    let stringN = n.toString();
    for (let i = 0; i < stringN.length; i++) {
        answer += parseInt(stringN[i]);
    }
    console.log(answer);
}
solution(123);