from django.http import HttpResponse
from django.shortcuts import render
from copy import deepcopy

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
}

def index(request, meal):
    servings = request.GET.get('servings', 1)
    recipe = deepcopy(DATA.get(meal))
    if recipe is not None:
        for item in recipe:
            recipe[item] *= int(servings)  
        context = {'recipe': recipe}
        return render(request, 'calculator/index.html', context)
    else:
        return HttpResponse('Такого рецепта нет')
