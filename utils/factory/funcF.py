from random import randint


def rand_ratio():
    return randint(840, 900), randint(473, 573)


def make_recipe():
    return
    {
        'title': 'Teste',
        'description': 'asdaysdhuasdhuahsduhasudh',
        'preparation_time': 16,
        'preparation_time_unit': 'Minutos',
        'servings': 5,
        'servings_unit': 'Porção',
        'preparation_steps': 'asdhasudhAHSUDHAUSDUAHSuhausdhuashduahsudhuashd',
        'created_at': '20-02-1996',
        'author': {
            'first_name': 'Reizon',
            'last_name': 'Teste'
        },
        'category': {
            'name': 'Merenda'
        },
        'cover': {
            'url': 'https://loremflickr.com/%s/%s/food,cook' % rand_ratio(),
        },
    }
