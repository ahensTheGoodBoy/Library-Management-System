from django.contrib import admin
from .models import categoryListModel, bookListModel, bookLendListModel, bookAuthorListModel, authorListModel, memberListModel, memberStatusModel, reservationListModel, reservationStatusListModel, fineListModel, lateListModel

# Register your models here.
@admin.register(categoryListModel)
class staffs(admin.ModelAdmin):
	list_display = ('cat_id', 'cat_name')
	ordering = ('cat_id',)
	search_fields = ('cat_id', 'cat_name')

@admin.register(bookListModel)
class staffs(admin.ModelAdmin):
	list_display = ('book_id', 'book_title', 'cat_id', 'pub_date', 'copies_own')
	ordering = ('book_id',)
	search_fields = ('book_id', 'book_title', 'cat_id', 'pub_date', 'copies_own')

@admin.register(bookAuthorListModel)
class staffs(admin.ModelAdmin):
	list_display = ('book_id', 'author_id')
	ordering = ('author_id',)
	search_fields = ('book_id', 'author_id')

@admin.register(authorListModel)
class staffs(admin.ModelAdmin):
	list_display = ('author_id', 'author_firstName', 'author_lastName')
	ordering = ('author_id',)
	search_fields = ('author_id', 'author_firstName', 'author_lastName')

@admin.register(memberListModel)
class staffs(admin.ModelAdmin):
	list_display = ('member_id', 'member_firstName', 'member_lastName', 'date_joined', 'status_id')
	ordering = ('member_id',)
	search_fields = ('member_id', 'member_firstName', 'member_lastName', 'date_joined', 'status_id')

@admin.register(memberStatusModel)
class staffs(admin.ModelAdmin):
	list_display = ('status_id', 'status_value')
	ordering = ('status_id',)
	search_fields = ('status_id', 'status_value')

@admin.register(bookLendListModel)
class staffs(admin.ModelAdmin):
	list_display = ('lend_id', 'book_id', 'member_id', 'lend_date', 'returned_date', 'return_status')
	ordering = ('lend_id',)
	search_fields = ('lend_id', 'book_id', 'member_id', 'lend_date', 'returned_date', 'return_status')

@admin.register(reservationListModel)
class staffs(admin.ModelAdmin):
	list_display = ('res_id', 'book_id', 'member_id', 'res_from_date', 'res_to_date', 'res_status_id')
	ordering = ('res_id',)
	search_fields = ('res_id', 'book_id', 'member_id', 'res_from_date', 'res_to_date', 'res_status_id')

@admin.register(reservationStatusListModel)
class staffs(admin.ModelAdmin):
	list_display = ('res_status_id', 'res_status_name')
	ordering = ('res_status_id',)
	search_fields = ('res_status_id', 'res_status_name')

@admin.register(fineListModel)
class staffs(admin.ModelAdmin):
	list_display = ('fine_id', 'late_id', 'fine_amount', 'fine_status')
	ordering = ('fine_id',)
	search_fields = ('fine_id', 'late_id', 'fine_amount', 'fine_status')

@admin.register(lateListModel)
class staffs(admin.ModelAdmin):
	list_display = ('late_id', 'member_id', 'book_id', 'lend_id')
	ordering = ('late_id',)
	search_fields = ('late_id', 'member_id', 'book_id', 'lend_id')
