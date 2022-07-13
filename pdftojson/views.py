from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from googletrans import Translator
import fitz as fitz
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializer import FileSerializer
# Create your views here.
class languageApi(APIView):
	def post(self, request, format=None):
		if request.method == "POST":
			lang = request.POST.get("lang")
			txt = request.POST.get("txt")
			translator = Translator()
			tr = translator.translate(txt, dest=lang)
			print(tr.text)
			return Response(tr.text)
            #return render(request, 'translate.html', {"result":tr.text})
		return Response("Try Again")

def parce_pdf(test):
    doc = fitz.open(stream=test.read(), filetype="pdf")  # this line is imporatant
    raw_text = ""
    for page in doc:
        raw_text = raw_text + str(page.get_text())
    return raw_text

class FileView(APIView):
	parser_classes = (MultiPartParser, FormParser)

	def post(self, request, *args, **kwargs):
		file_serializer = FileSerializer(data=request.data)
	    # test = request.data['file'].content_type
		test = request.FILES['file'] # send file object from front-end
		print(test)
		print(request.accepted_media_type)
		data = {'data':parce_pdf(test)}
		print(file_serializer)
	    # print(test)
		if file_serializer.is_valid():
			file_serializer.save()
			return Response(data, status=status.HTTP_201_CREATED)
		else:
			return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def parces_pdf(test):
    doc = fitz.open(stream=test.read(), filetype="pdf")  # this line is imporatant
    raw_text = ""
    for page in doc:
        raw_text = raw_text + str(page.get_text("json"))
    return raw_text

class FileViewjson(APIView):
	parser_classes = (MultiPartParser, FormParser)

	def post(self, request, *args, **kwargs):
		file_serializer = FileSerializer(data=request.data)
	    # test = request.data['file'].content_type	
		test = request.FILES['file'] # send file object from front-end
		print(test)
		print(request.accepted_media_type)
		data = {'data':parces_pdf(test)}
		print(file_serializer)
	    # print(test)
		if file_serializer.is_valid():
			file_serializer.save()
			return Response(data, status=status.HTTP_201_CREATED)
		else:
			return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)