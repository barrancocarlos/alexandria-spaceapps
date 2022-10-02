from django.shortcuts import render
from .models import Document

# Create your views here.

def home(request):
	return render(request, "index.html", {})

def nlp(request):
	query_docs = Document.objects.all()
	context = {"query_docs": query_docs}
	return render(request, "nlp.html", context)
