#factors.py

import sys

def factorize(n):
    #Function to find factorization of number
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i, n // i
        return None, None

def main():
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r') as file:
            for line in file:
                #convert the line to an integer
                n = int(line.strip())

                #find factorization
                factor1, factor2 = factorize(n)

                #print the result
                print(f"{n}={factor1}*{factor2}")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)

if __name__ == "__main__":
    main()
