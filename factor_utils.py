#factor_utils.py

def factorize(n):
    #Function to find factorization of a number
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i, n // i
        return None, None
