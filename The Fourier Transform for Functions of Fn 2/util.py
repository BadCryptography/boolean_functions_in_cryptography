#returns all possible bit combinations as a list of lists
def x_body(bits: int):
    body_range = range(2**bits)
    elements = [[int(bit) for bit in format(x, f"0{bits}b")] for x in body_range]
    return elements


def scalar(a:list[int],x:list[int])->int:
    return sum([ai*xi for ai, xi in zip(a,x)])

def character(a:list[int],x:list[int])->int:
    return int(pow(-1, scalar(a,x)))

def character_sum(a,x_body):
    return sum([character(a,x) for x in x_body])

def bitV2str(bitV:list[int])->str:
    return "".join([str(i) for i in bitV])

if __name__=="__main__":

    bits = 4
    body = x_body(bits=bits)

    #Scalar for each a in body
    for a in body:
        print(f"Current a={bitV2str(a)}", end="\n")
        for x in body:
            print(f"<{bitV2str(a)},{bitV2str(x)}>={scalar(a,x)}")

        
        print("\n\n")

    print("="*7)
    #Character for each a in body 
    for a in body:
        print(f"Current a={bitV2str(a)}", end="\n")
        for x in body:
            print(f"X_({bitV2str(a)})({bitV2str(x)})={character(a,x)}")

        
        print("\n\n")

    print("="*7)

    #Character sum for each a in body
    for a in body:
        print(f"Current a={bitV2str(a)}", end="\n")
        print(f"XSum(a)={character_sum(a, body)}")


