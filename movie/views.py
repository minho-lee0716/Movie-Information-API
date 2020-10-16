from django.http import JsonResponse
from django.views import View

class MovieView(View):
    def get(self, request):
        return JsonResponse({'message':'SUCCESS_TEST'}, status=200)
