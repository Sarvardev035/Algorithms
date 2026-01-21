/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    if (strs.length === 0) return "";

    let prefix = strs[0]; // birinchi so'z

    for (let i = 1; i < strs.length; i++) {
        while (strs[i].indexOf(prefix) !== 0) {
            prefix = prefix.slice(0, -1); // oxirgi harfni olib tashlaymiz
            if (prefix === "") return "";
        }
    }
    return prefix;
};