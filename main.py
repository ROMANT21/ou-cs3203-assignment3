def addList(list):
        sum = 0
        for item in list:
            sum += item
        return sum

def multiplyList(list):
    prod = 1
    for item in list:
        prod *= item
    return prod

if __name__ == "__main__":

    while True:
        list = input("Enter a series of integers seperated by spaces (e.g. 1 3 5 2): ")
        # Parse input from string to integers
        list = list.split(" ")
        try:
            list = [int(num) for num in list]
            break
        except:
            print("Invalide Operators in Input: Please make sure you only enter integers \n")

    # Print sum and products of user input
    print(f"The sum of all integers in the list is: {addList(list)}")
    print(f"The product of all integers in the list is: {multiplyList(list)}")