# sorting version numbers (i.e. 1.011.2, 5.4)
def order(l):
    return sorted(l, key = lambda s: len and list(map(int, s.split('.'))), reverse=False)
test = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
test1 = {"1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"}
print(order(test1))
