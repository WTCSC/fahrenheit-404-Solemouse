
option = int(input("1 for Celsius to Fahrenheit, 2 for Fahrenheit to Celsius: "))

if option == 1:
    tempc = float(input("Temp in Celsius: "))
    print(f"Temp in Fahrenheit: {tempc * 1.8 + 32}")

elif option == 2:
    tempf = float(input("Temp in Fahrenheit: "))
    print(f"Temp in Celsius: {(tempf - 32) * 0.5555}")

elif option == 3:
    exit()

else:
    print("Invalid choice. Please enter 1 or 2.")
