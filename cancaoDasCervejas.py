word = "garrafas"

for beer_num in range(10, 0, -1):
    print(beer_num, word, "de cerveja na prateleira.")
    print(beer_num, word, "de cerveja.")
    print("Pega uma e...")
    print("Passa pra cá!")
    print()
    if beer_num == 1:
        print("Acabou as cervejas da prateleira... :(")
    else:
        new_num = beer_num - 1
        if new_num == 1:
            word = "garrafa"
        print(new_num, word, "de cerveja na prateleira.")
    print()