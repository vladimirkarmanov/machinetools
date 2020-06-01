from django.core.paginator import Paginator


def get_objects_page(objs, obj_per_page, page_number):
    paginator = Paginator(objs, obj_per_page)
    page = paginator.get_page(page_number)
    return page
