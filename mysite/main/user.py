from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
import json
from . import models
import hashlib

@require_http_methods(["POST"])
def addUser(request):
    received_data = json.loads(request.body)
    # print (received_data)

    newUser = models.User(username=received_data['username'], password=addSalt(received_data['password']))

    if not models.User.objects.filter(username=newUser.username).exists():
        newUser.save(force_insert=True)
        return HttpResponse("Regist new user successfully!")
    else:
        return HttpResponse("Duplicate Username", status=400)

def addSalt(data):
    for i in range(10):
        data = (hashlib.md5((data + "eatDD").encode('utf-8')).hexdigest())
    return data