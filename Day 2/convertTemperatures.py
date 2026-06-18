# Write a Python program to convert temperatures to and from celsius, fahrenheit.

def convertTemperatures(temp = 0, scale = "fahrenheit_or_celsius"):
    if scale.lower() == "fahrenheit":
        return f"{(temp * 9/5) + 32}°F"
    elif scale.lower() == "celsius":
        return f"{(temp - 32) * 5/9}°C"
    return "Scale is wrong. It should be fahrenheit or celsius."

print(f"25°C = {convertTemperatures(25, "fahrenheit")}")
print(f"32°F = {convertTemperatures(32, "celsius")}")