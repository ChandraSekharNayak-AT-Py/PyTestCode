#Any Pytest should start with test_ or _test.
#pytest function/method name should start with test

def test_assertion():
    msg = 'Hello'
    assert msg == 'Hi', "If msg is not equal it's showing error"


