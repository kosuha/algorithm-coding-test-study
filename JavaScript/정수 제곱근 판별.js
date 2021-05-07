function solution(n) {
    if (Math.sqrt(n) === parseInt(Math.sqrt(n))) {
        return (Math.sqrt(n) + 1) * (Math.sqrt(n) + 1);
    } else {
        return -1;
    }
}

solution(3);