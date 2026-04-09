# scraper_computrabajo.py
# Aquí escribiremos nuestro scraper desde cero.
import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

async def main():
    print("Iniciando nuestro scraper de Computrabajo...")
    
    async with async_playwright() as p:
        # 1. Lanzamos el navegador de Chrome/Chromium 
        # (headless=False significa "No lo ocultes, quiero verlo funcionar")
        navegador = await p.chromium.launch(headless=False)
        
        # 2. Abrimos una pestaña nueva
        pagina = await navegador.new_page()
        
        # 3. Vamos a la página y buscamos empleos de Python
        flag = True
        while(flag):
            mensaje_pais = """
    Ingrese el código de su país para buscar en Computrabajo:
    - ar (Argentina)   - mx (México)      - pe (Perú)
    - co (Colombia)    - cl (Chile)       - ec (Ecuador)
    - uy (Uruguay)     - ve (Venezuela)   - cr (Costa Rica)
    Código: """
            codpais = input(mensaje_pais).strip().lower() # .strip es eliminar caracteres en blanco, .lower es convertir a minusculas
            tema = input("Ingrese el tema a buscar: ").replace(" ", "-").replace(",", "-").lower()
            url = f"https://{codpais}.computrabajo.com/trabajo-de-{tema}"
            url2=f"https://{codpais}.computrabajo.com/trabajo-de-{tema}?p=2"
            url3=f"https://{codpais}.computrabajo.com/trabajo-de-{tema}?p=3"
            
            if codpais not in ["ar", "mx", "pe", "co", "cl", "ec", "uy", "ve", "cr"]:
                print("Código de país no válido. Por favor, intente nuevamente.")
                flag = True
            else:
                flag = False

        


        alworks = []

        for npag in range(1, 6):
            if npag == 1:
                url_actual = f"https://{codpais}.computrabajo.com/trabajo-de-{tema}"
                print(f"\nNavegando a: {url_actual}")
            else:
                url_actual = f"https://{codpais}.computrabajo.com/trabajo-de-{tema}?p={npag}"
                print(f"Navegando a página {npag}: {url_actual}")
            
            await pagina.goto(url_actual)
            await pagina.wait_for_timeout(3000)
            
            html_pagina = await pagina.content()
            sopa_pagina = BeautifulSoup(html_pagina, "html.parser")
            
            # Buscamos los trabajos de ESTA página y los sumamos a nuestra bolsa
            trabajos_de_esta_pagina = sopa_pagina.find_all("article", class_="box_offer")
            alworks.extend(trabajos_de_esta_pagina)

        print(f"\n¡Listo! Se recolectaron un total de {len(alworks)} ofertas de empleo en las 5 páginas.")
        
        # 7. Mostramos los primeros 5 de la lista total para verificar
        print("Mostrando los primeros 5 resultados acumulados:")
        for tarjeta in alworks[:5]:
            titulo = tarjeta.find("h1") or tarjeta.find("h2")
            if titulo: 
                print("-> Trabajo:", titulo.text.strip().split('\n')[0])
        
        # 5. Finalmente somos educados y cerramos el navegador
        await navegador.close()
        print("Búsqueda finalizada.")

if __name__ == "__main__":
    # Función asincrónica
    asyncio.run(main())
