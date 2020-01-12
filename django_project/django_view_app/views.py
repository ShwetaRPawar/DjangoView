from django.http import  HttpResponse, HttpResponseRedirect
# Create your views here.

def home(request):
    print(request) # It display <WSGIRequest 'GET> means it display the requested method i.e POST, GET, DELETE etc
    print(dir(request)) # It disply all methods available in request
    print(request.get_full_path()) # It display the path
    return HttpResponse("<!DOCTYPE html><html><head><style>h1{color: red;}</style></head><body><h1>Hello World</body></html>")
    # It return html response to the user using method HttpResponse

# HttpResponse returns only one response at a time but HttpResponse object return multiple response at a time
def home1(request):
    respose = HttpResponse()
    # respose = HttpResponse(content_type='applocation/json') # we can set our own content type to response
    # respose = HttpResponse(content_type='text/html')
    respose.content = 'Hello Shweta' # We can set content to whole page of html
    respose.write('<p>This is response 1</p>')
    respose.write('<p>This is response 2</p>')
    respose.write('<p>This is response 3</p>')
    respose.write('<p>This is response 4</p>')

    return respose

def redirect_to_new(request):
    return HttpResponseRedirect('some/new')
    # It render to new URL/Page