/**
 * @param {number[]} arr
 * @return {number[][]}
 */
var minimumAbsDifference = function(arr) {
    // 1. Sort the array
    arr.sort((a, b) => a - b);

    // 2. Find the minimum difference
    let minDiff = Infinity;
    for (let i = 0; i < arr.length - 1; i++) {
        let diff = arr[i + 1] - arr[i];
        if (diff < minDiff) {
            minDiff = diff;
        }
    }

    // 3. Collect all pairs with that minimum difference
    let result = [];
    for (let i = 0; i < arr.length - 1; i++) {
        let diff = arr[i + 1] - arr[i];
        if (diff === minDiff) {
            result.push([arr[i], arr[i + 1]]);
        }
    }

    return result;
};
