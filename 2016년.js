// 2016년 1월 1일은 금요일
// 2016년 2월은 29일까지 있음.

solution(11, 17);

function solution(a, b) {
    const weekDays = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED'];
    const month = {
        1: 31,
        2: 29,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    let days = 0;

    if (a !== 1) {
        for (let i = 1; i <= a - 1; i++) {
            days += month[i];
        }
    }
    
    days += b;

    return weekDays[days % 7];
}