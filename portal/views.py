# -*- coding: utf-8 -*-
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from libs.annoying.decorators import render_to
from django.utils.translation import ugettext_lazy as _
from settings import *

from django.http import HttpResponse
from libs.annoying.fields import JSONField

import sys

sys.path.append(PROJECT_DIR)
from pce_kernel.storage_engines.web2py_dal.gluon.sql import DAL, Field, Table


@render_to(template="portal/index.html")
def index(request):
	print PROJECT_DIR
	return {'ok':'ok'}