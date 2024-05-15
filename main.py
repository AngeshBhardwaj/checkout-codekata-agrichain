from src.checkout import Checkout


if __name__ == '__main__':
    # s = input()

    shopping_cart = Checkout()
    shopping_cart.scan('A')
    shopping_cart.scan('B')
    shopping_cart.scan('C')
    shopping_cart.scan('A')
    shopping_cart.scan('B')
    shopping_cart.scan('A')
    shopping_cart.scan('A')
    shopping_cart.scan('A')
    shopping_cart.scan('A')

    total_price = shopping_cart.price
    print(total_price)