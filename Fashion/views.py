from django.shortcuts import render, get_object_or_404, redirect
from Fashion.models import vocalforlocal, vocalforlocal1, vocalforlocal2, shopclothing, shopfootwear, Budget_Add_Ons,shopBeauty
from maincontainer.models import CartItem
from django.http import HttpResponse
from decimal import Decimal,InvalidOperation
from mobileviews.models import bestseller,mainob
from HomeandKitchen.models import bedroom


def vocalforlocal13(request):
    allvocalforloacal = vocalforlocal.objects.all()
    allvocalforloacal2 = vocalforlocal2.objects.all()
    allvocalforloacal1 = vocalforlocal1.objects.all()
    allshopclothing = shopclothing.objects.all()
    allshopfootwear = shopfootwear.objects.all()
    allBudgetaddons = Budget_Add_Ons.objects.all()
    allshopbeauty = shopBeauty.objects.all()
   
    return render(request,'fashion.html',{
    'vocalforlocal':allvocalforloacal,
    'vocalforlocal1':allvocalforloacal1,
    'vocalforlocal2':allvocalforloacal2,
    'shopclothing':allshopclothing,
    'shopfootwear':allshopfootwear,
    'Budgetaddons':allBudgetaddons,
    'shopbeauty':allshopbeauty,
    })




#------------------------------------------------end for vocalforlocal2----------------------------------------------



def product_details_dynamic(request,product_type,product_id):
    model_map = {
        'shopclothing':shopclothing,
        'shopBudget':Budget_Add_Ons,
        'shopfootwear':shopfootwear,
        'shopBeauty':shopBeauty,
        'bestseller':bestseller,
        'bedroom':bedroom,
        'mainob':mainob,
    }

    content = ""
    imagemain = ""
    crazylower = ""
    term = ""

    model = model_map.get(product_type)
    if not model:
        return redirect('home')
    
    product = get_object_or_404(model,id=product_id)

    if product_type in ['shopclothing','shopBudget','shopfootwear','shopBeauty']:
        name = getattr(product,f"content{product_type}")
        price = getattr(product,f"price{product_type}")
        image = getattr(product,f"image{product_type}")

    elif product_type == 'bestseller':
        name = product.contentm
        price = product.pricewacth
        image = product.Imagem
    
    elif product_type == 'bedroom':
        name = product.content
        price = product.price
        image = product.image

    elif product_type == 'mainob':
        name = product.name
        price = product.startingprice
        image = product.image
        content = product.content
        imagemain = product.imagemain
        crazylower = product.crazylower
        term = product.term


    else:
        name,price,image = "unknown",0,0    

    context = {
        'product':product,
        'name':name,
        'price':price,
        'image':image,
        'product_type':product_type,
        'content':content,
        'imagemain':imagemain,
        'crazylower':crazylower,
        'term':term,
    }    
    return render(request,'product_detailsbedroom.html',context)













def add_to_cart_dynamic(request,product_type,product_id):
    model_map = {
        'shopclothing':shopclothing,
        'shopBudget':Budget_Add_Ons,
        'shopfootwear':shopfootwear,
        'shopBeauty':shopBeauty,
        'bestseller':bestseller,
        'bedroom':bedroom,
        'mainob':mainob,
    }
    model = model_map.get(product_type)
    if not model:
        return redirect("home")
    
    product = get_object_or_404(model,id = product_id)
    if product_type in ['shopclothing','shopBudget','shopfootwear','shopBeauty']:
        name = getattr(product,f"content{product_type}")
        price = getattr(product,f"price{product_type}")

    elif product_type == 'bestseller':
        name = product.contentm
        price = product.pricewacth

    elif product_type == 'bedroom':
        name = product.content
        price = product.price
    
    elif product_type == 'mainob':
        name = product.name
        price = product.startingprice

    else:
        name,price,image = "unknown",0,0    
    
    cart_item, created = CartItem.objects.get_or_create(
        product = None,
        content = name,
        price = price,
        off174 = 0,
        defaults={'quantity':1}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect(request.META.get('HTTP_REFERER','vocalforlocal'))    













def buy_now_dynamic(request, product_type, product_id):
    model_map = {
        'shopclothing': shopclothing,
        'shopBudget': Budget_Add_Ons,
        'shopfootwear': shopfootwear,
        'shopBeauty': shopBeauty,
        'bestseller':bestseller,
        'bedroom':bedroom,
        'mainob':mainob,
    }

    # ✅ Check model safely
    model = model_map.get(product_type)
    if not model:
        return redirect("home")

    # ✅ Fetch product
    product = get_object_or_404(model, id=product_id)

    if product_type in ['shopclothing','shopBudget','shopfootwear','shopBeauty']:
        name = getattr(product,f"content{product_type}")
        price_raw = getattr(product,f"price{product_type}")
        image = getattr(product,f"image{product_type}")


    elif product_type == 'bestseller':
        name = product.contentm
        price_raw = product.pricewacth
        image = product.Imagem

    elif product_type == 'bedroom':
        name = product.content
        price_raw = product.price
        image = product.image

    elif product_type == 'mainob':
        name = product.name
        price_raw = product.startingprice 
        image = product.image   
    
    else:
        name,price,image = "unknown",0,0     


    # ✅ Safe Decimal conversion
    try:
        price = Decimal(price_raw)
    except (InvalidOperation, TypeError, ValueError):
        price = Decimal(0)

    # ✅ Offer optional (since models don't have it)
    offer = Decimal(0)

    # ✅ Final price same as price (since no offer)
    final_price = price

    # ✅ Save clean values in session
    request.session['product_name'] = name
    request.session['product_price'] = str(price.quantize(Decimal('0.01')))
    request.session['product_offer'] = str(offer.quantize(Decimal('0.01')))
    request.session['product_final_price'] = str(final_price.quantize(Decimal('0.01')))

    # ✅ Optional: store user email
    if request.user.is_authenticated:
        request.session['user_email'] = request.user.email

    # ✅ Render template
    return render(request, "buy_now1.html", {
        "product": product,
        "name": name,
        "price": price,
        "offer": offer,
        "final_price": final_price,
        "image": image,
        "product_type": product_type,
    })