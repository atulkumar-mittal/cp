def gen_sets(st, bag):
    if len(st) == 1:
        bag.append(st[0])
        return

    gen_sets(st[-len(st) + 1:], bag)
    #print("bag {}".format(bag))
    db = [st[0] + s for s in bag]  # append the first character in each string returned by child call
    db.append(st[0])  # append the first character in dummy bag
    #print("db {}".format(db))
    bag.extend(db)  # append this whole result with returned values
    #print("bag is : {}".format(bag))


b = []
gen_sets('abcde', b)
print(b)
