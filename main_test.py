import random
import main


def test_init():
    ca = main.Names('ca2021.txt')

    lenofdict = len(ca._nlist)
    assert lenofdict == 200, "Invalid value. Expected 200"

    cnt = len([d for d in ca.nlist if d['Gender'] == 'F'])
    assert cnt == 100, "Invalid value. Expected 100"
    cnt = len([d for d in ca.nlist if d['Gender'] == 'M'])
    assert cnt == 100, "Invalid value. Expected 100"

    mydict = [{'Name': 'Alexander', 'Count': 1483, 'Gender': 'M'}, {'Name': 'Amelia',
                                                                    'Count': 1363, 'Gender': 'F'}, {'Name': 'Ava', 'Count': 1264, 'Gender': 'F'}]
    ca._nlist = mydict
    assert len(ca._nlist) == 3, "Expected 3"


def test_str():
    ca = main.Names('ca2021.txt')
    print(ca)
    assert ca.__str__ != None


def test_gt():
    ca = main.Names('ca2021.txt')
    fl = main.Names('fl2021.txt')
    result = ca > fl
    assert result == True, 'Expected True'

    mydict1 = [{'Name': 'Alexander', 'Count': 1483, 'Gender': 'M'}, {'Name': 'Amelia',
                                                                     'Count': 1363, 'Gender': 'F'}, {'Name': 'Ava', 'Count': 1264, 'Gender': 'F'}]
    ca.nlist = mydict1
    mydict2 = [{'Name': 'Oliver', 'Count': 1523, 'Gender': 'M'}, {'Name': 'Luna', 'Count': 1458, 'Gender': 'F'}, {
        'Name': 'Elijah', 'Count': 1498, 'Gender': 'M'}, {'Name': 'Amelia', 'Count': 1363, 'Gender': 'F'}]
    fl.nlist = mydict2
    result = ca > fl
    assert result == False, 'Expected False'


def test_printName():
    ca = main.Names('ca2021.txt')
    ret = ca.printName('C', 'Count', True)
    assert ret == 10, 'Expected 10'
    ret = ca.printName('E', 'Gender', False)
    assert ret == 23, 'Expected 23'
    mydict1 = [{'Name': 'Alexander', 'Count': 1483, 'Gender': 'M'}, {'Name': 'Amelia',
                                                                     'Count': 1363, 'Gender': 'F'}, {'Name': 'Ava', 'Count': 1264, 'Gender': 'F'}]
    ca.nlist = mydict1
    ret = ca.printName('A', 'Count', True)
    assert ret == 3, 'Expected 3'
