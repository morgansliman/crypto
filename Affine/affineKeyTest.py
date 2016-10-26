# This program proves that the keyspace of the affine cipher is limited
# to len(SYMBOLS) ^ 2.

import affineCipher, cryptoMath

message = 'Make things as simple as possible, but not simpler.'
for keyA in range(2, 100):
    key = keyA * len(affineCipher.SYMBOLS) + 1

    if cryptoMath.gcd(keyA, len(affineCipher.SYMBOLS)) == 1:
        print(keyA, affineCipher.encryptMessage(key, message))
        
