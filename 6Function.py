
def celcius2fahrenheit(cel):
    return 32 + cel * 1.8

if __name__ == '__main__':
    cel = float(input("Please enter a temperature in degrees celsius: "))
    print("Fahrenheit temperature: ", celcius2fahrenheit(cel))
