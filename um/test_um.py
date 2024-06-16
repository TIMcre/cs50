from um import count


def test_simpel():
    assert count("um um um") == 3
    assert count("Um") == 1
    assert count(" Um, um?") == 2
    assert count("um?") == 1


def test_complex():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2
    assert count("Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?") == 2

