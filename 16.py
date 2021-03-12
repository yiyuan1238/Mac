def next_in_sequence(a,b,c):
    if b - a == c - b:
        result = c + (c - b)
        return result
    else:
        return False

print(next_in_sequence(40,0,-40))
print(next_in_sequence(2,4,6))
print(next_in_sequence(-4,-1,5))