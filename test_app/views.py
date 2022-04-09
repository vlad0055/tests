from django.views.generic import ListView
from . models import Test_data



class Test_data(ListView):
    model = Test_data
    template_name="show_all_tests.html"
    context_object_name = 'test'
