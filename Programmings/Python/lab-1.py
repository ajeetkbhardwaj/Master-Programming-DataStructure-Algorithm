"""
1. Bitwise operators

"""
# %% 1.1. Bitwise AND
a = 9
print(bin(a)) # 0b1001
b = 3
print(bin(b)) # 0b0011
print(a & b) # 1
print(a | b) # 11
print(a ^ b) # 10
print(~a) # -10
print(a << 1) # 18
print(a >> 1) # 4

c = 0
print(bin(c)) # 0b0
print(~c) # -1
print(not(c)) # True


# %%
