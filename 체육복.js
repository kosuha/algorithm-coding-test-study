const n = 5;
const lost = [2, 4];
const reserve = [1, 3, 5];

solution(n, lost, reserve);

function solution(n, lost, reserve) {
    let answer = 0;
    let students = {};

    for (let i = 1; i <= n; i++) {
        if (reserve.includes(i)) {
            students[i] = 2;
        } else {
            students[i] = 1;
        }

        if (lost.includes(i)) {
            students[i] -= 1;
        }
    }

    for (let i = 1; i <= n; i++) {
        if (i !== n) {
            if (students[i] === 0 && students[i + 1] === 2) {
                students[i] += 1;
                students[i + 1] -= 1;
            } else if (students[i] === 2 && students[i + 1] === 0) {
                students[i] -= 1;
                students[i + 1] += 1;
            }
        }

        if (students[i] > 0) {
            answer++;
        }
    }

    console.log(answer);
    return answer;
}