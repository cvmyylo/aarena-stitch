import math

def generar_svg_olas(filepath, width=2560, height=1440):
    paso_x = 18
    paso_y = 18
    
    elementos = []
    
    # Definiciones de gradientes radiales para dar textura 3D rica y brillo
    defs = '''  <defs>
    <radialGradient id="brilloOla" cx="35%" cy="35%" r="65%">
      <stop offset="0%" stop-color="#FFF7C2" stop-opacity="1"/>
      <stop offset="50%" stop-color="#FFD700" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#D4AC00" stop-opacity="0.8"/>
    </radialGradient>
    <radialGradient id="brilloSecundario" cx="30%" cy="30%" r="70%">
      <stop offset="0%" stop-color="#FFEA75" stop-opacity="0.95"/>
      <stop offset="60%" stop-color="#E6C200" stop-opacity="0.85"/>
      <stop offset="100%" stop-color="#B89600" stop-opacity="0.6"/>
    </radialGradient>
  </defs>'''

    # Generar rejilla guiada por ecuaciones de olas marinas y dunas de arena (Forma de Ola Original)
    for y in range(-150, height + 150, paso_y):
        for x in range(-100, width + 100, paso_x):
            # Olas fluidas orgánicas (seno y coseno superpuestos)
            ola_principal = math.sin(x * 0.0026 + 0.4) * 170.0 + math.cos(x * 0.0052 + 1.2) * 85.0
            ola_secundaria = math.sin((x * 0.0038) - (y * 0.0025)) * 55.0
            crestas = math.cos(x * 0.0016 + y * 0.0018) * 65.0
            
            # Coordenada Y relativa a la forma de la ola
            y_ola = y - (ola_principal + ola_secundaria + crestas)
            
            # Intensidad de propagación de la ola desde arriba hacia abajo
            factor_y = max(0.0, 1.0 - (y_ola / 720.0))
            
            # Factor de apertura horizontal
            dist_centro_x = abs(x - (width / 2.0))
            factor_x = 1.0 - math.pow(dist_centro_x / (width * 0.68), 2.2)
            factor_x = max(0.15, factor_x)
            
            intensidad = factor_y * factor_x
            
            # Texturizado micro-granular
            granulado = math.sin(x * 0.12) * math.cos(y * 0.12) * 0.12
            intensidad_efectiva = max(0.0, intensidad + granulado)
            
            if intensidad_efectiva > 0.035:
                # Gradación de tamaños (de 9px a 0.5px)
                radio_max = 9.0
                radio = radio_max * math.pow(intensidad_efectiva, 0.75)
                
                if radio > 0.5:
                    opacidad = min(1.0, math.pow(intensidad_efectiva, 0.55) * 1.15)
                    
                    # Alternancia de gradientes radiales para dar volumen visual 3D
                    id_gradiente = "brilloOla" if ((x // paso_x) + (y // paso_y)) % 2 == 0 else "brilloSecundario"
                    
                    elementos.append(
                        f'  <circle cx="{x:.1f}" cy="{y:.1f}" r="{radio:.2f}" fill="url(#{id_gradiente})" opacity="{opacidad:.2f}"/>'
                    )

    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <!-- Patrón de Semitono Vectorial con Textura 3D y Forma de Olas - AgenciArena -->
{defs}
  <g>
{chr(10).join(elementos)}
  </g>
</svg>'''

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(svg_content)
        
    print(f"SVG original en forma de ola restaurado en {filepath}.")

if __name__ == "__main__":
    generar_svg_olas("/Users/camilomontalvanaguirre/Downloads/aarena-stitch/img/fondo-agenciarena.svg")
