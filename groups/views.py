# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.mixins import (LoginRequiredMixin, PermissionRequiredMixin)
from django.core.urlresolvers import reverse
from django.views import generic
# Create your views here.
from groups.models import Group, GroupMember

class CreateGroup(LoginRequiredMixin,generic.CreateView):
    fields = ('name','description')
    model = Group

class SingleGroup(genric.DetailView):
    model = Group

class ListGroups(generic.ListView):
    model = Group