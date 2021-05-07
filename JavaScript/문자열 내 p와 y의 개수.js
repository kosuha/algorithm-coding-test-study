solution("ooo");

function solution(s){
    let y = 0;
    let p = 0;
    
    if (s.match(/y/gi)) {
        y = s.match(/y/gi).length;
    }
    if (s.match(/p/gi)) {
        p = s.match(/p/gi).length;
    }

    return p === y;
}