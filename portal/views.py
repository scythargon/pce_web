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

from pce_kernel.storage_engines.web2py_dal.gluon.sql import DAL, Field, Table
import time

from PyConfigEngine import connection

@render_to(template="portal/index.html")
def index(request):
	db=DAL('sqlite://test.sqlite',folder=PROJECT_DIR+'/portal/db/')
	ret = []
	db.define_table('test',Field('time'))
	for row in db().select(db.test.ALL):
		print row.time
		ret.append(row.time)
	db.test.insert(time=time.ctime())
	db.commit()
	return {'ret':ret}

