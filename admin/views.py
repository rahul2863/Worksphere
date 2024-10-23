from django.shortcuts import render

# Create your views here.
def adminDashboard(requests):
    return render(requests,'admin/adminDashboard.html',{'title':'Admin Dashboard'})

def adminLogin(requests):
    if requests.method == 'GET':
        return render(requests,'admin/adminLogin.html',{'title':'Admin Login'})
    else:
        pass