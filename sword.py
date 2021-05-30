import random

class Sword:
    __sword_types = {
        'invalid': ([0, 0, 0, 0], [0, 0, 0, 0]),
        'tantou': ([50, 50, 50, 50], [699, 399, 999, 999]),
        'wakizashi': ([100, 100, 100, 100], [499, 499, 999, 999]),
        'uchigatana': ([100, 200, 200, 50], [999, 999, 999, 999]),
        'tachi': ([300, 350, 300, 350], [999, 999, 999, 999]),
        'ootachi': ([500, 600, 500, 200], [899, 899, 799, 599]),
        'naginata': ([400, 500, 700, 700], [699, 799, 799, 799]),
        'yari': ([400, 50, 500, 500], [699, 399, 799, 799]),
    }

    def __init__(self, _type='tachi'):
        if _type not in Sword.__sword_types:
            _type = 'invalid'
        self.__min_res, self.__max_res = Sword.__sword_types[_type]
    
    def make_recipe(self):
        recipe = (random.randint(a, b) for (a, b) in zip(self.__min_res, self.__max_res))
        return recipe
    
    @staticmethod
    def make_spinner():
        return sorted(Sword.__sword_types.keys())

if __name__ == '__main__':
    sword = Sword('tachi')
    print('Charcoal: {}\tSteel: {}\nCoolant: {}\tWhetstone: {}'.format(*(sword.make_recipe())))

    print(Sword.make_spinner())