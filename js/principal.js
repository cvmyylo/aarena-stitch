/**
 * AgenciArena - Script Principal de Interacción y Accesibilidad
 */

document.addEventListener('DOMContentLoaded', () => {
    // Manejo del menú desplegable móvil
    const botonMenu = document.getElementById('botonMenuMovil');
    const menuMovil = document.getElementById('menuMovil');

    if (botonMenu && menuMovil) {
        botonMenu.addEventListener('click', () => {
            const estaAbierto = menuMovil.classList.toggle('abierto');
            botonMenu.setAttribute('aria-expanded', estaAbierto);
        });
    }

    // Navegación con scroll suave que centra perfectamente cada sección en la pantalla al hacer clic
    const enlacesNavegacion = document.querySelectorAll('a[href^="#"]');
    enlacesNavegacion.forEach(enlace => {
        enlace.addEventListener('click', (e) => {
            const idTarget = enlace.getAttribute('href');
            if (idTarget && idTarget.startsWith('#') && idTarget.length > 1) {
                const destino = document.querySelector(idTarget);
                if (destino) {
                    e.preventDefault();
                    const cabecera = document.querySelector('.cabecera-principal');
                    const headerHeight = cabecera ? cabecera.offsetHeight : 94;
                    const rect = destino.getBoundingClientRect();
                    const windowHeight = window.innerHeight;
                    const targetHeight = rect.height;

                    // Calcular la posición exacta para centrar la sección verticalmente en la pantalla
                    let scrollTarget = window.pageYOffset + rect.top - headerHeight;
                    const espacioDisponible = windowHeight - headerHeight;

                    if (targetHeight < espacioDisponible) {
                        const offsetCentro = (espacioDisponible - targetHeight) / 2;
                        scrollTarget = window.pageYOffset + rect.top - headerHeight - offsetCentro;
                    }

                    window.scrollTo({
                        top: Math.max(0, scrollTarget),
                        behavior: 'smooth'
                    });

                    cerrarMenuMovil();
                }
            }
        });
    });

    // Modal Flotante de Galería Extendida ("VER MÁS PROYECTOS")
    const botonAbrirGaleria = document.getElementById('abrirModalGaleria');
    const modalGaleria = document.getElementById('modalGaleriaCompleta');
    const botonCerrarGaleria = document.getElementById('cerrarModalGaleria');

    if (botonAbrirGaleria && modalGaleria) {
        botonAbrirGaleria.addEventListener('click', (e) => {
            e.preventDefault();
            modalGaleria.classList.add('abierto');
        });
    }

    if (botonCerrarGaleria && modalGaleria) {
        botonCerrarGaleria.addEventListener('click', () => {
            modalGaleria.classList.remove('abierto');
        });

        modalGaleria.addEventListener('click', (e) => {
            if (e.target === modalGaleria) {
                modalGaleria.classList.remove('abierto');
            }
        });

        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && modalGaleria.classList.contains('abierto')) {
                modalGaleria.classList.remove('abierto');
            }
        });
    }

    // Modal de Política de Privacidad (Ley Chile N° 19.628)
    const botonPrivacidad = document.getElementById('abrirPrivacidad');
    const modalPrivacidad = document.getElementById('modalPrivacidad');
    const botonCerrarModal = document.getElementById('cerrarModalPrivacidad');

    if (botonPrivacidad && modalPrivacidad) {
        botonPrivacidad.addEventListener('click', (e) => {
            e.preventDefault();
            modalPrivacidad.classList.add('abierto');
        });
    }

    if (botonCerrarModal && modalPrivacidad) {
        botonCerrarModal.addEventListener('click', () => {
            modalPrivacidad.classList.remove('abierto');
        });

        // Cerrar modal al hacer clic en la capa exterior o presionar la tecla Escape
        modalPrivacidad.addEventListener('click', (e) => {
            if (e.target === modalPrivacidad) {
                modalPrivacidad.classList.remove('abierto');
            }
        });

        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && modalPrivacidad.classList.contains('abierto')) {
                modalPrivacidad.classList.remove('abierto');
            }
        });
    }

    // Actualización dinámica del enlace activo al hacer scroll por las secciones
    const secciones = document.querySelectorAll('section[id]');
    const enlacesNav = document.querySelectorAll('.navegacion-escritorio .enlace-navegacion');

    window.addEventListener('scroll', () => {
        let actualId = '';
        const scrollPosition = window.scrollY + (window.innerHeight / 3);

        secciones.forEach(seccion => {
            const top = seccion.offsetTop;
            const height = seccion.offsetHeight;
            if (scrollPosition >= top && scrollPosition < top + height) {
                actualId = seccion.getAttribute('id');
            }
        });

        enlacesNav.forEach(enlace => {
            enlace.classList.remove('activo');
            if (enlace.getAttribute('href') === `#${actualId}`) {
                enlace.classList.add('activo');
            }
        });
    }, { passive: true });

    // Manejo de envío del formulario de contacto (Lead capture)
    const formularioLead = document.querySelector('.formulario-lead');
    if (formularioLead) {
        formularioLead.addEventListener('submit', (e) => {
            e.preventDefault();
            alert('¡Gracias por comunicarte con AgenciArena! Hemos recibido tu solicitud y te responderemos en menos de 24 horas.');
            formularioLead.reset();
        });
    }
});

/**
 * Función auxiliar para cerrar el menú móvil desde enlaces
 */
function cerrarMenuMovil() {
    const menuMovil = document.getElementById('menuMovil');
    const botonMenu = document.getElementById('botonMenuMovil');
    if (menuMovil && menuMovil.classList.contains('abierto')) {
        menuMovil.classList.remove('abierto');
        if (botonMenu) botonMenu.setAttribute('aria-expanded', 'false');
    }
}
