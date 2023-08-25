# importing testing framework
import pytest
# importing the file(s) to test
import config
from DISClib.DataStructures.listnode import single_node
from DISClib.DataStructures.listnode import double_node
from DISClib.DataStructures.listnode import get_element
# asserting module imports
assert config
assert single_node
assert double_node
assert get_element

# global variables for testing
TEST_STR = "Hello Node!"
TEST_INT = 42
TEST_FLOAT = 42.0
TEST_BOOL = True
TEST_DICT = {
    "key1": "Hello Node!",
    "key2": 42,
    "key3": 42.0,
    "key4": [
        "value1",
        "value2",
        "value3",
        ],
    "key5": {
        "key1": "value1",
        "key2": "value2",
        "key3": "value3",
        },
    "key6": None,
    "key7": True,
    }
TEST_LT = [
    "value1",
    "value2",
    "value3",
    42,
    42.7,
    "Hello Node!",
    None,
    True,
    ]


def test_sll_node():
    """test_sll_node _summary_
    """
    # create a single linked list node
    node = single_node(TEST_STR)
    # assert that the node data is not None
    assert node.info == TEST_STR
    # assert that the node next_node is None or a single_node
    assert node.next_node is None or isinstance(node.next_node, single_node)


def test_dll_node():
    """test_dll_node _summary_
    """
    # create a double linked list node
    node = double_node(TEST_STR)
    # assert that the node data is not None
    assert node.info == TEST_STR
    # assert that the node next_node is None or a double_node
    assert node.next_node is None or isinstance(node.next_node, double_node)
    # assert that the node prev_node is None or a double_node
    assert node.prev_node is None or isinstance(node.prev_node, double_node)


def test_get_element():
    """test_get_element _summary_
    """
    # create a single linked list node
    node = single_node(TEST_STR)
    # get the node data with class function
    data = node.get_element()
    # assert that the node data is not None
    assert data == TEST_STR
    # assert that the data can be retrieved with the get_element function
    assert get_element(node) == TEST_STR
    # create a double linked list node
    node = double_node(TEST_STR)
    # get the node data with class function
    data = node.get_element()
    # assert that the node data is not None
    assert data == TEST_STR
    # assert that the data can be retrieved with the get_element function
    assert get_element(node) == TEST_STR


def test_sll_node_type():
    """test_sll_node_type _summary_
    """
    # TESTING WITH INT
    # create a single linked list node
    node = single_node(TEST_INT)
    # assert that the node is a single_node
    assert isinstance(node, single_node)
    # assert that the node info is an int
    assert isinstance(node.info, int)
    # assert the node next_node reference is None
    assert node.next_node is None or isinstance(node.next_node, single_node)

    # TESTING WITH FLOAT
    # create a single_node with float info
    node = single_node(TEST_FLOAT)
    # assert that the node info is a float
    assert isinstance(node.info, float)

    # TESTING WOTH BOOL
    # create a single_node with bool info
    node = single_node(TEST_BOOL)
    # assert that the node info is a bool
    assert isinstance(node.info, bool)

    # TESTING WITH STRING
    # create a single_node with string info
    node = single_node(TEST_STR)
    # assert that the node info is a string
    assert isinstance(node.info, str)

    # TESTING WITH DICT
    # create a single_node with dict info
    node = single_node(TEST_DICT)
    # assert that the node is a single_node
    assert isinstance(node, single_node)
    # assert that the node info is a dict
    assert isinstance(node.info, dict)
    # assert that the node info keys are the same as the dict keys
    for key in TEST_DICT.keys():
        assert key in node.info.keys()
        assert isinstance(node.info[key], type(TEST_DICT[key]))
    # assert the node next_node reference is None
    assert node.next_node is None or isinstance(node.next_node, single_node)

    # TESTING WITH LIST
    # create a single_node with list info
    node = single_node(TEST_LT)
    # assert that the node info is a list
    assert isinstance(node.info, list)
    # assert that the node info keys are the same as the list keys
    for i in range(len(TEST_LT)):
        assert node.info[i] == TEST_LT[i]


