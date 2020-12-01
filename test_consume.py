from mock import patch, MagicMock
import acm


@patch(acm.__name__ + ".func1", MagicMock(return_value="from_yy"))
def test_acm_func():
    assert "from_yy" == acm.func1()


@patch("python_patch_poc.acm.var1", "mock_attr_value")
def test_acm_var():

    assert "mock_attr_value" == acm.var1


@patch("python_patch_poc.acm.var1", 3)
def test_acm_add():

    assert 8 == acm.add(5)


def test_acm_add2():

    assert 15 == acm.add(5)
