# Sada govorimo o naprednijim funkcijama
def func(name, cypher = '000'):
    print(name, cypher)

    if cypher == '123':
        print('Kartica je 123')
    else:
        print('Sifra nije 123')

func('mladen', '124')