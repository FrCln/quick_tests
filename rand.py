seed = 42
p = 2**127 - 1
m = 254287
hash_ = [seed] * 20
for i in range(1, 20):
    hash_[i] = hash_[i-1] * p % m
    print(hash_[i])