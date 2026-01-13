from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.template.context_processors import request
from .models import Contact
# Create your views here.
def index(request):
    contacts = Contact.objects.all()
    return render(request=request, template_name='contacts/contacts.html',context= {'contacts': contacts} )

def store(request):
    if(request.method == 'POST'):
        file = request.FILES.get('image')
        Contact.objects.create(
            nom = request.POST['nom'],
            prenom = request.POST['prenom'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            image =  file
        )

        contacts = Contact.objects.all()
        return redirect('contacts')
        # return render( request, 'contacts/contacts.html',  {'contacts': contacts})

    
    return render(request, 'contacts/createContact.html')

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

    
