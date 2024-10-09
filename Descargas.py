from pytube import YouTube

def descarga_video(url, ruta_destino):
    try:
        #cargar el video usando la url proporcionzada 
        yt = YouTube(url)

        #mayor resolucion
        stream = yt.streams.get_highest_resolution()
        #ruta destino 
        stream.download(output_path=ruta_destino)

        print("descarga choida")

    except Exception as e:
            print(f"Error perro, no le echaste ganas: {e}")
#ruta url 
url = "https://www.youtube.com/watch?v=NJI0xym4OWg"
#ruta de destino a la descarga 
ruta_destino = "C:/Users/ismae/Downloads"
#llamada a la funcion descarga 
descarga_video(url, ruta_destino)
