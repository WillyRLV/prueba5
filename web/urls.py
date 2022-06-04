from django.urls import path

from . import views

app_name = 'web'

urlpatterns = [

 path('',views.index,name='index'),
 #llamando la plantilla  producto desde vistas
 path('producto/<int:producto_id>',views.producto,name='producto'),
 ##filtro
 path('Filtro/<int:categoria_id>',views.Filtro,name='Filtro'),
 ##carrito
 path('carrito',views.carrito,name='carrito'),
 ##carrito agregar
 path('agregarCarrito/<int:producto_id>',views.agregarCarrito,name='agregarCarrito'),
 #para eliminar
 path('eliminarProducto/<int:producto_id>',views.eliminarProducto,name='eliminarProducto'),
 ##para limpiar todo
path('limpiarCarrito',views.limpiarCarrito,name='limpiarCarrito'),


#################login###################################
 ##login
path('login',views.loginUsuario,name='loginUsuario'),
#crearusuario

path('crearUsuario',views.crearUsuario, name='crearUsuario'),


##vista cuenta usuario===
path('cuenta',views.cuentaUsuario,name='cuentaUsuario'),

#actualizar cliente

path('actualizarCliente',views.actualizarCliente,name='actualizarCliente'),

##registrar pedidos
path('registrarPedido',views.registrarPedido,name='registrarPedido'),

##registrarpeiddo pagado
path('pedidopagado',views.pedidopagado,name='pedidopagado')

]