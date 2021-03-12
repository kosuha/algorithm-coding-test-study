let numbersExample = {
    a: [2,1,3,4,1],
    b: [5,0,2,7]
}

console.log(solution(numbersExample.a));

function solution(numbers) {
    let answer = [];
    while (numbers.length > 1) {
        const x = numbers.shift();
        for (let i = 0; i < numbers.length; i++) {
            const y = numbers[i];
            if (!answer.includes(x + y)) {
                answer.push(x + y);
            }
        }
    }
    answer.sort((a, b) => a - b);
    return answer;
}