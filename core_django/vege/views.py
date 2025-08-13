from django.shortcuts import render, redirect
from vege.models import Recipe

def add_recipe(request):
    if request.method == "POST":
        recipe_name = request.POST.get("recipe_name")
        recipe_description = request.POST.get("recipe_description")
        recipe_image = request.FILES.get("recipe_image")

        Recipe.objects.create(
            recipe_name=recipe_name,
            recipe_description=recipe_description,
            recipe_image=recipe_image
        )

        return redirect('/recipe/') 

    recipes = Recipe.objects.all()
    return render(request, 'Recipe.html', {"recipes": recipes})
