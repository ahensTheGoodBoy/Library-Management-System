from .models import categoryListModel, bookListModel, bookAuthorListModel, authorListModel, memberListModel, memberStatusModel, bookLendListModel, reservationListModel, reservationStatusListModel, fineListModel, lateListModel
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def log_user_in(request):
    user_name = request.POST['username']
    password = request.POST['password']
    user = authenticate(request=request, username=user_name, password=password)
    if user is not None:
        login(request, user)
        messages.success(request, "You're successfully logged in...")
    else:
        messages.success(request, "There was an error logging in, please try again...")

def changePassword(request):
    new_password = request.POST['newpassword']
    re_new_password = request.POST['confirmpassword']
    if new_password == re_new_password:
        old_password = request.POST['oldpassword']
        if User.check_password(request.user, old_password) == True:
            User.set_password(request.user, new_password)
            User.save(request.user)
            login(request, authenticate(request=request, username=request.user, password=new_password))
            messages.success(request, "Your Password Changed.")
        else:
            messages.success(request, "Your entered a wrong old password. Please try again...")
    else:
        messages.success(request, "New Password and Confirm New Password did not match. Please try again...")

def show_category_list_count():
    return categoryListModel.objects.all().count()

def show_book_list_count():
    return bookListModel.objects.all().count()

def show_bookauthor_list_count():
    return bookAuthorListModel.objects.all().count()

def show_author_list_count():
    return authorListModel.objects.all().count()

def show_member_list_count():
    return memberListModel.objects.all().count()

def show_memberstatus_list_count():
    return memberStatusModel.objects.all().count()

def show_booklend_list_count():
    return bookLendListModel.objects.all().count()

def show_res_list_count():
    return reservationListModel.objects.all().count()

def show_resstatus_list_count():
    return reservationStatusListModel.objects.all().count()

def show_fine_list_count():
    return fineListModel.objects.all().count()

def show_late_list_count():
    return lateListModel.objects.all().count()

def get_categories_list():
    if categoryListModel.objects.all().count() == 0:
        return 'None'
    else:
        return categoryListModel.objects.all()

def add_category(request):
    catID = request.POST['categoryID']
    catName = request.POST['categoryName']
    categoryListModel.objects.create(cat_id=catID, cat_name=catName)
    messages.success(request, f'Category: {catName} was successfully added with id {catID}.')

def check_for_cat_id(request):
    catID = request.POST['categoryID']
    catName = request.POST['categoryName']
    if categoryListModel.objects.filter(cat_id=catID).count()!=0:
        return 'Non Unique ID'
    elif categoryListModel.objects.filter(cat_name=catName).count()!=0:
        return 'Non Unique Name'
    else:
        return 'All unique'