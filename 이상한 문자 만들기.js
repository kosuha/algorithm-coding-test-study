solution("try hello world");

function solution(s) {
    let answer = '';
    const splited = s.split(" ");
    
    for (let i = 0; i < splited.length; i++) {
        if (i !== 0) {
            answer += ' ';
        }
        const splitedChar = splited[i].split('');
        for (let j = 0; j < splitedChar.length; j++) {
            if (j % 2 === 0) {
                answer += splitedChar[j].toUpperCase();
            } else {
                answer += splitedChar[j].toLowerCase();
            }
        }
        
    }
    console.log(answer);
    return answer;
}