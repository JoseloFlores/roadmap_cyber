**Módulo Complementario - <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a> (Puerta de Enlace)**

**Nivel:** Principiante → Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> Nivel 1

**Objetivos de aprendizaje**

Al finalizar este módulo deberías poder:

-   Comprender qué es un <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>.

-   Entender por qué existe.

-   Saber cuándo interviene en una comunicación.

-   Comprender la relación entre <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>, Máscara y <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>.

-   Entender cómo aparece en los logs de un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>.

-   Identificar ataques relacionados con el <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>.

-   Saber cómo defenderlo.

**1. ¿Qué significa <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>?**

La palabra **<a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>** significa literalmente:

**Puerta de Enlace**

Es el dispositivo que permite salir de una red para llegar a otra.

Sin <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>, una computadora solo podría comunicarse con los equipos que pertenecen a su misma subred.

**Analogía**

Imagina una ciudad.

Tu casa está en un barrio.

Puedes caminar por las calles de tu barrio sin problema.

Pero si quieres ir a otra ciudad necesitas tomar una autopista.

El acceso a esa autopista sería el <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>.

Mi Casa

↓

Calles del barrio

↓

<a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>

↓

Autopista

↓

Otra ciudad

**En una red ocurre exactamente lo mismo.**

Supongamos:

Tu PC

192.168.1.15

Servidor

192.168.1.50

Los <a href="../../GLOSARIO.md#dos" target="_blank">dos</a> pertenecen a la misma red.

La PC envía la información directamente.

El <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a> no participa.

Pero ahora quieres acceder a:

Google

142.250.xxx.xxx

Esa dirección pertenece a otra red.

Entonces ocurre:

Mi PC

↓

<a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>

↓

ISP

↓

Internet

↓

Google

Sin <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a> nunca llegarías a Internet.

**2. ¿Dónde está el <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>?**

En una casa normalmente es:

El router Wi-Fi.

Ejemplo:

Router

192.168.1.1

Todas las computadoras utilizan esa dirección como <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>.

En una empresa puede ser:

-   Router

-   Firewall

-   Router + Firewall

-   Switch de Capa 3 (Layer 3 Switch)

**3. Configuración típica**

Supongamos una PC.

<a href="../../GLOSARIO.md#ip" target="_blank">IP</a>

192.168.10.25

Máscara

255.255.255.0

<a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>

192.168.10.1

¿Qué significa?

La PC sabe que:

Su red es:

192.168.10.X

Si el destino comienza igual:

192.168.10.X

Habla directamente.

Si el destino es:

8.8.8.8

Entonces piensa:

\"Ese equipo no pertenece a mi red.\"

Por lo tanto envía el paquete al <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>.

**¿Cómo decide la PC?**

La PC realiza un razonamiento muy simple.

Pregunta:

¿El destino pertenece a mi red?

Si la respuesta es:

**Sí**

↓

Envía directamente.

Si la respuesta es:

**No**

↓

Envía al <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>.

Este proceso ocurre millones de veces por segundo en Internet.

**4. Ejemplo paso a paso**

Supongamos:

Mi PC

<a href="../../GLOSARIO.md#ip" target="_blank">IP</a>

192.168.1.25

Máscara

255.255.255.0

<a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>

192.168.1.1

Quiero comunicarme con:

192.168.1.100

La PC compara.

Los <a href="../../GLOSARIO.md#dos" target="_blank">dos</a> pertenecen a:

192.168.1

Resultado:

No utiliza el <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>.

Habla directamente.

Ahora quiero acceder a:

172.217.172.46

(Una <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> pública de un servicio de Google).

Mi computadora compara.

192.168.1.X

↓

172.217.172.X

Son redes distintas.

Entonces ocurre:

Mi PC

↓

<a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>

↓

Router ISP

↓

Internet

↓

Google

**5. ¿Qué hace realmente el <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>?**

El <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a> recibe el paquete.

Luego analiza:

-   Dirección destino.

-   Tabla de rutas.

-   Regla de firewall.

-   Política de seguridad.

Después decide:

-   Permitir.

-   Bloquear.

-   Reenviar.

-   Registrar el evento en un log.

**6. <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a> y Firewall**

En muchas empresas el <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a> y el Firewall son el mismo equipo.

Por ejemplo:

Usuarios

↓

Firewall

↓

Internet

El Firewall actúa como:

-   <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>.

