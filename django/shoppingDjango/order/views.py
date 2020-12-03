from django.shortcuts import render, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required

from .models import Order
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string

import weasyprint
# Create your views here.

@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    context = {
        'order': order,
    }

    return render(request, 'order/admin/detail.html', context)

@staff_member_required
def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    context = {
        'order': order,
    }
    html = render_to_string('order/admin/pdf.html', context)

    response = HttpResponse(content_type='application/pdf')
    response["Content-Disposition"] = f"filename=order_{order.id}.pdf"

    weasyprint.HTML(string=html).write_pdf(response, stylesheets=[
        weasyprint.CSS(settings.STATICFILES_DIRS[0] + '/css/pdf.css')
    ])

    return response

