from django.shortcuts import render

class UnderConstructionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        print("Call from Middleware")
        response = render(request, 'mysite/siteuc.html')
        return response