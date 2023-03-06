Simple Binary to Decimal Converter and Decimal to Binary Converter
This is a simple binary to decimal converter and decimal to binary converter made in Python. It does not require any external packages to work.

Binary to Decimal Converter
To convert binary to decimal, call the binary_to_decimal function and pass the binary number as an argument:
<code>
def binary_to_decimal(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal*2 + int(digit)
    return decimal
 </code> 
Here's an example usage:
<code>
binary_number = "1101"
decimal_number = binary_to_decimal(binary_number)
print(decimal_number)
 </code>
Output:
13

Decimal to Binary Converter
To convert decimal to binary, call the decimal_to_binary function and pass the decimal number as an argument:
<code>
def decimal_to_binary(decimal):
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return binary
</code>

Here's an example usage:
<code>
decimal_number = 13
binary_number = decimal_to_binary(decimal_number)
print(binary_number)
</code>
Output:
1101
