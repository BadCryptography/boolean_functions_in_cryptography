from util import x_body, character, bitV2str

#The idea of the fourier-transformation is to see how a function
#reacts in different frequencies (in electronics)
#in the specific case of boolean functions, the fourier-transformation
#is held a little simpler; we create the sum over all function results
#multiplied by their character, while holding a specific a, which
#represents the frequency we currently are looking for 
#it is important to know, that the result of the transformation is not
#limited to 1 and 0 but is a whole number!

def fourier_transform(a:list[int], fvals:list[int], body:list[int])->int:
    return sum([y*character(a,x) for (x, y) in zip(body,fvals)])

#for the inversion we need the list of function values of the transformation
def fourier_inversion(x:list[int], tfvals:list[int], body:list[int])->int:
    return int(sum([fval*character(a,x) for a,fval in zip(body,tfvals)])/len(body))


def inversion_check(original_values:list[int], reconstructed_values:list[int]):
    print(all(f == i for f, i in zip(original_values, reconstructed_values)))

if __name__ == "__main__":
    bits = 3
    body = x_body(bits)
    fvals = [0, 1, 1, 0, 1, 0, 0, 1]  # Originale Funktionswerte über F2^3

    # Fourier-Transformation berechnen
    tfvals = [fourier_transform(a, fvals, body) for a in body]

    # Inverse Transformation zur Rekonstruktion
    itfvals = [fourier_inversion(x, tfvals, body) for x in body]

    print("Fourier-Transformation der Funktion (jeweils für a in F2^3):")
    print(f"{'a':<10} {'TF[a]':>6}")
    print("-" * 20)
    for a, val in zip(body, tfvals):
        print(f"{bitV2str(a):<10} {val:>6}")
    
    print("\nRekonstruierte Funktionswerte aus der Inversion:")
    print(f"{'x':<10} {'f(x)':>6}")
    print("-" * 20)
    for x, val in zip(body, itfvals):
        print(f"{bitV2str(x):<10} {val:>6}")  


    inversion_check(fvals, itfvals)
