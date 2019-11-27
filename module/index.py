'''
Marginal utility of a product for each quantity
'''
import click
from matplotlib import pyplot as plt

def utility_finder(quantity, product_name):
    '''
    Get all values from CLI
    '''
    while True:
        try:
            utility = int(input('For {} {} what added happiness do you get ?\n'
                                .format(quantity, product_name)))
        except ValueError:
            print("Error, enter a number please.\n")
            continue
        else:
            break
    return utility

def set_utility(maximum_quantity, product_name):
    '''
    Set utility in function of the product's quantity
    '''
    i = 1
    utility = []
    while i <= maximum_quantity:
        utility.append(utility_finder(i, product_name))
        i = i + 1
    return utility

def quantity_finder():
    '''
    Determining the maximal quantity
    '''
    while True:
        try:
            maximum_quantity = int(input('Please enter the maximum quantity :\n'))
            if maximum_quantity <= 0:
                print("Error, the maximum value can't be equal or inferior to zero.\n")
                continue
        except ValueError:
            print("Error, enter a number please.\n")
            continue
        else:
            break
    return maximum_quantity

@click.command()
def create_graph():
    '''
    Program which outputs a graph that plots the product's utility in function of the quantity.
    '''
    product_name = input('Please enter a product :\n')
    maximum_quantity = quantity_finder()
    quantity = range(1, maximum_quantity + 1)
    utility = set_utility(maximum_quantity, product_name)
    plt.plot(quantity, utility)
    plt.ylabel("Utility")
    plt.xlabel("Quantity")
    plt.grid(True)
    plt.title("{}'s utility in function of the quantity".format(product_name))
    plt.show()

if __name__ == '__main__':
    create_graph()
