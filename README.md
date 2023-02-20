Cómo probar las funcionalidades de mi entrega:
* Para ver las 3 clases models solicitadas solo acceder al archivo models.py 
* El boton REGISTRO MEDICOS es el formulario para ingresar datos en la DB de los medicos, la cual puede verse en la seccion medicos que se encuentra entre las secciones de arriba.
* El boton BUSQUEDA MEDICOS es el formulario para leer datos en la DB, decidí poner como id de busqueda el atributo credencial de la clase Medicos cuyo valor mínimo sea de 4 cifras entonces debe poner el número de credencial, si usted creo un usuario cuya credencial es 1234 debe buscar 1234 y aparecerá nombre apellido y la credencial correspondiente
* las herencias fueron realizadas por lo tanto podrá darse cuenta simplemente mirando los archivos 
* luego desde la admin consola puede ver que gracias al metodo magico '__str__' se visualizan los datos de cada medico creado
