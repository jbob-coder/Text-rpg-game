# THE GAME — Registro de errores: pixel art, alcance y ejecución
Fecha: 2026-10-27 (America/Puerto_Rico)  
Estado: **INCIDENTE DOCUMENTADO / LIMPIEZA NO EJECUTADA NI VALIDADA**  
Repositorio: `jbob-coder/Text-rpg-game`  
Rama de autoridad: `docs/master-game-development-program`  
HEAD de autoridad comprobado: `dac5d22cdbe211d0d35d3df98b542be2653f1b85`  
Rama de trabajo: `cleanup/remove-pixel-art-20261027`

## Directiva vigente del propietario

El propietario rechazó explícitamente la dirección pixel art de THE GAME y pidió **borrar todo lo relacionado con pixel art**; después ordenó **documentar los errores**. Estas instrucciones recientes sustituyen la suposición de que documentos antiguos de diseño visual siguen siendo la decisión vigente. No debe cambiarse ni borrarse el RPG narrativo, su estado, reglas, guardado o contenido por confundir la presentación con el motor.

**Definición de alcance de la limpieza:** retirar de la implementación y documentación activa la presentación pixel art: assets PNG asociados, catálogos/renderizadores y animaciones exclusivas de ese estilo, pruebas exclusivas de ese renderer, nombres/build/workflow que lo presenten como estilo obligatorio, y mandatos documentales incompatibles. La aplicación Android, si se conserva, debe tener antes o en el mismo cambio un consumidor no-pixel funcional del motor. La eliminación de archivos en una rama NO implica su purga del historial Git.

## Hechos de repositorio constatados

