import random
import string
char_set = string.ascii_uppercase + string.digits
yoyo = ''.join(random.sample(char_set*6, 6))
print(yoyo)