from googletrans import Translator

from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
import json

@require_http_methods(["GET", "OPTIONS"])
def translate(request):
    translator = Translator(service_urls=['translate.google.cn'])
    source = '我还是不开心！'
    text = translator.translate(source,src='zh-cn',dest='en').text
    # text = '{"me":"you"}'
    text = '{"text":"' + text + '"}'
    return HttpResponse(text, content_type="application/json")