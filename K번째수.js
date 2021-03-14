const array = [1, 5, 2, 6, 3, 7, 4];
const commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]];

solution(array, commands);

function solution(array, commands) {
    let result = [];
    for (let i = 0; i < commands.length; i++) {
        const slicedArray = array.slice(commands[i][0] - 1, commands[i][1]);
        const sortedArray = slicedArray.sort((x, y) => { return x - y });
        const number = sortedArray[commands[i][2] - 1];
        result.push(number);
    }
    
    return result;
}