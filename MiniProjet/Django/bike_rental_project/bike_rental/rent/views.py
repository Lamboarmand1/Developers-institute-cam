from django.shortcuts import render, redirect
from .models import *
from .forms import AddRentalForm
from django.contrib import messages

# Create your views here.
def show_rental(request):
    all_rentals = Rental.objects.all().order_by('rental_date')
    return render(request, 'rental.html', {'rentals':all_rentals})

def show_rental_details(request, pk):
    rental = Rental.objects.get(id=pk)
    return render(request, 'rental_details.html', {'rent':rental})

def add_rental(request):
    form = AddRentalForm()
    if request.method == 'POST':
        form = AddRentalForm(request.POST)
        if form.is_valid():
            cust_id = form.cleaned_data['customer_id']
            v_id = form.cleaned_data['vehicle_id']
            try:
                customer = Customer.objects.get(id=cust_id)
            except:
                messages.error(request, 'Bad customer id')
            else:
                try:
                    vehicle = Vehicle.objects.get(id=v_id)
                except:
                    messages.error(request, 'Bad Vehicle id')
                else:
                    if vehicle.return_date:
                        new_rental = Rental(customer_id= cust_id, vehicle_rent_id=v_id)
                        new_rental.save()
                return redirect('/rent/rental')
    return render(request, 'add_rental.html', {'form':form})

def show_customer(request):
    all_customers = Customer.objects.all().order_by('firstname')
    return render(request, 'customers.html', {'customers':all_customers})

def show_customer_details(request, pk):
    customer = Customer.objects.get(id=pk)
    return render(request, 'customer_details.html', {'customer':customer})

