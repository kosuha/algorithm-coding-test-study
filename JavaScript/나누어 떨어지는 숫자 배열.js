solution([5, 9, 7, 10], 5);

function solution(arr, divisor) {
    let answer = [];
    
    for (let i = 0; i < arr.length; i++) {
        if(arr[i] % divisor === 0) {
            answer.push(arr[i]);
        }
    }

    answer.sort((a, b) => a - b);

    if (answer.length === 0) {
        answer.push(-1);
    }

    return answer;
}