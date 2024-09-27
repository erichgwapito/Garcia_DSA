def print_diamond(n):
    if n % 2 == 0:
        return "Please provide an odd integer."
    
    for i in range(n):
        # To calculate the number of spaces and stars for each row
        stars = '*' * (2 * i + 1) if i <= n // 2 else '*' * (2 * (n - i - 1) + 1)
        spaces = ' ' * abs((n // 2) - i)
        
        # Printing the row 
        print(spaces + stars)

# 
print_diamond(5)