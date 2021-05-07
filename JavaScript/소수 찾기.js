function solution(n) {
    let array = [];
    const sqrt_n = parseInt(Math.sqrt(n));

    for (let i = 1; i <= n; i++) {
        array.push(i);
    }

    for (let i = 2; i <= sqrt_n; i++) {
        for (let j = i; j <= array.length; j+=i) {
            if (j !== i && array[j] % i === 0) {
                array.splice(j, 1);
            }
        }
    }

    array.shift();
console.log(array);
    return array.length;
}

solution(10);