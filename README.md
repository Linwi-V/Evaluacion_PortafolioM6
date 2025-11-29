# Gestor de Tareas - Django Framework

Sistema de gestión de tareas desarrollado con Django que permite a los usuarios registrarse, autenticarse y administrar sus tareas personales de manera segura y eficiente.

## Descripción del Proyecto

Este proyecto forma parte del portafolio del Módulo 6 del Bootcamp Desarrollo Full Stack de Python, donde se implementan las funcionalidades fundamentales del framework Django para el desarrollo de aplicaciones web empresariales. El sistema permite a cada usuario gestionar sus propias tareas de forma privada, con un sistema completo de autenticación y autorización.

## Problemática Resuelta

En el contexto personal y profesional, la gestión efectiva de tareas es fundamental para la productividad. Sin embargo, muchas soluciones existentes son complejas, requieren suscripciones o no garantizan la privacidad de los datos del usuario.

Este sistema resuelve:
- **Gestión personal**: Cada usuario tiene su propio espacio privado de tareas
- **Simplicidad**: Interfaz intuitiva sin funcionalidades innecesarias
- **Seguridad**: Sistema de autenticación robusto con protección de datos
- **Accesibilidad**: Aplicación web gratuita y de código abierto
- **Privacidad**: Las tareas de cada usuario son completamente privadas

## Enfoque de Desarrollo

El proyecto siguió una metodología estructurada basada en los fundamentos de Django:

### 1. Análisis de Requisitos
- Identificación de necesidades básicas de gestión de tareas
- Definición de requerimientos de autenticación y autorización
- Planificación de modelo de datos simple pero efectivo

### 2. Diseño de Arquitectura
- Adopción del patrón MVT (Model-View-Template) de Django
- Diseño de modelo Tarea con campos esenciales
- Planificación de flujo de autenticación (registro, login, logout)

### 3. Desarrollo por Capas

**Capa de Datos:**
- Implementación del modelo Tarea para el panel admin
- Sistema de almacenamiento en memoria para demostración
- Configuración de base de datos SQLite

**Capa de Lógica:**
- Desarrollo de vistas para operaciones CRUD
- Implementación de sistema de autenticación con django.contrib.auth
- Creación de decoradores @login_required para protección de rutas
- Funciones auxiliares en utils.py

**Capa de Presentación:**
- Sistema de templates con herencia (base.html)
- Formularios Django con validación integrada
- Integración de Bootstrap para diseño responsivo
- Feedback visual para acciones del usuario

### 4. Implementación de Seguridad
- Configuración de protección CSRF
- Validación de formularios con Django Forms
- Hash automático de contraseñas con PBKDF2
- Control de acceso basado en usuario autenticado

### 5. Testing y Refinamiento
- Pruebas de funcionalidad de autenticación
- Validación de operaciones CRUD
- Verificación de aislamiento de datos entre usuarios
- Testing de interfaz en diferentes navegadores

### 6. Documentación
- Creación de README detallado
- Documentación de investigación en INVESTIGACION_DJANGO.md
- Comentarios en código para mantenibilidad
- Configuración de .gitignore para buenas prácticas

### Buenas Prácticas Aplicadas
- Separación de responsabilidades (MVT)
- Código DRY con sistema de templates
- Protección de rutas sensibles
- Validación de datos en servidor
- Control de versiones desde el inicio
- Configuración preparada para producción
## Características Principales

### Funcionalidades Implementadas

- **Sistema de autenticación completo**

  - Registro de nuevos usuarios
  - Inicio de sesión seguro
  - Cierre de sesión
  - Protección de rutas con decorador `@login_required`
- **Gestión de tareas**

  - Crear nuevas tareas con título y descripción
  - Visualizar lista de tareas personales
  - Ver detalle completo de cada tarea
  - Eliminar tareas con confirmación
- **Seguridad y privacidad**

  - Cada usuario solo puede ver y gestionar sus propias tareas
  - Protección CSRF en todos los formularios
  - Validación de datos con Django Forms
  - Contraseñas hasheadas automáticamente
- **Panel de administración**

  - Panel admin de Django configurado y personalizado
  - Gestión de usuarios y tareas desde el admin
  - Modelo de datos registrado y funcional
- **Interfaz de usuario**

  - Diseño responsivo con Bootstrap 5.3
  - Navegación intuitiva
  - Feedback visual para acciones del usuario
  - Plantillas con sistema de herencia

## Tecnologías Utilizadas

- **Python 3.12**
- **Django 5.2.7**
- **Bootstrap 5.3** (CDN)
- **HTML5 / CSS3**
- **Git / GitHub**

## Arquitectura del Proyecto

El proyecto sigue el patrón arquitectónico **MVT (Model-View-Template)** de Django:

- **Models**: Definición del modelo Tarea para el panel de administración
- **Views**: Lógica de negocio para gestión de tareas y autenticación
- **Templates**: Interfaces HTML dinámicas con sistema de herencia
- **Forms**: Validación y procesamiento de datos de usuario
- **Utils**: Funciones auxiliares para almacenamiento en memoria

## Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git

## Instalación y Configuración

### 1. Clonar el repositorio

```bash
git clone https://github.com/Linwi-V/Evaluacion_PortafolioM6.git
cd Evaluacion_Portafolio
```

