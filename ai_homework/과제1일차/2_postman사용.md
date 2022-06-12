#urls.py

urlpatterns = [
    path('', message),
    path('test/', PlaceAPI.as_view()),
]

![image](https://user-images.githubusercontent.com/78908697/173222723-efd91f44-5723-4dd2-85fd-84b7c609cf6b.png)


#views.py

def message(request):
    message = {'message':'success!!!'}
    return JsonResponse(message)
![image](https://user-images.githubusercontent.com/78908697/173222726-1c733c63-3340-47a4-933a-e2498ca00e04.png)


#postman
![image](https://user-images.githubusercontent.com/78908697/173222848-f4626df9-3765-4d5e-b18b-efe7c29ef628.png)
