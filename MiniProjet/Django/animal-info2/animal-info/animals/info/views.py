from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import AddAnimalForm
from .models import Animals, Family
from django.views import generic

#generic ListView : do a query all in the model specified
class AnimalIndex(generic.ListView):
    template_name = 'animal_s.html'
    model = Animals #it's like executing the command Animals.objects.all()

#generic CreateView : create a new instance of the model with data
# coming from the form and save it
class AddAnimals(generic.CreateView):
    template_name = 'add_animal.html' #the template to render
    form_class = AddAnimalForm  # AddAnimalForm we created earlier in forms.py

    def form_valid(self, form): #will check if our form is valid and save the data
        post_to_add = form.cleaned_data
        print(post_to_add)
        return super().form_valid(form)

    # Create your views here.
def home(request):
    all_animals= Animals.objects.all() #query to get all the animals instances in my Animals table
    if request.method == 'POST': #necessary to get data from the user
        #We are inside the post http method
        print('in_post')
        #we fetch the user search with the value of the input's atribute name (animal-searcg)
        search_result = request.POST.get('animal-search')
        print(search_result)
        #we filter animals instances that corresponds to the user searc text
        animal_searched = Animals.objects.filter(name__contains = search_result.title())
        return render(request, 'home.html', {'animals':animal_searched,
                                             'search' : search_result} )
    return render(request, 'home.html', {'animals':
                                         all_animals})


def family(request, X):
    family_object = Family.objects.filter(id=X).first() #method first() is used to get the first match in the queryset, since filter return a queryset (a list)
    print(family_object)
    animal_in_family= Animals.objects.filter(family_id=X)
    return render(request, 'home.html', {'animals':animal_in_family,
                                         'family': family_object})

def animal(request, id):
    animal = Animals.objects.get(id=id)
    print(animal.name, animal.legs, animal.family.name)
    #animal = Animals.objects.filter(id=id).first()

    return render(request, 'animal.html', {'a':animal})

def add_animal(request):
    if request.method == 'POST':
        print('in post')
        add_form = AddAnimalForm(request.POST, request.FILES)
        if add_form.is_valid():
            print('in valid')
            new_animal = add_form.save() #we can use the save method directly on the form because it comes from modelForm and it creates a new animal instance
            messages.success(request, f'New Animal {new_animal.name} saved')
            return redirect('home')
    else:
        add_form = AddAnimalForm()
        return render(request, 'add_animal.html', {'form_a':add_form})


def buy(request, id):
    animal = Animals.objects.get(id=id) #first we get the animal the user wants to buy
    animal.owner.set([request.user]) # we set the current user to be the owner of this animal
    messages.success(request, 'Animal ajouté à votre panier')
    return redirect('home')

def show_panier(request):
    #we want to filter all the animals owned by the current user
    animals_inside_cart = Animals.objects.filter(owner=request.user)
    return render(request, 'panier.html', {'animals': animals_inside_cart})