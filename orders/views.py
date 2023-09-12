from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrderForm
from .models import Order

# Create your views here.
def orders(request):
    
    return render(request, 'order.html',{})

def order(request):
    o_id = request.session.get('o_id')
    #request.session['o_id']= None
    #form = OrderForm.objects.o_id
    form = Order.objects.filter(order_id = o_id)
    print(str(form))


    #o_id = request.GET.get('o_id','')
    print(str(o_id))
    return render(request, 'order.html',{'form': form})
    #return render(request, 'order.html')