from django.shortcuts import render
from .models import*
# Create your views here.

def index(request):  #render oluşturmak demek,request ise ilk parametresi
    urunler=Urunler.objects.all() #urunler isminde bir değişken oluşturduk ve urunler tablosundaki tüm verileri aldık.veri tabanındaki herürün satırı aslında bir objedir.
    print(urunler)
    context={
        'urunler':urunler #burada context deme sebebi renderda üçüncüde kendi context dediği için bizde context dedik ürünlerimizi yolladık artık htmlde urunler olarak kullanacağız.
    }
    return render(request,"index.html",context)#index.html sayfasını açmak için render kullandık.Context olarak değerlerimizi html'e yolladıık.


def detay(request,id):
    urun=Urunler.objects.filter(id=id)
    context={
        "urun":urun
    }
    return render(request,'detay.html',context)