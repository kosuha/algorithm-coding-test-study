const new_id = "=.=";

solution(new_id);

function solution(new_id) {
    let user_id = new_id;
    user_id = user_id.toLowerCase();
    user_id = user_id.replace(/[^a-z0-9_.-]/g, "");
    user_id = user_id.replace(/\.+/g, ".");
    user_id = user_id.replace(/^\.|\.$/g, "");
    if (user_id === '') {
        user_id = 'a';
    }
    if (user_id.length >= 16) {
        user_id = user_id.replace(user_id.slice(15 - user_id.length), "");
        user_id = user_id.replace(/\.$/g, "");
    }
    while (user_id.length <= 2) {
        user_id = user_id + user_id[user_id.length - 1];
    }
    
    return user_id;
}