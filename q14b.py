class Triple():
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, other):
        # write code here
        return Triple(self.x - other.x, self.y - other.y, self.z - other.z)

class TripleVector():
    def __init__(self, triples):
        # TripleVector has one attribute that's a list. elements are Triple()
        self.triples = list(triples)
    def __sub__(self, other):
        # write code here

        # case 1: other is a TripleVector
        if type(other) == TripleVector:
            print ("TripleVector")

        # case 2: other is a Triple object
        elif type(other) == Triple:
            print ("Triple")

        # case 3: other is an integer
        elif type(other) == int:
            print ("int")

        # otherwise: return None
        else:
            print ("none of the above")
            return None

a = TripleVector( [ Triple(1,1,1), Triple(3,3,3) ] )
b = 2

c = a - b
