from django.shortcuts import render, redirect
from django.test import Client
from .models import Questionnaire
from .forms import CreateQuestionnaireForm, QuestionnaireBasicForm, QuestionnaireInjuryForm

def home(request):
    return render(request, 'home.html',{})

def questionnaire(request):
    
    if request.user.is_authenticated:
        if request.method == "POST":
            form = CreateQuestionnaireForm(request.POST)
            task = form.save(commit=False)
            task.user_email = request.user.email

            return redirect('questionnaire_basic') 

                
        else:
            form = QuestionnaireBasicForm()
        context = {'form' : form}
        return render(request, 'questionnaire.html', context)
    else: 
        return redirect('accounts/login')
    
    

def questionnaire_basic(request):
    
    if request.user.is_authenticated:
        if request.method == "POST":
            form = QuestionnaireBasicForm(request.POST)
            task = form.save(commit=False)
            
            task.save()

            #print("id: "+ str(form.instance.pk))
            if task.injury == True:
                request.session['que'] = form
                return redirect('questionnaire_injury') 
            
            
        else:
            form = QuestionnaireBasicForm()

        context = {'form' : form}

        return render(request, 'questionnaire_basic.html', context)
    else: 
        return redirect('accounts/login')
    
    
def questionnaire_injury(request):
    
    #que = request.session.get('que', None)

    if request.user.is_authenticated:
        if request.method == "POST":
            form = QuestionnaireInjuryForm(request.POST)
            #obj = Questionnaire.objects.filter(pk="pk")

            form.save()
            #print("obj: "+ str(obj))
        else:
            form = QuestionnaireInjuryForm()
        context = {'form' : form}
        return render(request, 'questionnaire_injury.html', context)
    else: 
        return redirect('accounts/login')
    