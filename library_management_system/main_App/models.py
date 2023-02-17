from django.db import models

# Create your models here.
class categoryListModel(models.Model):
    cat_id=models.CharField('Category ID',max_length=250)
    cat_name=models.CharField('Category Name',max_length=500)

class bookListModel(models.Model):
    book_id=models.CharField('Id',max_length=250)
    book_title=models.CharField('Name',max_length=500)
    cat_id=models.CharField('Category ID',max_length=250)
    pub_date=models.CharField('Publication Date',max_length=250)
    copies_own=models.IntegerField('Copies')

class bookAuthorListModel(models.Model):
    book_id=models.CharField('Book Id',max_length=250)
    author_id=models.CharField('Author ID',max_length=250)

class authorListModel(models.Model):
    author_id=models.CharField('Author ID',max_length=250)
    author_firstName=models.CharField('First Name', max_length=500)
    author_lastName=models.CharField('Last Name',max_length=500)

class memberListModel(models.Model):
    member_id=models.CharField('ID',max_length=250)
    member_firstName=models.CharField('First Name',max_length=500)
    member_lastName=models.CharField('Last Name',max_length=500)
    date_joined=models.DateField('Date Joined',max_length=250)
    status_id=models.DateField('Status ID',max_length=250)

class memberStatusModel(models.Model):
    status_id=models.DateField('Status ID',max_length=250)
    status_value=models.CharField('Status Value',max_length=250)

class bookLendListModel(models.Model):
    lend_id=models.CharField('ID',max_length=250)
    book_id=models.CharField('Book Id',max_length=250)
    member_id=models.CharField('Member ID',max_length=250)
    lend_date=models.DateField('Lend On',max_length=250)
    returned_date=models.DateField('Returned On',max_length=250)
    return_status=models.CharField('Return Status',max_length=250)

class reservationListModel(models.Model):
    res_id=models.CharField('ID',max_length=250)
    book_id=models.CharField('Book Id',max_length=250)
    member_id=models.CharField('Member ID',max_length=250)
    res_from_date=models.DateField('Reserve From',max_length=250)
    res_to_date=models.DateField('Reserve To',max_length=250)
    res_status_id=models.CharField('Reservation Status',max_length=250)

class reservationStatusListModel(models.Model):
    res_status_id=models.CharField('Status ID',max_length=250)
    res_status_name=models.CharField('Status',max_length=500)

class fineListModel(models.Model):
    fine_id=models.CharField('ID',max_length=250)
    late_id=models.CharField('Late ID',max_length=250)
    fine_amount=models.IntegerField('Amount')
    fine_status=models.CharField('Status',max_length=250)

class lateListModel(models.Model):
    late_id=models.CharField('Late ID',max_length=250)
    member_id=models.CharField('Member ID',max_length=250)
    book_id=models.CharField('Book Id',max_length=250)
    lend_id=models.CharField('ID',max_length=250)