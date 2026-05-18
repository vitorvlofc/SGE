from django.shortcuts import render


def home(request):
    product_metrics = {
        'total_cost_price': 5000,
        'total_salling_price': 500000,
        'total_quantity': 1500000,
        'total_profit': 1000000,
    }
    context = {'product_metrics': product_metrics}

    return render(request, 'home.html', context)