# # -*- encoding: utf-8 -*-
# # -*- coding: utf-8 -*
#
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.shortcuts import render
# from django.views.generic import TemplateView, FormView, ListView
#
# #from braces.views import UserFormKwargsMixin
#
# from .forms import BuscaForm
# #from .mixins import GerarFichaAjax
# from .models import Ficha
#
# class HomeView(LoginRequiredMixin, TemplateView):
#     template_name = 'index.html'
#
#     def get_context_data(self, **kwargs):
#         contexto = super(HomeView, self).get_context_data(**kwargs)
#         contexto['form'] = BuscaForm()
#         return contexto
#
# class FichasSearch(LoginRequiredMixin, FormView): #GerarFichaAjax
#
#     template_name = 'index.html'
#     form_class = BuscaForm
#
# class Fichas(LoginRequiredMixin, ListView):
#
#     template_name = 'fichas.html'
#     model = Ficha
#     context_object_name = 'fichas'
#
#     def get_queryset(self):
#         alvos = self.request.session.get('alvos', [])
#         tipo = self.request.session.get('tipo', 'I')
#         # print(alvos)
#         # print(tipo)
#         queryset = None
#         tamanho = len(alvos)
#         if tamanho > 0 and tamanho <= 1000:
#             if tipo == 'I':
#                 queryset = Ficha.objects.all().filter(instalacao__isnull=False).filter(instalacao__in=alvos)
#             else:
#                 queryset = Ficha.objects.all().filter(cc__in=alvos)
#
#         return queryset