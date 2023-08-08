"""
write test cases for calc_cli.py

"""
def test_add_cli():
    from subprocess import check_output
    assert check_output(['python', 'cal_cli.py', 'add', '1', '2']) == b'3\n'
    
def test_sub_cli():
    from subprocess import check_output
    assert check_output(['python', 'cal_cli.py', 'sub', '4', '2']) == b'2\n'
    
def test_mul_cli():
    from subprocess import check_output
    assert check_output(['python', 'cal_cli.py', 'mul', '2', '3']) == b'6\n'

def test_div_cli():
    from subprocess import check_output
    assert check_output(['python', 'cal_cli.py', 'div', '6', '3']) == b'2.0\n'

def test_sqrt_cli():
    from subprocess import check_output
    assert check_output(['python', 'cal_cli.py', 'sqrt', '4']) == b'2.0\n'