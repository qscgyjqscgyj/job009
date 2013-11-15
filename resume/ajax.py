# -*- coding: utf-8 -*-
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from main.models import Gender, MaritalStatus, City, AdArea, AdCategory, AdSubCategory
from resume.widgets import ColumnCheckboxSelectMultiple, columnize
from django import forms
from django.utils.translation import ugettext_lazy as _


@dajaxice_register
def gender_marital(request, option):
    dajax = Dajax()
    out = []
    gender = Gender.objects.get(name=option)
    for status in MaritalStatus.objects.filter(gender=gender):
        out.append(u"<option value='" + str(status.pk) + u"'>%s</option>" % status.name)
        if len(out) == 1:
            out[0] = u"<option value='" + str(status.pk) + u"'>%s</option>" % status.name
    dajax.assign('#id_marital_status', 'innerHTML', ''.join(out))
    return dajax.json()


@dajaxice_register
def city_area(request, option):
    dajax = Dajax()
    out = []
    city = City.objects.get(name=option)
    for area in AdArea.objects.filter(city=city):
        out.append(u"<option value='" + str(area.pk) + u"'>%s</option>" % area.name)
        if len(out) == 1:
            out[0] = u"<option value='" + str(area.pk) + u"'>%s</option>" % area.name
    if len(out) > 0:
        dajax.assign('#id_area', 'innerHTML', ''.join(out))
        dajax.remove_css_class('#id_area_tr', 'area_none')
    else:
        dajax.add_css_class('#id_area_tr', 'area_none')
        dajax.assign('#id_area', 'innerHTML', ''.join(out))
    return dajax.json()


def get_pk(pk):
    a = []
    for sub in list(AdSubCategory.objects.all()):
        a.append(sub.pk)
    return a.index(pk)

@dajaxice_register
def category_subcategory(request, option):
    dajax = Dajax()
    category = AdCategory.objects.get(name=option)
    sub_category = AdSubCategory.objects.filter(category=category)
    column_sizes = columnize(len(sub_category), 3)
    columns = []
    for column_size in column_sizes:
        columns.append(sub_category[:column_size])
        sub_category = sub_category[column_size:]
    out = []
    for column in columns:
        out.append(u'<ul>')
        for sub in column:
            out.append(u"<li><label for='id_subcategory_" + str(get_pk(sub.pk)) +
                       u"'><input id='id_subcategory_" + str(get_pk(sub.pk)) +
                       u"' name='subcategory' type='checkbox' value='" + str(sub.pk) + u"'>" + u" " + sub.name +
                       u"</label></li>")
        out.append(u'</ul>')
    dajax.assign('._ad-subcategory-td', 'innerHTML', ''.join(out))
    return dajax.json()