from django.http import HttpResponse
from django.shortcuts import render


# def homePage(request):
#     data = {
#         'tittle': 'Home page',
#         'bdata': 'Welcome to MyBlog...',
#         'clist': ['PHP', 'Java', 'Django'],
#         'numbers': [10, 15, 20, 21, 25, 27],
#         'student_deatils': [
#             {'name': 'ram', 'phone': 975693276},
#             {'name': 'sam', 'phone': 369696339},
#         ]
#     }
#     return render(request, 'index.html', data)

def homePage(request):
    return render(request, 'index.html')


def leftSidebar(request):
    return render(request, 'left-sidebar.html')


def rightSidebar(request):
    return render(request, 'right-sidebar.html')


def noSidebar(request):
    return render(request, 'no-sidebar.html')


def contactUs(request):
    return render(request, 'contacts.html')


def aboutUs(request):
    return render(request, 'about-us.html')


def UserForm(request):
    data = {'sum': None}
    try:
        if request.method == 'GET':
            # n1 = int(request.GET['Value1'])
            # n2 = int(request.GET['Value2'])
            n1 = int(request.GET.get('Value1'))
            n2 = int(request.GET.get('Value2'))
            data['sum'] = n1 + n2
    except:
        pass
    return render(request, 'UserForm.html', data)


def userpostform(request):
    data = {}
    try:
        # n1 = int(request.POST['Value1'])
        # n2 = int(request.POST['Value2'])

        n1 = int(request.POST.get('Value1'))
        n2 = int(request.POST.get('Value2'))
        data = {
            'n1': n1,
            'n2': n2,
            'sum': n1 + n2
        }
    except:
        pass
    return render(request, 'userpostform.html', data)


def course(request):
    return HttpResponse('<div> welcome to my course </div>now check dynamic url i am sending value 29 <a href="../course/29" >check now</a> <a href="../" >Home</a>')


def courseDetails(request, courseId):
    return HttpResponse('Its showing dynamic url value ' + courseId + ' <a href="../" >Home</a')
