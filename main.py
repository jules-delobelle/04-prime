"""A program for prime verifications"""

from math import sqrt

#### Fonction secondaire


def isprime(p):
    """
    This function tell if a number is prime or not

    Args:
        p (int): the number to be verified

    Returns:
        premier (bool): true if p is prime, false otherwise

    """
    premier = True
    if p == 1:
        premier = False
    else:
        for k in range(2, int(sqrt(p)+1)):
            if p % k == 0:
                premier = False
                break

    return premier

#### Fonction principale


def main():
    """
    Main function, execute different tests
    """
    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
