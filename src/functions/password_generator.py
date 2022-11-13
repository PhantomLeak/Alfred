import random
import string
import alfred as af 

def create_password(pLen):

    words = string.ascii_letters + string.digits + string.punctuation

    result_str = ''.join(random.choice(words) for i in range(pLen))
    print(f'\nHere is you {pLen} digit password: {result_str}\n')
    af.alfred_main(1)

