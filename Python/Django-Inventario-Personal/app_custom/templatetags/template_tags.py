from django.template import Library
 
register = Library()
 
@register.filter(name='class')
def addclass(field, attr):
    classe = field.as_widget(attrs={'class': attr})
    return classe