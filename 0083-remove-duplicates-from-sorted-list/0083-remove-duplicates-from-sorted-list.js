var deleteDuplicates = function(head) {
    let current = head;

    while (current && current.next) {
        if (current.val === current.next.val) {
            // remove duplicate
            current.next = current.next.next;
        } else {
            // move forward
            current = current.next;
        }
    }

    return head;
};