from datetime import date
from error import LargoExcedidoException
from anuncio import Video, Display, Social

class Campaña:
    def __init__(self, nombre: str, fecha_inicio: date, fecha_termino: date, datos_anuncios: tuple):
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_termino = fecha_termino
        self._anuncios = []
        
        clases_anuncio = {"Video": Video, "Display": Display, "Social": Social}
        
        for d in datos_anuncios:
            tipo = d.get("tipo")
            if tipo in clases_anuncio:
                params = {k: v for k, v in d.items() if k != "tipo"}
                if tipo != "Video": 
                    params.pop("ancho", None)
                    params.pop("alto", None)
                self._anuncios.append(clases_anuncio[tipo](**params))
                
    @property
    def nombre(self) -> str: 
        return self._nombre
        
    @nombre.setter
    def nombre(self, valor: str):
        if len(valor) > 250: 
            raise LargoExcedidoException("El nombre supera los 250 caracteres.")
        self._nombre = valor
        
    fecha_inicio = property(lambda self: self._fecha_inicio, lambda self, v: setattr(self, '_fecha_inicio', v))
    fecha_termino = property(lambda self: self._fecha_termino, lambda self, v: setattr(self, '_fecha_termino', v))
    anuncios = property(lambda self: self._anuncios)
    
    
    def __str__(self) -> str:
        c = [sum(1 for a in self._anuncios if isinstance(a, cls)) for cls in (Video, Display, Social)]
        return (f"Nombre de la campaña: {self.nombre}\n"
                f"Fecha de inicio: {self.fecha_inicio}\n"
                f"Fecha de término: {self.fecha_termino}\n"
                f"Anuncios: {c[0]} Video, {c[1]} Display, {c[2]} Social")

