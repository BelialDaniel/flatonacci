import pytest
from flatonacci import flatonacci

@pytest.mark.it("gets first 8 iterations from [1, 1, 1]")
def test_first():
    signature = [1, 1, 1]
    result = flatonacci(signature, 8)
    assert result == [1, 1 ,1, 3, 5, 9, 17, 31]

@pytest.mark.it("gets first 8 iterations from [0, 0, 1]")
def test_second():
    signature = [0, 0, 1]
    result = flatonacci(signature, 12)
    assert result == [0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149]
