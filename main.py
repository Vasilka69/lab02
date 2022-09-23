def simple(n):
    sieve = list(range(n + 1))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(2*i, len(sieve), i):
                sieve[j] = 0
    return sieve

def main():
    print(simple(15))

main()