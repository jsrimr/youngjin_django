from __future__ import unicode_literals
from .models import Log

from django.core.paginator import Paginator
from django.shortcuts import render
from django.db.models import Q

from django.views import generic

from braces.views import SelectRelatedMixin

# Exporting csv files

from django.http import HttpResponseRedirect, HttpResponse
import csv

from django.views.decorators.csrf import csrf_exempt

from . import models
from django.http import Http404

from django.contrib.auth import get_user_model
User = get_user_model()

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.views import generic
from django.http import Http404

from braces.views import SelectRelatedMixin

from . import models

from django.contrib import messages


# Create your views here.

class listlogs(generic.ListView):

    model = models.Log
    print("LOADING MODEL ?")
    template_name = 'view_page/list_logs.html'

    def get_queryset(self):
        try:
            search_keyword = self.request.GET.get('search_keyword')
            from_date = self.request.GET.get('from_date')
            to_date = self.request.GET.get('to_date')

            if to_date is None:
                to_date = '2999-01-01'
            if from_date is None:
                from_date = '2010-01-01'
            if search_keyword is None:
                search_keyword = ""

            self.log_user = User.objects.all()

        except:
            print("Replace this line with raise Http404")
        else:
            print("ABOUT to FAIL")

            #print("DDD", self.get('dpt'))

            print("THIS IS IT1", self.kwargs.get('dpt'))

            self.log_user = User.objects.prefetch_related('view_page').get(dpt__iexact = self.kwargs.get('dpt'))

            print("THIS IS IT2", self.log_user)
            print("OMG IM GONNA CRY", self.log_user.view_page.all())

            return self.log_user.view_page.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['log_user'] = self.log_user
        return context


@csrf_exempt
def export_sales_csv(request):

    to_date = request.GET.get('to_date')
    from_date = request.GET.get('from_date')
    #$('.date').val()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="log.csv"'
    writer = csv.writer(response)
    writer.writerow(['A', 'B', 'C', 'D', 'E'])
    log_list = Log.objects.all().values_list('id', 'log_date', 'log_time', 'log_userid', 'log_question', 'log_answer')\
                                .filter(log_date__range=[from_date, to_date], log_userid = 'a')
    for log in log_list:
        writer.writerow(log)
    return response