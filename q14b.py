class Triple():
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, other):
        # write code here
        return Triple(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __repr__(self):
        return f"({self.x},{self.y},{self.z})"

class TripleVector():
    def __init__(self, triples):
        # TripleVector has one attribute that's a list. elements are Triple()
        self.triples = list(triples)

    def __len__(self):
        return len(self.triples)

    def __sub__(self, other):
        # write code here

        # case 1: other is a TripleVector
        if type(other) == TripleVector and len(self) == len(other):
            print ("TripleVector")

            newTriplesList = []
            for triple1, triple2 in zip(self.triples, other.triples): 
                newTriplesList.append(triple1-triple2)
            return TripleVector(newTriplesList)

        # case 2: other is a Triple object
        elif type(other) == Triple:
            print ("Triple")
            newTriplesList = []
            for triple1 in self.triples: 
                newTriplesList.append(triple1-other)
            return TripleVector(newTriplesList)

        # case 3: other is an integer
        elif type(other) == int:
            print ("int")
            newTriplesList = []
            for triple1 in self.triples: 
                a = Triple(triple1.x-other, triple1.y-other, triple1.z-other)
                newTriplesList.append(a)
            return TripleVector(newTriplesList)
        

        # otherwise: return None
        else:
            print ("none of the above")
            return None

a = TripleVector( [ Triple(1,1,1), Triple(3,3,3) ] )
#b = Triple(0,1,2)
#b = TripleVector( [ Triple(0,1,2) ] )
#b = TripleVector( [ Triple(0,1,2), Triple(1,2,3) ] )
b = 2

[(-1,-1,-1), (1,1,1)]

c = a - b
print( f"result: {c.triples}" )
