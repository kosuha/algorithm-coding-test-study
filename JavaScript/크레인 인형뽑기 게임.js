const board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]];
const moves = [1,5,3,5,1,2,1,4];

solution(board, moves);

function solution(board, moves) {
    let result = 0;
    const n = board.length;
    let baguni = [];

    while (moves.length > 0) {
        let where = moves.shift() - 1;
        
        for (let i = 0; i < n; i++) {            
            if(board[i][where] !== 0) {
                let doll = board[i].splice(where, 1, 0)[0];
                if (doll === baguni[0]) {
                    baguni.shift();
                    result += 2;
                } else {
                    baguni.unshift(doll);
                }
                break;
            }
        }
    }

    return result;
}