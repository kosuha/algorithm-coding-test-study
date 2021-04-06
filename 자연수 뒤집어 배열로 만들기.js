function solution(n) {
    let answer = [];
    let str = n.toString();
    for (let i = 0; i < str.length; i++){
        answer.unshift(parseInt(str[i]));
    }
    return answer;
}