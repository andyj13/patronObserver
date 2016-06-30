# Implementación del patrón observador en Python
  El sujeto específico en este caso es la clase A, que es la que contiene el vector general donde se guardan los vectores que se van agregando.
  Cada vez que se agrega un vector a la clase A, por medio de opciones se puede determinar qué operaciones se desea que realice y es cuando se actualiza la lista de observadores.
  Al realizar la o las operaciones elegidas se verifica qué operación es la que el observador específico está dando seguimiento (si es una suma o una resta o ambas) y se da la notificación según la operación que haya elegido.
  
  
  Se delegó la tarea de las operaciones para que fuera más sencillo modificar el programa y agregar más operaciones como multiplicaciones o divisiones. Se tiene un supertipo llamado <Operaciones> en las cuales se pueden implementar las operaciones que se requieran; para este ejercicio solo se implementaron las operaciones Suma y Resta.
  
## Integrantes:
  -Pablo Garzona    1503309
  -Luis Makepeace   1567612
  -Andy Velásquez   1584613
