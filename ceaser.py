alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
s = input("Enter string: ")
key = int(input("Enter key: "))
while key > 26:
	key-=26
for x in set(s):
	if x in alpha:
		new_char = ord(x)+key
		if (97 <= new_char <= 122) or (65 <= new_char <= 90):
			s = s.replace(x, chr(new_char))
		else:
			s = s.replace(x, chr(new_char-26))
print(s)