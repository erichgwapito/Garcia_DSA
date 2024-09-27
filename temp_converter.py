def convert_temperature():
    while True:
        try:
            # Prompt user for temperature input
            temperature = float(input("Enter the temperature: "))
            
            # Ask user for the conversion type
            conversion_type = input("Type 'C' to convert from Celsius to Fahrenheit or 'F' to convert from Fahrenheit to Celsius: ").strip().upper()
            
            # Perform the conversion based on the type
            if conversion_type == 'C':
                converted_temp = (temperature * 9/5) + 32
                print(f"{temperature:.2f}°C is equal to {converted_temp:.2f}°F.")
            elif conversion_type == 'F':
                converted_temp = (temperature - 32) * 5/9
                print(f"{temperature:.2f}°F is equal to {converted_temp:.2f}°C.")
            else:
                print("Invalid conversion type. Please enter letter 'C' or 'F' only.")
            
        except ValueError:
            print("Invalid input. Please enter a valid temperature.")
        
        # Ask the user if they want to try again
        again = input("Would you like to try again? (yes/no): ").strip().lower()
        if again != 'yes':
            print("byebye!!!")
            break

# Ensure the script runs only if executed directly
if __name__ == "__main__":
    convert_temperature()