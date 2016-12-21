__author__ = 'taksenov'
# coding=utf-8

# imports
from django.db import connection
from professors.models import *
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context, RequestContext

# Вывод новостей
def infoView(request):

    # ВЫБОРКА ПУНКТОВ МЕНЮ
    menu_main = connection.cursor()
    menu_main.execute ("""
    SELECT * FROM www__base.info_menu_main;
    """)
    menuMain = menu_main.fetchall()

    # ВЫБОРКА ПОД-ПУНКТОВ МЕНЮ
    menu_item = connection.cursor()
    menu_item.execute ("""
    SELECT * FROM www__base.info_menu_item im
    ORDER BY im.name
    ;
    """)
    menuItem = menu_item.fetchall()

    # Внимание! Если хочешь не иметь проблем с CSRF
    # то везде используй RequestContext!
    templ = get_template('info.html')
    html = templ.render(
                        RequestContext(request,
                                       {
                                        'menuMain': menuMain,
                                        'menuItem': menuItem,
                                       }
                                       )
                       )
    return HttpResponse(html)
