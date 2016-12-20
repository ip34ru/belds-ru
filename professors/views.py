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
def professorsView(request):
    inside_professors = connection.cursor()
    inside_professors.execute ("""
    SELECT p.*
    FROM beldsi_base.professors_professors p
    WHERE p.isdualjobholder = 0
    ;
    """)
    inProfessors = inside_professors.fetchall()

    dualJobholderProfessors = connection.cursor()
    dualJobholderProfessors.execute ("""
    SELECT p.*
    FROM beldsi_base.professors_professors p
    WHERE p.isdualjobholder = 1
    ;
    """)
    dualJobProfessors = dualJobholderProfessors.fetchall()

    dualProfessors = connection.cursor()
    dualProfessors.execute ("""
    SELECT p.*
    FROM beldsi_base.professors_professors2 p
    ;
    """)
    professors2 = dualProfessors.fetchall()

    dual_job_holder = connection.cursor()
    dual_job_holder.execute ("""
    SELECT * FROM beldsi_base.professors_dual_job_holder;
    """)
    professors3 = dual_job_holder.fetchall()

    # ВЫБОРКА ПУНКТОВ МЕНЮ
    menu_main = connection.cursor()
    menu_main.execute ("""
    SELECT * FROM beldsi_base.professors_menu_main;
    """)
    menuMain = menu_main.fetchall()

    # ВЫБОРКА ПОД-ПУНКТОВ МЕНЮ
    menu_item = connection.cursor()
    menu_item.execute ("""
    SELECT * FROM beldsi_base.professors_menu_item;
    """)
    menuItem = menu_item.fetchall()

    # Внимание! Если хочешь не иметь проблем с CSRF
    # то везде используй RequestContext!
    templ = get_template('professors.html')
    html = templ.render(
                        RequestContext(request,
                                       {
                                        'inProfessors': inProfessors,
                                        'dualJobProfessors': dualJobProfessors,
                                        'professors2': professors2,
                                        'professors3': professors3,
                                        'menuMain': menuMain,
                                        'menuItem': menuItem,
                                       }
                                       )
                       )
    return HttpResponse(html)