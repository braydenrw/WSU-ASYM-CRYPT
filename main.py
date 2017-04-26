import KeyGeneration
from Encrypt import Encrypt
from Decrypt import Decrypt
from os import path
from types import IntType


if __name__ == '__main__':
    p_file = 'ptext.txt'
    c_file = 'ctext.txt'

    if not path.exists('./pubkey.txt') or not path.exists('./prikey.txt'):
        print 'Public or private key not found',
        try:
            sd = input('generating keys, enter a seed: ')
            assert type(sd) is IntType, 'Seed is not an integer: %r' % sd
            KeyGeneration.key_gen(sd)
            print 'Generation done written in \'pubkey.txt\' and \'prikey.txt\''
        except NameError, e:
            print 'Incorrect input, seed is not an integer'
            exit(e)

    encrypt = raw_input('Encrypting or decrypting [e/d]: ')
    if encrypt == 'e':
        assert path.exists('./' + p_file), 'ptext.txt does not exist'
        Encrypt(p_file)
    elif encrypt == 'd':
        assert path.exists('./' + c_file), 'ctext.txt does not exist'
        Decrypt(c_file)
    else:
        print 'Invalid input'
