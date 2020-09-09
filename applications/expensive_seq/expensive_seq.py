# Your code here
lookup_table = {}

def expensive_seq(x, y, z):
    if x <= 0:
        return y + z
    if x > 0:
        result = 0
        for i in range(1,4):
            if not (x-i,y+i,z*i) in lookup_table:
                lookup_table[(x-i,y+i,z*i)] = expensive_seq(x-i,y+i,z*i)
            result += lookup_table[(x-i,y+i,z*i)]
        lookup_table[(x,y,z)] = result
        return result


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
