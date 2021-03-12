let participant = ["marina", "josipa", "nikola", "vinko", "filipa"];
let completion = ["josipa", "filipa", "marina", "nikola"];

solutionB(participant, completion);

// 효율성 실패
function solutionA(participant, completion) {
    for (let i = 0; i < completion.length; i++) {
        const indexOfName = participant.indexOf(completion[i]);
        participant.splice(indexOfName, 1);
    }
    return participant[0];
}

// 성공
function solutionB(participant, completion) {
    participant.sort();
    completion.sort();
    
    for (let i = 0; i < participant.length; i++) {
        if (completion[i] !== participant[i]) {
            return participant[i]
        }
    }
}