from django.contrib import admin

from chat.models import Person,Argument,Party,LoginUser

class PersonAdmin(admin.ModelAdmin):

    list_display = ('person_name', 'person_position', 'person_consti')

    search_fields = ['person_name']

admin.site.register(Person,PersonAdmin)

class ArgumentAdmin(admin.ModelAdmin):

    list_display=['upvote','time']

admin.site.register(Argument,ArgumentAdmin)

class PartyAdmin(admin.ModelAdmin):
    list_display=['party_name','party_type']

admin.site.register(Party,PartyAdmin)
admin.site.register(LoginUser)
