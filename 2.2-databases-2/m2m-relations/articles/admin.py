from django.contrib import admin
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError
from .models import Article, Tags, Scope

class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                count += 1
        
        if count > 1 or count == 0:
            raise ValidationError('Выберите основной тэг')
        return super().clean() 



class ArticleTagsInLine(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset
    


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id','title']
    inlines = [ArticleTagsInLine]
    

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']