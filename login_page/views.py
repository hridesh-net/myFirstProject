from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template.loader import render_to_string
from . models import Candidates
from django.http import HttpResponse, JsonResponse
from . serializers import CandidatesSerializer
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
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
        candidates = CandidatesSerializer(all_data, many=True)
        return JsonResponse(candidates.data)

class CandidateList(generics.ListCreateAPIView):
    queryset = Candidates.objects.all()
    serializer_class = CandidatesSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = CandidatesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CandidatesDetail(APIView):
    def get_object(self, pk):
        try:
            return Candidates.objects.get(pk=pk)
        except Candidates.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        candidate = self.get_object(pk)
        serializer = CandidatesSerializer(candidate)
        return Response(serializer.data)
    
    def put(self, request, pk):
        candidate = self.get_object(pk)
        serializer = CandidatesSerializer(candidate, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return(serializer.data)
        return Response(serializer.error, status=400)
    
    def delete(self, request, pk):
        candidate = self.get_object(pk)
        candidate.delete()
        return Response(status=204)