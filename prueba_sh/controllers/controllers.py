# -*- coding: utf-8 -*-
# from odoo import http


# class PruebaSh(http.Controller):
#     @http.route('/prueba_sh/prueba_sh/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/prueba_sh/prueba_sh/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('prueba_sh.listing', {
#             'root': '/prueba_sh/prueba_sh',
#             'objects': http.request.env['prueba_sh.prueba_sh'].search([]),
#         })

#     @http.route('/prueba_sh/prueba_sh/objects/<model("prueba_sh.prueba_sh"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('prueba_sh.object', {
#             'object': obj
#         })
