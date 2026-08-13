import sys, math

def generar_svg_halftone_agenciarena(filepath, width=2560, height=1440):
    """
    Genera un archivo SVG puramente vectorial con el patrón de semitono (Ben-Day dots)
    de color amarillo #FFD700 sobre fondo transparente (Canal Alfa).
    """
    filas_circulos = []
    
    # Parámetros del entramado de semitono
    paso = 22  # Distancia entre puntos
    angulo = math.radians(45) # Ángulo clásico de semitono (45 grados)
    cos_a = math.cos(angulo)
    sin_a = math.sin(angulo)
    
    # Centro de la cascada de puntos en la cabecera
    centro_x = width / 2.0
    centro_y = -100.0
    
    radio_maximo = 9.5
    
    # Generar rejilla con rotación a 45°
    for y in range(-200, height + 200, paso):
        for x in range(-200, width + 200, paso):
            # Rotación sutil
            rx = x * cos_a - y * sin_a
            ry = x * sin_a + y * cos_a
            
            # Distancia relativa desde el centro de origen del héroe
            dx = x - centro_x
            dy = y - centro_y
            
            # Forma de la onda orgánica asimétrica
            distancia_radial = math.sqrt((dx * 0.85)**2 + (dy * 0.9)**2)
            variacion_onda = math.sin(x * 0.003 + y * 0.002) * 120.0
            distancia_efectiva = distancia_radial + variacion_onda
            
            # Factor de atenuación (intencional de arriba hacia abajo y bordes)
            factor_vertical = 1.0 - (y / (height * 0.82))
            factor_horizontal = 1.0 - (abs(dx) / (width * 0.65))
            
            intensidad = factor_vertical * factor_horizontal
            
            if intensidad > 0.02:
                radio = radio_maximo * math.pow(intensidad, 0.85)
                # Gradación sutil de opacidad en los bordes para fade out suave
                opacidad = min(1.0, intensidad * 1.3)
                
                if radio > 0.6:
                    filas_circulos.append(
                        f'  <circle cx="{x:.1f}" cy="{y:.1f}" r="{radio:.2f}" opacity="{opacidad:.2f}"/>'
                    )

    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <!-- Patrón de Semitono Ben-Day Vectorial Nítido - AgenciArena -->
  <g fill="#FFD700">
{chr(10).join(filas_circulos)}
  </g>
</svg>'''

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(svg_content)
    
    print(f"SVG generado exitosamente en {filepath} con {len(filas_circulos)} elementos vectoriales.")

if __name__ == "__main__":
    generar_svg_halftone_agenciarena("/Users/camilomontalvanaguirre/Downloads/aarena-stitch/img/fondo-agenciarena.svg")
