const stages = [2, 1, 6, 2, 2, 4, 3, 3];
const N = 5;

function solution(N, stages) {
    let array = [];
    for (let i = 1; i <= N; i++) {
        let clear = 0;
        let failed = 0;
        let failRatio = 0;

        for (let j = 0; j < stages.length; j++) {
            if (stages[j] > i) {
                clear++;
            } else if (stages[j] === i) {
                failed++;
            }
        }

        if (clear + failed !== 0) {
            failRatio = failed / (clear + failed);
        }
        
        array.push({stage: i, failRatio: failRatio});
    }
    
    array.sort((a, b) => {
        return b.failRatio - a.failRatio;
    });

    let answer = [];
    for (let i = 0; i < array.length; i++) {
        answer.push(array[i].stage);
    }

    return answer;
}

solution(N, stages);