import lines


def test_empty():
    assert lines.is_empty("\n") == True
    assert lines.is_empty("test") == False
    assert lines.is_empty("#test") == True
    assert lines.is_empty("     ") == True


def test_amount():
    assert lines.amount_lines(["test", "test", "", "\n", "#"]) == 2
