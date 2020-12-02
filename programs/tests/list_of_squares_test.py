from programs import list_of_squares

def test_list_of_squares():
    d = {1:1, 2:4, 3:9, 4:16, 5:25}
    assert list_of_squares.list_of_squares(5) == d