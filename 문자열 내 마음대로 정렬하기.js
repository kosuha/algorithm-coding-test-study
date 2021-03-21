function solution(strings, n) {
    let answer = strings.sort().sort((a, b) => {
        if (a[n] < b[n]) {
            return -1;
        }
        if (a[n] > b[n]) {
            return 1;
        }
        return 0;
    });
    return answer;
}