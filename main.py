class Names:
    #################
    # Implement the class Names
    pass


def main():
    # Test code for your class
    ca = Names('ca2021.txt')
    print(ca)
    fl = Names('fl2021.txt')
    print(fl)
    print(ca.nlist)
    print(fl.nlist)

    if ca > fl:
        print('The name class ca is greater than fl')
    else:
        print('The name class fl is greater than or equal to ca')

    ca.printName('C', 'Count', True)
    ca.printName('D', 'Name', False)
    fl.printName('A', 'Count', True)
    fl.printName('E', 'Name', False)


if __name__ == '__main__':
    main()
