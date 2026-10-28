# THE GAME — Verificación incremental del engine y matriz de incidencias

**Tipo:** auditoría descriptiva y registro de evidencia; sin cambios de gameplay.  
**Fecha local de la revisión:** 2026-10-27, America/Puerto_Rico (algunos eventos de GitHub figuran el 2026-10-28 UTC).  
**Repositorio:** `jbob-coder/Text-rpg-game`.  
**Rama de implementación autoritativa:** `docs/master-game-development-program`.  
**Commit fijado:** [`369621af7469175fdc3ddf964f470fcc8fa6b295`](https://github.com/jbob-coder/Text-rpg-game/commit/369621af7469175fdc3ddf964f470fcc8fa6b295).  
**Documento general complementario:** [PR #93 — ENGINE_RUNTIME_CODE_AUDIT_2026-10-27.md](https://github.com/jbob-coder/Text-rpg-game/pull/93), todavía candidato, no fusionado en el momento del cotejo.  
**Límite:** las observaciones de código se verificaron por lectura remota; no se ejecutaron pruebas nuevas en esta sesión. Los resultados de GitHub Actions citados corresponden a los commits de sus respectivos PR y **no** acreditan una nueva ejecución sobre este documento ni sobre el merge SHA.

## Propósito y autoridad

Este registro **no** reemplaza la documentación arquitectónica del PR #93. Actualiza los estados de arreglos de misiones, identifica fronteras de error que todavía aparecen en el commit fijado y registra una divergencia entre la presentación actual y la dirección del propietario: juego principalmente textual con mapa como superficie visual. No añade mecánicas, escenas, assets, NPC, ni nuevos requisitos de producto por iniciativa del auditor.

**Importante sobre ramas:** `main` continúa apuntando al commit inicial `6f8d9c5bf6592275ac655e6200b38b7dfa26e23a`; no contiene la implementación revisada. El archivo `AGENTS.md` de la rama autoritativa también advierte que `main` no es el programa de implementación. No debe interpretarse una corrección en `main` como corrección del engine sin una promoción autorizada.

## Estados de las correcciones existentes

| ID | Área | Estado en `369621a` | Evidencia |
| --- | --- | --- | --- |
| Q-001 | Ciclos de prerrequisitos entre objetivos de una misión | **CORREGIDO EN AUTORIDAD** | [PR #88 fusionado](https://github.com/jbob-coder/Text-rpg-game/pull/88); `quests.py` implementa `_validate_objective_prerequisite_cycles`, incluido caso autorreferente y ciclos de varios nodos. `tests/test_quests.py` contiene regresiones. |
| Q-002 | Poder fallar un objetivo que todavía estaba bloqueado por prerrequisitos | **CORREGIDO EN AUTORIDAD** | [PR #91 fusionado](https://github.com/jbob-coder/Text-rpg-game/pull/91), merge `369621a`; `test_locked_objective_cannot_fail_or_take_failure_route` y pruebas del caso desbloqueado. |
| V-001 | Tipos de condiciones/efectos malformados provocan excepción ajena al contrato | **CANDIDATO; NO FUSIONADO** | [PR #87](https://github.com/jbob-coder/Text-rpg-game/pull/87). No inferir que la rama de autoridad incorpora esa corrección. |
| S-001 | Guardados concurrentes y cierre de entrada CLI | **CANDIDATO; NO FUSIONADO** | [PR #89](https://github.com/jbob-coder/Text-rpg-game/pull/89). |
| S-002 | EOF y errores de guardado en CLI | **CANDIDATO; NO FUSIONADO** | [PR #90](https://github.com/jbob-coder/Text-rpg-game/pull/90); revisar solapamiento con #89, no integrar ambos por número. |
| S-003 | Lectura de guardados inexistentes/ilegibles y errores de I/O | **CANDIDATO DEPENDIENTE; NO FUSIONADO** | [PR #92](https://github.com/jbob-coder/Text-rpg-game/pull/92), basado sobre la rama del PR #89, no directamente sobre autoridad. |
| D-001 | Inventario arquitectónico del motor | **DOCUMENTACIÓN EN REVISIÓN** | [PR #93](https://github.com/jbob-coder/Text-rpg-game/pull/93), escrito contra el HEAD anterior `dac5d22...`; no declararlo actualizado automáticamente después de #88 y #91. |

### Matriz de comportamientos/riesgos aún observables en el código de autoridad

Los estados **CONFIRMADO POR LECTURA** describen expresiones y secuencias presentes en el código fijado; **no equivalen a fallo reproducido en Android ni a incidente de datos de usuario**.

#### E-001 — Entrada de consola sin manejo de EOF

- **Estado:** CONFIRMADO POR LECTURA; reproducción de proceso pendiente.
- **Dueño:** [`src/textrpg/cli.py`](https://github.com/jbob-coder/Text-rpg-game/blob/369621af7469175fdc3ddf964f470fcc8fa6b295/src/textrpg/cli.py), función `play()`.
- **Causa:** `command = input_fn("> ").strip()` aparece antes del `try/except` usado para interpretar números. Un `EOFError` de stdin cerrado no se captura dentro del bucle; `main()` solo captura `RuleError`.
- **Impacto esperable:** terminación mediante excepción en vez de salida controlada si se agota la entrada.
- **Aceptación propuesta:** test con `input_fn` que eleve `EOFError`; el bucle debe salir sin traceback ni alterar el estado. Mantener manejo diferenciado de `KeyboardInterrupt` según contrato CLI acordado.
- **Solución candidata:** #89 / #90; verificar su relación y estado de merge antes de cualquier cambio.

#### E-002 — Errores del sistema de archivos atraviesan la CLI

- **Estado:** CONFIRMADO POR LECTURA; prueba con permisos/disco pendiente.
- **Dueños:** [`cli.py`](https://github.com/jbob-coder/Text-rpg-game/blob/369621af7469175fdc3ddf964f470fcc8fa6b295/src/textrpg/cli.py) y [`persistence.py`](https://github.com/jbob-coder/Text-rpg-game/blob/369621af7469175fdc3ddf964f470fcc8fa6b295/src/textrpg/persistence.py).
- **Causa:** el comando `save` manual llama `save_state` fuera del `try` y el autosave no captura `OSError`. `load_state` usa `Path(...).read_text()` sin normalizar `OSError`; `main` captura únicamente `RuleError`.
- **Impacto esperable:** archivo inexistente, permiso denegado, disco inaccesible o fallo de escritura pueden salir como excepción no controlada en CLI. Si falla el autosave tras una elección válida, la elección ya podría haberse aplicado en memoria.
- **Aceptación propuesta:** errores de lectura/escritura simulados, error visible con semántica estable y distinción clara entre avance de partida en memoria y persistencia fallida. No inventar éxito de guardado.
- **Solución candidata:** #89 / #90 / #92; #92 depende de #89.

#### E-003 — Nombre temporal de guardado compartido

- **Estado:** RIESGO CONFIRMADO POR PATRÓN DE CÓDIGO; colisión concurrente no reproducida aquí.
- **Dueño:** [`src/textrpg/persistence.py`](https://github.com/jbob-coder/Text-rpg-game/blob/369621af7469175fdc3ddf964f470fcc8fa6b295/src/textrpg/persistence.py), `save_state()`.
- **Causa:** `target.with_suffix(target.suffix + ".tmp")` produce el mismo archivo temporal para dos operaciones sobre el mismo destino. El reemplazo final es atómico para una operación aislada, pero ese patrón **no demuestra aislamiento** entre escritores simultáneos.
- **Aceptación propuesta:** test de intercalado o concurrencia con destino compartido; probar ausencia de interferencia y limpieza de temporales si ocurre una excepción. No declarar corrupción real sin reproducción.
- **Solución candidata:** #89.

#### E-004 — Publicación anticipada de partida cargada en Android

- **Estado:** FRONTERA DE ATOMICIDAD OBSERVADA POR LECTURA; reproducción completa pendiente.
- **Dueño:** [`src/textrpg/android_bridge.py`](https://github.com/jbob-coder/Text-rpg-game/blob/369621af7469175fdc3ddf964f470fcc8fa6b295/src/textrpg/android_bridge.py), `AndroidGameSession.load()`.
- **Causa:** `self.state = load_state(self._save_path)` asigna una nueva sesión antes de `self.scene_view()`. Si esa proyección falla, el `except` devuelve `AndroidBridgeError`, pero no restaura `self.state` anterior.
- **Prueba mínima propuesta:** cargar un JSON estructuralmente válido cuya `scene_id` no exista en las escenas del contenido cargado; comprobar el error y comparar una instantánea profunda de `self.state` antes/después. Añadir pruebas para fallos de proyección si la ruta admite otras inconsistencias.
- **Impacto potencial:** error presentado como carga fallida aunque el estado en memoria haya sido sustituido. **No se afirma pérdida real de guardados.**
- **Relación:** revisar [CPR-006](../overseer/code_problems/CPR-006_android_session_state_publication_alias_atomicity.md) y [PR #80](https://github.com/jbob-coder/Text-rpg-game/pull/80) antes de crear un arreglo paralelo. El informe de este archivo no reclama ni cierra ese trabajo.

#### E-005 — Presentación de escenas ilustradas contradice el alcance textual solicitado

- **Estado:** DIVERGENCIA DE REQUISITO CONFIRMADA (no fallo interno del renderizador).
- **Dirección del propietario en la conversación de trabajo:** conservar el **mapa** como vista visual; interacciones, decisiones y narrativa deben ser **texto**, sin añadir simulación de animaciones ni nuevo contenido gráfico por iniciativa propia. Es una intención de producto; no confundirla con una tarea de eliminación ya ejecutada.
- **Evidencia de implementación:** [`GameScreen.kt`](https://github.com/jbob-coder/Text-rpg-game/blob/369621af7469175fdc3ddf964f470fcc8fa6b295/android/app/src/main/java/com/thegame/rpg/ui/GameScreen.kt) invoca `SceneIllustration(...)` en `StorySection` y `NarrativePanel` para pantallas estrechas y anchas. [`SceneIllustration.kt`](https://github.com/jbob-coder/Text-rpg-game/blob/369621af7469175fdc3ddf964f470fcc8fa6b295/android/app/src/main/java/com/thegame/rpg/ui/SceneIllustration.kt) dibuja canvas, sprites, overlays y efectos de cuadros animados. `GameScreen.kt` posee también el renderizador del mapa mediante `PixelMapArtCatalog`; son superficies distintas.
- **Conclusión:** el área ilustrada sigue **presente en la implementación**, independientemente de que existan documentos anteriores que hayan propuesto retirarla. No declarar eliminación hecha sin diff + pruebas.
- **Aceptación propuesta para una tarea posterior expresamente acotada:** eliminar solo consumidores de ilustración narrativa de la UI, **preservar mapa funcional**, elecciones, textos, estados, persistencia y contratos player-safe; ajustar pruebas de UI que hoy esperan `story-pixel-header` o `scene-illustration`. No eliminar assets o proyecciones de datos sin auditoría de consumidores y decisión de alcance.

## Confirmaciones de pruebas (sin extrapolación)

- [Acciones de PR #88, run 40613747891](https://github.com/jbob-coder/Text-rpg-game/actions/runs/40613747891): éxito en candidato de PR. Log de `python-engine`: **482 pruebas, OK**. Log de `android-emulator-smoke`: **35 pruebas, 0 fallidas** y compilación exitosa. El run corresponde al merge sintético del PR anterior a la fusión; no a una nueva ejecución sobre `369621a`.
- [Acciones de PR #91, run 40614181134](https://github.com/jbob-coder/Text-rpg-game/actions/runs/40614181134): la consulta de estado del PR devuelve `completed/success`; no se extrae aquí un nuevo número de tests.
- La consulta de workflows vinculados directamente al SHA `369621a` no devolvió un run de PR. **Ausencia de run en esa consulta no demuestra ausencia de cualquier CI en otras modalidades.**
- En esta sesión no se ejecutaron `unittest`, Gradle, emulador ni dispositivo físico. No se afirma APK construido, instalable o publicado.

## Verificación antes de aceptar correcciones

1. Confirmar HEAD de `docs/master-game-development-program`, revisar los PR abiertos y sus ramas base reales.
2. Preparar casos RED mínimos para E-001/E-002/E-003/E-004, cada uno con snapshot antes/después y sin mutación inesperada; para E-005 usar un test de estructura de UI y conservar el test del mapa.
3. Integrar solamente la corrección mínima del dueño correspondiente, sin introducir sistemas nuevos ni mover la lógica de reglas hacia Kotlin.
4. Ejecutar `PYTHONPATH=src python -m unittest discover -s tests -v`; si cambia el puente o UI, ejecutar además tests de Android, compilación y, cuando sea posible, emulador/dispositivo.
5. Guardar SHA exacto, prueba RED/GREEN, diff y estado del PR; solo entonces cambiar `CANDIDATO` por `CORREGIDO EN AUTORIDAD`.

## Handoff

**COMPLETED:** lectura de HEAD, verificación de PR #88 y #91 fusionados, cotejo de #87/#89/#90/#92/#93 y matriz estática E-001–E-005.  
**NOT DONE:** pruebas de reproducción, arreglos de código, retirada de ilustraciones, integración de candidatos, aprobación de PR ni publicación de APK.  
**NEXT:** revisar los candidatos de guardado/CLI sin solaparlos, reproducir E-004 bajo el dueño CPR-006 y acordar una tarea específica de presentación texto+mapa antes de tocar la UI.  
**Riesgo de deriva:** los PR pueden fusionarse después de este informe; los estados solo son válidos en el SHA fijado.

---

## Revisión posterior — ciclo ♾️ / 2026-10-28

**Nuevo HEAD observado de autoridad:** `fe7e277d8ad53be7c97f454f6185794a41de4879`. El informe anterior sigue anclado al SHA `369621a`; **no trasladar automáticamente todas sus afirmaciones al nuevo HEAD sin diff**. Esta adenda recoge evidencia nueva de PR y CI, no reescribe el historial.

### QA de sustitución visual texto + mapa: conflicto de dos candidatos

| Candidato | Observación verificada | Estado / requisito de salida |
| --- | --- | --- |
| [PR #97](https://github.com/jbob-coder/Text-rpg-game/pull/97), `676515ec70817d5d28282a82b83194b621a8c5e2` | [Run 40620429532](https://github.com/jbob-coder/Text-rpg-game/actions/runs/40620429532): `python-engine=success`, `android-emulator-smoke=success`, `android-unit-and-assemble=FAILURE`. Error Kotlin `:app:compileDebugUnitTestKotlin` en `android/app/src/test/java/com/thegame/rpg/ui/PixelMapTravelTransitionCatalogTest.kt:10`: `Unresolved reference 'PixelMapTravelTransitionCatalog'`; el test sigue imponiendo el catálogo pixelado que `PixelMapTravelTransition.kt` ya sustituyó por aviso de viaje textual. | **CI ROJA**, no merge. Reemplazar prueba de ocho frames por validación del contrato textual y del mapa conservado; no eliminar pruebas para forzar verde. Comentario de revisión publicado en el PR (ID `6469316049`). |
| [PR #94](https://github.com/jbob-coder/Text-rpg-game/pull/94), `506235dacdf2fb07c9478db8982cb31d8ddf1226` | [Run 40619522192](https://github.com/jbob-coder/Text-rpg-game/actions/runs/40619522192): **los tres jobs SUCCESS**. Diff de **94 archivos**; elimina por completo antiguos test suites instrumentados `GameScreenTest.kt` y `CharacterStatsSectionTest.kt` y reescribe presentación ampliamente. | **CI VERDE en el candidato**, pero la cobertura anterior eliminada requiere evaluación/recuperación semántica para estado, decisiones, navegación y equipo. Comentario publicado en el PR (ID `6469316801`). |

**No combinar ambos PR sin reconciliación.** Preferir solución mínima y pruebas que conserven los contratos reales, con mapa visual permitido, sin animación/ilustración de narrativa ni restauración de pixel art. La eliminación de un test cuya función desapareció puede ser legítima **solo** si se demuestra que las capacidades de usuario que importan siguen probadas por otro test. Verde en una suite reducida no equivale a equivalencia de cobertura.

### Estado observado de otros PR al efectuar esta revisión

- **PR #98** (protección de suma de atributos `add_player` contra overflow): candidato abierto, HEAD `73caaf959e5520faa6c1aa3c41e20b4a71651909`; run `40690222845` **in_progress** en la consulta. Un run anterior del PR, `40619901640`, fue success para **otro HEAD**. No confundirlos.
- **PR #89** (archivo temporal concurrente y cierre de entrada CLI): HEAD `e6f43186a10dc9929e33659f680d5eaa56a7a0f1`, run `40690104472` **in_progress**.
- **PR #92** (límite de I/O de guardados): HEAD `5c8228adebe08346351c2d9ac21c75491e58b4e0`, base **la rama de #89**, no la de autoridad; run `40690167814` **in_progress**.
- Un estado **in_progress** no equivale a PASS ni FAIL; consultar el run final, compatibilidad y merge antes de cerrar cualquiera de los riesgos E-001/E-002/E-003. Evitar que el PR #90 solapado entre sin reconciliación.

### Límite de ejecución y siguiente acción

Se leyó el log de GitHub Actions del job `122593008826` para establecer el primer error de Kotlin, y se contrastaron patches/PRs #94 y #97 y el estado de los commits recientes. El intento local de `git ls-remote` contra GitHub falló por resolución DNS de `github.com`: **no se ejecutaron pruebas locales ni se instaló APK**. Los comentarios enviados a PR #94 y #97 son las únicas modificaciones ajenas a esta documentación; **no se modificó motor, UI, assets, tests, ni la rama de autoridad**.

**NEXT:** esperar el resultado real de #89/#92/#98, reconciliar un solo cambio visual (incluyendo pruebas funcionales de reemplazo) y ejecutar CI exact-head antes de cualquier merge.
