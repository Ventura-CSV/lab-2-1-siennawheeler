import main
import io
import sys
import re


def test_main_100_20():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '100 \n 20'
    sys.stdin = io.StringIO(datastr)

    main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)
    # p = re.compile('[\w,\W]*100[\w,\W]*')
    # res = p.match(lines[0])
    # print(res.group())
    res = re.search('100', lines[0])
    assert res != None
    print(res.group())
    assert res.group() == '100', 'Expected 100'

    res = re.search('20', lines[1])
    assert res != None
    print(res.group())
    assert res.group() == '20', 'Expected 20'

    res = re.search('80', lines[2])
    assert res != None, 'The final price error'
    print(res.group())
    assert res.group() == '80', 'Expected 80'


def test_main_200_40():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '200 \n 20'
    sys.stdin = io.StringIO(datastr)

    main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)
    # p = re.compile('[\w,\W]*100[\w,\W]*')
    # res = p.match(lines[0])
    # print(res.group())
    res = re.search('200', lines[0])
    assert res != None
    print(res.group())
    assert res.group() == '200', 'Expected 200'

    res = re.search('40', lines[1])
    assert res != None
    print(res.group())
    assert res.group() == '40', 'Expected 40'

    res = re.search('160', lines[2])
    assert res != None, 'The final price error'
    print(res.group())
    assert res.group() == '160', 'Expected 160'
