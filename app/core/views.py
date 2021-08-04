from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from .serializers import UserSerializer, AuthTokenSerializer


from core.controller.ControllerHistTurno import ControllerHistTurno
from core.controller.ControllerPuesto import ControllerPuesto
from core.controller.ControllerIdioma import ControllerIdioma
from .controller.ControllerDept import ControllerDept
from .controller.ControllerUsuario import ControllerUsuario
from .controller.ControllerTurno import ControllerTurno
from .controller.ControllerTipoRol import ControllerTipoRol
from .controller.ControllerScope import ControllerScope
from .controller.ControllerEstatus import ControllerEstatus
from .controller.ControllerRol import ControllerRol
from .controller.ControllerLogin import ControllerLogin
from .controller.ControllerDeptTurno import ControllerDeptTurno
from rest_framework.response import Response
from rest_framework.views import APIView


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for the user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class Departamentoview(APIView):
    def post(self, request):
        respuesta = ControllerDept.creardepartamento(request)
        return Response(respuesta)

    def get(self, request, id_departamento=None):
       respuesta =ControllerDept.listardepartamento(id_departamento)
       return Response(respuesta)
    
class Turnoview(APIView):
    def post(self, request):
        respuesta = ControllerTurno.crearturno(request)
        return Response(respuesta)

    def get(self, request, id_turno=None):
       respuesta = ControllerTurno.listarturno(id_turno)
       return Response(respuesta)
       
class Tipo_Rolview(APIView):
    def post(self, request):
        respuesta = ControllerTipoRol.creartipo_rol(request)
        return Response(respuesta)

    def get(self, request, id_tipo_rol=None):
       respuesta = ControllerTipoRol.listartipo_rol(id_tipo_rol)
       return Response(respuesta)

class Scopeview(APIView):
    def post(self, request):
        respuesta = ControllerScope.crearscope(request)
        return Response(respuesta)

    def get(self, request, id_scope=None):
       respuesta = ControllerScope.listarscope(id_scope)
       return Response(respuesta)

class Estatusview(APIView):
    def post(self, request):
        respuesta = ControllerEstatus.crearestatus(request)
        return Response(respuesta)

    def get(self, request, id_estatus=None):
       respuesta = ControllerEstatus.listarestatus(id_estatus)
       return Response(respuesta)

class Idiomaview(APIView):
    def post(self, request):
        respuesta = ControllerIdioma.crearidioma(request)
        return Response(respuesta)

    def get(self, request, id_idioma=None):
       respuesta = ControllerIdioma.listariridioma(id_idioma)
       return Response(respuesta)

class Rolview(APIView):
    def post(self, request):
        respuesta = ControllerRol.crearrol(request)
        return Response(respuesta)

    def get(self, request, id_rol=None):
       respuesta = ControllerRol.listarrol(id_rol)
       return Response(respuesta)

class Departamento_Turnoview(APIView):
    def post(self, request):
        respuesta = ControllerDeptTurno.creardepartamento_turno(request)
        return Response(respuesta)

    def get(self, request, id_departamento_turno=None):
       respuesta = ControllerDeptTurno.listardepartamento_turno(id_departamento_turno)
       return Response(respuesta)

class Puestoview(APIView):
    def post(self, request):
        respuesta = ControllerPuesto.crearpuesto(request)
        return Response(respuesta)

    def get(self, request, id_puesto=None):
       respuesta = ControllerPuesto.listarpuesto(id_puesto)
       return Response(respuesta)

class Usuarioview(APIView):
    def post(self,request):
            respuesta = ControllerUsuario.crearUsuario(request)
            return Response(respuesta)

    def get(self, request, id_usuario=None):
        respuesta =ControllerUsuario.listarUsuario(id_usuario)
        return Response(respuesta)

class PerfilUsuarioview(APIView):
    def get(self, request, p_nombre=None):
        respuesta =ControllerUsuario.verPerfil(p_nombre)
        return Response(respuesta)
    
class Historial_TurnoView(APIView):
    def post(self,request):
            respuesta = ControllerHistTurno.crearhistorial_turno(request)
            return Response(respuesta)

    def get(self, request, id_historial_turno=None):
        respuesta =ControllerHistTurno.listarhistorialturno(id_historial_turno)
        return Response(respuesta)

class LoginView(APIView):
    def post(self,request):
            respuesta = ControllerLogin.login(request)
            return Response(respuesta)
