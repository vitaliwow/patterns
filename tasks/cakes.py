def cakes(recipe, available):
    min_cakes = []
    for k, v in recipe.items():
        if k not in available:
            return 0
        min_cakes.append(available[k] // v)
    return min(min_cakes)


if __name__ == "__main__":
    print(cakes({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100},  {"sugar": 500, "flour": 2000, "milk": 2000}))
