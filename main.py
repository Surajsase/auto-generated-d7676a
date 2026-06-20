def calculate_cube(n):
    """
    Calculate the cube of a number.
    
    Args:
        n (int): The number to calculate the cube of.
    
    Returns:
        int: The cube of the number.
    """
    return n ** 3

def main():
    """
    Print the cube of a number.
    """
    num = 5
    cube = calculate_cube(num)
    print(f"The cube of {num} is: {cube}")

if __name__ == "__main__":
    main()