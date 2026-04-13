# 1) Store 10 in `a` and -10 in `b`.
a = 10
b = -10
# 2) Perform a right shift on `a` by 1 and print the result.
#    (Right shift means moving all bits one place to the right.)
print("a >> 1=", a >> 1)
# 3) Perform a right shift on `b` by 1 and print the result.
#    (Negative numbers also shift, but the sign is kept.)
print("b >> 1=", b >> 1)
# 4) Change `a` to 5 and keep `b` as -10.
a = 5
b = -10
# 5) Perform a left shift on `a` by 1 and print the result.
#    (Left shift means moving all bits one place to the left.)
print("a << 1=", a << 1)
# 6) Perform a left shift on `b` by 1 and print the result.
print("b << 1=", b << 1)
