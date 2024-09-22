a = 10  # 1010 in binary
b = 4   # 0100 in binary

# Bitwise AND operator (&)
and_result = a & b  # 1010 & 0100 = 0000 (decimal 0)
print("Bitwise AND:", a, "&", b, "=", and_result)

# Bitwise OR operator (|)
or_result = a | b  # 1010 | 0100 = 1110 (decimal 14)
print("Bitwise OR:", a, "|", b, "=", or_result)

# Bitwise XOR operator (^)
xor_result = a ^ b  # 1010 ^ 0100 = 1110 (decimal 14)
print("Bitwise XOR:", a, "^", b, "=", xor_result)

# Bitwise NOT operator (~)
not_result = ~a  # ~1010 = -(1010 + 1) = -11
print("Bitwise NOT: ~", a, "=", not_result)

# Bitwise LEFT SHIFT operator (<<)
left_shift_result = a << 2  # 1010 << 2 = 101000 (decimal 40)
print("Bitwise LEFT SHIFT:", a, "<< 2 =", left_shift_result)

# Bitwise RIGHT SHIFT operator (>>)
right_shift_result = a >> 2  # 1010 >> 2 = 0010 (decimal 2)
print("Bitwise RIGHT SHIFT:", a, ">> 2 =", right_shift_result)
