#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def convert_temperature(unit, temp):
    temp_convert_celsius = ((float(temp) - 32) * 5 / 9)
    temp_convert_fahrenheit = ((float(temp) * 1.8) + 32)

    if unit == "C" and (float(temp) >= 0 or float(temp) <= 0):
        print("Converting to Fahrenheit...")
        print("The temperature in Celsius is " + str(temp) + " and the temperature in Fahrenheit is " + str(
            temp_convert_fahrenheit) + ".")
    elif unit == "F" and (float(temp) >= 0 or float(temp) <= 0):
        print("Converting to Celsius...")
        print("The temperature in Fahrenheit is " + str(float(temp)) + " and the temperature in Celsius is " + str(
            temp_convert_celsius) + ".")
    else:
        print("Invalid Unit")

while True:
    unit = str(input("Input Degree: 'C' for Celsuis or 'F' for Fahrenheit \n")).capitalize()
    if unit == "C":
        print("Unit is Celsius.")
        break;
    elif unit == "F":
        print("Unit is Fahrenheit.")
        break;
    else:
        print("Invalid Unit.\n Enter either 'c' for Celsius or 'f' for Fahrenheit")


while True:
    temp = input("Input the temperature to be converted \n")
    try:
        val = float(temp)
        print("Input number is: ", val)
        break;
    except ValueError:
        print("This is not a Integer.\nPlease enter a valid Number")
convert_temperature(unit, temp)


# In[ ]:




