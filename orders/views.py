from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrderForm
from .models import Order
from scripts.payment import Payment
from scripts.bot import OrderBot

# Create your views here.
def orders(request):
    
    return redirect('profile')

def order(request, order_id):
    
    

    if Order.objects.get(order_id=order_id).email_adress == request.user.email:
        if Order.objects.get(order_id=order_id).visible == False:
            return redirect('error')
        
        form = Order.objects.filter(order_id = order_id)
        #print('order site')
        price = 100
        if request.method == "POST":
            pay = Payment(price=price, user_email=request.user.email, order_id=order_id)
            if pay == 'payment_accepted':

                
                form.update(order_status = "PA")
                OrderBot(order_id=order_id, user_email=request.user.email, pay_price=price)
                return redirect('paymentsuccess')
            
        else:
            pass
        return render(request, 'order.html',{'form': form})
    
    if request.user.is_admin:
        form = Order.objects.filter(order_id = order_id)
        return render(request, 'order.html',{'form': form})
    else:
        return redirect('error')
    
    

def payment_success(request):
    return render(request, 'payment_success.html', {})
