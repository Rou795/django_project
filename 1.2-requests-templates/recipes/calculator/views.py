from django.shortcuts import render, reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'yakisoba': {
        'удон, г': 200,
        'лук, шт.': 1,
        'морковь, шт.': 0.5,
        'курица, г': 0.5,
        'соевый соус, ст.л.': 2,
        'устричный соус, ст.л.': 2
    }
}
RECIPETES = {'omlet': 'Омлет', 'pasta': 'Паста', 'buter': 'Бутерброд', 'yakisoba': 'Якисоба'}


def home_view(request):
    pages = {}
    for key in DATA:
        pages[RECIPETES[key]] = reverse(key)
    context = {
        'pages': pages
    }
    return render(request, 'home.html', context)


def get_recipe(request):
    recipe = DATA[request.path.strip('/')]
    num = int(request.GET.get('servings', 1))
    for key in recipe:
        recipe[key] *= num
    context = {'recipe': recipe,
               'name': RECIPETES[request.path.strip('/')]}
    return render(request, 'calculator/index.html', context)

