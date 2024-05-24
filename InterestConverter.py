import math

# Title of program
print("\n====Interest Converter====")

# Display menu of options
print("\nChoose an option:")
print("\n1. Simple Interest Rate")
print("2. Effective Annual Interest Rate")
print("3. Effective Periodic Interest Rate")
print("4. Nominal Interest Rate")
print("5. Simple Investment Calculator")
print("6. Close application")

# Get user input
userInput = input("\nEnter an option to continue: ")

#Function to display menu
def displayMenu():
    # Display menu of options
    print("\nConvert from:")
    print("\n1. Simple Interest Rate")
    print("2. Effective Annual Interest Rate")
    print("3. Effective Periodic Interest Rate")
    print("4. Nominal Interest Rate")
    print("5. Simple Investment Calculator")              
    print("6. Close application")

    # Get user input
    userInput = input("\nEnter an option to continue: ")


while (userInput != "6"):

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
            y = float(input("\nEffective Period (y) = "))
            x = float(input("Simple Period (x) = "))
            i1 = float(input("Simple Interest Rate (i1) = "))

            #Formula
            Effi2 = round(float((pow((1 + x*(i1)),1/y) - 1)*(100)),4)

            #Show answer
            print("\nEffective Interest Rate (Effi2) = ",Effi2,"%")
            
            #Close program
            close = input("\nClose? (Y/N) ")
            if (close == "Y"):
                break
            else:
                displayMenu()

        #Variables (Nominal)
        if (userInSimple == "2"):
            y = float(input("\nNominal Period (y) = "))
            x = float(input("Simple Period (x) = "))
            i1 = float(input("Simple Interest Rate (i1) = "))

            #Formula
            Nomi2 = round(float(((1 + x*i1) ** (1/y) - 1) * (y) * 100),4)

            #Show answer
            print("\nNominal Interest Rate (Nomi2) = ",Nomi2,"%")

            #Close program
            close = input("\nClose? (Y/N) ")
            if (close == "Y"):
                break
            else:
                displayMenu()

        #Variables (Effective Periodic)
        if (userInSimple == "3"):
            y = float(input("\nEffective Period (y) = "))
            x = float(input("Simple Period (x) = "))
            i1 = float(input("Simple Interest Rate (i1) = "))
            
            #Formula
            Effi2 = round(float((pow((1 + x*(i1)),1/y) - 1)*(100)),4)

            #Show answer
            print("\nEffective Interest Rate (Effi2) = ",Effi2,"%")
            
            #Close program
            close = input("\nClose? (Y/N) ")
            if (close == "Y"):
                break
            else:
                displayMenu()



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
            y = float(input("\nSimple Period (y) = "))
            x = float(input("Effective Period (x) = "))
            i1 = float(input("Effective Interest Rate (i1) = "))

            #Formula
            Simi2 = round(float((((1 + i1) ** x - 1)/y)* 100),4)

            #Show answer
            print("\nSimple Effective Interest Rate (Simi2) = ",Simi2,"%")
            
            #Close program
            close = input("\nClose? (Y/N) ")
            if (close == "Y" or close == "y"):
                break
            else:
                displayMenu()

        #Variables (Nominal)
        if (userInEffAn == "2"):
            y = float(input("\nNominal Period (y) = "))
            x = float(input("Effective Period (x) = "))
            i1 = float(input("Effective Interest Rate (i1) = "))

            #Formula
            Nomi2 = round((float((1 + i1) ** (x / y) - 1) * y * 100),4)

            #Show answer
            print("\nNominal Interest Rate (Nomi2) = ",Nomi2,"%")
            
            #Close program
            close = input("\nClose? (Y/N) ")
            if (close == "Y"):
                break
            else:
                displayMenu()

        #Variables (Effective Periodic)
        if (userInEffAn == "3"):
            y = float(input("\nEffective Period (y) = "))
            x = float(input("Effective Interest Rate 1 (x) = "))
            i = float(input(" Effective Interest Rate 2 (i) = "))

            #Formula
            Effi2 = round(float(((1 + i) ** (x/y) - 1) * 100),4)

            #Show answer
            print("\nEffective Interest Rate (Effi2) = ",Effi2,"%")
            
            #Close program
            close = input("\nClose? (Y/N) ")
            if (close == "Y"):
                break
            else:
                displayMenu()



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
            y = float(input("\nSimple Period (y) = "))
            x = float(input("Effective Period (x) = "))
            i1 = float(input("Effective Interest Rate (i1) = "))

            #Formula
            Simi2 = round(float((((1 + i1) ** x - 1)/y)* 100),4)

            #Show answer
            print("\nSimple Effective Interest Rate (Simi2) = ",Simi2,"%")
            
            #Close program
            close = input("Close? (Y/N) ")
            if (close == "Y"):
                break
            else:
                displayMenu()

        #Variables (Nominal)
        if (userInEffPer == "2"):
            y = float(input("\nNominal Period (y) = "))
            x = float(input("Effective Period (x) = "))
            i1 = float(input("Effective Interest Rate (i1) = "))

            #Formula
            Nomi2 = round((float((1 + i1) ** (x / y) - 1) * y * 100),4)

            #Show answer
            print("\nNominal Interest Rate (Nomi2) = ",Nomi2,"%")
            
            #Close program
            close = input("\nClose? (Y/N) ")
            if (close == "Y"):
                break
            else:
                displayMenu()

        #Variables (Effective Periodic)
        if (userInEffPer == "3"):
            y = float(input("\nEffective Period (y) = "))
            x = float(input("Effective Interest Rate 1 (x) = "))
            i = float(input("Effective Interest Rate 2 (i) = "))

            #Formula
            Effi2 = round(float(((1 + i) ** (x/y) - 1) * 100),4)

            #Show answer
            print("\nEffective Interest Rate (Effi2) = ",Effi2,"%")
            
            #Close program
            close = input("\nClose? (Y/N) ")
            if (close == "Y"):
                break
            else:
                displayMenu()


        #Variables (Effective Annual)
        if (userInEffPer == "4"):
            y = float(input("\nEffective Period (y) = "))
            x = float(input("Effective Interest Rate 1 (x) = "))
            i = float(input("Effective Interest Rate 2 (i) = "))

            #Formula
            Effi2 = round(float(((1 + i) ** (x/y) - 1) * 100),4)

            #Show answer
            print("\nEffective Interest Rate (Effi2) = ",Effi2,"%")
            
            #Close program
            close = input("\nClose? (Y/N) ")
            if (close == "Y"):
                break
            else:
                displayMenu()



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
            y = float(input("\nSimple Period (y) = "))
            x = float(input("Nominal Period (x) = "))
            i1 = float(input("Nominal Interest Rate (i1) = "))

            #Formula
            Simpi2 = round(float(((1 + (i1/x)) ** (x) - 1)/(y) * 100),4)

            #Show answer
            print("\nSimple Interest Rate (Simpi2) = ",Simpi2,"%")
            
            #Close program
            close = input("\nClose? (Y/N) ")
            if (close == "Y"):
                break
            else:
                displayMenu()

        #Variables (Nominal)
        if (userInNom == "2"):
            p1 = float(input("\nNominal Period 1 (p1) = "))
            p2 = float(input("Nominal Period 2 (p2) = "))
            i1 = float(input("Nominal Interest Rate (i1) = "))

            #Formula
            Nomi2 = round(float(((1 + (i1/p1)) ** (p1/p2) - 1) * (p2) * 100),4)

            #Show answer
            print("\nNominal Interest Rate (Nomi2) = ",Nomi2,"%")
            
            #Close program
            close = input("\nClose? (Y/N) ")
            if (close == "Y"):
                break
            else:
                displayMenu()

        #Variables (Effective Periodic)
        if (userInNom == "3"):
            p1 = float(input("\nNominal Period (p1) = "))
            p2 = float(input("Effective Period (p2) = "))
            i1 = float(input("Nominal Interest Rate (i1) = "))

            #Formula
            Effi2 = round(float(((1 + (i1/p1)) ** (p1/p2) - 1) * 100),4)

            #Show answer
            print("\nEffective Interest Rate (Effi2) = ",Effi2,"%")
            
            #Close program
            close = input("\nClose? (Y/N) ")
            if (close == "Y"):
                break
            else:
                displayMenu()

        #Variables (Effective Annual)
        if (userInNom == "4"):
            p1 = float(input("\nNominal Period (p1) = "))
            p2 = float(input("Effective Period (p2) = "))
            i1 = float(input("Nominal Interest Rate (i1) = "))

            #Formula
            Effi2 = round(float(((1 + (i1/p1)) ** (p1/p2) - 1) * 100),4)

            #Show answer
            print("\nEffective Interest Rate (Effi2) = ",Effi2,"%")
            
            #Close program
            close = input("\nClose? (Y/N) ")
            if (close == "Y"):
                break
            else:
                displayMenu()



    # Simple Investment Calculator
    if (userInput == "5"):
        print("\n====Simple Investment Calculator====")
        print("\nOptions:")
        print("\n1. Simple Interest Method")
        print("2. Compound Interest and Effective Annual Interest")
        print("3. Compound Interest and Effective Periodic Interest")
        print("4. Compound Interest and Nominal Interest Rate")

        # Get user input
        userInSimInv1 = input("\nEnter an option to continue: ")
        
        if (userInSimInv1 == "1"):
            print("\nCalculate:")
            print("\n1. Future Value")
            print("2. Present Value")
            print("3. Term of Investment")
            print("4. Simple Interest Rate")
            print("5. Amount of Interest Earned")

            # Get user input
            userInSimInv2 = input("\nEnter an option to continue: ")

            #Future Value
            if(userInSimInv2 == "1"):
                c = float(input("\nPresent Value (c) = "))
                n = float(input("Term of Investment (n) = "))
                i = float(input("Interest Rate (i) = "))
                p = float(input("Period (p) = "))

                #Formula
                FV = round(float(c * (1 + n * p * i)),2)

                #Show answer
                print("\nFuture Value (FV) = ",FV)

                #Close program
                close = input("\nClose? (Y/N) ")
                if (close == "Y"):
                    break
                else:
                    displayMenu()

            
            #Present Value
            if(userInSimInv2 == "2"):
                FV = float(input("\nFuture Value (FV) = "))
                n = float(input("Term of Investment (n) = "))
                i = float(input("Interest Rate (i) = "))
                p = float(input("Period (p) = "))

                #Formula
                c = round(float(FV/(1 + n * p * i)),2)

                #Show answer
                print("\nPresent Value (c) = ",c)

                #Close program
                close = input("\nClose? (Y/N) ")
                if (close == "Y"):
                    break
                else:
                    displayMenu()

            
            #Term of Investment
            if(userInSimInv2 == "3"):
                FV = float(input("\nFuture Value (FV) = "))
                c = float(input("Present Value (c) = "))
                i = float(input("Interest Rate (i) = "))

                #Formula
                n = round(float((FV/c - 1) / i),2)

                #Show answer
                print("\nTerm of Investment (n) = ",n)

                #Close program
                close = input("\nClose? (Y/N) ")
                if (close == "Y"):
                    break
                else:
                    displayMenu()

            
            #Simple Interest Rate
            if(userInSimInv2 == "4"):
                FV = float(input("\nFuture Value (FV) = "))
                c = float(input("Present Value (c) = "))
                n = float(input("Term of Investment (n) = "))

                #Formula
                i = round(float((100) * ((FV/c) - 1) / n),2)

                #Show answer
                print("\nSimple Interest Rate (i) = ",i, "%")

                #Close program
                close = input("\nClose? (Y/N) ")
                if (close == "Y"):
                    break
                else:
                    displayMenu()


            #Interest Earned
            if(userInSimInv2 == "5"):
                i = float(input("\nInterest Rate (i) = "))
                c = float(input("Present Value (c) = "))
                n = float(input("Term of Investment (n) = "))
                p = float(input("Period (p) = "))

                #Formulas
                FV = round(float(c * (1 + n * p * i)),2)
                IE = round(float(FV - c),2)

                #Show answer
                print("\nInterest Earned = R",IE)

                #Close program
                close = input("\nClose? (Y/N) ")
                if (close == "Y"):
                    break
                else:
                    displayMenu()


        #Compound + Effective Annual
        if (userInSimInv1 == "2"):
            print("\nCalculate:")
            print("\n1. Future Value")
            print("2. Present Value")
            print("3. Term of Investment")
            print("4. Effective Annual Interest Rate")
            print("5. Amount of Interest Earned")

            # Get user input
            userInSimInv2 = input("\nEnter an option to continue: ")

            #Future Value
            if(userInSimInv2 == "1"):
                c = float(input("\nPresent Value (c) = "))
                n = float(input("Term of Investment (n) = "))
                i = float(input("Interest Rate (i) = "))

                #Formula
                FV = round(float(c * (pow((1 + i),n))),2)

                #Show answer
                print("\nFuture Value (FV) = ",FV)

                #Close program
                close = input("\nClose? (Y/N) ")
                if (close == "Y"):
                    break
                else:
                    displayMenu()


            #Present Value
            if(userInSimInv2 == "2"):
                FV = float(input("\nFuture Value (FV) = "))
                n = float(input("Term of Investment (n) = "))
                i = float(input("Interest Rate (i) = "))

                #Formula
                c = round(float(FV / pow(1 + i,n)),2)

                #Show answer
                print("\nPresent Value (c) = ",c)

                #Close program
                close = input("\nClose? (Y/N) ")
                if (close == "Y"):
                    break
                else:
                    displayMenu()


            #Term of Investment
            if(userInSimInv2 == "3"):
                FV = float(input("\nFuture Value (FV) = "))
                c = float(input("Present Value (c) = "))
                i = float(input("Interest Rate (i) = "))

                #Formula
                n = round(float(math.log(FV/c)/math.log(1 + i)),3)

                #Show answer
                print("\nTerm of Investment (n) = ",n)

                #Close program
                close = input("\nClose? (Y/N) ")
                if (close == "Y"):
                    break
                else:
                    displayMenu()


            #Effective Annual Interest Rate
            if(userInSimInv2 == "4"):
                FV = float(input("\nFuture Value (FV) = "))
                c = float(input("Present Value (c) = "))
                n = float(input("Term of Investment (n) = "))

                #Formula
                i = round(float((pow(FV/c, 1/n) - 1) * 100),2)

                #Show answer
                print("\nEffective Annual Interest Rate (i) = ",i,"%")

                #Close program
                close = input("\nClose? (Y/N) ")
                if (close == "Y"):
                    break
                else:
                    displayMenu()


            #Interest Earned
            if(userInSimInv2 == "5"):
                i = float(input("\nInterest Rate (i) = "))
                c = float(input("Present Value (c) = "))
                n = float(input("Term of Investment (n) = "))

                #Formulas
                FV = round(float(c * pow((1 + i), n)),2)
                IE = round(float(FV - c),2)

                #Show answer
                print("\nInterest Earned = R",IE)

                #Close program
                close = input("\nClose? (Y/N) ")
                if (close == "Y"):
                    break
                else:
                    displayMenu()



        #Compound + Effective Periodic
        if (userInSimInv1 == "3"):
            print("\nCalculate:")
            print("\n1. Future Value")
            print("2. Present Value")
            print("3. Term of Investment")
            print("4. Effective Periodic Interest Rate")
            print("5. Amount of Interest Earned")

            # Get user input
            userInSimInv2 = input("\nEnter an option to continue: ")

            #Future Value
            if(userInSimInv2 == "1"):
                c = float(input("\nPresent Value (c) = "))
                n = float(input("Term of Investment (n) = "))
                i = float(input("Interest Rate (i) = "))
                p = float(input("Period (p) = "))

                #Formula
                FV = round(float(c * pow((1 + i), n * p)),2)

                #Show answer
                print("\nFuture Value (FV) = R",FV)

                #Close program
                close = input("\nClose? (Y/N) ")
                if (close == "Y"):
                    break
                else:
                    displayMenu()

            
            #Present Value
            if(userInSimInv2 == "2"):
                FV = float(input("\nFuture Value (FV) = "))
                n = float(input("Term of Investment (n) = "))
                i = float(input("Interest Rate (i) = "))
                p = float(input("Period (p) = "))

                #Formula
                c = round(float(FV / pow((1 + i), n * p)),2)

                #Show answer
                print("\nPresent Value (c) = R",c)

                #Close program
                close = input("\nClose? (Y/N) ")
                if (close == "Y"):
                    break
                else:
                    displayMenu()

            
            #Term of Investment
            if(userInSimInv2 == "3"):
                FV = float(input("\nFuture Value (FV) = "))
                c = float(input("Present Value (c) = "))
                i = float(input("Interest Rate (i) = "))
                p = float(input("Period (p) = "))

                #Formula
                n = round(float((math.log(FV/c) / math.log(1 + i)) / p),2)

                #Show answer
                print("\nTerm of Investment (n) = ",n)

                #Close program
                close = input("\nClose? (Y/N) ")
                if (close == "Y"):
                    break
                else:
                    displayMenu()


            #Effective Periodic Interest Rate
            if(userInSimInv2 == "4"):
                FV = float(input("\nFuture Value (FV) = "))
                c = float(input("Present Value (c) = "))
                n = float(input("Term of Investment (n) = "))
                p = float(input("Period (p) = "))

                #Formula
                i = round(float((pow(FV/c, 1/(n*p)) - 1) * 100),2)

                #Show answer
                print("\nEffective Periodic Interest Rate (i) = ",i,"%")

                #Close program
                close = input("\nClose? (Y/N) ")
                if (close == "Y"):
                    break
                else:
                    displayMenu()


            #Interest Earned
            if(userInSimInv2 == "5"):
                i = float(input("\nInterest Rate (i) = "))
                c = float(input("Present Value (c) = "))
                n = float(input("Term of Investment (n) = "))
                p = float(input("Period (p) = "))

                #Formulas
                FV = round(float(c * pow((1 + i), n*p)),2)
                IE = round(float(FV - c),2)

                #Show answer
                print("\nInterest Earned = R",IE)

                #Close program
                close = input("\nClose? (Y/N) ")
                if (close == "Y"):
                    break
                else:
                    displayMenu()

        

        #Nominal
        if (userInSimInv1 == "4"):
            print("\nCalculate:")
            print("\n1. Future Value")
            print("2. Present Value")
            print("3. Term of Investment")
            print("4. Nominal Interest Rate")
            print("5. Amount of Interest Earned")

            # Get user input
            userInSimInv2 = input("\nEnter an option to continue: ")

            #Future Value
            if(userInSimInv2 == "1"):
                c = float(input("\nPresent Value (c) = "))
                n = float(input("Term of Investment (n) = "))
                i = float(input("Interest Rate (i) = "))
                p = float(input("Period (p) = "))

                #Formula
                FV = round(float(c * pow(1 + i/p, n*p)),2)

                #Show answer
                print("\nFuture Value (FV) = R",FV)

                #Close program
                close = input("\nClose? (Y/N) ")
                if (close == "Y"):
                    break
                else:
                    displayMenu()

            
            #Present Value
            if(userInSimInv2 == "2"):
                FV = float(input("\nFuture Value (FV) = "))
                n = float(input("Term of Investment (n) = "))
                i = float(input("Interest Rate (i) = "))
                p = float(input("Period (p) = "))

                #Formula
                c = round(float(FV / pow((1 + i/p), n * p)),2)

                #Show answer
                print("\nPresent Value (c) = R",c)

                #Close program
                close = input("\nClose? (Y/N) ")
                if (close == "Y"):
                    break
                else:
                    displayMenu()


            #Term of Investment
            if(userInSimInv2 == "3"):
                FV = float(input("\nFuture Value (FV) = "))
                c = float(input("Present Value (c) = "))
                i = float(input("Interest Rate (i) = "))
                p = float(input("Period (p) = "))

                #Formula
                n = round(float((math.log(FV/c) / math.log(1 + i/p)) / p),2)

                #Show answer
                print("\nTerm of Investment (n) = ",n)

                #Close program
                close = input("\nClose? (Y/N) ")
                if (close == "Y"):
                    break
                else:
                    displayMenu()


            #Nominal Interest Rate
            if(userInSimInv2 == "4"):
                FV = float(input("\nFuture Value (FV) = "))
                c = float(input("Present Value (c) = "))
                n = float(input("Term of Investment (n) = "))
                p = float(input("Period (p) = "))

                #Formula
                i = round(float((pow(FV/c, 1/(n*p)) - 1) * p * 100),2)

                #Show answer
                print("\nNominal Interest Rate (i) = ",i,"%")

                #Close program
                close = input("\nClose? (Y/N) ")
                if (close == "Y"):
                    break
                else:
                    displayMenu()


            #Interest Earned
            if(userInSimInv2 == "5"):
                i = float(input("\nInterest Rate (i) = "))
                c = float(input("Present Value (c) = "))
                n = float(input("Term of Investment (n) = "))
                p = float(input("Period (p) = "))

                #Formulas
                FV = round(float(c * pow((1 + i/p), n*p)),2)
                IE = round(float(FV - c),2)

                #Show answer
                print("\nInterest Earned = R",IE)

                #Close program
                close = input("\nClose? (Y/N) ")
                if (close == "Y"):
                    break
                else:
                    displayMenu()

    # Exit the program
    if (userInput == "6"):
        exit()
