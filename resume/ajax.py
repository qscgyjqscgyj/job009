# -*- coding: utf-8 -*-
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from main.models import Gender, MaritalStatus


@dajaxice_register
def gender_marital(request, option):
    dajax = Dajax()
    out = []
    gender = Gender.objects.get(name=option)
    for status in MaritalStatus.objects.filter(gender=gender):
        out.append("<option value='" + str(status.pk) + "'>%s</option>" % status.name)
        if len(out) == 1:
            out[0] = "<option value='" + str(status.pk) + "' selected='selected'>%s</option>" % status.name
    dajax.assign('#id_marital_status', 'innerHTML', ''.join(out))
    return dajax.json()