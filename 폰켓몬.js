function solution(nums) {
    let choose = [];
    for (let i = 0; i < nums.length; i++) {
        if (!choose.includes(nums[i])) {
            choose.push(nums[i]);
        }
        if (choose.length === nums.length/2) {
            return choose.length;
        }
    }
    return choose.length;
}