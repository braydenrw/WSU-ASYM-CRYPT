class Decrypt:
    def __init__(self, ctext):
        self.ctext = ctext
        self.pub_key = ()
        self.pri_key = ()
        self.main()

    def read_ctext(self):
        with open(self.ctext, 'r') as f:
            plain = f.read()
            f.close()

        plain = plain[:-1]
        c = plain.split(' ')
        for i in range(0, c.__len__()):
            c[i] = tuple(map(int, c[i].split(',')))

        return c

    def read_keys(self):
        with open('pubkey.txt', 'r') as pub_txt, open('prikey.txt', 'r') as pri_txt:
            self.pub_key = tuple(map(int, pub_txt.read().split(' ')))
            self.pri_key = tuple(map(int, pri_txt.read().split(' ')))
            pub_txt.close(), pri_txt.close()

    @staticmethod
    def write_dtext(m_bin):
        m_hex = format(int(m_bin, 2), 'x')
        if m_hex.__len__() % 2 != 0:
            m_hex = format(int(m_hex, 16), '0' + str(m_hex.__len__() + 1) + 'x')
        with open('dtext.txt', 'w') as f:
            m = m_hex.decode('hex')
            f.write(m)
            f.close()
        print '\nSome output:\n', m[0:60]+'[...]', '\nThe rest may be viewed in \'dtext.txt\''

    def decrypt(self, c):
        """
        Asymmetric decryption of cipher text pairs.

        :param c: Array of cipher text pairs
        :return: Binary representation of decrypted cipher blocks.
        """
        p = self.pri_key[0]
        d = self.pri_key[2]
        m_bin = ''
        for pair in c:
            m_bin += format((pow(pair[0], p - 1 - d, p) * pair[1] % p) % p, '032b')
        return m_bin

    def main(self):
        self.read_keys()
        c = self.read_ctext()
        m_bin = self.decrypt(c)
        self.write_dtext(m_bin)
