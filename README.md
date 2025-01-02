# Entrega-final-FrazzettoLucas

# Proyecto Final: Blog con Django

Este proyecto es un sistema de blogs desarrollado con Django como trabajo final para el curso de Python realizado en Coderhouse. Permite la creacion, edicion, eliminacion y visualizacion de blogs, junto con un sistema de auth y gestion de usuarios.


Accede al sitio en http://127.0.0.1:8000/.
Link al video explicativo: https://drive.google.com/file/d/1j54N-9n-gd2lkLmr2cVonxB1azMExmQl/view?usp=drive_link

---

#### **. Features implementados**

1. **Sistema de blogs:**
   - Crear, editar, eliminar y listar blogs.
   - Cada blog incluye título, subtítulo, cuerpo, autor, fecha e imagen.
   - Los blogs se muestran en una lista y pueden visualizarse en detalle.

2. **Sistema de autenticación:**
   - Creacion de usuarios (`/accounts/signup/`).
   - Inicio y cierre de sesion (`/accounts/login/` y `/accounts/logout/`).
   - Gestion de perfil

3. **Diseño :**
   - Estilizado con Bootstrap 5.
   - Navbar con opciones dinamicas segun el estado del usuario (autenticado o no).

4. **Panel de administración:**
   - Acceso al panel de Django Admin para gestionar usuarios y blogs.

5. **Mensajes de confirmación:**
   - Notificaciones claras para acciones como creación, edición o eliminación de datos.

6. **Validaciones:**
   - Restricción de acceso a vistas protegidas.
   - Validaciones en formularios.


## Pruebas a realizar

1. **Autenticación:**
   - Registrar un nuevo usuario desde `/accounts/signup/`.
   - Iniciar sesión con las credenciales creadas. coderuser/coder2024
   - Cerrar sesión desde el menú desplegable.

2. **Gestión de blogs:**
   - Crear un nuevo blog desde `/blog/new/`. - Si el usuario no esta registrado lo deriva al login
   - Editar un blog existente desde `/blog/<id>/edit/`. Elegir ID desde 1 al 5 para probar edcion. Si el usuario no esta registrado lo deriva al login
   - Eliminar un blog existente desde `/blog/<id>/delete/`. Elegir ID desde 1 al 5 para probar borrado.  Si el usuario no esta registrado lo deriva al login
   - Ver el detalle de un blog en `/blog/<id>/`.

3. **Gestión de perfil:**
   - Editar el perfil desde `/accounts/profile/edit/`.
   - Editar el perfil desde Dropdown
   - Eliminar la cuenta desde `/accounts/profile/delete/`. O desde la edicion tambien se puede

4. **Validaciones:**
   - Intentar acceder a rutas protegidas sin estar autenticado (por ejemplo, `/blog/create/`) y confirmar que redirige al login. "Es importante explicar que la proteccion a veces la toma y a veces no, pero lo que necesitamos proteger lo ahcemos con @login_required
   - Probar formularios con datos incompletos y verificar los mensajes de error.

5. **Panel de administración:**
   - Acceder al panel en `/admin/` y realizar operaciones básicas. admin/m0t0n3t4
