function solution(s, n) {
    const alphabet = 'abcdefghijklmnopqrstuvwxyz';
    const upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    const s_array = s.split('');

    for (let i = 0; i < s_array.length; i++) {
        if (alphabet.includes(s_array[i])) {
            s_array.splice(i, 1, alphabet[(alphabet.indexOf(s_array[i]) + n) % alphabet.length]);
        } else if (upper_alphabet.includes(s_array[i])) {
            s_array.splice(i, 1, upper_alphabet[(upper_alphabet.indexOf(s_array[i]) + n) % upper_alphabet.length].toUpperCase());
        }
    }
    
    return s_array.join('');
}

solution('z A', 1);