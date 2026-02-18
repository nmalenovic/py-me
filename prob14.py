class Point():
    """ Represents a point in two-dimensional space. """
    def __init__(self, x, y):
        self.x = x
        self.y = y

class ListOfPoints():
    def __init__(self, points):
        """ ListOfPoints has one attribute, which is a list.
        The elements are Point objects
        """
        self.points = list(points)
        
    def __len__(self):
        return len(self.points) # Returns the length of the internal list

    def __mul__(self, other):
        if ( type ( other ) is ListOfPoints and len(other) == len(self)):
            print ( 'Case 1: LoP * LoP' )
        elif ( type ( other ) is Point ):
            print ( 'Case 2: LoP * P' )
        elif ( type ( other ) is int ):
            print ( 'Case 3: LoP * int' )
        else:
            print ( 'Case 4: LoP * anything other then LoP, P, int' )
        
        return None

# --------------------------
print ( f"case 1: LoP * LoP" )
lop = ListOfPoints( [ Point(1,2), Point(5,5) ] )
other = ListOfPoints( [ Point(0,0), Point(5,5) ] )
result = lop * other
print ( f"E#1: result = [ (0,0), (25, 25) ]" )
print ( f"A#1: result = {result}" )

# --------------------------
print ( f"case 2: LoP * P" )
other = Point(2,2)
result = lop * other
print ( f"E#2: result = [ (2,4), (10,10) ]" )
print ( f"A#2: result = {result}" )

# --------------------------
print ( f"case 3: LoP * int" )
other = 4
result = lop * other
print ( f"E#3: result = [ (3,6), (15,15) ]" )
print ( f"A#3: result = {result}" )

# --------------------------
print ( f"case 4: LoP * anything other then LoP, P, int" )
other = ListOfPoints( [ Point(0,0), Point(5,5), Point(7,7) ] )
result = lop * other
print ( f"E#4: result = None" )
print ( f"A#4: result = {result}" )
