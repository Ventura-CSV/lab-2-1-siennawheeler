def main():

    regular = int(input('Enter the regular price: '))
    rate = int(input('Enter the discount rate: '))

    # regular = 100
    # rate = 20

    discount = regular * rate // 100
    final = regular - discount
    print(f'Regular Price: {regular}')
    print(f'Discount Amount: {discount}')
    print(f'Final Price: {final}')


if __name__ == '__main__':
    main()
