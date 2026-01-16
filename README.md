## Examen Final – FastAPI + MongoDB

API REST para la gestión de Usuarios usando FastAPI y MongoDB.

## Respuestas:

1. Creo que elegír Flask es más inteligente porque te deja empezar con menos estructura y menos peso. Para un “Hola usuario” no necesitas un sistema de autenticación, panel admin, ORM, migraciones, configuración compleja, ni múltiples apps internas. Con Flask puedes tener algo funcional en un solo archivo y pocas líneas, por ejemplo una ruta que retorne un saludo. En cambio Django te obliga a crear un proyecto, configurar settings, urls, apps, etc. Eso hace el código inicial más largo y más complejo para un objetivo tan simple.


2. Porque si el cliente entrara a la cocina se romperia todo, explicandolo en puntos:

- Rompería la seguridad: podría ver información interna, tocar cosas que no debe, robar datos o alterar pedidos. En una api, eso sería como que el cliente acceda directo a la base de datos o a la lógica interna del servidor.

- Rompería el orden/estandarización: cada cliente haría pedidos a su manera, causando caos. La interfaz (mesero) existe para imponer reglas: qué se puede pedir, en qué formato, validaciones, permisos, errores claros.

Analizo que en en una API, la interfaz (endpoints) actúa como mesero: controla el acceso, valida, autentica y mantiene un flujo ordenado de datos. El servidor/cocina queda protegido y consistente.


3. Es mejor usar WebSockets cuando necesitas actualizaciones en tiempo real y bidireccionales, sin estar consultando cada segundo, se podrian dar ejemplos como:

- Juego online: posiciones de jugadores, disparos, chat, eventos del mapa. Necesitas latencia baja y mensajes constantes. Mantener la conexión abierta permite enviar/recibir cambios al instante.

- Banco (en casos puntuales): notificaciones en vivo como “tu transferencia se confirmó” o “alerta de fraude” mientras el usuario está logueado.

Por qué con la “llamada abierta” el servidor puede empujar eventos al cliente apenas ocurren, con menos retraso y menos tráfico repetido que REST.

## ✍️ Autor
___________________________________

Alfred David Paucar Principe
Cibertec / PYTHON API DEVELOPER
Fecha: 15/01/2026