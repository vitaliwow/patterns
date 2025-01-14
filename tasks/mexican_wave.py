def wave(people):
    return [people[:pos] + p.capitalize() + people[pos + 1:] for pos, p in enumerate(people) if p.isalpha()]

if __name__ == "__main__":
    # print(wave("hello"))
    print(wave("two words"))