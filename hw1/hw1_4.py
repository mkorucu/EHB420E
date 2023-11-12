'''
	Bitwise operations
'''
print("Bitwise operators are used to calculate bit-level operations. These operations are useful when setting the registers of a microcontroller or its peripherals.")
print("For example: & is bitwise AND operation. It ands every bits of 2 number and returns the result.")
a = 5 #101
b = 6 #110
print("the result of a(5) & b(6) is equal to " + str(a & b)) # 101 & 110 => 1&1 , 0&1 , 1&0 => 1,0,0 => 100 = 4
print("In the same manner, | means bitwise OR, ^ means bitwise XOR, ~ means bitwise NOT, << shifts number to the left, >> shifts number to the right handside.")
print("a(5) | b(6) equals to " + str(a | b)) # 101 | 110 => 111 = 7
print("a(5) ^ b(6) equals to " + str(a ^ b)) # 101 ^ 110 => 011 = 3
print("bitwise not of a(5) equals to" + str(~a)) # 101 => 0101= 2
print("a(5) 2 times shifted to the left equals to " + str(a << 2)) # 101 << 2 => 10100 = 20
print("b(6) 2 times shifted to the right equals to " + str(b >> 2)) # 110 >> 2 => 1 = 1


'''
Special operators
'''
print("Special operators are 'is' and 'is not' operators.")
print("These operators are used to compare the identity of two objects, which means checking if the memory locations of two objects are same.")

c = [3,4,5]
d = 4
print("c and d are two different variable in memory. Therefore, their 'is' operation is equal to " + str(c is d)) 


'''
Membership operators
'''
print("Membership operators are used to check if a value is inluded in a sequence or collection, such as strings, lists, tuples, or sets. The membership operators available in Python are \"in\" and \"not in\".")
text = "Hello, world!"
print("Hello" in text)  # True - "Hello" is present in the string
print("hi" not in text)  # True - "hi" is not present in the string
