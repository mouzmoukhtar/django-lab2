from django.shortcuts import render
from book.models import Book
from django.http import HttpResponse, HttpResponseRedirect
from book.forms import BookForm
# Create your views here.
def getallbooks(request):
    all_books = Book.objects.all()
    context = {'bid': all_books}
    return render(request, 'book/allbooks.html', context)


def getbook(request,bk_id):
    bk = Book.objects.get(id = bk_id)
    context = {'book': bk}
    return render(request, 'book/onebook.html', context) 


def newbook(request):
    bk_form = BookForm()
    if request.method == 'POST':
        bk_form = BookForm(request.POST)
        if bk_form.is_valid():
            bk_form.save()
            return HttpResponseRedirect('/book/all')

    context = {'book_form':bk_form}
    return render(request, 'book/newbook.html', context)


def editbook(request, bk_id):
    bk = Book.objects.get(id = bk_id)
    bk_form = BookForm(instance = bk)
    if request.method == 'POST':
        bk_form = BookForm(request.POST, instance)
        if bk_form.is_valid():
            bk_form.save()
            return HttpResponseRedirect('/book/all')

    context = {'book_form':bk_form}
    return render(request, 'book/newbook.html', context)


def deletebook(rquest, bk_id):
    bk = Book.objects.get(id = bk_id)
    bk.delete()
    return HttpResponseRedirect('/book/all')
