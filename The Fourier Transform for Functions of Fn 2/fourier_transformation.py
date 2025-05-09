"""
NOTE: THIS IS SIMPLY A FOOLISH IMPLEMENTATION OF THE ALGORITHM THAT HAS A
RUNTIME OF O(N*2^(2N))
THE NEXT FILE WILL CONTAIN A MORE EFFICIANT ALGORITHM WITH A SIGNIFICANTLY
REDUCED RUNTIME
"""


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
    x_value_pairing = zip(body,fvals)
    multiplicands = [fval*character(a,x) for x, fval in x_value_pairing]

    return sum(multiplicands)

#for the inversion we need the list of function values of the transformation
def fourier_inversion(x:list[int], tfval:list[int], body:list[int])->int:
    dividend = len(body)

    a_value_pairing = zip(body,tfval)
    multiplicands = [tfval*character(x,a) for a, tfval in a_value_pairing]

    return int(sum(multiplicands)/dividend)

def invasion_correct(original_function_values:list[int], inverted_function_values:list[int]):
    return all(f == i for f,i in zip(original_function_values, inverted_function_values))

if __name__ == "__main__":

    bits = 7
    body = x_body(bits)

    function_values = [
        1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0,
        1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1,
        0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0,
        1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1,
        0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1,
        1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1,
        0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0,
        1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1
    ]

    print("1. Fourier-Transformation wird berechnet...")
    fourier_transformed = [fourier_transform(a, function_values, body) for a in body]

    print("2. Inverse Fourier-Transformation wird berechnet...")
    inverted_values = [fourier_inversion(x, fourier_transformed, body) for x in body]

    print("3. Ergebnisüberprüfung...")
    is_correct = invasion_correct(function_values, inverted_values)

    if is_correct:
        print("Die Inversion stimmt mit den Originalwerten überein!")
    else:
        print("FEHLER: Die Inversion stimmt NICHT mit den Originalwerten überein!")
        print(f"{'x':<10} {'Original':>10} {'Invers':>10} {'OK?':>6}")
        print("-" * 40)
        for x, orig, inv in zip(body, function_values, inverted_values):
            status = "OK" if orig == inv else "FAIL"
            print(f"{bitV2str(x):<10} {orig:>10} {inv:>10} {status:>6}")

    # Optional: Nur nicht-null Fourier-Koeffizienten anzeigen
    print("\nNicht-null Fourier-Koeffizienten:")
    print(f"{'a':<10} {'TF[a]':>10}")
    print("-" * 25)
    for a, val in zip(body, fourier_transformed):
        if val != 0:
            print(f"{bitV2str(a):<10} {val:>10}")
