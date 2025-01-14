def tower_builder(n_floors):
    floors = []
    total = n_floors * 2 - 1
    for i in range(n_floors):
        stars = i * 2 + 1
        space = (total - stars) // 2 if (total - stars) / 2 > 0 else 0
        floors.append(" " * space + "*" * stars + " " * space)
    return floors


if __name__ == "__main__":
    assert tower_builder(1) == ['*', ]
    assert tower_builder(2) == [' * ', '***']
    assert tower_builder(3) == ['  *  ', ' *** ', '*****']
