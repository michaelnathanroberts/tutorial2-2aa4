'''MVP Plan
1. Get environment set up
- one by one  instead of many items
- one provinces instead of many (ON here)
- calculate tax + 5% discount for ON item
- 13% sales tax
'''

DISCOUNT = 0.05
TAX = 0.13

def main():
    item_price = float(input("Enter the item's price: "))
    final_price = item_price * (1 - DISCOUNT) * (1 + TAX)
    print("The final price is ${:.2f}".format(final_price))

main()