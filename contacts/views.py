from django.shortcuts import get_object_or_404, redirect, render
from .models import Contact
from .forms import ContactForm
from django.views.generic import ListView , View , CreateView , UpdateView , DeleteView , DetailView
from django.forms import ValidationError
from django.urls import reverse_lazy

# from carnet_jours.contacts.models import Contact
# from carnet_jours.contacts.forms import ContactForm
# Create your views here.

# def index(request):
#     contacts = Contact.objects.all()
#     return render(request=request, template_name='contacts/contacts.html',context= {'contacts': contacts} )


# lister la view contact avec la methode des classe 

class ListContactView(ListView):
    model = Contact
    template_name = 'contacts/contacts.html' 
    context_object_name = "contacts"

# def store(request):
#      forms = ContactForm()    
#      if(request.method == 'POST'):
#             forms = ContactForm(request.POST)
#             if forms.is_valid():
#                 forms.save()

#                 # Contact.objects.create(
#                 #     # nom = request.POST['nom'],
#                 #     # prenom = request.POST['prenom'],
#                 #     # email = request.POST['email'],
#                 #     # phone = request.POST['phone']

#                 #     # une autre facon de faire en utilisant la classe ContacForm

#                 #     nom = forms.cleaned_data.get('nom'),
#                 #     prenom = forms.cleaned_data.get('prenom'),
#                 #     email = forms.cleaned_data.get('email'),
#                 #     phone =forms.cleaned_data.get('phone'),
#                 # )


#             return render( request, 'contacts/contacts.html' )

#      return render(request, 'contacts/createContact.html' ,  {'forms': forms})




# storecontact la view contact avec la methode des classe 

# class StoreContact(View):
#     def get(self , request):
#         forms = ContactForm
#         return render(request, 'contacts/createContact.html' ,  {'forms': forms})
    
#     def post(self , request):
#         try:
#             forms = ContactForm(request.POST)
#             if forms.is_valid():
#               forms.save()
#               return redirect("contacts")
#         except ValidationError:
#             return render(request , 'contacts/contacts.html' , {'forms': forms})   

class CreateContacView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contacts/createContact.html'
    success_url = reverse_lazy('contacts')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['forms'] = ContactForm()
        return context








# def edite(request, id:int):
#     contact = get_object_or_404(Contact, id = id)
#     if request.method == 'POST':
#         nom = request.POST['nom']
#         prenom = request.POST['prenom']
#         email = request.POST['email']
#         phone = request.POST['phone']

#         contact.nom = nom
#         contact.prenom = prenom
#         contact.email = email
#         contact.phone = phone

#         contact.save()

#         return redirect('contacts')


#     return render(request, 'contacts/editContact.html', {'contact':contact})


class UpdateContactView(UpdateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contacts/editContact.html' 
    context_object_name = 'contact' 
    success_url = reverse_lazy('contacts')  

# def delete(request, id:int):
#     try:
#         contact = get_object_or_404(Contact, id = id)
#         print(contact)
#         contact.delete() 
            
#         return redirect('contacts')
#     except Exception as e:
#         message = e
#         return render(request, 'contacts', {'message':message})

class DeleteContactView(DeleteView):
    model = Contact
    template_name = "contacts/contact_list.html"
    success_url = reverse_lazy('contacts')


# def show(request, id):
#     contact = get_object_or_404(Contact, id = id)

#     return render(request, 'contacts/showdetail.html', {'contact': contact})


class DetailContactView(DetailView):
    model = Contact
    template_name='contacts/showdetail.html'
    context_object_name = 'contact'

    
