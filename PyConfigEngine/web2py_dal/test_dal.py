# -*- coding: utf-8 -*-
import random
from gluon.sql import *

params = dict(uri='sqlite://test_storage.db', pool_size=10)
db = DAL(**params)

db.define_table('mytable', Field('myfield', 'text'), Field('myfield2', 'integer'))

db.mytable.insert(myfield = ("W" + str(random.random()*10)), myfield2 = random.random()*10)
db.commit()

rows = db(db.mytable.myfield!=None).select()

for row in rows:
    print row.myfield, " -> ", row.myfield2