-   Router.

-   Filtro de seguridad.

Cuando el tráfico llega:

El Firewall verifica:

-   ¿Está permitido?

-   ¿Existe una regla?

-   ¿Está bloqueado?

-   ¿Debe registrarse?

**7. <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a> y <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a>**

Recordemos el <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a>.

PC

192.168.1.20

↓

<a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>

↓

181.25.30.40

(<a href="../../GLOSARIO.md#ip" target="_blank">IP</a> Pública)

↓

Internet

El <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a> cambia la <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> privada por la <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> pública mediante <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a> para que el tráfico pueda viajar por Internet y regresar correctamente.

**8. ¿Cómo aparece en un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>?**

En un <a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a> es muy común ver registros como:

Origen

192.168.10.15

↓

<a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>

192.168.10.1

↓

Destino

8.8.8.8

↓

Puerto

53

↓

<a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>

Como analista debes interpretar:

-   Equipo interno.

-   Sale por el <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>.

-   Consulta <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>.

-   Parece tráfico normal.

Otro ejemplo:

192.168.10.25

↓

<a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>

↓

185.xxx.xxx.xxx

↓

Puerto 4444

Como analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> pensarías:

-   ¿Qué proceso inició la conexión?

-   ¿El usuario debería conectarse a esa <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>?

-   ¿El puerto 4444 está autorizado?

-   ¿Podría ser un malware comunicándose con un servidor C2?

**9. ¿Cómo puede atacar un ciberdelincuente el <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>?**

**Ataque 1 -- Cambiar el <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>**

Un malware modifica la configuración de red.

Antes:

<a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>

192.168.1.1

Después:

<a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>

192.168.1.200

El atacante controla esa <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>.

Todo el tráfico pasa por él.

Esto facilita un ataque de **Man-in-the-Middle (<a href="../../GLOSARIO.md#mitm" target="_blank">MitM</a>)**.

**Ataque 2 -- <a href="../../GLOSARIO.md#arp" target="_blank">ARP</a> Spoofing**

El atacante envía respuestas <a href="../../GLOSARIO.md#arp" target="_blank">ARP</a> falsas diciendo:

\"Yo soy el <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>.\"

Las víctimas comienzan a enviarle el tráfico.

El atacante puede:

-   Espiar.

-   Modificar.

-   Bloquear comunicaciones.

**Ataque 3 -- Comprometer el Router o Firewall**

Si el <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a> tiene una vulnerabilidad o credenciales débiles, un atacante podría:

-   Cambiar reglas de firewall.

-   Redirigir tráfico.

-   Abrir puertos.

-   Capturar información.

Por eso proteger el <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a> es crítico.

**10. ¿Cómo defender el <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>?**

-   Cambiar las contraseñas por defecto.

-   Mantener el firmware actualizado.

-   Limitar el acceso administrativo.

-   Habilitar autenticación multifactor cuando sea posible.

-   Monitorear cambios en la configuración.

-   Revisar periódicamente las tablas <a href="../../GLOSARIO.md#arp" target="_blank">ARP</a> y de rutas.

-   Utilizar ACL y reglas de firewall con el principio de menor privilegio.

-   Registrar eventos y enviarlos al <a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a>.

**11. Aplicación práctica en un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

**Ejemplo 1**

**Alerta:**

Equipo

192.168.10.50

<a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>

192.168.10.1

Destino

8.8.8.8

Puerto

53

**Interpretación:**

Consulta <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a> saliendo por el <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>. A priori es un comportamiento normal.

**Ejemplo 2**

**Alerta:**

<a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>

192.168.10.1

↓

Miles de intentos <a href="../../GLOSARIO.md#ssh" target="_blank">SSH</a>

**Interpretación:**

El <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a> está siendo atacado.

**Acciones:**

-   Revisar logs del firewall.

-   Verificar intentos exitosos y fallidos.

-   Comprobar si las credenciales administrativas fueron comprometidas.

-   Evaluar el bloqueo de las <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> de origen.

**Ejemplo 3**

**Alerta:**

Varios equipos

<a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a> configurado:

192.168.10.200

El <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a> esperado era:

192.168.10.1

**Interpretación:**

Es una alerta crítica. Puede indicar una modificación maliciosa de la configuración de red o un intento de interceptar el tráfico.

**Resumen**

**<a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>**

-   Es la puerta de salida hacia otras redes.

