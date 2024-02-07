const exp = require("constants");

function specialArray(nums) {
    function determine_if_special(n) {
        let cnt = 0
        for(let idx = 0; idx < nums.length; idx++) {
            if(n <= nums[idx]) {
                cnt++
            }
            // no point in continuing
            if(cnt > n) {
                return(-1)
            }
        }
        return cnt
    }

    for(let i = 0; i < nums.length; i++) {
        let candidate = i + 1;
        let count = determine_if_special(candidate)

        if(count == candidate) {
            return candidate
        }
    }
    return -1;
}

module.exports = specialArray;