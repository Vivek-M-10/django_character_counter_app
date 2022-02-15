from django.shortcuts import render


def home_page(request):
    return render(request, "Home Page.html")


def arraysum(request):
    djtext = request.GET.get('text', 'default')
    print(djtext)
    count = 0
    punct = ''' !@#$%^&*(){}[]|\:;"'<>?,./'''
    print(punct)
    for i in djtext:
        if(i not in punct):
            count+=1

    print(count)
    param = {'Count': count}
    return render(request, 'sum.html', param)

    return render(request, 'sum.html')
