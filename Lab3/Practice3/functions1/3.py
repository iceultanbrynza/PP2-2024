def solve(numheads, numlegs):
    rabbits = (numlegs - 2*numheads)/2
    chickens = numheads - rabbits
    print("Number of rabbits: ", rabbits, "Number of chickens: ", chickens)
heads = int(input())
legs = int(input())
solve(heads, legs)