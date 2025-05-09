# Objetivo de tener una base de datos

- Tener un sistema de cuentas (Usuario : Contraseña)

- Cada cuenta podrá:
- Tener un historial de los plan realizados en terraform
- Agregar recursos a los cuales les quiera hacer un seguimiento, especificando el tipo de seguimiento, 
    estos tipos de seguimiento pueden ser: (notify_when_destroy, notify_, seguridad, criticos)
- Poder modificar estructura ya existente sin la necesidad de hacer un apply a todos los recursos, modificando los recursos que quieran modificarse

## Creacion de la base de datos
Utilizar docker, para alojar una base de datos PostgreSQL
Utilizar flask para construir una APIRest para operar con PostgreSQL
La api de flask alojarla tambien en docker
