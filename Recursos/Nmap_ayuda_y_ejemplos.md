Uso: nmap [Tipo(s) de escaneo] [Opciones] {especificación de objetivos}
## ESPECIFICACIÓN DE OBJETIVOS:
Se pueden pasar nombres de host, direcciones IP, redes, etc.
Ej: scanme.nmap.org, microsoft.com/24, 192.168.0.1; 10.0.0-255.1-254

* -iL <nombre_archivo>: Entrada desde una lista de hosts/redes.
* -iR <num_hosts>: Elegir objetivos al azar.
* --exclude <host1[,host2][,host3],...>: Excluir hosts/redes.
* --excludefile <archivo_exclusión>: Excluir lista desde un archivo.

## DOSCUBRIMIENTO DE HOSTS:

* -sL: Escaneo de lista - simplemente lista los objetivos a escanear.
* -sn: Escaneo de Ping - desactiva el escaneo de puertos.
* -Pn: Trata a todos los hosts como en línea - omite el descubrimiento de hosts.
* -PS/PA/PU/PY[lista_puertos]: Descubrimiento TCP SYN, TCP ACK, UDP o SCTP a los puertos indicados.
* -PE/PP/PM: Descubrimiento mediante solicitudes ICMP echo, timestamp y netmask.
* -PO[lista_protocolos]: Ping de protocolo IP.
* -n/-R: No realizar resolución DNS nunca / Realizarla siempre [por defecto: a veces].
* --dns-servers <serv1[,serv2],...>: Especificar servidores DNS personalizados.
* --system-dns: Utilizar el resolutor DNS del sistema operativo.
* --traceroute: Trazar la ruta de saltos hacia cada host.

## TÉCNICAS DE ESCANEO:

* -sS/sT/sA/sW/sM: Escaneos TCP SYN/Connect()/ACK/Window/Maimon.
* -sU: Escaneo UDP.
* -sN/sF/sX: Escaneos TCP Null, FIN y Xmas.
* --scanflags <flags>: Personalizar las banderas (flags) del escaneo TCP.
* -sI <host_zombie[:puerto_sondeo]>: Escaneo pasivo (Idle scan).
* -sY/sZ: Escaneos SCTP INIT/COOKIE-ECHO.
* -sO: Escaneo de protocolos IP.
* -b <host_relevo_FTP>: Escaneo de rebote FTP (FTP bounce).

## ESPECIFICACIÓN DE PUERTOS Y ORDEN DE ESCANEO:

* -p <rango_puertos>: Escanear solo los puertos especificados. Ej: -p22; -p1-65535; -p U:53,111,137,T:21-25,80,139,8080,S:9
* --exclude-ports <rango_puertos>: Excluir los puertos especificados del escaneo.
* -F: Modo rápido - Escanea menos puertos que el escaneo por defecto.
* -r: Escanear puertos secuencialmente - no aleatorizar.
* --top-ports <número>: Escanear los <número> puertos más comunes.
* --port-ratio <proporción>: Escanear puertos más comunes que la <proporción> indicada.

## DETECCIÓN DE SERVICIOS/VERSIONES:

* -sV: Sondear puertos abiertos para determinar información de servicio/versión.
* --version-intensity <nivel>: Establecer de 0 (ligero) a 9 (probar todas las sondas).
* --version-light: Limitar a las sondas más probables (intensidad 2).
* --version-all: Probar cada una de las sondas (intensidad 9).
* --version-trace: Mostrar actividad detallada del escaneo de versiones (para depuración).

## ESCANEO CON SCRIPTS (NSE):

* -sC: Equivalente a --script=default.
* --script=<scripts_Lua>: <scripts_Lua> es una lista separada por comas de directorios, archivos de script o categorías de script.
* --script-args=<n1=v1,[n2=v2,...]>: Proporcionar argumentos a los scripts.
* --script-args-file=nombre_archivo: Proporcionar argumentos de script NSE en un archivo.
* --script-trace: Mostrar todos los datos enviados y recibidos.
* --script-updatedb: Actualizar la base de datos de scripts.
* --script-help=<scripts_Lua>: Mostrar ayuda sobre los scripts.

## DETECCIÓN DE SISTEMA OPERATIVO (OS):

* -O: Activar la detección de sistema operativo.
* --osscan-limit: Limitar la detección de OS a objetivos prometedores.
* --osscan-guess: Adivinar el OS de forma más agresiva.

## TIEMPO Y RENDIMIENTO:
Las opciones que toman un <tiempo> se expresan en segundos, o se puede añadir 'ms' (milisegundos), 's' (segundos), 'm' (minutos) o 'h' (horas) al valor (ej. 30m).

