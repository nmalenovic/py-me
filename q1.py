def sequence(n):
    if n == 0:
        print ( f"-- sequence(0): base case = 0" )
        result = 0
    elif n == 1:
        print ( f"-- sequence(1): base case = 1" )
        result = 1
    else:
        print ( f"-- sequence({n}): 2 * sequence({n-1}) + sequence({n-2}) ... now calculating sequence ({n-1}) ..." )
        
        seqn1 = sequence(n-1)
        print ( f"-- sequence({n}): calculated sequence({n-1}) to be {seqn1} ... now calculating sequence({n-2})" )

        seqn2 = sequence(n-2)
        print ( f"-- sequence({n}): calculated sequence({n-2}) to be {seqn2}" )

        result = 2 * seqn1 + seqn2
        print ( f"-- sequence({n}): result = 2 * sequence({n-1}) + sequence({n-2}) = {result}" )
    
    return result


print ( f"| Case #1: sequence(4)" )
result = sequence(4)
print ( f"| Expected #1: sequence(4) = 2 * sequence(3) + sequence(2) = 2 * (2 * sequence(2) + sequence(1)) + (2*sequence(1)+sequence(0)) = ..." )
print ( f"|              ... 2 * (2 * (2*sequence(1)+sequence(0)) + sequence(1)) + (2*sequence(1)+sequence(0))" )
print ( f"| Answer #1: sequence(4) = {result}" )
