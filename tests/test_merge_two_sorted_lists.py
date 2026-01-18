from problems.merge_two_sorted_lists import (
    list_to_listnode,
    listnode_to_list,
    merge_two_lists,
)


def test_examples():
    assert listnode_to_list(merge_two_lists(list_to_listnode([1, 2, 4]), list_to_listnode([1, 3, 4]))) == [1, 1, 2, 3, 4, 4]
    assert listnode_to_list(merge_two_lists(None, None)) == []
    assert listnode_to_list(merge_two_lists(None, list_to_listnode([0]))) == [0]
