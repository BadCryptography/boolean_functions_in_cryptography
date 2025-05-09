
from util import character, x_body, bitV2str, bitV2int

def fast_fourier_transformation(a, fvals, body):

    #separate x into two sets
    #first contains all strings that end in 0
    #second contains all strings that end in 1
    x_zero_last = []
    x_one_last = []
    fvals_for_zero_last = []
    fvals_for_one_last = []

    a_rest = a[:-1]

    for x, f in zip(body, fvals):
        if x[-1] == 0:
            x_zero_last.append(x)
            fvals_for_zero_last.append(f)
        else:
            x_one_last.append(x)
            fvals_for_one_last.append(f)

    result_zero_sum = sum([fval*character(a_rest,x[0:-1]) for x,fval in zip(x_zero_last,fvals_for_zero_last)])
    result_one_sum = ((-1)**a[-1])*sum([fval*character(a_rest,x[0:-1]) for x,fval in zip(x_one_last,fvals_for_one_last)])
    return result_zero_sum+result_one_sum


#computes all coefficients
#this code is produced by ChatGPT
def fastest_fourier_transformation(fvals:list[int])->list[int]:
    n = len(fvals)
    if n == 1:
        return fvals.copy()  # Basisfall: nur ein Wert
    
    half = n // 2
    left = fastest_fourier_transformation(fvals[:half])   # rekursiv linke Hälfte
    right = fastest_fourier_transformation(fvals[half:])  # rekursiv rechte Hälfte

    result = [0] * n
    for i in range(half):
        result[i] = left[i] + right[i]
        result[i + half] = left[i] - right[i]
    
    return result
