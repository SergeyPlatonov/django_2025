from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from home.forms import AddressForm, PeopleSearchForm
from home.models.address import Address
from home.models.person import Person


# Create your views here.
class HomeView(TemplateView):
    template_name = "hello_world.html"

    # def get(self, request):
    #     context = {"username": "guy"}
    #     return render(request, "hello_world.html", context)

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context = {"username": "guy"}
        return context


# def list_people_view(request: HttpRequest) -> HttpResponse:
#     people_response = """
#     <h1>People</h1>
#         <ul>
#     """

#     people = Person.objects.all()
#     people = people.filter(address__province__iexact="ab")

#     for person in people:
#         people_response += f"<li>{person}</li>"

#     people_response += "</ul>"
#     return HttpResponse(people_response)


class PeopleView(ListView):
    paginate_by = 10
    model = Person

    def post(self, q: str, *args, **kwargs) -> HttpResponse:
        return render("hello_world.html")

    def get_queryset(self):
        query_set = super().get_queryset()
        query = self.request.GET.get("q")
        if query:
            query_set = query_set.filter(first_name=query)

        return query_set


class PersonDetailView(DetailView):
    model = Person


class AddressView(View):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        context = {"form": AddressForm()}
        return render(request, "address_form.html", context)

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        
        address = AddressForm(data=request.POST)
        # if address.is_valid():
        #     address.save()
        #     return render(request, "address_form.html", {"form": AddressForm(), "success": True})
        context = {"form": address}
        return render(request, "address_form.html", context)

class AddressListView(ListView):
    paginate_by = 20
    model = Address
    
class AddressDetailView(DetailView):
    model = Address

class AddressCreateView(CreateView):
    model = Address
    fields = ["street", "unit_number", "city", "province", "postal_code", "country"]

class AddressUpdateView(UpdateView):
    model = Address
    fields = ["street", "unit_number", "city", "province", "postal_code", "country"]

class AddressDeleteView(DeleteView):
    model = Address
    success_url = reverse_lazy["address_list"]
    
