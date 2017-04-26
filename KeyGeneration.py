from random import randrange, seed, randint


def key_gen(s):
    """
    Wrapper for the actual prime number generator, this function writes the keys to their respective files
    after it's properly generated.

    :param s: Seed s is user input so the private and public keys are the same if the same seed is used
    """
    seed(s)
    p = select_prim()
    d = randint(1, p)
    e2 = pow(2, d, p)
    with open('pubkey.txt', 'w') as pub_txt, open('prikey.txt', 'w') as pri_txt:
        pub_txt.write(str(p) + ' 2 ' + str(e2))
        pri_txt.write(str(p) + ' 2 ' + str(d))
        pub_txt.close(), pri_txt.close()

    print 'public key:  (', p, 2, e2, ')'
    print 'private key: (', p, 2, d, ')'


def check_prim(q):
    """
    Checks if the generated q results in a coinciding prime p that can be used for key generation.

    :param q: Generated 31 bit prime with the high bit on.
    :return p: p = 2q + 1 if p is also prime return otherwise select_prim for a new q
    """
    p = 2 * q + 1
    if is_prim(p, 5):
        return p
    else:
        return select_prim()


def select_prim():
    """
    Generates a random 31 bit integer q, where 2 is a primitive root of q.  Then calls check_prim(q)
    to see if there is a correlating p prime.

    :return: Returns check_prim() result, see docstring for more info.
    """
    min_num = 2147483648
    max_num = 4294967296

    q = randint(min_num, max_num)
    if q < min_num:
        q += min_num
    while q > max_num:
        q //= 2

    while q < max_num:
        if is_prim(q, 5) and q % 12 == 5:
            return check_prim(q)
        q += 1
        if q >= max_num:
            q = min_num  # Just in case random generates after the last prime in the list


def is_prim(n, k):
    """
    Rabin-Miller primality checker for large numbers since the numbers are fairly large.

    :param n: Prime number to be checked.
    :param k: Number of checks in Rabin-Miller.
    :return: True or False if the number is probably prime or not.
    """
    if n % 2 == 0:
        return False
    r, s = 0, n - 1
    while s % 2 == 0:
        s //= 2
        r += 1

    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue

        for _i in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True
