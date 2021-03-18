solution(125);

function solution(n) {
    let ternary = [];
    let result = 0;
    let number = n;

    while (number >= 3) {
        ternary.unshift(number % 3);
        number = parseInt(number / 3);
    }

    ternary.unshift(number);

    for (let i = 0; i < ternary.length; i++) {
        result += ternary[i] * Math.pow(3, i);
    }

    return result;
}