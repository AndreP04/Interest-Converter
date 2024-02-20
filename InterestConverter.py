# Title of program
print("\n====Interest Converter====")

# Display menu of options
print("\nConvert from:")
print("\n1. Simple Interest Rate")
print("2. Effective Annual Interest Rate")
print("3. Effective Periodic Interest Rate")
print("4. Nominal Interest Rate")
print("5. Close application")

# Get user input
userInput = input("\nEnter an option to continue: ")

while (userInput != "5"):

    # Simple Interest Rate
    if (userInput == "1"):
        print("\n====Simple Interest Rate Converter====")
        print("\nConvert to:")
        print("\n1. Effective Annual Interest Rate")
        print("2. Nominal Interest Rate")
        print("3. Effective Periodic Interest Rate")
        break

    # Effective Annual Interest Rate
    if (userInput == "2"):
        print("\n====Effective Annual Interest Rate Converter====")
        print("\nConvert to:")
        print("\n1. Simple Interest Rate")
        print("2. Nominal Interest Rate")
        print("3. Effective Periodic Interest Rate")
        break

    # Effective Periodic Interest Rate
    if (userInput == "3"):
        print("\n====Effective Periodic Interest Rate Converter====")
        print("\nConvert to:")
        print("\n1. Simple Interest Rate")
        print("2. Nominal Interest Rate with same compounding")
        print("3. Nominal Interest Rate with different compounding")
        print("4. Effective Periodic Interest Rate with different compounding")
        print("5. Effective Annual Interest Rate")
        break

    # Nominal Interest Rat
    if (userInput == "4"):
        print("\n====Nominal Interest Rate Converter====")
        print("\nConvert to:")
        print("\n1. Simple Interest Rate")
        print("2. Nominal Interest Rate with different compounding")
        print("3. Effective Periodic Interest Rate with same compounding")
        print("4. Effective Periodic Interest Rate with different compounding")
        print("5. Effective Annual Interest Rate")
        break

    # Exit the program
    if (userInput == "5"):
        exit()
