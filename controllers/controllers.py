# -*- coding: utf-8 -*-
from odoo import http

from odoo.http import request
from odoo.addons.web.controllers.main import serialize_exception

import json
import string
import random


class BaseRest(http.Controller):
    @http.route('/api/auth', auth='none', type='http', methods=['POST'], csrf=False)
    @serialize_exception
    def index(self, **kw):
        """ user, password """
        response = {}
        if 'user' in kw and 'password' in kw:
            session = request.session
            login = request.session.authenticate(
                session['db'], kw['user'], kw['password']
            )
            print(login)
            if not login:
                response['status'] = 'denied'
                return request.make_response(json.dumps(response), [('Access-Control-Allow-Origin', '*')])

            users = request.env['res.users'].sudo().search(
                [('login', '=', kw['user'])])
            if users:
                for user in users:
                    if not user['token']:
                        token = self.get_token(user)
                    response = {
                        "name": user['name'] or "",
                        "user": user['login'] or "",
                        "token": user['token'] or token,
                        "email": user['email']
                    }
            if not response:
                response['status'] = 'error'
            return request.make_response(json.dumps(response), [('Access-Control-Allow-Origin', '*')])
        else:
            response['status'] = 'error'
            return request.make_response(json.dumps(response), [('Access-Control-Allow-Origin', '*')])

    def get_token(self, user):
        length = 25
        letters = string.ascii_letters + '1234567890'
        token = ''.join(random.choice(letters) for i in range(length))
        print("Random string is:", token)
        user.sudo().write({"token": token})
        return token

    @http.route('/api/register', auth='none', type='http', methods=['POST'], csrf=False)
    def register(self, **kw):
        response = {}
        new_user = request.env['res.users'].sudo().create({
            'login': kw['username'], 
            'password': kw['password'], 
            'name': kw['name'],
            'email': kw['email']
        })
        if new_user:
            response['result'] = 'success'
        else:
            response['result'] = 'failed'
        return request.make_response(json.dumps(response), [('Access-Control-Allow-Origin', '*')])


# class Emergency(http.Controller):
#     @http.route('/emergency/emergency/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/emergency/emergency/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('emergency.listing', {
#             'root': '/emergency/emergency',
#             'objects': http.request.env['emergency.emergency'].search([]),
#         })

#     @http.route('/emergency/emergency/objects/<model("emergency.emergency"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('emergency.object', {
#             'object': obj
#         })
