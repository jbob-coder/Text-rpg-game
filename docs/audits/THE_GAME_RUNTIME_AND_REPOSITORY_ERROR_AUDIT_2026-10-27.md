# THE GAME — Auditoría de errores y riesgos (verificación por fuente y CI)

**Fecha de auditoría:** 2026-10-27, zona horaria America/Puerto_Rico  
**Repositorio examinado:** `jbob-coder/Text-rpg-game` — **NO** Eirenfall, Mansion Story ni Godseed.  
**Rama de autoridad:** `docs/master-game-development-program`  
**SHA comprobado:** `dac5d22cdbe211d0d35d3df98b542be2653f1b85`  
**Rama del informe:** `audit/the-game-runtime-errors-20261027`  
**Modo:** documentación y verificación **sin modificaciones del motor, UI, contenido, assets, CI ni guardados**.

## Interpretación de estados y límites

- **CONFIRMADO — CI RED:** fallo reproducido en un ejecutor GitHub Actions sobre un commit preciso. No implica que **todos** los casos hayan sido reproducidos sobre el HEAD de autoridad.
- **CONFIRMADO — CÓDIGO:** una trayectoria causal de código está presente en el HEAD comprobado. Los efectos de usuario se consideran **pendientes de prueba en un APK**.
- **RIESGO — NECESITA PRUEBA:** el código permite una secuencia problemática en determinadas condiciones, pero la secuencia no fue ejecutada durante esta auditoría.
- **PENDIENTE — NO ES REGRESIÓN:** funcionalidad o verificación incompleta; no declarar bug sin ejecución.
- **SIN HALLAZGO:** chequeo de integridad estática sin inconsistencias observadas en los campos examinados; no demuestra ausencia total de errores.

## Hallazgos priorizados

### TG-AUD-001 — P0: carga Android no atómica; estado jugable reemplazado antes de validación

**Estado:** **CONFIRMADO — CI RED + fuente actual afectada**. Registro previo: [CPR-006](../overseer/code_problems/CPR-006_android_session_state_publication_alias_atomicity.md), OR-036.

**Fuente:** [`src/textrpg/android_bridge.py`, líneas 38–45, 191–195 y 491–494](../../src/textrpg/android_bridge.py); [`src/textrpg/persistence.py`](../../src/textrpg/persistence.py); [`tests/test_android_bridge.py`](../../tests/test_android_bridge.py).

**Causa:** `AndroidGameSession.__init__` establece `self.state = content.state` (alias mutable). `load()` hace `self.state = load_state(...); return self.scene_view()` en ese orden. `loads_state()` valida estructura, pero no la pertenencia del `scene_id` al contenido cargado. Una partida JSON estructuralmente válida con escena desconocida sustituye el estado antes de que `scene_view()` rechace la escena; el error resultante es `VIEW_ERROR`, no el `LOAD_ERROR` esperado para carga rechazada.

