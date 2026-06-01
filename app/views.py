import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from . import metrics


@login_required(login_url='/login/')
def home(request):
    product_metrics = metrics.get_product_metrics()
    sales_metrics = metrics.get_sales_metrics()
    daily_sales_data = metrics.get_daily_sales_data()
    daily_sales_quantity_data = metrics.get_daily_sales_quantity_data()
    graphic_product_category_metric = metrics.get_graphic_product_category_metric()
    graphic_product_brand_metric = metrics.get_graphic_product_brand_metric()

    context = {'product_metrics': product_metrics, 'sales_metrics': sales_metrics, 'daily_sales_data': json.dumps(daily_sales_data), 'daily_sales_quantity_data': json.dumps(daily_sales_quantity_data), 'graphic_product_category_metric': json.dumps(graphic_product_category_metric), 'graphic_product_brand_metric': json.dumps(graphic_product_brand_metric)}

    return render(request, 'home.html', context)
