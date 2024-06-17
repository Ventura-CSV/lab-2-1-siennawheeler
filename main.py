def main():

    original_price = int(input('Enter the regular price: '))
    rate = int(input('Enter the discount rate: '))

    # regular = 100
    # rate = 20

    discount_amount = int(original_price * rate / 100)     # complete this statement to calcualte the discount amount
    final_price = int(original_price - discount_amount)         # complete this statement to calculate the final price

    print(f'Regular Price: {}'.format(original_price))
    print(f'Discount Amount: {}'.format(discount_amount))
    print(f'Final Price: {}'.format(final_price))

   ##################################################
   # Do not delete the return statement
   ##################################################
    return original_price, discount_amount, final_price


if __name__ == '__main__':
    main()