* -T<0-5>: Establecer plantilla de tiempo (más alto es más rápido).
* --min-hostgroup/max-hostgroup <tamaño>: Tamaños de grupo para el escaneo paralelo de hosts.
* --min-parallelism/max-parallelism <num_sondas>: Paralelización de sondas.
* --min-rtt-timeout/max-rtt-timeout/initial-rtt-timeout <tiempo>: Especifica el tiempo de ida y vuelta (RTT) de la sonda.
* --max-retries <intentos>: Limita el número de retransmisiones de sondas de escaneo de puertos.
* --host-timeout <tiempo>: Desistir del objetivo después de este tiempo.
* --scan-delay/--max-scan-delay <tiempo>: Ajustar el retraso entre sondas.
* --min-rate <número>: Enviar paquetes no más lento que <número> por segundo.
* --max-rate <número>: Enviar paquetes no más rápido que <número> por segundo.

## EVASIÓN DE CORTAFUEGOS/IDS Y SUPLANTACIÓN (SPOOFING):

* -f; --mtu <val>: Fragmentar paquetes (opcionalmente con la MTU indicada).
* -D <señuelo1,señuelo2[,ME],...>: Ocultar un escaneo con señuelos (decoys).
* -S <Dirección_IP>: Suplantar la dirección de origen.
* -e <interfaz>: Usar la interfaz especificada.
* -g/--source-port <num_puerto>: Usar el número de puerto de origen indicado.
* --proxies <url1,[url2],...>: Reenviar conexiones a través de proxies HTTP/SOCKS4.
* --data <cadena_hex>: Añadir una carga útil (payload) personalizada en hexadecimal a los paquetes enviados.
* --data-string <cadena>: Añadir una cadena ASCII personalizada a los paquetes enviados.
* --data-length <num>: Añadir datos aleatorios a los paquetes enviados.
* --ip-options <opciones>: Enviar paquetes con las opciones IP especificadas.
* --ttl <val>: Establecer el campo de tiempo de vida (TTL) de IP.
* --spoof-mac <dirección_mac/prefijo/nombre_proveedor>: Suplantar tu dirección MAC.
* --badsum: Enviar paquetes con una suma de verificación (checksum) TCP/UDP/SCTP falsa.

## SALIDA (OUTPUT):

* -oN/-oX/-oS/-oG <archivo>: Guarda el escaneo en formato normal, XML, s|<rIpt kIddi3 y Grepable, respectivamente, en el archivo indicado.
* -oA <nombre_base>: Guarda en los tres formatos principales a la vez.
* -v: Aumentar el nivel de detalle / verbosidad (usar -vv o más para un mayor efecto).
* -d: Aumentar el nivel de depuración (usar -dd o más para un mayor efecto).
* --reason: Mostrar la razón por la que un puerto está en un estado particular.
* --open: Mostrar solo los puertos abiertos (o posiblemente abiertos).
* --packet-trace: Mostrar todos los paquetes enviados y recibidos.
* --iflist: Imprimir las interfaces y rutas del host (para depuración).
* --append-output: Añadir al final de los archivos de salida en lugar de sobrescribirlos.
* --resume <nombre_archivo>: Reanudar un escaneo abortado.
* --noninteractive: Desactivar interacciones en tiempo de ejecución a través del teclado.
* --stylesheet <ruta/URL>: Hoja de estilo XSL para transformar la salida XML a HTML.
* --webxml: Referenciar la hoja de estilo de Nmap.Org para un XML más portable.
* --no-stylesheet: Evitar asociar la hoja de estilo XSL con la salida XML.

## MISCELÁNEA:

* -6: Activar el escaneo IPv6.
* -A: Activar la detección de OS, detección de versiones, escaneo con scripts y traceroute.
* --datadir <nombre_dir>: Especificar la ubicación personalizada de los archivos de datos de Nmap.
* --send-eth/--send-ip: Enviar usando tramas Ethernet sin procesar (raw) o paquetes IP.
* --privileged: Asumir que el usuario tiene privilegios totales.
* --unprivileged: Asumir que el usuario carece de privilegios de sockets sin procesar (raw).
* -V: Imprimir el número de versión.
* -h: Imprimir esta página de resumen de ayuda.

## EJEMPLOS:

* nmap -v -A scanme.nmap.org
* nmap -v -sn 192.168.0.0/16 10.0.0.0/8
* nmap -v -iR 10000 -Pn -p 80

CONSULTE LA PÁGINA DEL MANUAL (https://nmap.org/book/man.html) PARA VER MÁS OPCIONES Y EJEMPLOS.
------------------------------
Si estás preparando un comando específico, dime qué tipo de escaneo quieres hacer o qué seguridad quieres evadir y puedo ayudarte a armar la línea de comandos exacta.