**Evidencia ejecutada:** [CI RED, run 37863493737](https://github.com/jbob-coder/Text-rpg-game/actions/runs/37863493737), commit test-first `808f704d81fc5d58948038f1158cc20e12464480`: **481 tests, 3 fallos**, exactamente `test_construction_detaches_live_state_from_content_template`, `test_load_unknown_authored_scene_keeps_playable_session` y `test_successful_load_keeps_content_template_detached`. [CI GREEN, run 37863439739](https://github.com/jbob-coder/Text-rpg-game/actions/runs/37863439739), commit correctivo `3b3ac9a5e8961f32a8140765d977d9c92a44b1e3`: **481/481 Python OK**; también Android unit/build y emulador correctos en ese commit.

**Estado de integración:** la corrección sigue en [PR #80](https://github.com/jbob-coder/Text-rpg-game/pull/80) **OPEN / DRAFT / UNMERGED**, rama `agent/nodus-p11-cpr006-load-atomicity`. Comparación contra autoridad: **2 commits adelante, 258 detrás** en esta revisión; la compatibilidad de merge y una pasada de CI antigua no prueban integración actual. En el HEAD de autoridad aún se ve el patrón de carga defectuoso.

**Corrección/aceptación:** construir candidato separado, validarlo contra el motor y toda la proyección player-safe **antes** de publicar; preservar identidad/snapshot anterior ante rechazo, emitir error de carga estable, mantener save schema v1 y probar con el HEAD de integración más reciente. No fusionar a ciegas la rama divergente.

### TG-AUD-002 — P1: un error recuperable puede reemplazar la pantalla de juego por la pantalla de arranque

**Estado:** **CONFIRMADO — CÓDIGO; reproducción Android pendiente**.

**Fuente:** [`GameViewModel.kt` líneas 80–141 y 303–307](../../android/app/src/main/java/com/thegame/rpg/GameViewModel.kt), [`GameScreen.kt` líneas 61–121 y 163–181](../../android/app/src/main/java/com/thegame/rpg/ui/GameScreen.kt).

**Causa:** una elección inválida, guardar/cargar sin éxito, cambiar equipo o viajar puede invocar `publishFailure()`; esta función cambia `bootState` a `BootState.Error`, pero no invalida necesariamente el snapshot del juego. `TheGameRoot` sólo pinta la partida si `bootState == Ready && snapshot != null`; en otro caso muestra `PixelBootScreen`, que no ofrece una acción de recuperación. El flujo no diferencia fallo **inicial/fatal** de fallo **de operación recuperable**.

**Impacto previsible:** pérdida de acceso a los controles de la sesión visible tras una operación fallida, incluso cuando el estado anterior podría seguir siendo válido. **No** se afirma pérdida de datos ni se afirma prueba en teléfono.

**Prueba requerida:** en test Compose/actividad arrancada, con snapshot jugable ejecutar `LOAD / CONTINUE` sin archivo, `CHOICE_ERROR`, `TRAVEL_ERROR` y `SAVE_ERROR`; exigir mensaje de error no fatal, pantalla jugable y controles disponibles, sin mutación del snapshot. Reparar en ViewModel/UI sin duplicar reglas Python.

### TG-AUD-003 — P1: bloqueo de reintento de arranque después de error temporal

**Estado:** **CONFIRMADO — CÓDIGO; impacto en dispositivo pendiente**.

**Fuente:** [`GameViewModel.kt` líneas 59–77](../../android/app/src/main/java/com/thegame/rpg/GameViewModel.kt), [`GameScreen.kt` líneas 163–181](../../android/app/src/main/java/com/thegame/rpg/ui/GameScreen.kt).

**Causa:** `startIfNeeded()` marca `startRequested = true` antes de iniciar el motor y nunca lo revierte cuando el arranque falla. El layout de error solamente presenta texto. Llamar de nuevo a `startIfNeeded()` con el mismo ViewModel no reintenta.

**Aceptación:** error recuperable ofrece retry explícito, sin sesiones duplicadas ni concurrencia; si el fallo es terminal, debe explicarse así. Prueba con `FakeGameEngine` que falla una vez y luego arranca.

### TG-AUD-004 — P2: el guardado puede terminar en disco antes de que falle la respuesta del puente

**Estado:** **RIESGO — NECESITA PRUEBA**, no falla demostrada.

**Fuente:** [`src/textrpg/android_bridge.py` líneas 486–489](../../src/textrpg/android_bridge.py), [`src/textrpg/persistence.py` función `save_state()`](../../src/textrpg/persistence.py).

**Secuencia:** el puente hace `save_state(...); return self.scene_view()` dentro de la misma operación. Si la persistencia termina correctamente, pero la proyección posterior falla, se reporta `SAVE_ERROR` aunque el archivo podría haber sido reemplazado. No contradice que `save_state` use escritura temporal + reemplazo atómico: el problema potencial es el **contrato del resultado del guardado**.

**Aceptación:** prueba de inyección de fallo entre escritura y proyección; definir si el guardado retorna éxito independiente de la visualización y mantener integridad de bytes. No asumir corrupción de archivos ordinarios.

### TG-AUD-005 — P2: elección confirmada en el motor, pero respuesta de proyección no atómica

**Estado:** **RIESGO — NECESITA PRUEBA**, no regresión confirmada.

**Fuente:** [`src/textrpg/android_bridge.py` líneas 201–206](../../src/textrpg/android_bridge.py); [`src/textrpg/core.py` `RulesEngine.choose` (aprox. líneas 325–400)](../../src/textrpg/core.py).

**Alcance causal:** `RulesEngine.choose()` sí utiliza snapshot y rollback **dentro de la aplicación de efectos**; este hecho está verificado y no debe ignorarse. Sin embargo, el puente llama a `choose(state, id)`, elimina `android.map_location_override` y **después** proyecta `scene_view()`. Un fallo posterior de proyección no está protegido por ese rollback del motor.

**Aceptación:** inyectar un fallo de proyección tras una elección válida y comprobar el contrato deseado (respuesta, estado y retry) antes de cambiar código. No reportar mutación corrupta real sin ejecución.

### TG-AUD-006 — P1 documental/de producto: la documentación exige pixel art pese a la instrucción más reciente del propietario

**Estado:** **CONFLICTO DE ALCANCE CONFIRMADO**, no fallo de compilación.

**Fuente:** [`docs/VISUAL_BIBLE.md`](../VISUAL_BIBLE.md), [`docs/assets/PIXEL_ASSET_MASTER_PLAN.md`](../assets/PIXEL_ASSET_MASTER_PLAN.md), [`README.md`](../../README.md), [`MainActivity.kt`](../../android/app/src/main/java/com/thegame/rpg/MainActivity.kt). El README y el código Android aún contienen pixel-art; el visual bible lo llama obligación de producto.

**Decisión reciente del usuario:** rechazó esa dirección visual y ordenó retirar lo relativo a pixel art; posteriormente exigió **no restaurar** material retirado. **Nunca interpretar documentación histórica como una nueva autorización para producir sprites o animaciones.**

**Estado de ejecución:** en el HEAD auditado el material histórico sigue existiendo. Esta auditoría **no** lo borra ni redefine otra estética. El registro previo está en la rama `cleanup/remove-pixel-art-20261027`: `docs/incidents/2026-10-27_PIXEL_ART_SCOPE_AND_EXECUTION_ERRORS.md`.

**Acción de control:** un futuro cambio de presentación exige delimitación explícita de repositorio y versión, migración coherente de dependencias y comprobación; ninguna eliminación de motor/saves/estado por similitud de nombres.

### TG-AUD-007 — P2 operativo: `main` no es la implementación ejecutable y la CI por `push` no cubre la rama de autoridad

**Estado:** **CONFIRMADO — ÁRBOL + WORKFLOW**. No es necesariamente un defecto involuntario: el README admite que `main` es placeholder.

**Fuente:** [`README.md`](../../README.md), [`.github/workflows/android-pixel-client.yml`](../../.github/workflows/android-pixel-client.yml). Verificación del árbol de `main@6f8d9c5bf6592275ac655e6200b38b7dfa26e23a`: **un solo archivo, `README.md`**. La implementación examinada vive en `docs/master-game-development-program@dac5d22...`. El workflow existente ejecuta `push` sólo en `feature/android-pixel-client-v1` y `pull_request` cuando cambian rutas escogidas; un push directo a la rama de autoridad no queda automáticamente cubierto por este workflow.

**Impacto:** una persona que clone el `main` por defecto obtiene un README, no el código jugable. Una modificación directa de la rama de autoridad no queda probada por el trigger `push` mencionado.

**Aceptación:** mantener señalización inequívoca en la entrada al proyecto, establecer checks obligatorios para la rama autoritativa o el merge-state requerido sin cambiar el esquema de releases sin aprobación.

### TG-AUD-008 — P2 coordinación: documento de tareas con estados históricos que contradicen la directiva más reciente dentro del mismo archivo

**Estado:** **CONFIRMADO — DOCUMENTACIÓN**.

**Fuente:** [`docs/AI_TASK_BULLETIN_BOARD.md`](../AI_TASK_BULLETIN_BOARD.md), líneas ~29–45 frente a ~57–75 y ~940–962; [`README.md`](../../README.md), líneas 7–10.

La nota superior de cierre de agentes declara **P11/CPR-006 RELEASED → READY / OWNER-PAUSED / UNCLAIMED**; apartados históricos inferiores todavía dicen **IN_PROGRESS / Nodus**. El texto superior dice que prevalece; sin embargo, lectores o agentes que extraigan sólo bloques inferiores pueden retener el estado incorrecto. El README también reproduce el estado histórico de Nodus como activo. **No** crear reclamaciones nuevas ni activar agentes basándose en bloques obsoletos.

**Acción:** generar vistas de estado desde una sola fuente, marcar secciones de historial o mantener resumen consolidado al inicio. Revalidar la autoridad viva antes de cada ejecución.

### TG-AUD-009 — P1 de completitud, NO bug ejecutado: cadena táctica y aceptación de integración todavía bloqueadas

**Estado:** **PENDIENTE — NO ES REGRESIÓN**.

**Fuente:** [Bulletin](../AI_TASK_BULLETIN_BOARD.md), entradas D-072 a D-076. A este checkpoint, **D-072 IN_PROGRESS / Silex**; **D-073**, **D-074** y **D-076** **BLOCKED** por sus dependencias. La corrección P11 para la carga tampoco está integrada. No declarar que el RPG táctico integrado ya está completo porque existan esquemas y tests de componentes.

**Acción:** terminar D-072 y sus pruebas de aftermath, luego D-073 bridge, D-074 Android y D-076 gate exact-head, manteniendo separados los dueños de estado y la privacidad del NPC.

### TG-AUD-010 — P2 cobertura faltante: pruebas positivas no sustituyen la inyección de fallos de las rutas de recuperación

**Estado:** **BRECHA DE VERIFICACIÓN**, no fallo nuevo.

**Fuente:** [`tests/test_android_bridge.py`](../../tests/test_android_bridge.py), que en autoridad comprueba guardado/carga normal y fallo de esquema inválido, pero no carga que deserializa correctamente y falla *después* por escena desconocida. [`SaveRepositoryTest.kt`](../../android/app/src/test/java/com/thegame/rpg/save/SaveRepositoryTest.kt) comprueba conservación de bytes tras fallos, pero no la publicación atómica de `AndroidGameSession.state` ni la pantalla Android recuperable.

**Aceptación:** cobertura `invalid-but-deserializable save`, `load failure after successful boot`, `save projection failure`, `choice projection failure`, `retry after boot failure`, `session/content alias isolation`. No sustituir una prueba Python del estado por una prueba Compose de la vista.

## Pruebas y comprobaciones efectivamente observadas

| Fuente | Resultado verificado | Límite |
|---|---|---|
| [GitHub Actions run 40608571513](https://github.com/jbob-coder/Text-rpg-game/actions/runs/40608571513), commit `f45936f1dae7592bbcc866d0a0b7f0aa0ed07f5c`, rama de auditoría anterior | **Python 479 tests: OK**. **Android unit/build: success**. **Emulador 35/35: 0 fallos**. | Prueba una rama de PR sobre la autoridad observada, **no** el APK del usuario y **no** las nuevas pruebas P11 de carga. El emulador registró avisos de consola/color buffer sin fallos de los 35 tests. |
| [GitHub Actions RED 37863493737](https://github.com/jbob-coder/Text-rpg-game/actions/runs/37863493737), `808f704...` | **Python 481: 3 FAIL** — los tres casos CPR-006. | Corrida intencional test-first del código anterior. |
| [GitHub Actions GREEN 37863439739](https://github.com/jbob-coder/Text-rpg-game/actions/runs/37863439739), `3b3ac9a...` | **Python 481: OK; Android unit/build/emulador: success**. | PR #80 no fusionada y ahora divergente del HEAD actual. |
| Revisión estática de `content/vertical_slice_01.json` y `content/vertical_slice_01_room_presence.json` | **19 escenas, 9 nodos, 8 enlaces, 4 misiones, 4 escenas con presencia**. **Cero errores** de referencias externas de `next_scene`, `location_id`, enlaces de mapa, `next_stage`, duplicados de opción o presencia huérfana en los campos examinados. | No sustituye la validación completa del contenido ni cubre lógica dinámica de todas las rutas; no se ejecutó este chequeo como test Python instalado. |

**Limitación de herramientas:** no se pudo clonar el repositorio en la máquina de auditoría: `git ls-remote` falló por resolución DNS de `github.com`; se obtuvieron los archivos y logs mediante el conector GitHub. **No se ejecutaron localmente suites, APK ni dispositivo Android** en esta sesión. No declarar PASSED o FAILED en ejecución si sólo se leyó la fuente.

## Plan de corrección por prioridad (sin cambiar aquí el código)

1. **P0, CPR-006:** resolver la publicación atómica de carga y aislamiento de alias mediante un candidato actualizado frente al HEAD, conservar save schema v1, reproducir RED/GREEN y pruebas de integración.
2. **P1, Android recuperación:** separar errores fatales del arranque de operaciones fallidas después de `Ready`; testear elección, carga, guardado, equipo y viaje inválidos sin perder la pantalla jugable.
3. **P1, arranque:** habilitar recuperación/reintento de fallos temporales comprobando que no se duplican sesiones.
4. **P2, pruebas de contrato:** cubrir guardado antes de proyección y elección confirmada antes de fallo de proyección; cambiar sólo si las reproducciones verifican ruptura de contrato.
5. **P2, producto/CI/docs:** detener la interpretación del pixel art como dirección vigente, normalizar estados de agentes y evitar usar `main` placeholder como fuente de gameplay. No inventar estética sustituta.
6. **P1, dependencias de juego:** mantener D-072 → D-073 → D-074 → D-076 como incompleto; no inventar progreso de tests ni merge.

## Reglas de continuidad

- **Revisar repositorio y rama antes de cualquier cambio.** Este documento aplica sólo a THE GAME.
- **No borrar ni recuperar recursos** durante una auditoría. No tocar partidas de usuario, contenido, motor, ramas ajenas ni la rama de autoridad por inferencia.
- Diferenciar pruebas ejecutadas, lectura de fuente, riesgos condicionados y funciones todavía no implementadas.
- Para cerrar cada hallazgo, exigir: enlace al commit y PR exactos, regresión que falle antes y pase después cuando sea ejecutable, full suite Python, build Android, pruebas de emulador cuando aplique y evidencia de merge a la autoridad. **Ningún hallazgo en este documento queda marcado como resuelto por mera documentación.**

**Resultado de esta actividad:** informe de errores creado en rama separada; ningún fichero jugable alterado, sin merge ni release. La auditoría es amplia pero **no una prueba de que se hayan detectado todos los errores posibles**.


---

## Segunda ronda: hallazgos nuevos TG-AUD-011 a TG-AUD-014 — 2026-10-27

Esta ronda conserva los 10 hallazgos previos sin reclasificar riesgos como errores reproducidos. **No se modificó ni ejecutó el código del juego.** Lectura directa de fuentes en `docs/master-game-development-program@dac5d22cdbe211d0d35d3df98b542be2653f1b85`.

### TG-AUD-011 — P1: el cliente Android omite un archivo auxiliar de presencia de personajes

**Estado:** **CONFIRMADO POR CADENA DE CÓDIGO + ARCHIVOS DE AUTORÍA; falta test Android de regresión.** Afecta los datos de **presencia** de personajes en las escenas, no el funcionamiento intrínseco de las reglas narrativas.

**Fuentes de autoridad (líneas del HEAD examinado):**
- [`android/app/src/main/java/com/thegame/rpg/engine/PythonGameEngine.kt` líneas 208–227 y 310–330](../../android/app/src/main/java/com/thegame/rpg/engine/PythonGameEngine.kt): `ChaquopySessionGateway.start()` llama a `installContent()`, que copia **únicamente** `vertical_slice_01.json` al directorio `filesDir/content/`.
- [`src/textrpg/content.py` líneas 176–220](../../src/textrpg/content.py): `load_content_pack()` sólo incorpora `vertical_slice_01_room_presence.json` si existe **junto al archivo principal en el sistema de archivos**. Si no está, prosigue silenciosamente.
- [`content/vertical_slice_01_room_presence.json`](../../content/vertical_slice_01_room_presence.json): cinco registros de aparición entre cuatro escenas: dos actores en `OPENING_DEPOT_BLACKOUT`, uno en `OPENING_DECISION`, `OPENING_RECOVERY` y `OPENING_TUNNEL`.
- [`content/vertical_slice_01.json`](../../content/vertical_slice_01.json): en las 19 escenas examinadas no hay listas `actors` embebidas.
- [`src/textrpg/room_projection.py`](../../src/textrpg/room_projection.py): `scene.get("actors", [])` devuelve lista vacía cuando el auxiliar no se incorporó.
- [`android/app/src/androidTest/java/com/thegame/rpg/ActivityBootSmokeTest.kt`](../../android/app/src/androidTest/java/com/thegame/rpg/ActivityBootSmokeTest.kt): las pruebas de arranque verifican escena/avatar/decisiones, pero no que la proyección de actores de la partida **real instalada** incluya los registros del auxiliar.

**Resultado lógico en instalación limpia:** el archivo auxiliar no llega al directorio desde el que Python lo busca; la proyección `room.actors` queda vacía para esas escenas aunque el JSON auxiliar exista dentro del repositorio y posiblemente como asset del paquete. `assets.srcDir("../../content")` en `android/app/build.gradle.kts` incluye assets de origen, pero **no implica** que el auxiliar haya sido extraído al mismo directorio que el JSON principal.

**Límites:** este defecto **no demuestra** que el APK del usuario muestre o deba mostrar sprites; únicamente detecta pérdida de metadatos de presencia de personajes dentro del contrato de datos. No se inspeccionó ni instaló el APK concreto.

**Regresión requerida:** arrancar Android con `filesDir/content` limpio, inspeccionar el payload del puente en la escena `OPENING_DEPOT_BLACKOUT` y comparar `room.actors[*].presentation_id` con el resultado de `load_content_pack` ejecutado sobre `content/vertical_slice_01.json` acompañado por su sidecar. Validar paridad sin inferir o inventar una presentación visual. **No reintroducir pixel art**: una futura corrección del empaquetado sólo tiene sentido si el campo semántico de presencia permanece requerido por la arquitectura aprobada.

### TG-AUD-012 — P2: sustitución no atómica del archivo de contenido Android

**Estado:** **CONFIRMADO EN CÓDIGO COMO PATRÓN DE RIESGO; escenario de fallo aún NO reproducido**.

**Fuente:** [`PythonGameEngine.kt` líneas 310–330](../../android/app/src/main/java/com/thegame/rpg/engine/PythonGameEngine.kt).

**Causa:** `installContent()` prepara `vertical_slice_01.json.tmp`, **borra** `vertical_slice_01.json` anterior y **después** intenta `temp.renameTo(target)`; si el renombrado falla, hace `temp.copyTo(target, overwrite = true)`. El reemplazo no es un único paso atómico, aunque los bytes de origen se copien antes a un temporal. Con error de escritura, falta de espacio o fallo durante la copia alternativa puede quedar sin archivo válido en el destino.

**Impacto potencial:** arranque fallido y pérdida de copia previa de contenido instalada. No hay evidencia de pérdida de partida guardada: la ruta de saves está separada.

**Aceptación:** probar fallo de `renameTo` y de `copyTo` con archivos temporales; preservar siempre un fichero anterior verificable o recuperar la instalación mediante mecanismo de rollback; no borrar el destino hasta disponer de reemplazo verificable.

### TG-AUD-013 — P2: guardado manual en CLI puede abortar fuera del manejador de errores

**Estado:** **CONFIRMADO — CÓDIGO; reproducción automatizada pendiente**.

**Fuentes:** [`src/textrpg/cli.py` líneas 88–119 y 136–152](../../src/textrpg/cli.py), [`src/textrpg/persistence.py` líneas 78–88](../../src/textrpg/persistence.py); [`tests/test_cli.py`](../../tests/test_cli.py).

**Causa y frontera:**
- `play()` procesa el comando literal `save` **antes** del bloque `try/except (ValueError, RuleError)`; por tanto `save_state()` puede propagar `OSError` fuera del ciclo.
- El autosave tras una decisión sí se encuentra dentro del `try`, pero `OSError` **no** está en las excepciones capturadas.
- `main()` sólo captura `RuleError`; tampoco convierte a un resultado controlado un fallo de escritura/lectura del sistema de archivos.
- La suite `tests/test_cli.py` verificada tiene tres tests de presentación, decisión y estado, sin inyección de fallo de escritura.

**Impacto:** directorio no escribible, disco sin espacio o ruta inválida podrían terminar la consola con traceback en lugar de un error recuperable con partida en memoria.

**Pruebas:** `unittest.mock.patch("textrpg.cli.save_state", side_effect=OSError(...))`, `input_fn` controlado y captura de mensajes, comprobando que un error de I/O no cierre el ciclo ni altere el estado. Establecer qué error de lectura al invocar `--load-save` es recuperable o terminal con salida clara. **No afirmar una reproducción real** hasta ejecutarla.

### TG-AUD-014 — P2: pruebas de Android no cubren la paridad real del sidecar

**Estado:** **BRECHA DE COBERTURA**, no regresión independiente.

**Fuentes:** [`ActivityBootSmokeTest.kt`](../../android/app/src/androidTest/java/com/thegame/rpg/ActivityBootSmokeTest.kt), [`tests/test_room_projection.py`](../../tests/test_room_projection.py), [`tests/test_d064_android_scene_projection_source.py`](../../tests/test_d064_android_scene_projection_source.py).

**Evidencia:** los tests unitarios Python prueban `build_room_projection` con actores incrustados directamente en diccionarios, y los tests de pantalla Android comprueban el arranque y la navegación, pero no la **extracción del sidecar durante el inicio real**. Las pruebas estáticas del renderer comprueban referencias al campo `room.actors`, no que el campo esté poblado en el APK.

**Cierre requerido:** un test sobre la sesión Chaquopy iniciada desde assets empaquetados y directorio vacío, comparando sólo IDs/presencia de escenas, además de una prueba de instalación limpia/actualización y error de sidecar. Evitar afirmar que las 35 pruebas de emulador detectan errores fuera de sus aserciones.

### Recuento y garantías tras esta ronda

**Total de hallazgos registrados en el informe: 14 (10 iniciales + 4 nuevos).** Los hallazgos TG-AUD-004, 005, 012 y 013 siguen sujetos a prueba adicional; TG-AUD-009 y 014 son pendientes de integración/cobertura, no regresiones demostradas. **TG-AUD-011 es una divergencia demostrable entre rutas de carga**, pero falta comprobarla en el APK del usuario.

**Actividad realizada:** lectura de archivos de GitHub y comparación de flujo de empaquetado Android ↔ cargador Python ↔ proyección de escena; auditoría de frontera CLI/persistencia; documentación en rama aislada. **No se ejecutaron tests nuevos, no hubo borrados, no se tocaron recursos visuales, motor, ni saves.**