### 2. Crear y activar entorno virtual

**En Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**En Mac/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar migraciones

```bash
python manage.py migrate
```

### 5. Crear superusuario (para acceder al panel admin)

```bash
python manage.py createsuperuser
```

Seguir las instrucciones para crear usuario administrador.

### 6. Ejecutar el servidor de desarrollo

```bash
python manage.py runserver
```

### 7. Acceder a la aplicación

- **Aplicación principal**: http://127.0.0.1:8000/
- **Panel de administración**: http://127.0.0.1:8000/admin/

## Estructura del Proyecto

```
Portafolio_Modulo6/
├── manage.py
├── requirements.txt
├── README.md
├── INVESTIGACION_DJANGO.md
├── .gitignore
├── gestor_tareas/              # Configuración del proyecto
│   ├── settings.py            # Configuraciones generales
│   ├── urls.py                # URLs principales
│   └── wsgi.py
└── tareas/                     # Aplicación principal
    ├── models.py              # Modelo Tarea para admin
    ├── views.py               # Lógica de vistas
    ├── urls.py                # URLs de la aplicación
    ├── forms.py               # Formularios Django
    ├── utils.py               # Funciones de utilidad
    ├── admin.py               # Configuración del panel admin
    └── templates/
        └── tareas/
            ├── base.html           # Plantilla base
            ├── lista_tareas.html   # Lista de tareas
            ├── crear_tarea.html    # Formulario de creación
            ├── detalle_tarea.html  # Detalle de tarea
            ├── login.html          # Inicio de sesión
            └── registro.html       # Registro de usuarios
```

## Funcionalidades Técnicas Implementadas

### Sistema de Plantillas Django

El proyecto utiliza el sistema de plantillas de Django con herencia para evitar duplicación de código:

- **base.html**: Plantilla principal con navbar y estructura general
- Plantillas específicas que extienden la base
- Sistema de bloques para contenido dinámico
- Integración de Bootstrap para diseño responsivo

### Formularios Django

Implementación de Django Forms para validación y procesamiento de datos:

- **TareaForm**: Formulario para crear tareas con validación integrada
- **UserCreationForm**: Formulario de registro de Django (modificado)
- **AuthenticationForm**: Formulario de inicio de sesión
- Tokens CSRF para seguridad
- Validación automática de datos

### Autenticación y Autorización

Sistema completo de autenticación utilizando django.contrib.auth:

- Registro de usuarios con validación de contraseñas
- Login/Logout con redirecciones configuradas
- Decorador `@login_required` para proteger vistas
- Gestión de sesiones
- Cada usuario accede solo a sus datos

### Panel de Administración

Configuración del panel admin de Django:

- Modelo Tarea registrado en el admin
- Personalización de la vista de lista
- Filtros y búsqueda configurados
- Gestión completa de usuarios y permisos

## Almacenamiento de Datos

**Almacenamiento en memoria** (para la aplicación principal)

- Lista Python en `utils.py` que almacena tareas durante la sesión
- Datos se pierden al reiniciar el servidor
- Implementado para cumplir con los requisitos del módulo

## Seguridad Implementada

- **Protección CSRF**: Tokens en todos los formularios
- **Autenticación requerida**: Decoradores en vistas protegidas
- **Validación de datos**: Django Forms con validación automática
- **Contraseñas seguras**: Hash automático con PBKDF2
- **Escape automático**: Protección XSS en templates
- **Control de acceso**: Usuarios solo acceden a sus propios datos

## Configuración para Producción

El archivo `settings.py` incluye comentarios para configuración de producción:

- DEBUG configurado para desarrollo
- ALLOWED_HOSTS preparado para producción
- Configuraciones de seguridad comentadas y documentadas
- SECRET_KEY debe moverse a variables de entorno en producción

## Documentación Adicional

Para más información sobre Django y las decisiones técnicas del proyecto, consultar:

- [INVESTIGACION_DJANGO.md](INVESTIGACION_DJANGO.md) - Investigación completa sobre el framework

## Aprendizajes Clave

Durante el desarrollo de este proyecto se aplicaron los siguientes conceptos:

1. Arquitectura MVT de Django
2. Sistema de templates con herencia
3. Formularios Django y validación
4. Autenticación y autorización
5. Panel de administración personalizado
6. Seguridad en aplicaciones web
7. Git y control de versiones
8. Buenas prácticas de documentación

## Autor

**Linwi Vargas** - Productor de Videojuegos en formación

- GitHub: [@Linwi-V](https://github.com/Linwi-V)
- LinkedIn: [Linwi Vargas Campos](https://www.linkedin.com/in/linwi-vargas-campos/)
- Itch.io: [linwi.itch.io](https://linwi.itch.io/)

Proyecto desarrollado como parte del Bootcamp de Desarrollo Full Stack Python -  Evaluación de Portafolio Módulo 6

## Licencia

Este proyecto es de uso educativo como parte del portafolio de aprendizaje.

## Notas

- Las tareas en la aplicación principal se almacenan en memoria y se pierden al reiniciar
- El panel admin utiliza base de datos real para demostración
- Para uso en producción se recomienda migrar completamente a persistencia en base de datos
- DEBUG debe configurarse como False en entornos de producción
