#Any Pytest should start with test_ or _test.
#pytest function/method name should start with test
#-v :- more info about meta data
#-s :- login output
#pytest select also single file with help of file name py.test <fie name> -v -s
#Method name should have sence
#-k :- name extension for string pattern
# py.test -k secondprogram -v -s

def test_firstprogram():
    print('Hi')

def test_secondprogram():
    print('Good Morning')