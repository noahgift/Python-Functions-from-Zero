from hello import with_input


def test_with_input():
    result = with_input("blue")
    assert result["old"] == "blue"
