from django.shortcuts import render

from machinetools.utils import get_objects_page


class ListViewMixin:
    model = None
    template_name = None
    default_order = None
    orders = None
    obj_per_page = 9

    def get(self, request):
        search_query = request.GET.get('search', '')
        order = request.GET.get('order')
        if search_query:
            object_list = self.get_queryset_by_search_query(search_query)
        elif order in self.orders:
            object_list = self.model.objects.order_by(order)
        else:
            order = self.default_order
            object_list = self.model.objects.order_by(order)

        page_number = request.GET.get('page', 1)
        page = get_objects_page(object_list, self.obj_per_page, page_number)
        return render(request, self.template_name, {'order': order, 'search_value': search_query, 'page': page})
