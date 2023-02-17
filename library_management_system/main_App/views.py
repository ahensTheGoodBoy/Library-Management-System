from django.contrib import messages
from django.shortcuts import render, redirect
from .functions import log_user_in, changePassword, show_author_list_count, show_book_list_count, show_bookauthor_list_count, show_booklend_list_count, show_category_list_count, show_fine_list_count, show_late_list_count, show_member_list_count, show_memberstatus_list_count, show_res_list_count, show_resstatus_list_count, get_categories_list, add_category

# Create your views here.
def login_page(request):
    if request.method=='POST':
        if 'username' in request.POST:
            log_user_in(request)
        elif 'newpassword' in request.POST:
            changePassword(request)
        else:
            pass
        return redirect('/')
    else:
        context = {'counts': {
            'authorList':show_author_list_count(),
            'bookList':show_book_list_count(),
            'bookauthorList': show_bookauthor_list_count(),
            'booklendList':show_booklend_list_count(),
            'categoryList':show_category_list_count(),
            'fineList':show_fine_list_count(),
            'lateList':show_late_list_count(),
            'memberList':show_member_list_count(),
            'memberstatusList':show_memberstatus_list_count(),
            'resList':show_res_list_count(),
            'resstatusList':show_resstatus_list_count()
            }
        }
        return render(request,'index.html',context)

def categorylist_page(request):
    if request.method=='POST':
        if 'newpassword' in request.POST:
            changePassword(request)
        return redirect('/')
    else:
        categorylist=get_categories_list()
        if categorylist=='None':
            context={}
        else:
            context={'categories':categorylist} 
        return render(request, 'categoryList.html',context)

def add_category_page(request):
    if request.method=='POST':
        if 'categoryID' in request.POST:
            add_category(request)
        return redirect('/')
    else:
        return render(request, 'addCategory.html',{})