-   Generalmente corresponde al router, firewall o switch de capa 3.

-   Decide cómo reenviar el tráfico entre redes.

-   Es esencial para acceder a Internet.

-   Suele realizar <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a> y aplicar políticas de seguridad.

**Conceptos clave para memorizar**

  -------------------------------------------------------------------------------
  **Concepto**     **Debes recordar**
  ---------------- --------------------------------------------------------------
  <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>          Puerta de enlace hacia otras redes.

  Mismo segmento   La comunicación suele ser directa, sin pasar por el <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>.

  Otra subred      El tráfico se envía al <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>.

  <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a>              El <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a> puede traducir <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> privadas a públicas.

  Firewall         En muchas empresas también cumple el rol de <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>.

  <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>              El <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a> es una fuente clave de logs y alertas.
  -------------------------------------------------------------------------------

**💡 Consejo como tu entrenador para un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

Hay una pregunta que debes hacerte **cada vez que veas un log de red**:

**\"¿Ese paquete necesitó pasar por el <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a> o no?\"**

Si la respuesta es **no**, probablemente la comunicación fue dentro de la misma subred.

Si la respuesta es **sí**, entonces el tráfico cruzó un límite entre redes, y allí es donde suelen actuar el router o el firewall. Eso significa que probablemente existan **logs, reglas de filtrado, traducción <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a> o políticas de seguridad** que puedes revisar durante una investigación.

Ese hábito mental es muy valioso en un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> porque te ayuda a reconstruir el recorrido del tráfico y a entender **dónde buscar evidencias** cuando investigas un incidente.

**Evaluación -- Módulo Complementario: <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a> (Nivel <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>)**

**10 preguntas Multiple Choice**

**Instrucciones:** Responde sin consultar el material. Al finalizar encontrarás las respuestas con su justificación.

**Pregunta 1**

¿Qué es un <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>?

**A)** Un servidor <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>.

**B)** La puerta de enlace que permite comunicar una red con otras redes.

**C)** Un antivirus.

**D)** Un protocolo de Internet.

**Pregunta 2**

En una red doméstica, el <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a> suele ser:

**A)** La impresora.

**B)** El router Wi-Fi.

**C)** El monitor.

**D)** El switch.

**Pregunta 3**

¿Cuándo utiliza una computadora el <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>?

**A)** Siempre.

**B)** Solo cuando se comunica con equipos de otra red o subred.

**C)** Nunca.

**D)** Solo cuando imprime documentos.

**Pregunta 4**

Una PC tiene la siguiente configuración:

<a href="../../GLOSARIO.md#ip" target="_blank">IP</a>

192.168.1.20

Máscara

255.255.255.0

<a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>

192.168.1.1

Quiere comunicarse con:

192.168.1.80

¿Qué ocurre?

**A)** Utiliza el <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>.

**B)** Se comunica directamente con el destino.

**C)** Debe salir a Internet.

**D)** La comunicación es imposible.

**Pregunta 5**

La misma PC ahora quiere acceder a:

8.8.8.8

¿Qué hace?

**A)** Envía el tráfico al <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>.

**B)** Se comunica directamente.

**C)** Cambia su dirección <a href="../../GLOSARIO.md#ip" target="_blank">IP</a>.

**D)** Utiliza el <a href="../../GLOSARIO.md#broadcast" target="_blank">Broadcast</a>.

**Pregunta 6**

¿Qué función adicional suele realizar un <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a> empresarial?

**A)** Traducir direcciones mediante <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a>.

**B)** Fabricar direcciones <a href="../../GLOSARIO.md#mac" target="_blank">MAC</a>.

**C)** Cambiar la velocidad del disco duro.

**D)** Crear usuarios en Windows.

**Pregunta 7**

¿Qué ataque intenta hacer que los equipos crean que el atacante es el <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>?

**A)** SQL Injection.

**B)** Phishing.

**C)** <a href="../../GLOSARIO.md#arp" target="_blank">ARP</a> Spoofing.

**D)** XSS.

**Pregunta 8**

Como analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> observas:

<a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a> configurado

192.168.1.200

Valor esperado

192.168.1.1

¿Qué sospechas?

**A)** Una actualización de Windows.

**B)** Una posible modificación maliciosa de la configuración de red.

**C)** Un cambio de fondo de pantalla.

**D)** Una actualización del navegador.

**Pregunta 9**