- `README.md` declara una experiencia RPG basada en texto; `src/textrpg/cli.py` renderiza escena, descripción y opciones numéricas. Su ruta jugable se ejecuta con `PYTHONPATH=src python -m textrpg.cli content/vertical_slice_01.json --save local_save.json`.
- La rama de autoridad contiene código de un cliente Android Compose con pixel art. `MainActivity.kt` importa `TheGamePixelTheme` y `TheGameRoot` del UI pixel. `GameScreen.kt` consume numerosas clases `Pixel*`, incluido un renderer de escenas y avatar. Por tanto, borrar indiscriminadamente `Pixel*.kt` rompe referencias de compilación.
- Inventario de rutas observado en el árbol de ese HEAD: **24 archivos PNG** en `android/app/src/main/res/drawable-nodpi/`; **39 archivos Kotlin principales Android**, incluidos múltiples catálogos `Pixel*`; **30 Kotlin unit-test**, varios específicos del pixel art; **3 instrumented tests**, de los cuales hay expectativas visuales del renderer. Son recuentos de rutas, NO tests ejecutados.
- `docs/VISUAL_BIBLE.md`, `docs/assets/PIXEL_ASSET_MASTER_PLAN.md` y `docs/assets/PIXEL_ART_RUNTIME_COMPOSITION_STANDARD.md` exigen pixel art. Son evidencia de una dirección *documentada anteriormente*, no autorización para contradecir la instrucción actual del propietario.
- El código gráfico o un caso de prueba que espera un sprite **no prueban** que el APK concreto del usuario tenga visuales ni que esos elementos estén verificados en dispositivo.
- PR [#86](https://github.com/jbob-coder/Text-rpg-game/pull/86): **CLOSED / UNMERGED**. Sus dos archivos añadidos se retiraron de la rama de trabajo anterior. No se integraron en la rama de autoridad.
- La rama `cleanup/remove-pixel-art-20261027` se creó a partir de `dac5d22...`. **Antes de este registro**, la comparación con la rama de autoridad devolvió `identical`: cero archivos diferentes. Se creó un blob Git con un prototipo de pantalla de texto (`94d93df976e016f125abac220912cf68fe46d782`), pero **no se añadió al árbol ni se ejecutó**. Crear un blob no equivale a actualizar la aplicación.
- No se ha ejecutado en esta actividad un build Android, tests Python/Kotlin, emulador, captura de pantalla ni instalación APK. No atribuir `PASS` a pruebas no ejecutadas.

## Errores observados

| ID | Error | Manifestación / daño | Corrección exigida | Estado |
| --- | --- | --- | --- | --- |
| E-01 | **Ignorar el objetivo del usuario** | En lugar de trabajar sobre la experiencia del RPG, el asistente desvió reiteradamente la conversación hacia sprites y auditorías no solicitadas. | Tomar la instrucción explícita del propietario como prioridad y limitar el trabajo a su alcance. | RECONOCIDO |
| E-02 | **Confundir código existente con funciones disponibles** | Se describió como visualmente integrado algo que sólo se había leído en código y documentación; no se comprobó el APK del usuario. | Etiquetar por separado: `FUENTE`, `INTEGRADO`, `BUILD VERIFICADO`, `DISPOSITIVO VERIFICADO`. | RECONOCIDO; dispositivo NO VERIFICADO |
| E-03 | **Interpretar contratos documentales antiguos como mandato actual** | La documentación pixel art se trató como obligación pese al rechazo explícito del propietario. | Invalidar esas órdenes visuales en la documentación activa y dejar constancia de la revocación. | PENDIENTE MIGRACIÓN |
| E-04 | **Crear trabajo no solicitado y ruido en GitHub** | Se creó una auditoría/prueba y PR #86 en vez de corregir el problema pedido. | PR #86 cerrada sin merge; retirar residuos de trabajo y no crear derivados innecesarios. | REVERTIDO EN SU RAMA |
| E-05 | **Responder con promesas y progreso en vez de resultados** | Reiterados mensajes de «revisar con calma» y «trabajando» no distinguieron trabajo planeado de cambios integrados. | Registrar SHA, archivos realmente cambiados, comandos y resultados por etapa; no llamar «terminado» a un plan. | RECONOCIDO |
| E-06 | **Riesgo de borrado destructivo sin mapa de dependencias** | Borrar las clases `Pixel*` de Android sin reemplazar `MainActivity`/`GameScreen`, renderizadores y pruebas dejaría referencias irresueltas o impediría producir APK. | Sustituir primero el consumidor Android por UI textual y aplicar una eliminación coherente; verificar compilación y pruebas antes de merge. | ABIERTO |
| E-07 | **Riesgo de arrastrar pixel art desde docs/CI** | Aunque se eliminen sprites del código, README, documentación, manifests, screenshots, workflow y versión `0.1.0-pixel-client-v1` pueden perpetuar el diseño rechazado. | Auditar referencias restantes en fuentes, tests, build y docs, y cambiar sólo las que formen parte de esta línea visual. | ABIERTO |
| E-08 | **No establecer evidencia ejecutable antes de afirmar integración** | Inspecciones estáticas y pruebas escritas se confundieron con comportamiento confirmado en ejecución. | Ejecutar `PYTHONPATH=src python -m unittest discover -s tests -v`; ejecutar pruebas/compilación Android, conservar logs y distinguir limitaciones ambientales. | NO EJECUTADO |
| E-09 | **Riesgo de borrar datos o contratos ajenos al pixel art** | `src/textrpg/visuals.py`, `room_projection.py`, los registros `GameSnapshot` y `content/vertical_slice_01_room_presence.json` pueden transportar identidad/presencia semántica, no únicamente sprites. | Conservar reglas, save schema, IDs, información player-safe y contenido narrativo salvo migración específica con evidencia. | CONTROL DE ALCANCE |
| E-10 | **No registrar previamente dueño/conflictos para cambios relevantes** | Se inició trabajo de PR #86 sin seguir plenamente el circuito de coordinación de `AGENTS.md`. | Antes de integrar cambios de Android cruzados con documentación, comprobar Bulletin, coordinación y políticas de merge; no usurpar tareas de otros agentes. | RECONOCIDO |

## Falla técnica que se evita deliberadamente

Si se eliminan los 24 PNG y el catálogo `PixelAssetCatalog.kt` dejando la aplicación Compose actual intacta, las referencias a clases y recursos `R.drawable.pixel_*` permanecerán en la UI. La eliminación aislada rompe el contrato de compilación y no resuelve el objetivo «THE GAME sin pixel art».

### Migración segura y verificable (pendiente, no confundirse con trabajo ejecutado)

1. Mantener sin cambios el motor de decisiones y los contratos de `GameSnapshot`, estado, NPC, inventario, misiones y guardado.
2. Crear el reemplazo **textual/no-pixel** para la raíz Android y todas las acciones actuales: elegir, ver estado, equipar, viajar, guardar/cargar y accesibilidad. No inventar mecánicas.
3. Retirar los renderizadores y catálogos exclusivos de pixel art, las 24 PNG, las pruebas de estilo sustituido; actualizar los tests de acciones reales de la nueva interfaz.
4. Eliminar de la **documentación activa** el mandato de pixel art y sus planes de producción como decisiones vigentes; conservar el mínimo registro histórico que explique por qué se descartó esa dirección, sin presentarlo como requerimiento actual.
5. Actualizar versión, workflows de CI, referencias de documentación y cualquier lista de recursos de APK que dependan del estilo anterior.
6. Ejecutar suites Python y Android, build, smoke de inicio/elecciones/save-load. Inspeccionar el APK en emulador o dispositivo; si no se pudo probar, marcar explícitamente `NO VERIFICADO`. No publicar ni fusionar una versión rota.
7. Comparar contra la rama de autoridad viva y someter la sustitución a revisión antes de merge. No borrar repositorio completo, datos de usuario, historia Git ni otras ramas.

## Estado de ejecución al redactar este registro

**Completado:** revisión del repositorio y de la PR #86, identificación de dependencias e inventario de fuentes; documentación de errores en esta rama de limpieza.

**No completado:** eliminación e integración del pixel art, sustitución comprobada del cliente Android, compilación, tests, APK, verificación de teléfono, merge o cambio en la rama autoritativa.

Esta distinción es obligatoria en futuras respuestas al propietario.
