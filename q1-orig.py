def sequence(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return 2 * sequence(n-1) + sequence(n-2)
    


result = sequence(2)
print ( f"sequence(2) = {result}" )
# 2 * sequence(1) + sequence(0) = 2 * 1 + 0 = 2 <-- sequence(2)

result = sequence(3)
print ( f"sequence(3) = {result}" )
# 2 * sequence(2) + sequence(1) = 2 * 2 + 1 = 5 <-- sequence(3)

result = sequence(4)
print ( f"sequence(4) = {result}" )
# 2 * sequence(3) + sequence(2) = 2 * 5 + 2 = 12 <-- sequence(4)
