from django.shortcuts import render, render_to_response, redirect, RequestContext
from django.http import HttpResponse
from people.forms import PeopleForm, ContactForm, BaseContactFormSet
from django.forms.formsets import formset_factory
from people.models import People, PastHistory, Contact
from django.contrib import messages

# Create your views here.


def register(request):
    ContactFormSet = formset_factory(ContactForm, formset=BaseContactFormSet)

    if request.method == 'POST':
        people_form = PeopleForm(request.POST)
        contact_formset = ContactFormSet(request.POST)       

        if people_form.is_valid() and contact_formset.is_valid():
            people_cleaned = people_form.cleaned_data

            # create user
            __people = People.objects.create(
                name=people_cleaned['name'],
                gender=people_cleaned['gender'],
                birthday=people_cleaned['birthday'],
                age=people_cleaned['age'],
                identity_number=people_cleaned['identity_number'],
                phone=people_cleaned['phone'],
                address=people_cleaned['address'],
                average_monthly_income=people_cleaned['average_monthly_income'],
                weight = people_cleaned['weight'],
                blood_type = people_cleaned['blood_type'],
                hospital_records = people_cleaned['hospital_records'],
                complaint = people_cleaned['complaint'],
                food_allergy_history = people_cleaned['food_allergy_history'],
                medicine_allergy_history = people_cleaned['medicine_allergy_history']
            )

            # create contact
            for contact_form in contact_formset:
                name = contact_form.cleaned_data.get('name')
                phone = contact_form.cleaned_data.get('phone')

                if name and phone:
                    __contact = Contact.objects.create(
                        name=name,
                        phone=phone,
                        people=__people
                    )

            # create people and past history relationship
            past_historys = people_cleaned['past_history']
            for i, past_history in enumerate(past_historys):
                    db_past_history = PastHistory.objects.get(id=past_history.id)
                    db_past_history.people.add(__people)

            if __people:
                messages.success(reques, '市民資料已成功登載')
                #return redirect('register', {'messages': messages})
                return render_to_response("people/register.html", context_instance=RequestContext(request))
        else:
            pass
    elif request.method == 'GET':
        people_form = PeopleForm()
        contact_formset = ContactFormSet
    return render(request, 'people/register.html', {'people_form': people_form, 'contact_formset': contact_formset})
