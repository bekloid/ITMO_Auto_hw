def test_f1 ():
    assert ('home', 'work') == ('home', 'work')


def test_f2():
    assert 'QA' != 'QC'

def test_f3():
    assert not (1, 1, 2, 3, 5) == (2, 3, 5)

