# snake_tests.py
from snake_view import get_color
from snake_main import get_next_head_position, subtract_one_from_all_positives, add_apple_at_random_location, is_legal_move

def run_all():
    ''' Run all tests for the snake program '''
    # As you add more test functions to this file, call them here
    test_get_color()
    test_add_apple_at_random_location() 
    test_get_next_head_position() 
    test_is_legal_move() 
    test_subtract_one_from_all_positives()

def test_get_color():
    print('Tester get_color...', end='')
    assert '#d82159' == get_color(-1)
    assert 'white' == get_color(0)
    assert '#ee7192' == get_color(1)
    assert '#ee7192' == get_color(42)
    print('OK')
    
def test_get_next_head_position():
    print('Tester get_next_head_position...', end='')
    assert (3, 9) == get_next_head_position((3, 8), 'east')
    assert (3, 7) == get_next_head_position((3, 8), 'west')
    assert (2, 8) == get_next_head_position((3, 8), 'north')
    assert (4, 8) == get_next_head_position((3, 8), 'south')
    assert (1, 6) == get_next_head_position((1, 5), 'east')
    assert (1, 4) == get_next_head_position((1, 5), 'west')
    assert (0, 5) == get_next_head_position((1, 5), 'north')
    assert (2, 5) == get_next_head_position((1, 5), 'south')
    print('OK')
    
def test_subtract_one_from_all_positives():
    print('Tester subtract_one_from_all_positives...', end='')
    a = [[2, 3, 0], [1, -1, 2]]
    subtract_one_from_all_positives(a)
    assert [[1, 2, 0], [0, -1, 1]] == a

    b = [[2, 0], [0, -1]]
    subtract_one_from_all_positives(b)
    assert [[1, 0], [0, -1]] == b
    print('OK')
    
def test_add_apple_at_random_location():
    print('Tester add_apple_at_random_location...', end='')
    NUMBER_OF_RUNS = 1000
    legal_states = [
        [[2, 3, -1, -1], [1, 0, 0, 0]],
        [[2, 3, -1, 0], [1, -1, 0, 0]],
        [[2, 3, -1, 0], [1, 0, -1, 0]],
        [[2, 3, -1, 0], [1, 0, 0, -1]],
    ]
    counters = [0] * len(legal_states)
    for _ in range(NUMBER_OF_RUNS):
        a = [[2, 3, -1, 0], [1, 0, 0, 0]]
        add_apple_at_random_location(a)
        assert a in legal_states
    print('OK')
    
def test_is_legal_move():
    print('Tester is_legal_move...', end='')
    board = [
        [0, 3, 4],
        [0, 2, 5],
        [0, 1, 0],
        [-1, 0, 0],
    ]
    assert is_legal_move((2, 2), board) is True
    assert is_legal_move((1, 3), board) is False # Utenfor brettet
    assert is_legal_move((1, 1), board) is False # Krasjer med seg selv
    assert is_legal_move((0, 2), board) is False # Krasjer med seg selv

    assert is_legal_move((0, 0), board) is True
    assert is_legal_move((3, 0), board) is True # Eplets posisjon er lovlig
    assert is_legal_move((3, 2), board) is True
    assert is_legal_move((-1, 0), board) is False # Utenfor brettet
    assert is_legal_move((0, -1), board) is False # Utenfor brettet
    assert is_legal_move((3, -1), board) is False # Utenfor brettet
    assert is_legal_move((3, 3), board) is False # Utenfor brettet
    assert is_legal_move((4, 2), board) is False # Utenfor brettet
    print('OK')
    
if __name__ == '__main__':
    print('Starting snake_test.py')
    run_all()
    print('Finished snake_test.py')