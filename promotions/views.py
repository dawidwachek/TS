from django.shortcuts import render, redirect
from .models import Reflink




def reflink(request, ref_id):
    reflink_uses = Reflink.objects.filter(reflink_id = ref_id)
    if reflink_uses:
        #print('True')
        reflink_id = Reflink.objects.get(reflink_id = ref_id).uses_reflink
        reflink_uses = Reflink.objects.filter(reflink_id = ref_id)
        reflink_uses.update(uses_reflink = reflink_id + 1)
        reflink_id = Reflink.objects.get(reflink_id = ref_id).uses_reflink
    


    return redirect('home')
    #return render(request, 'home.html',{})