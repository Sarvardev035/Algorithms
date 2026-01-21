/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(list1, list2) {
    let dummy = new ListNode(0); // soxta bosh
    let current = dummy;        // yurib boradigan pointer

    while (list1 !== null && list2 !== null) {
        if (list1.val < list2.val) {
            current.next = list1;      // kichigini ulaymiz
            list1 = list1.next;        // list1 ni oldinga siljitamiz
        } else {
            current.next = list2;      // list2 ni ulaymiz
            list2 = list2.next;        // list2 ni oldinga siljitamiz
        }
        current = current.next;        // current ham oldinga yuradi
    }

    // qaysi biri qolgan bo'lsa, to'liq ulab yuboramiz
    if (list1 !== null) {
        current.next = list1;
    } else {
        current.next = list2;
    }

    return dummy.next; // haqiqiy bosh
};
