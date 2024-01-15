from django.shortcuts import render, redirect
from.models import Register, Book, Issue
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        data = Register.objects.create(name=name,  phone=phone, email=email,  username=username, password=password, type=1)
        data.save()
        # data1 = Login.objects.create(username=username, password=password, type=1)
        # data1.save()
        return HttpResponse(" Registered Successfully ")


def login(request):
    if request.method == 'POST':
        username = request. POST['username']
        password = request. POST['password']

        try:
            data = Register.objects.get(username=username)
            if data.password == password:
                request.session['id'] = data.id       #seasion created to continue
                if data.type == 1:
                    return redirect(bookstore)
                else:
                    return redirect(librarian)
            else:
                return HttpResponse("PASSWORD ERROR")
        except Exception:
            return HttpResponse("USERNAME ERROR")
    else:
        return render(request, 'login.html')



def logout(request):
    if 'id' in request.session:
        request.session.flush()
        return render(request, 'home.html')
    else:
        return redirect(login)


def history(request):
    if 'id' in request.session:
        data=Issue.objects.all()
        return render(request, 'history.html', {'data': data})
    else:
        return redirect(login)

def userhistory(request):
    if 'id' in request.session:
        userid = request.session['id']
        data = Issue.objects.filter(username=userid).all()
        return render(request, 'userhistory.html', {'data': data})
    else:
        return redirect(login)


def issuebooksuccess(request):
    if 'id' in request.session:
        return render(request, 'issuebooksuccess.html')
    else:
        return redirect(login)




def bookstore(request):
    if 'id' in request.session:
        user = request.session['id']
        data = Book.objects.all()
        return render(request, 'bookstore.html', {'data': data, 'user': user})
    else:
        return redirect(login)




def editprofileview(request):
    if 'id' in request.session:
        return render(request, 'editprofileview.html')
    else:
        return redirect(login)

def editprofilesuccess(request):
    if 'id' in request.session:
        return render(request, 'editprofilesuccess.html')
    else:
        return redirect(login)


def editprofile(request):
    if 'id' in request.session:
        user = request.session['id']
        if request.method =='GET':
            data = Register.objects.get(id=user)
            return render(request,'editprofileview.html',context={'data':data})
        if request.method == "POST":
            newname = request.POST['newname']
            newphone = request.POST['newphone']
            newemail = request.POST['newemail']
            data = Register.objects.get(id=user)
            try:
                data = Register.objects.get(id=user)
                data.name = newname
                data.phone = newphone
                data.email = newemail
                data.save()
                return render(request,'editprofilesuccess.html')
            except Exception:
                context = {
                    'msg': "username Error"
                }
                return render(request, 'editprofileview.html', context)
        else:
            return render(request, 'editprofileview.html')
    else:
        return redirect(login)




def changepassword(request):
    if 'id' in request.session:
        return render(request, 'changepassword.html')
    else:
        return redirect(login)

def passview(request):
    if 'id' in request.session:
        user = request.session['id']
        if request.method == "POST":
            password = request.POST['password']
            new = request.POST['new']
            try:
                data1 = Register.objects.get(id=user)
                if data1.password == password:
                    data1.password = new
                    data1.save()
                    return redirect(bookstore)
                else:
                     return HttpResponse("password error")
            except Exception:
              return HttpResponse("username error")
        else:
            return redirect(changepassword)
    else:
        return redirect(login)

def changepasswordsuccess(request):
    if 'id' in request.session:
        return render(request, 'changepasswordsuccess.html')
    else:
        return redirect(login)

def affairview(request,id):
    if 'id' in request.session:
        data = Book.objects.get(id=id)
        return render(request, 'affair.html', {'data': data})
    else:
        return redirect(login)


def librarian(request):
    if 'id' in request.session:
        data = Book.objects.all()
        return render(request, 'librarian.html', {'data': data})
    return redirect(login)

def addbook(request):
    if 'id' in request.session:
      if request.method == 'POST':
          BOOK_NAME=request.POST['bookname']
          AUTHOR=request.POST['author']
          GENRE=request.POST['genre']
          DESCRIPTION=request.POST['description']
          IMAGE=request.FILES['image']

          data2=Book.objects.create(bookname=BOOK_NAME, author=AUTHOR, genre=GENRE, description=DESCRIPTION, image=IMAGE)
          data2.save()
          return redirect(librarian)
      else:
          return render(request, 'addbook.html')
    else:
        return redirect(login)

def deletebook(request,id):
    if 'id' in request.session:
        data =Book.objects.get(id=id)
        data.delete()
        return redirect(librarian)
    else:
        return redirect(login)


def editbook(request,id):
    data = Book.objects.get(id=id)
    if request.method == 'POST':
        newbookname = request.POST['bookname']
        newauthor = request.POST['author']
        newgenre = request.POST['genre']
        newdescription = request.POST['description']
        newimage = request.FILES['image']

        try:
            data = Book.objects.get(id=id)
            if data.id == id:
                data.bookname = newbookname
                data.author = newauthor
                data.genre = newgenre
                data.description = newdescription
                data.image = newimage
                data.save()
                return redirect(librarian)
            else:
                return HttpResponse("Book Not Found")
        except Exception:
            return HttpResponse("Check The Book  Name")
    else:
         return render(request, 'editbook.html', {'data': data})

def getbook(request):
    if 'id' in request.session:
        userid = request.session['id']
        user = Register.objects.get(id=userid)
        if request.method=='POST':
            bookid=request.POST["bookid"]
            currentbok=Book.objects.get(id=bookid)
            if Issue.objects.filter(bookname=currentbok).exists():
                return render(request,'booknotfound.html')
            else:
                data=Issue.objects.create(username=user,bookname=currentbok)
                data.save()
                return render(request,'issuebooksuccess.html')
        else:
            return redirect(userhistory)
    else:
        return redirect(login)


def returnbook(request, id):
    if 'id' in request.session:
        data = Issue.objects.get(id=id)
        data.delete()
        return redirect(userhistory)
    else:
        return redirect(login)



def search(request):
    if 'id' in request.session:
        books=None
        search_data=None
        if request.method == "GET":
            search = request.GET.get('search')
            if search:
                search_data = Book.objects.filter(bookname__icontains=search)
            else:
                books = Book.objects.all()
        return render(request, 'bookstore.html', {'data': books, 'data1': search_data})
    else:
        return redirect(login)



