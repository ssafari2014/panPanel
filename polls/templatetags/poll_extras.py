from django import template
from jalali_date import date2jalali,datetime2jalali
from articles_module.models import article
register = template.Library()


def lower(value):  # Only one argument.
    """Converts a string into all lowercase"""
    return value.lower()


@register.filter(name='jalali_create_dates')
def jalali_create_dates(value):
    return date2jalali(value)