¿Por qué el <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a> es una fuente importante de información para un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>?

**A)** Porque normalmente registra el tráfico que entra y sale de la red.

**B)** Porque guarda las contraseñas de los usuarios.

**C)** Porque almacena los documentos de la empresa.

**D)** Porque crea direcciones <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> públicas.

**Pregunta 10**

¿Cuál sería la primera pregunta que debería hacerse un Analista <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> al investigar una comunicación de red?

**A)** ¿Qué marca tiene la computadora?

**B)** ¿El tráfico necesitó pasar por el <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>?

**C)** ¿Qué color tiene el cable de red?

**D)** ¿Cuántos años tiene el usuario?

**Respuestas y Justificación**

**1) ✅ B**

El <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a> conecta una red con otras redes y actúa como punto de salida hacia Internet u otras subredes.

**2) ✅ B**

En la mayoría de los hogares, el router Wi-Fi cumple la función de <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>.

**3) ✅ B**

El <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a> solo interviene cuando el destino está fuera de la subred local.

**4) ✅ B**

Ambos equipos pertenecen a la red **192.168.1.0/24**, por lo que se comunican directamente sin utilizar el <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>.

**5) ✅ A**

La dirección **8.8.8.8** pertenece a otra red, por lo que la PC envía el tráfico al <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>.

**6) ✅ A**

Además de enrutar tráfico, muchos Gateways realizan **<a href="../../GLOSARIO.md#nat" target="_blank">NAT</a>**, permitiendo que varias <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> privadas compartan una <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> pública.

**7) ✅ C**

El **<a href="../../GLOSARIO.md#arp" target="_blank">ARP</a> Spoofing** engaña a los equipos haciéndoles creer que el atacante es el <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>, facilitando ataques de tipo **Man-in-the-Middle (<a href="../../GLOSARIO.md#mitm" target="_blank">MitM</a>)**.

**8) ✅ B**

Un cambio inesperado del <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a> puede indicar una configuración maliciosa o un intento de interceptar el tráfico.

**9) ✅ A**

El <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a> suele ser un router o firewall que registra conexiones, reglas aplicadas, bloqueos y traducciones <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a>, convirtiéndose en una fuente clave de evidencia para un <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>.

**10) ✅ B**

La primera pregunta ayuda a orientar la investigación:

-   **Si el tráfico no pasó por el <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>**, probablemente ocurrió dentro de la misma subred.

-   **Si pasó por el <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>**, es posible revisar logs del router o firewall, reglas de seguridad, <a href="../../GLOSARIO.md#nat" target="_blank">NAT</a> y eventos registrados.

**🎯 Consejo como tu instructor de <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a>**

Hasta este punto ya dominas los fundamentos de redes que más se utilizan en un **<a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> Nivel 1**:

-   ✅ Direcciones <a href="../../GLOSARIO.md#ip" target="_blank">IP</a> públicas y privadas.

-   ✅ Modelo <a href="../../GLOSARIO.md#osi" target="_blank">OSI</a>.

-   ✅ Modelo <a href="../../GLOSARIO.md#tcp" target="_blank">TCP</a>/<a href="../../GLOSARIO.md#ip" target="_blank">IP</a>.

-   ✅ Máscaras de subred.

-   ✅ Subredes.

-   ✅ <a href="../../GLOSARIO.md#gateway" target="_blank">Gateway</a>.

A partir del siguiente módulo, te recomiendo comenzar con **Puertos y Protocolos de Red (<a href="../../GLOSARIO.md#http" target="_blank">HTTP</a>, <a href="../../GLOSARIO.md#https" target="_blank">HTTPS</a>, <a href="../../GLOSARIO.md#dns" target="_blank">DNS</a>, <a href="../../GLOSARIO.md#ssh" target="_blank">SSH</a>, <a href="../../GLOSARIO.md#ftp" target="_blank">FTP</a>, <a href="../../GLOSARIO.md#smtp" target="_blank">SMTP</a>, RDP, SMB, etc.)**. Es uno de los temas que más aparece en entrevistas técnicas para <a href="../../GLOSARIO.md#soc" target="_blank">SOC</a> y en las alertas reales de herramientas como **Splunk**, **Microsoft Sentinel**, **QRadar** o **Elastic <a href="../../GLOSARIO.md#siem" target="_blank">SIEM</a>**. Ahí empezarás a conectar toda la teoría de redes con incidentes reales.
