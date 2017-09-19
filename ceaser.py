alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
s = input("Enter string: ")
key = int(input("Enter key: "))
answer = []
while key > 26:
	key-=26
for x in (s):
	if x in alpha:
		new_char = ord(x)+key
		if (97 <= ord(x) <= 122 and new_char <= 122) or (65 <= ord(x) <= 90 and new_char <= 90):
			answer.append(chr(new_char))
		else:
			answer.append(chr(new_char-26))
	else:
		answer.append(x)
print(('').join(answer))