from django.shortcuts import render
from .models import Document
import PyPDF2 as PyPDF2

# Create your views here.


def home(request):
	return render(request, "index.html", {})


def nlp(request):
	query_docs = Document.objects.all()
	context = {"query_docs": query_docs}
	return render(request, "nlp.html", context)


def nlpsingle(request):
	doc_id = request.GET['id']
	query_docs = Document.objects.get(pk=doc_id)
	#NL Processing
	pre_url = "static/assets/corpus/"
	pos_url = ".pdf"
	pdf = query_docs.doc_id
	pdf_url = pre_url + pdf + pos_url
	mypdf = open(pdf_url, mode='rb')
	pdfReader = PyPDF2.PdfFileReader(mypdf)
	text = ''
	for i in range(0, pdfReader.numPages):    
		pageObj = pdfReader.getPage(i)
		text=text+pageObj.extractText()
	context = {"query_docs": query_docs, "text": text}
	return render(request, "nlp-single.html", context)
