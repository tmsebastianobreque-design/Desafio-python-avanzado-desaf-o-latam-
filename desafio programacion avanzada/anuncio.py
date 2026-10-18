from abc import ABC, abstractmethod
from error import SubTipoInvalidoException

class Anuncio(ABC):
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str):
        self.ancho = ancho
        self.alto = alto
        self.url_archivo = url_archivo
        self.url_clic = url_clic
        self.sub_tipo = sub_tipo

    ancho = property(lambda self: self._ancho, lambda self, v: setattr(self, '_ancho', v if v > 0 else 1))
    alto = property(lambda self: self._alto, lambda self, v: setattr(self, '_alto', v if v > 0 else 1))
    url_archivo = property(lambda self: self._url_archivo, lambda self, v: setattr(self, '_url_archivo', v))
    url_clic = property(lambda self: self._url_clic, lambda self, v: setattr(self, '_url_clic', v))

    @property
    def sub_tipo(self) -> str: return self._sub_tipo
    @sub_tipo.setter
    def sub_tipo(self, valor: str):
        if valor not in getattr(type(self), "SUB_TIPOS", ()):
            raise SubTipoInvalidoException(f"Subtipo '{valor}' inválido para {getattr(type(self), 'FORMATO', '')}.")
        self._sub_tipo = valor

    @staticmethod
    def mostrar_formatos():
        for idx, cls in enumerate([Video, Display, Social], 1):
            print(f"FORMATO {idx}:\n==========\n" + "\n".join(f"- {s}" for s in cls.SUB_TIPOS) + "\n")

    @abstractmethod
    def comprimir_anuncio(self): pass
    @abstractmethod
    def redimensionar_anuncio(self): pass


class Video(Anuncio):
    FORMATO, SUB_TIPOS = "Video", ("instream", "outstream")

    def __init__(self, url_archivo: str, url_clic: str, sub_tipo: str, duracion: int):
        super().__init__(1, 1, url_archivo, url_clic, sub_tipo)
        self.duracion = duracion

    duracion = property(lambda self: self._duracion, lambda self, v: setattr(self, '_duracion', v if v > 0 else 5))
    ancho = property(lambda self: self._ancho, lambda self, v: setattr(self, '_ancho', 1))
    alto = property(lambda self: self._alto, lambda self, v: setattr(self, '_alto', 1))

    def comprimir_anuncio(self): print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN.")
    def redimensionar_anuncio(self): print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN.")


class Display(Anuncio):
    FORMATO = "Display"
    SUB_TIPOS = ("traditional", "native") 
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN.")
    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN.")



class Social(Anuncio):
    FORMATO, SUB_TIPOS = "Social", ("facebook", "linkedin")
    def comprimir_anuncio(self): print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN.")
    def redimensionar_anuncio(self): print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN.")

