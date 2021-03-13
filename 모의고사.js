const answers = [1,2,3,4,5,1,2,3,4,5];

studentAnswerPatterns = {
    1: [1, 2, 3, 4, 5],
    2: [2, 1, 2, 3, 2, 4, 2, 5],
    3: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
}

solution(answers);

function solution(answers) {
    let result = [];
    let studentAnswers = {};
    let studentLength = Object.keys(studentAnswerPatterns).length;
    let scores = [];

    for (let i = 0; i < studentLength; i++) {
        studentAnswers[i + 1] = studentAnswer(answers.length, studentAnswerPatterns[i + 1]);
        const score = checkAnswer(answers, studentAnswers[i + 1]);
        scores.push(score);
    }

    const scoreMax = Math.max.apply(null, scores);

    while (scores.indexOf(scoreMax) !== -1) {
        result.push(scores.indexOf(scoreMax) + 1);
        scores.splice(scores.indexOf(scoreMax), 1, -1);
    }

    return result;
}

function studentAnswer(answersLength, pattern) {
    let result = [];

    for (let i = 0; i < answersLength; i++) {
        const remainder = (i + 1) % pattern.length;
        if (remainder === 0) {
            result.push(pattern[pattern.length - 1]);
        } else {
            result.push(pattern[remainder - 1]);
        }
    }

    return result;
}

function checkAnswer(answers, studentAnswer) {
    let result = 0;

    for (let i = 0; i < answers.length; i++) {
        if (answers[i] === studentAnswer[i]) {
            result++;
        }
    }

    return result;
}