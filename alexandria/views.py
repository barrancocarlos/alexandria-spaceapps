from django.shortcuts import render
from .models import Document
import seaborn as sns
import matplotlib.pyplot as plt
import PyPDF2 as PyPDF2
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import string
from rake_nltk import Rake
import pandas as pd

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
    pre_url = "/static/assets/images/"
    pos_url = ".png"
    freq_img = query_docs.doc_id
    freq_url = pre_url + freq_img + pos_url
    context = {"query_docs": query_docs, "freq_url": freq_url}
    return render(request, "nlp-single.html", context)


def nlprocess(request):
    doc_id = request.GET['id']
    query_docs = Document.objects.get(pk=doc_id)
    #Pdf path
    pre_url = "static/assets/corpus/"
    pos_url = ".pdf"
    pdf = query_docs.doc_id
    pdf_url = pre_url + pdf + pos_url
	#NLP Summary
    mypdf = open(pdf_url, mode='rb')
    pdfReader = PyPDF2.PdfFileReader(mypdf)
    text = ''
    for i in range(0, pdfReader.numPages):
         pageObj = pdfReader.getPage(i)
         ext = text+pageObj.extractText()     
	#tokenize
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text)
	#frequency table
    freqTable = dict()
    for word in words:
        word = word.lower()
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1    
	#store sentences
    sentences = sent_tokenize(text)
    sentenceValue = dict()
    for sentence in sentences:
        for word, freq in freqTable.items():
            if word in sentence.lower():
                if sentence in sentenceValue:
                    sentenceValue[sentence] += 1
                else:
                    sentenceValue[sentence] = 1
          
    sumValues = 0
    for sentence in sentenceValue:
        sumValues += sentenceValue[sentence]
        average = int(sumValues / len(sentenceValue))
	#store sentences in summary
    summary = ''
    for sentence in sentences:
        if (sentence in sentenceValue) and (sentenceValue[sentence] > (2 * average)):
            summary += " " + sentence    
    rake_nltk_var = Rake()
    #remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    #rake
    rake_nltk_var.extract_keywords_from_text(text)
    keyword_extracted = rake_nltk_var.get_ranked_phrases()
    #Creating FreqDist for whole BoW, keeping the 20 most common tokens
    all_fdist = nltk.FreqDist(keyword_extracted).most_common(20)       
    context = {"query_docs": query_docs, "summary": summary,"all_fdist": all_fdist}
    return render(request, "nlp-single.html", context)
