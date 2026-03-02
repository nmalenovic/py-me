class Triple():
        def __init__(self, x=0, y=0, z=0):
            self.x = x
            self.y = y
            self.z = z
        def __sub__(self, other):
            # write code here
            return Triple(self.x - other.x, self.y - other.y, self.z - other.z)


# how do you test: substraction between two Tiple objects, e.g. a-b
a = Triple(3,3,3)
b = Triple(1,1,1)
c = a - b
print ( a )
print ( b )
print ( c )
