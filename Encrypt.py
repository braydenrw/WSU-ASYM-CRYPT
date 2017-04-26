from random import randint
from binascii import hexlify


class Encrypt:
    def __init__(self, ptext):
        self.ptext = ptext
        self.pub_key = ()
        self.facs = []
        self.main()

    def read_ptext(self):
        with open(self.ptext, 'r') as f:
            plain = f.read()
            f.close()

        return int(hexlify(plain), 16)

    def read_pub(self):
        with open('pubkey.txt', 'r') as f:
            self.pub_key = tuple(map(int, f.read().split(' ')))
            f.close()

    @staticmethod
    def write_ctext(c):
        with open('ctext.txt', 'w') as f:
            for item in c:
                f.write(str(item[0]) + ',' + str(item[1]) + ' ')
            f.close()
        print '\nSome encrypted output: \n', str(c[0:5])+'[...]', '\nThe rest may be viewed in \'ctext.txt\''

    def check_size(self, m):
        return True if m < self.pub_key[0] else False

    def encrypt(self, m):
        """
        Asymmetric encryption of binary data read from a text file.

        :param m: Integer representation of text.
        :return: Array of cipher text pairs.
        """
        p = self.pub_key[0]
        g = self.pub_key[1]
        e2 = self.pub_key[2]
        c = []

        loop = format(m, '0b')
        x = loop.__len__()
        if x % 32 != 0:
            x = x + 32 - x % 32
        loop = format(m, '0' + str(x) + 'b')
        length = format(p, '033b').__len__()
        if self.check_size(m):
            ind_arr = [1]
        else:
            ind_arr = [i for i in range(1, loop.__len__(), length - 1)]

        for i in ind_arr:
            k = randint(0, p)
            c1 = pow(g, k, p)
            c2 = (pow(e2, k, p) * int(loop[i - 1:i + length - 2], 2) % p) % p
            c.append((c1, c2))

        return c

    def main(self):
        self.read_pub()
        m = self.read_ptext()
        c = self.encrypt(m)
        self.write_ctext(c)
