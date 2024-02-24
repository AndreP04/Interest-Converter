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

        userInSimple = input("\nEnter an option to continue: ")

        #Variables (Effective Annual)
        if (userInSimple == "1"):
            y = float(input("y = "))
            x = float(input("x = "))
            i1 = float(input("i1 = "))

            #Formula
            Effi2 = round(float((pow((1 + x*(i1)),1/y) - 1)*(100)),4)

            #Show answer
            print(Effi2,"%")
            
            #Close program
            close = input("Close? ")
            if (close == "Y"):
                break

        #Variables (Nominal)
        if (userInSimple == "2"):
            y = float(input("y = "))
            x = float(input("x = "))
            i1 = float(input("i1 = "))

            #Formula
            Nomi2 = round(float(((1 + x*i1) ** (1/y) - 1) * (y) * 100),4)

            #Show answer
            print(Nomi2,"%")

            #Close program
            close = input("Close? ")
            if (close == "Y"):
                break

        #Variables (Effective Periodic)
        if (userInSimple == "3"):
            y = float(input("y = "))
            x = float(input("x = "))
            i1 = float(input("i1 = "))
            
            #Formula
            Effi2 = round(float((pow((1 + x*(i1)),1/y) - 1)*(100)),4)

            #Show answer
            print(Effi2,"%")
            
            #Close program
            close = input("Close? ")
            if (close == "Y"):
                break



    # Effective Annual Interest Rate
    if (userInput == "2"):
        print("\n====Effective Annual Interest Rate Converter====")
        print("\nConvert to:")
        print("\n1. Simple Interest Rate")
        print("2. Nominal Interest Rate")
        print("3. Effective Periodic Interest Rate")

        userInEffAn = input("\nEnter an option to continue: ")

        #Variables (Simple)
        if (userInEffAn == "1"):
            y = float(input("y = "))
            x = float(input("x = "))
            i1 = float(input("i1 = "))

            #Formula
            Simi2 = round(float((((1 + i1) ** x - 1)/y)* 100),4)

            #Show answer
            print(Simi2,"%")
            
            #Close program
            close = input("Close? ")
            if (close == "Y"):
                break

        #Variables (Nominal)
        if (userInEffAn == "2"):
            y = float(input("y = "))
            x = float(input("x = "))
            i1 = float(input("i1 = "))

            #Formula
            Nomi2 = round((float((1 + i1) ** (x / y) - 1) * y * 100),4)

            #Show answer
            print(Nomi2,"%")
            
            #Close program
            close = input("Close? ")
            if (close == "Y"):
                break

        #Variables (Effective Periodic)
        if (userInEffAn == "3"):
            y = float(input("y = "))
            x = float(input("x = "))
            i1 = float(input("i1 = "))

            #Formula
            Effi2 = round(float(((1 + i1) ** (x/y) - 1) * 100),4)

            #Show answer
            print(Effi2,"%")
            
            #Close program
            close = input("Close? ")
            if (close == "Y"):
                break



    # Effective Periodic Interest Rate
    if (userInput == "3"):
        print("\n====Effective Periodic Interest Rate Converter====")
        print("\nConvert to:")
        print("\n1. Simple Interest Rate")
        print("2. Nominal Interest Rate")
        print("3. Effective Periodic Interest Rate")
        print("4. Effective Annual Interest Rate")
        
        userInEffPer = input("\nEnter an option to continue: ")

        #Variables (Simple)
        if (userInEffPer == "1"):
            y = float(input("y = "))
            x = float(input("x = "))
            i1 = float(input("i1 = "))

            #Formula
            Simpi2 = round(float((((1 + i1) ** x - 1)/y)* 100),4)

            #Show answer
            print(Simpi2,"%")
            
            #Close program
            close = input("Close? ")
            if (close == "Y"):
                break

        #Variables (Nominal)
        if (userInEffPer == "2"):
            y = float(input("y = "))
            x = float(input("x = "))
            i1 = float(input("i1 = "))

            #Formula
            Nomi2 = round((float((1 + i1) ** (x / y) - 1) * y * 100),4)

            #Show answer
            print(Nomi2,"%")
            
            #Close program
            close = input("Close? ")
            if (close == "Y"):
                break

        #Variables (Effective Periodic)
        if (userInEffPer == "3"):
            y = float(input("y = "))
            x = float(input("x = "))
            i = float(input("i = "))

            #Formula
            Effi2 = round(float(((1 + i) ** (x/y) - 1) * 100),4)

            #Show answer
            print(Effi2,"%")
            
            #Close program
            close = input("Close? ")
            if (close == "Y"):
                break


        #Variables (Effective Annual)
        if (userInEffPer == "4"):
            y = float(input("y = "))
            x = float(input("x = "))
            i = float(input("i = "))

            #Formula
            Effi2 = round(float(((1 + i) ** (x/y) - 1) * 100),4)

            #Show answer
            print(Effi2,"%")
            
            #Close program
            close = input("Close? ")
            if (close == "Y"):
                break



    # Nominal Interest Rate
    if (userInput == "4"):
        print("\n====Nominal Interest Rate Converter====")
        print("\nConvert to:")
        print("\n1. Simple Interest Rate")
        print("2. Nominal Interest Rate")
        print("3. Effective Periodic Interest Rate")
        print("4. Effective Annual Interest Rate")

        userInNom = input("\nEnter an option to continue: ")
    
    #Variables (Simple)
        if (userInNom == "1"):
            y = float(input("y = "))
            x = float(input("x = "))
            i1 = float(input("i1 = "))

            #Formula
            Simpi2 = round(float(((1 + i1/x) ** (x) - 1)/y),4)

            #Show answer
            print(Simpi2,"%")
            
            #Close program
            close = input("Close? ")
            if (close == "Y"):
                break

    # Exit the program
    if (userInput == "5"):
        exit()
