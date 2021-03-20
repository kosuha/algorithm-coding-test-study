function solution(a, b) {
    let answer = 0;

    for (let i = 0; i <= Math.abs(a - b); i++) {
        if (a - b < 0) {
            answer += a + i;
        } else if (a - b > 0) {
            answer += a - i;
        } else {
            answer = a;
        }
    }

    return answer;
}