from django.forms import ModelForm, ImageField
from .models import Order

class OrderForm(ModelForm):
    BRANCH_CHOICES = (('k','Katipunan branch'), ('m', 'Makati branch'))
    class Meta:
        model = Order
        fields = ["product_name", "product_quantity", "branch_choice", 
        "user_name", "shipping_address", "phone_number"]