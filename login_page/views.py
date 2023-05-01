from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template.loader import render_to_string
from . models import Candidates
from django.http import HttpResponse, JsonResponse
from . serializers import CandidatesSerializer
# Create your views here.

weeks = {
    'monday': 'Welcom to Monday',
    'tuesday': 'Welcom to tuesday',
    'wednesday': 'Welcom to wednesday'
}

def index(request):
    # response_txt = render_to_string('login_page/index.html')
    week_list = list(weeks.keys())
    # print(request, "this is the request")
    return render(request, 'login_page/index.html', {
        'week_list': week_list
    })

# def monday(request, week):
#     try:
#         response_txt = weeks[week]
#         return HttpResponse(response_txt)
#     except:
#         raise Http404()
    
def tue(request):
    return render(request, 'login_page/tuesday.html')

def index_page(request):
    try:
        all_data = Candidates.objects.all()
    except:
        return HttpResponse("Sorry!!Not Found", status = 404)
    if request.method == 'GET':
        candidates = CandidatesSerializer(all_data, many = True)
        return JsonResponse(candidates.data, safe = False)
