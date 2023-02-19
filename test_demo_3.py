#Any Pytest should start with test_ or _test.
#pytest function/method name should start with test
#-v :- more info about meta data
#-s :- login output
#pytest select also single file with help of file name py.test <fie name> -v -s
#Method name should have sence
#-k :- name extension for string pattern
# py.test -k secondprogram -v -s
#-m :- marker :-  py.test -m smoke -v -s


import pytest



def test_secondprogram_1():
    a = 10
    b = 20
    c = a+b
    return c

@pytest.mark.xfail
def test_secondprogram_2():
    d = 60
    assert test_secondprogram_1.c > d