def test_dll_node_type():
    """test_dll_node_type _summary_
    """

    # TESTING WITH INT
    # create a single linked list node
    node = double_node(TEST_INT)
    # assert that the node is a double_node
    assert isinstance(node, double_node)
    # assert that the node info is an int
    assert isinstance(node.info, int)
    # assert the node next_node reference is None
    assert node.next_node is None or isinstance(node.next_node, double_node)
    assert node.prev_node is None or isinstance(node.prev_node, double_node)

    # TESTING WITH FLOAT
    # create a double_node with float info
    node = double_node(TEST_FLOAT)
    # assert that the node info is a float
    assert isinstance(node.info, float)

    # TESTING WOTH BOOL
    # create a double_node with bool info
    node = double_node(TEST_BOOL)
    # assert that the node info is a bool
    assert isinstance(node.info, bool)

    # TESTING WITH STRING
    # create a double_node with string info
    node = double_node(TEST_STR)
    # assert that the node info is a string
    assert isinstance(node.info, str)

    # TESTING WITH DICT
    # create a double_node with dict info
    node = double_node(TEST_DICT)
    # assert that the node is a double_node
    assert isinstance(node, double_node)
    # assert that the node info is a dict
    assert isinstance(node.info, dict)
    # assert that the node info keys are the same as the dict keys
    for key in TEST_DICT.keys():
        assert key in node.info.keys()
        assert isinstance(node.info[key], type(TEST_DICT[key]))
    # assert the node next_node reference is None
    assert node.next_node is None or isinstance(node.next_node, double_node)
    assert node.prev_node is None or isinstance(node.prev_node, double_node)

    # TESTING WITH LIST
    # create a double_node with list info
    node = double_node(TEST_LT)
    # assert that the node info is a list
    assert isinstance(node.info, list)
    # assert that the node info keys are the same as the list keys
    for i in range(len(TEST_LT)):
        assert node.info[i] == TEST_LT[i]


def test_sll_node_ref():
    """test_sll_node_ref _summary_
    """
    # create two different single linked list nodes
    node_a = single_node(TEST_STR)
    node_b = single_node("Hello Next Node!")
    # assigning node_a next_node reference to node_b
    node_a.next_node = node_b
    # assert that node_a next_node reference is node_b
    assert node_a.next_node == node_b
    # assert that node_b next_node reference is None or a single_node
    assert node_b.next_node is None or isinstance(node_b.next_node, single_node)


def test_dll_node_ref():
    """test_dll_node_ref _summary_
    """
    # create three different double linked list nodes
    node_a = double_node(TEST_STR)
    node_b = double_node("Hello Next Node!")
    node_c = double_node("Hello Prev Node!")

    # assigning node_a next_node reference to node_b
    node_a.next_node = node_b
    # assigning node_b prev_node reference to node_c
    node_a.prev_node = node_c
    # assert that node_a next_node reference is node_b
    assert node_a.next_node == node_b
    # assert that node_b prev_node reference is node_c
    assert node_a.prev_node == node_c
    # assert that node_b next_node reference is None or a double_node
    assert node_a.next_node is None or node_a.next_node == node_b
    # assert that node_c prev_node reference is None or a double_node
    assert node_a.prev_node is None or node_a.prev_node == node_c


def test_sll_node_typerr():
    """test_sll_node_err _summary_
    """
    # type error test data list
    type_err_lt = [
        TEST_INT,
        TEST_FLOAT,
        TEST_BOOL,
        TEST_DICT,
        TEST_LT,
        ]

    for type_var in type_err_lt:
        # create a single linked list node with type error data
        with pytest.raises(TypeError) as err_info:
            node = single_node(type_var)
            assert node is not None
        # assert if the type error is raised
        assert isinstance(err_info.value, TypeError)
        assert err_info.match("Invalid data type for node info")


if __name__ == "__main__":
    pytest.main(["-v", "-s", "test_struct_listnode.py"])
