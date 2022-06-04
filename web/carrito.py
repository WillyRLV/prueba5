from os import popen


class Cart:
    def __init__(self,request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart")#canasta del carrito
        montoTotal = self.session.get("cartMontoT")
        if not cart:##si no está creada
            cart = self.session["cart"]={}#se creará un diccionario vacio
            montoTotal = self.session["cartMontoT"] = "0"
        self.cart = cart
        self.montoTotal = float(montoTotal)

        
    def add(self,producto,qty):
        ##====Esto buscará los productos por id  en el diccionario "cart"
        ##si no existe agrega un dato nuevo
        if str(producto.id) not in self.cart.keys():
        ##===================================
            self.cart[producto.id] ={
                "producto_id":producto.id,
                "nombre":producto.nombre,
                "cantidad": qty,
                "precio":str(producto.precio),
                "imagen":str(producto.imagen.url),
                "total":str(qty * producto.precio),
                "categoria":producto.categoria.nombre
            }

        else:
            for key,value in self.cart.items():
                if key== str(producto.id):
                    value["cantidad"] = int(value["cantidad"] + qty)
                    value["total"] = float(value["cantidad"] * float(value['precio']))
                    break       
        self.save()



    ##para eliminar
    def delete(self,producto):
        producto_id = str(producto.id)
        if producto_id in self.cart:
            del self.cart[producto_id]
            self.save()

    ##para eliminar todo
    def clear(self):
        self.session["cart"]={}
        self.session["cartMontoT"]= "0"
        
            
        
    ##=============================================================
    def save(self):
        #para acumular los precios para el monto total
        montoTotal = 0
        for key,value in self.cart.items():
            montoTotal += float(value["total"])
            
        #================ASIGNAR===============================
        self.session["cartMontoT"] = montoTotal
        #================================================
        self.session["cart"] = self.cart
        self.session.modified = True
    
            
            

        