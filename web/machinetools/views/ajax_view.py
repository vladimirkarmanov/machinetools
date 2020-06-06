import json
import math

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def calc_turning(request):
    if request.is_ajax() and request.method == 'POST':
        json_data = json.loads(request.body)
        n = json_data.get('n')
        Vc = json_data.get('Vc')
        D = json_data.get('D')
        Vf = json_data.get('Vf')
        f = json_data.get('f')
        ap = json_data.get('ap')
        Q = json_data.get('Q')

        try:
            if n and f:
                Vf = float(n) * float(f)
            if Vf and n:
                f = float(Vf) / float(n)
            if Vf and f:
                n = float(Vf) / float(f)
            if Vc and D:
                n = (float(Vc) * 1000) / (float(D) * math.pi)
            if D and n:
                Vc = (float(D) * math.pi * float(n)) / 1000
            if Vc and ap and f and D:
                Q = float(Vc) * float(ap) * float(f) * (1 - (float(ap) / float(D)))
        except ValueError:
            return JsonResponse({'error': 'Ошибка при расчете. Возможно вы ввели некорректные значения.'})

        data = {
            'n': n,
            'Vc': Vc,
            'D': D,
            'Vf': Vf,
            'f': f,
            'ap': ap,
            'Q': Q
        }
        return JsonResponse(data)


@csrf_exempt
def calc_drilling(request):
    if request.is_ajax() and request.method == 'POST':
        json_data = json.loads(request.body)
        n = json_data.get('n')
        Vc = json_data.get('Vc')
        D = json_data.get('D')
        Vf = json_data.get('Vf')
        f = json_data.get('f')
        Q = json_data.get('Q')

        try:
            if n and f:
                Vf = float(n) * float(f)
            if Vf and n:
                f = float(Vf) / float(n)
            if Vf and f:
                n = float(Vf) / float(f)
            if Vc and D:
                n = (float(Vc) * 1000) / (float(D) * math.pi)
            if D and n:
                Vc = (float(D) * math.pi * float(n)) / 1000
            if Vf and D:
                Q = (float(Vf) * math.pi * float(D) ** 2) / 4000
        except ValueError:
            return JsonResponse({'error': 'Ошибка при расчете. Возможно вы ввели некорректные значения.'})

        data = {
            'n': n,
            'Vc': Vc,
            'D': D,
            'Vf': Vf,
            'f': f,
            'Q': Q
        }
        return JsonResponse(data)


@csrf_exempt
def calc_boring(request):
    if request.is_ajax() and request.method == 'POST':
        json_data = json.loads(request.body)
        n = json_data.get('n')
        Vc = json_data.get('Vc')
        D = json_data.get('D')
        D1 = json_data.get('D1')
        Vf = json_data.get('Vf')
        f = json_data.get('f')
        Q = json_data.get('Q')

        try:
            if n and f:
                Vf = float(n) * float(f)
            if Vf and n:
                f = float(Vf) / float(n)
            if Vf and f:
                n = float(Vf) / float(f)
            if Vc and D:
                n = (float(Vc) * 1000) / (float(D) * math.pi)
            if D and n:
                Vc = (float(D) * math.pi * float(n)) / 1000
            if Vf and D and D1:
                Q = (float(Vf) * math.pi * (float(D) ** 2 - float(D1) ** 2)) / (4000)
        except ValueError:
            return JsonResponse({'error': 'Ошибка при расчете. Возможно вы ввели некорректные значения.'})

        data = {
            'n': n,
            'Vc': Vc,
            'D': D,
            'D1': D1,
            'Vf': Vf,
            'f': f,
            'Q': Q
        }
        return JsonResponse(data)


@csrf_exempt
def calc_milling(request):
    if request.is_ajax() and request.method == 'POST':
        json_data = json.loads(request.body)
        n = json_data.get('n')
        Vc = json_data.get('Vc')
        z = json_data.get('z')
        D = json_data.get('D')
        Vf = json_data.get('Vf')
        fz = json_data.get('fz')
        ae = json_data.get('ae')
        ap = json_data.get('ap')
        Q = json_data.get('Q')

        try:
            if n and fz and z:
                Vf = float(fz) * float(z) * float(n)
            if Vf and n:
                fz = float(Vf) / (float(z) * float(n))
            if Vf and fz:
                n = float(Vf) / (float(fz) * float(z))
            if Vc and D:
                n = (float(Vc) * 1000) / (float(D) * math.pi)
            if D and n:
                Vc = (float(D) * math.pi * float(n)) / 1000
            if ae and ap and Vf:
                Q = (float(ae) * float(ap) * float(Vf)) / 1000
        except ValueError:
            return JsonResponse({'error': 'Ошибка при расчете. Возможно вы ввели некорректные значения.'})

        data = {
            'n': n,
            'Vc': Vc,
            'z': z,
            'D': D,
            'Vf': Vf,
            'fz': fz,
            'ae': ae,
            'ap': ap,
            'Q': Q
        }
        return JsonResponse(data)
