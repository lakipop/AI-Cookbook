movies={"Action": ["Die Hard", "Mad Max: Fury Road", "John Wick"],
        "Comedy": ["The Hangover", "Superbad", "Step Brothers"],
        "drama":["Shawshank Redemption", "Forrest Gump", "The Godfather"]}

genre= input("Enter a genre: ")
def filtergenre(genre):
        if genre not in movies:
                print("Invalid genre")
        else:
                for movies in movies[genre]:
                        print(movies)
print("--- Recommended Movies ---")
filtergenre(genre)

import pandas as pd




def formula(a,b,c,d):
    formula1= a or b
    formula2= not b and c
    formula3= formula1 and formula2
    return formula3

    values = [0,1]
    data = []
    for a in values:
        for b in values:
            for c in values:
                for d in values:
                    result = formula(a,b,c,d)
                    data.append({'a': a, 'b': b, 'c': c, 'd': d, 'result': result})
                    print(f"a: {a}, b: {b}, c: {c}, d: {d} => Result: {result}")

                df = pd.DataFrame(data)
                df = df.set_index(['a', 'b', 'c', 'd'])
                print(df)






