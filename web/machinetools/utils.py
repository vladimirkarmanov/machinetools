import sys
import uuid
from io import BytesIO

from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.paginator import Paginator


def get_objects_page(objs, obj_per_page, page_number):
    paginator = Paginator(objs, obj_per_page)
    page = paginator.get_page(page_number)
    return page


def generate_unique_filename():
    return str(uuid.uuid4())


def compress_image(uploaded_image):
    temp_image = Image.open(uploaded_image)
    output_io_stream = BytesIO()
    temp_image.save(output_io_stream, format='JPEG', quality=80, optimize=True)
    output_io_stream.seek(0)
    uploaded_image = InMemoryUploadedFile(output_io_stream,
                                          'ImageField',
                                          f'{generate_unique_filename()}.jpg',
                                          'image/jpeg',
                                          sys.getsizeof(output_io_stream),
                                          None)
    return uploaded_image
