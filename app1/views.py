from django.shortcuts import render
from .models import *

def qidirish(request):
    if request.method == 'POST':
        soz=request.POST['q_soz']
        soz1=Soz.objects.filter(soz=soz)
        if len(soz1)>0:
            b=N_soz.objects.filter(soz_id=soz1[0])
            return render(request,'result.html',{'soz':soz1[0],'n_soz':b})
        else:
            b=N_soz.objects.filter(n_soz=soz)
            # return render(request,'result.html',{'soz':t_soz[0],'n_soz':b})
            if len(b) > 0:
                t_soz = Soz.objects.filter(id=b[0].soz_id.id)
                b = N_soz.objects.filter(soz_id=t_soz[0])
                return render(request, 'result.html', {'soz': t_soz[0], 'n_soz': b})
            else:
                return render(request,'result.html',{'soz':"Bizning bazada bumday so`z yo`q"})
        # else:
        #     xato="Bu so`z bizning bazada yo`q"
        #     return render(request,'result.html',{'B_xato':xato})
    return render(request, 'result.html')
    # if request.method != 'POST':
    #     soz69 = request.POST['qn_soz']
    #     soz1 = N_soz.objects.filter(soz=soz69)
    #     c = Soz.objects.filter(soz_id=soz1[0])
    #     return render(request, 'result.html', {'soz': soz1[0], 'n_soz': c})
# def qidirish_n(request):
#     if request.method == 'POST':
#         n_soz=request.POST['q_soz']
#         soz1=N_soz.objects.filter(soz=n_soz)
#
#         return render(request,'result.html',{'soz':soz1[0]})
#     return render(request, 'result.html')
# Create your views here.
