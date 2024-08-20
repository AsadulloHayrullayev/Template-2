from django.shortcuts import render

def menu_view(request):
    menu_items = [
        {"name":"Home","url": "index", "active":True},
        {"name":"Company","url": "index", "active":False},
        {"name":"About","url": "index", "active":False},
        {"name":"Subscription","url": "index", "active":False},
        {"name":"Contact","url": "index", "active":False},
    ]
    return {'menu_items': menu_items}

def holder_view(request):
    holder_items = [
        {
            "name":"Riding Mountain Bike",
            "info":"Aenean cursus imperdiet nisl id fermentum. Aliquam pharetra dui laoreet vulputate dignissim. Sed id metus id quam auctor molestie eget ut augue.",
            "img":"static/images/graph-03.svg",
            "image_width":90,
            "image_height":None,
            "active":True
        },
        {
            "name":"Volley Ball Intense Training",
            "info":"Maecenas eu dictum felis, a dignissim nibh. Mauris rhoncus felis odio, ut volutpat massa placerat ac. Curabitur dapibus iaculis mi gravida luctus. Aliquam erat volutpat.",
            "img":"static/images/graph-02.svg",
            "image_width":None,
            "image_height":87,
            "active":True
        },
        {
            "name":"Learn Surfing From Experts",
            "info":"Maecenas eu dictum felis, a dignissim nibh. Mauris rhoncus felis odio, ut volutpat massa placerat ac. Curabitur dapibus iaculis mi gravida luctus. Aliquam erat volutpat.",
            "img":"static/images/graph-01.svg",
            "image_width":None,
            "image_height":71,
            "active":True
        },
        {
            "name":"Archers Club",
            "info":"Maecenas eu dictum felis, a dignissim nibh. Mauris rhoncus felis odio, ut volutpat massa placerat ac. Curabitur dapibus iaculis mi gravida luctus. Aliquam erat volutpat.",
            "img":"static/images/img-01.png",
            "image_width":684,
            "image_height":624,
            "active":True
        },
    ]
    return {'holder_items': holder_items}
def review(request):
    review_items=[
        {
        "img":"static/images/logo-1.png",
        "image_width":124,
        "image_height":84,
        "info":"Sed vestibulum scelerisque urna, eu finibus leo facilisis sit amet. Proin id dignissim magna. Sed varius urna et pulvinar venenatis."
        },
        {
        "img":"static/images/logo-2.png",
        "image_width":148,
        "image_height":90,
        "info":"Donec euismod dolor ut ultricies consequat. Vivamus urna ipsum, rhoncus molestie neque ac, mollis eleifend nibh." 
        },
        {
        "img":"static/images/logo-3.png",
        "image_width":100,
        "image_height":100,
        "info":"In efficitur in velit et tempus. Duis nec odio dapibus, suscipit erat fringilla, imperdiet nibh. Morbi tempus auctor felis ac vehicula." 
        },
        {
        "img":"static/images/logo-4.png",
        "image_width":108,
        "image_height":50,
        "info":"Fusce pharetra erat id odio blandit, nec pharetra eros venenatis. Pellentesque porttitor cursus massa et vestibulum." 
        },
    ]
    return{'review_items':review_items}
def pricetag(request):
    price_items=[
        {"user":"Students",
         "symbol":"$",
         "value":"8",
         "per":"per month",
         "benefits":"Personal License",
        },
        {"user":"Professional",
         "symbol":"$",
         "value":"19",
         "per":"per month",
         "benefits":"Personal License",
         "benefits2":"Email Support",
        },
        {"user":"Agency",
         "symbol":"$",
         "value":"49",
         "per":"per month",
         "benefits":"1-12 Team Members",
         "benefits2":"Phone Support",
        },
        {"user":"Enterprise",
         "symbol":"$",
         "value":"79",
         "per":"per month",
         "benefits":"Unlimited Team Members",
         "benefits2":"24/7 Phone Support",
        },   
    ]
    return{'price_items': price_items}

def index_view(request):
    context = {}
    context.update(menu_view(request))
    context.update(holder_view(request))
    context.update(review(request))
    context.update(pricetag(request))
    return render(request, 'index.html', context)
