# Python program to count the number of distinct
# characters present in the string str
S = "Welcome World"
a = ""
for i in S:
	if i not in a:
		a += i
print(len(a))
