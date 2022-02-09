from django import forms

class AddRentalForm(forms.Form):
    customer_id = forms.IntegerField(label='Enter the customer id')
    vehicle_id = forms.IntegerField()
