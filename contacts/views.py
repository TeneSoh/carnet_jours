from django.forms import ValidationError
from django.shortcuts import get_object_or_404, redirect, render
from .models import Contact
from .forms import ContactForm


# Create your views here.
def index(request):
    contacts = Contact.objects.all()
    return render(request=request, template_name='contacts/contacts.html',context= {'contacts': contacts} )

def store(request):
    forms = ContactForm()
    if(request.method == 'POST'):
        try:
            print(f'{request.POST['nom']}')
            forms = ContactForm(request.POST)
            print(forms.is_valid())
            if forms.is_valid():
                # print("is valid")
                forms.save()
                # Contact.objects.create(
                #     # nom = request.POST['nom'],
                #     # prenom = request.POST['prenom'],
                #     # email = request.POST['email'],  
                #     # phone = request.POST['phone'],

                #     # utilisation de la classe ContactsForm
                #     nom = forms.cleaned_data.get('nom'),
                #     prenom = forms.cleaned_data.get('prenom'),
                #     email = forms.cleaned_data.get('email'),
                #     phone = forms.cleaned_data.get('phone'),
                # )
                return redirect('contacts')
        except ValidationError:
            print("except")
            print(forms.errors)
            return render( request, 'contacts/contacts.html', {'forms': forms})
        # contacts = Contact.objects.all()
        # print(contacts[0].nom)

    
    return render(request, 'contacts/createContact.html', {'forms': forms})

def edite(request, id:int):
    contact = get_object_or_404(Contact, id = id)
    if request.method == 'POST':
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        email = request.POST['email']
        phone = request.POST['phone']

        contact.nom = nom
        contact.prenom = prenom
        contact.email = email
        contact.phone = phone

        contact.save()

        return redirect('contacts')


    return render(request, 'contacts/editContact.html', {'contact':contact})
        

def delete(request, id:int):
    try:
        contact = get_object_or_404(Contact, id = id)
        print(contact)
        contact.delete() 
            
        return redirect('contacts')
    except Exception as e:
        message = e
        return render(request, 'contacts', {'message':message})


def show(request, id):
    contact = get_object_or_404(Contact, id = id)

    return render(request, 'contacts/showdetail.html', {'contact': contact})

    
