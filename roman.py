decimal = int(input("Enter a Decimal Number: "))

def dec_to_roman(decimal):

    dicc = {1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}

    roman = ''
    for value, numeral in dicc.items():
        while decimal >= value:
            roman += numeral
            decimal -= value
    return roman

print(dec_to_roman(decimal))