from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from .forms import usersFormsModel, emiCalculater
from . import emi
import operator


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

    if request.method == "GET":
        resultData = request.GET.get('finalresult')

    return render(request, 'about-us.html', {'resultData': resultData})


def submitForm(request):

    try:
        n1 = request.POST.get('num1')
        n2 = request.POST.get('num2')
        meg = request.POST.get('num3')
        email = request.POST.get('email')

        return HttpResponse("<div>Welcome {} {}</div><div>email : {}</div><p>{}</p>".format(n1, n2, email, meg))
    except:
        pass


def emicalculater(request):

    fn = emiCalculater()
    data = {'form': fn}
    if request.method == 'GET':
        try:
            ResultData = request.GET.get('emipermonth')
            data = {
                'form': fn,
                'ResultData': ResultData
            }
            print(ResultData)
            return render(request, 'emicalculater.html', data)
        except:
            pass

    return render(request, 'emicalculater.html', data)


def SubmitEmi(request):

    resultData = {}
    if request.method == 'POST':
        resultData = emi.emicalculation(request)

    return resultData


def calculater(request):
    data = {}
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }

    if request.method == 'POST':
        try:
            n1 = int(request.POST.get('n1'))
            n2 = int(request.POST.get('n2'))
            opt = request.POST.get('opt')

            if opt in ops:
                try:
                    result = ops[opt](n1, n2)
                except ZeroDivisionError:
                    result = 'Error: Division by zero'
            else:
                result = 'Invalid operator'

            data['resultData'] = result

        except ValueError:
            data['resultData'] = 'Error: Invalid input'

    return render(request, 'calculater.html', data)


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

    finalvalue = 0
    data = {}
    try:
        # n1 = int(request.POST['Value1'])
        # n2 = int(request.POST['Value2'])

        n1 = int(request.POST.get('Value1'))
        n2 = int(request.POST.get('Value2'))
        finalvalue = n1 + n2
        data = {
            'n1': n1,
            'n2': n2,
            'sum': finalvalue
        }

        url = "/about-us/?finalresult={}".format(finalvalue)

        return HttpResponseRedirect(url)
    except:
        pass
    return render(request, 'userpostform.html', data)


def userformmodel(request):

    finalvalue = 0
    fn = usersFormsModel()
    data = {'form': fn}
    try:

        n1 = int(request.POST.get('Value1'))
        n2 = int(request.POST.get('Value2'))
        finalvalue = n1 + n2
        data = {
            'form': fn,
            'n1': n1,
            'n2': n2,
            'sum': finalvalue
        }

        url = "/about-us/?finalresult={}".format(finalvalue)

        return HttpResponseRedirect(url)
    except:
        pass
    return render(request, 'userformmodel.html', data)


def course(request):
    return HttpResponse('<div> welcome to my course </div>now check dynamic url i am sending value 29 <a href="../course/29" >check now</a> <a href="../" >Home</a>')


def courseDetails(request, courseId):
    return HttpResponse('Its showing dynamic url value ' + courseId + ' <a href="../" >Home</a')
