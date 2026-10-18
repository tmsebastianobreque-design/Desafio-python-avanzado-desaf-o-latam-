from datetime import date
from campaña import Campaña
from error import LargoExcedidoException, SubTipoInvalidoException

if __name__ == "__main__":
    anuncios_iniciales = (
        {
            "tipo": "Video",
            "url_archivo": "video_promo.mp4",
            "url_clic": "https://clics.com",
            "sub_tipo": "instream",
            "duracion": 15
        },
    )
    
    campaña_test = Campaña(
        nombre="Campaña Inicial Black Friday",
        fecha_inicio=date(2026, 11, 1),
        fecha_termino=date(2026, 11, 30),
        datos_anuncios=anuncios_iniciales
    )
    
    print("--- Estado Inicial ---")
    print(campaña_test)
    print("----------------------\n")

    nuevo_nombre = input("Ingrese el nuevo nombre para la campaña: ")
    nuevo_sub_tipo = input("Ingrese el nuevo subtipo para el anuncio de video: ")

    try:
        campaña_test.nombre = nuevo_nombre
        if campaña_test.anuncios:
            campaña_test.anuncios[0].sub_tipo = nuevo_sub_tipo
        
        print("\n[ÉXITO] Atributos modificados correctamente.")
        print(campaña_test)
        
    except (LargoExcedidoException, SubTipoInvalidoException) as e:
        mensaje_error = f"[ERROR] {type(e).__name__}: {str(e)}"
        print(f"\n{mensaje_error}")
        
        with open("error.log", "a", encoding="utf-8") as archivo_log:
            archivo_log.write(f"{date.today()} - {mensaje_error}\n")
        print("[LOG] Guardado en 'error.log'.")
