def calculate_voltage(current, resistance):
    return current * resistance
    
def calculate_current(voltage, resistance):
    if resistance == 0:
        return None 
    return voltage / resistance

def calculate_resistance(voltage, current):
    if current == 0: 
        return None
    return voltage / current 
    
def get_float(prompt):
    while True:
        try: 
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a correct value.")
    
def main():
    print("Hello User. This is the Ohm's Law Calculator.")
    
    while True:
        print("\nWhat would you like to calculate?")
        choice = input("Type 'V' if you want for Voltage, 'I' for Current, or 'R' for Resistance and 'exit' if you don't want to do this: ").strip().upper()
        
        if choice == 'V':
            current = get_float("Enter the current (I) in Amperes: ")
            resistance = get_float("Enter the resistance (R) in Ohms: ")
            voltage = calculate_voltage(current, resistance)
            print(f"The voltage (V) is: {voltage:.2f} Volts.")
        
        elif choice == 'I':
            voltage = get_float("Enter the voltage (V) in Volts: ")
            resistance = get_float("Enter the resistance (R) in Ohms: ")
            current = calculate_current(voltage, resistance)
            if current is None:
                print("Error: Resistance cannot be zero.")
            else:
                print(f"The current (I) is: {current:.2f} Amperes.")
                
                
        elif choice == 'R':
            voltage = get_float("Enter the voltage (V) in Volts: ")    
            current = get_float("Enter the current (I) in Amperes: ")
            resistance = calculate_resistance(voltage, current)
            if resistance is None:
                print("ERROR: Current cannot be zero.")
            else:
                print(f"The resistance (R) is: {resistance:.2f} Ohms.")
        
        elif choice == 'EXIT':
            print("Thank you for using the Ohm's Law Calculator. Byebye, User!")
            break
        
        else:
            print("Invalid choice. Please enter 'V', 'I', 'R', or 'exit' ONLY.")

if __name__ == "__main__":
    main()