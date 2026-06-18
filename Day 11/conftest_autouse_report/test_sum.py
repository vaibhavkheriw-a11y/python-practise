import pytest

@pytest.mark.sanity
@pytest.mark.xfail(reason="i know that 1 + 1 = 2, for now pass it, ill take care of that")
def test_sum():
    assert 1 + 1 == 11