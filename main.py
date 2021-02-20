from blockchain import Blockchain


if __name__ == '__main__':
    blockchain = Blockchain()

    new = input('Qual a menssagem do primeiro bloco: ')
    blockchain.add_new_block(new)

    new2 = input('Qual a menssagem do segundo bloco: ')
    blockchain.add_new_block(new2)

    new3 = input('Qual a menssagem do terceiro bloco: ')
    blockchain.add_new_block(new3)

    ask = input('Gostaria de ver todos os blocos? ')

    if ask == 'sim' or 'Sim':
        print(blockchain.get_all())
        print('\nFim.')
    else:
        print('FIm.')