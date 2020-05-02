# coding: utf-8

#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import webapp2
from webapp2_extras import jinja2
from model.usuario import Usuario

class MainHandler(webapp2.RequestHandler):
    def get(self):
        valores_plantilla = {
        }
        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("index.html",
            **valores_plantilla)
        )

    def post(self):
        usuario = self.request.get("usuario")
        password = self.request.get("password")

        if(not(usuario) or not(password)):
            return self.response.write("Error de autenticacion")
        else:
            try:
                usuario_pre = Usuario.query(Usuario.nombre == usuario and Usuario.password == password).order(Usuario.nombre)
            except ValueError:
                usuario_pre = None

            if(not(usuario_pre) or usuario_pre.count() != 1):
                return self.response.write("El nombre de usuario o la contraseña son incorrectos.")
            else:
                return self.redirect("/libros/listado")

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
