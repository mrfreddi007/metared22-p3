def roll(text):
    return text[::-1]

def swoop(text):
    text = list(text)
    for i in range(len(text)):
        if text[i] not in '{}':
            text[i] = chr(ord(text[i]) - (i % 6))
    return ''.join(text)

# password = input("Enter the password: ")
# if swoop(roll(password)) == "}zudidsbybwxaqaqehxbebimt`jks{XNidpk":
# 	print("Welcome in!")
# else:
#     print("Sorry, wrong password.")


flag = swoop("}zudidsbybwxaqaqehxbebimt`jks{XNidpk")
print(roll(flag))