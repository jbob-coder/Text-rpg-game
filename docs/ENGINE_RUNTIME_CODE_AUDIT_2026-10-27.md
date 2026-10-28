# THE GAME — Auditoría del motor: arquitectura, lenguajes y ejecución

**Tipo:** documentación técnica descriptiva de implementación existente (no especificación de características nuevas).  
**Fecha:** 2026-10-27 (America/Puerto_Rico).  
**Repositorio:** jbob-coder/Text-rpg-game.  
**Rama de autoridad inspeccionada:** docs/master-game-development-program.  
**HEAD de referencia:** dac5d22cdbe211d0d35d3df98b542be2653f1b85.  
**Alcance:** código fuente, contratos Android, datos, persistencia, CLI y pruebas. No hay cambios en el motor, escenas, partidas ni interfaces mediante este documento.  
**Importante:** la rama por defecto main es un placeholder con solo README; NO es la implementación autoritativa. Los PR abiertos se describen por separado y NO se consideran integrados.

## 1. Qué es este engine

THE GAME es un RPG de elecciones dirigido por contenido escrito y reglas deterministas. El contenido (escenas, requisitos, resultados, condiciones) está declarado en JSON; el motor decide cuáles opciones son visibles, si están habilitadas y qué modificaciones produce la elección. El motor no genera libremente la trama ni requiere IA generativa durante la partida.

El **motor de reglas** es Python, no Kotlin ni Godot. Existen dos clientes: una consola local Python para desarrollar/probar el contenido y una aplicación Android con UI Kotlin/Jetpack Compose. La presencia de imágenes y catálogos de pixel art en el cliente Android no convierte el núcleo del RPG en un motor gráfico; esa presentación está separada de la autoridad de reglas.

## 2. Lenguajes y dependencias constatados

| Área | Lenguaje / formato | Evidencia | Papel |
| --- | --- | --- | --- |
| Reglas, simulación, validación, guardado, terminal y puente | Python >= 3.10 | pyproject.toml; src/textrpg/ | Es la autoridad de estado y de reglas de juego. |
| Escenas, registros, estado inicial y guardado | JSON UTF-8 | content/*.json; persistence.py; json_contract.py | Datos declarativos y serialización con validación. |
| App Android, DTO, ViewModel y pantallas | Kotlin | android/app/src/main/java/com/thegame/rpg/ | Presentación, ciclo de vida, interacción y mapeo a datos visibles. |
| Interfaz Android | Jetpack Compose | MainActivity.kt; GameScreen.kt; build.gradle.kts | UI declarativa; no debe recalcular reglas ocultas. |
| Python integrado en Android | Chaquopy | android/app/build.gradle.kts; PythonGameEngine.kt | Carga Python y llama al puente en el mismo proceso de la aplicación. |
| Construcción y CI Android | Gradle Kotlin DSL, YAML | android/*.gradle.kts; .github/workflows/ | Dependencias, compilación, tests y emulador. |

El paquete Python declara version 0.1.0, Python >= 3.10 y ninguna dependencia Python de ejecución en pyproject.toml. Android configura Python 3.10 en Chaquopy, Java 17 para compilación, minSdk 24 y targetSdk 37 en el árbol inspeccionado. Esto es **configuración verificada en archivos**, no una afirmación de compatibilidad en un teléfono físico.

## 3. Mapa de arquitectura real

    content/vertical_slice_01.json
               |
               v
    content.load_content_pack()
      valida pack, registries y estado inicial
               |
               v
    GameState + RulesEngine (Python)
      escenas / decisiones / estados / dominios
               |
          +----+--------------------+
          |                         |
          v                         v
    cli.py (terminal)      android_bridge.AndroidGameSession
                                   |
                          vistas sin secretos
                                   |
                          ChaquopySessionGateway
                                   |
                          PythonGameEngine.kt
                                   |
                          GameSnapshot / mapper
                                   |
                          GameViewModel / StateFlow
                                   |
                          Jetpack Compose / usuario

Para persistencia, tanto CLI como el puente Android llaman a persistence.py para convertir GameState a JSON de esquema 1. Las operaciones de lectura/escritura y el ciclo de vida de Android no sustituyen al estado autoritativo Python.

## 4. Inicio de una partida

1. El cliente selecciona un paquete JSON.
2. content.load_content_pack() lo decodifica con loads_strict_json(), que rechaza constantes no finitas y desbordamientos numéricos.
3. content_pack_from_mapping() valida escenas, misiones, poderes, registros, referencias, mapas tácticos cuando corresponda, imágenes de identidad y estado inicial; opcionalmente combina el sidecar de presencia de sala.
4. Se construye GameState desde initial_state y RulesEngine con las definiciones autorizadas. Los campos iniciales desconocidos o escenas inexistentes producen RuleError.
5. Se muestra la escena actual mediante build_scene_view(), no el objeto crudo de escena.

El paquete actual content/vertical_slice_01.json tiene content_id CONTENT_VERTICAL_SLICE_01, título The Dead Relay, canon_status provisional_canon, 19 escenas y 4 misiones en el HEAD inspeccionado. Estos conteos son inventario de datos, no prueba de que todas las rutas del contenido estén completas.

## 5. Qué contiene GameState

src/textrpg/core.py define GameState como dataclass mutable y serializable. Contiene seed, scene_id, turn, time_minutes, player, flags, relationships, knowledge, inventory, quests, npcs, party, abilities, equipment, perks, schema_version e history. No se deben inventar campos al cargar guardados: validate_game_state_structure() comprueba la forma superior y otras funciones validan contratos específicos.

**Cuidado:** GameState.snapshot() devuelve un diccionario de referencias a estructuras anidadas. NO es por sí mismo una copia profunda. RulesEngine.choose() sí realiza deepcopy(state.snapshot()) antes de aplicar efectos y llama a _restore_snapshot() si falla la transacción. Al reparar otras operaciones, no debe suponerse que snapshot() aísla mutaciones anidadas.

## 6. Qué pasa cuando el jugador escoge una opción

Ruta Python: RulesEngine.build_scene_view(state) -> available_choices(state) -> choose(state, choice_id).

1. _available_authored_choices() filtra por visible_if y evalúa requires. Las opciones bloqueadas pueden mostrarse con disabled_reason; las invisibles no se exponen.
2. choose() rechaza un ID invisible o bloqueado mediante RuleError.
3. Si existe check, _resolve_check() calcula el resultado desde estadísticas efectivas, habilidad, dificultad y una variación **determinista**.
4. La variación se obtiene del hash SHA-256 de seed, turn, scene_id y choice_id, no de aleatoriedad no reproducible; elegir la misma opción desde el mismo estado de entrada produce la misma tirada.
5. Se selecciona el outcome correspondiente (o default), se valida next_scene y el coste temporal, y se prepara una copia profunda del estado para rollback.
6. _apply_effects() modifica los dominios permitidos (banderas, jugador, inventario, relaciones, conocimiento, misiones, NPC y demás efectos soportados); advance_time() aplica el tiempo autorizado.
7. En éxito aumenta turn, cambia scene_id si procede y anexa un evento al history. En una excepción durante la fase transaccional restaura el estado anterior y propaga el error.

**No confundir:** la determinación de una elección evita azar no reproducible dentro de ese check; no certifica por sí sola que todas las integraciones y efectos de otros subsistemas sean transaccionalmente perfectos.

## 7. Módulos de reglas y responsabilidad

| Ruta | Responsabilidad observada |
| --- | --- |
| src/textrpg/core.py | GameState, RulesEngine, acceso a escenas, condiciones, checks y efectos de elecciones. |
| src/textrpg/content.py + validation.py | Carga, validación de referencias y requisitos de los paquetes de contenido. |
| src/textrpg/schema.py + stats.py + modifiers.py + status.py | Atributos, habilidades, recursos, fórmulas derivadas, modificadores y proyecciones de estado. |
| src/textrpg/simulation.py | Tiempo, condiciones temporales, recuperación, entrenamiento y validación previa de avance. |
| src/textrpg/quests.py | Inicio, objetivos/prerrequisitos, progreso, fallo y etapas de misiones. |
| src/textrpg/social.py | Relaciones, memorias, conocimiento, objetivos y eventos sociales de NPC. |
| src/textrpg/equipment.py | Equipo, espacios, requisitos y bonificaciones. |
| src/textrpg/powers.py + progression.py | Poderes, técnicas, costes, dominio, prerrequisitos y progresión. |
| src/textrpg/combat_*.py | Esquema, estado, mapa, línea de visión, reglas, conocimiento e IA táctica; disponibilidad del cliente debe verificarse por separado. |
| src/textrpg/room_projection.py + visuals.py | Proyección visible de actores de sala y contratos visuales. |
| src/textrpg/persistence.py + json_contract.py | Guardado/carga versionada y decodificación JSON estricta. |
| src/textrpg/android_bridge.py | Fachada Python de operaciones Android y proyecciones de información visible. |
| src/textrpg/cli.py | Cliente de consola para la vertical slice y su guardado/reanudación. |

La implementación actual de stats define siete atributos: might, agility, endurance, intellect, will, perception y presence. Las fórmulas de derivados están en schema.py como datos; deben corregirse allí o mediante su pipeline legítimo, no duplicarse arbitrariamente en Android.

## 8. Cómo funciona Android

MainActivity.kt inicia la interfaz Compose y observa GameViewModel. GameViewModel encapsula GameEngine (implementado por PythonGameEngine), publica GameUiState mediante StateFlow y presenta errores de arranque/operación.

PythonGameEngine.kt ejecuta llamadas en Dispatchers.IO y delega al ChaquopySessionGateway. Este inicia el runtime Python, instala el contenido de assets, importa textrpg.android_bridge y llama a create_session(contentFile, saveFile). La ruta de guardado prevista en Kotlin es filesDir/saves/slot-0.json. El puente devuelve diccionarios Python, convertidos a estructuras Kotlin por mapeo y validación; los DTO conforman GameSnapshot.

La sesión Python AndroidGameSession aplica choose, travel, equip, unequip, inspect_status, save y load. Su _view_for() crea bloques player-safe scene/status/inventory/quests/map/room/visuals/meta y traduce fallos de reglas a AndroidBridgeError. Un cliente no debe leer state.npcs, condiciones secretas ni definiciones crudas como si fueran vistas autorizadas.

**Límite:** la prueba de arranque Android en emulador no equivale a validación real en Galaxy A03 u otro teléfono físico.

## 9. Guardado, reanudación y riesgos

persistence.py usa CURRENT_SCHEMA_VERSION = 1. dumps_state() valida estructura y serializa como JSON estricto (sin NaN). loads_state() rechaza JSON inválido, versión incompatible, campos desconocidos y estructura superior inaceptable. save_state() escribe temporalmente en un archivo con sufijo .tmp y lo reemplaza sobre el destino.

**Riesgos observables en la rama de referencia:**
- play() usa input_fn sin manejar EOFError/KeyboardInterrupt en el bucle: terminar stdin puede causar salida por excepción.
- El guardado manual y automático puede propagar fallos de disco/permisos; en autosave el estado de la decisión ya puede haber avanzado.
- load_state() hace read_text() directamente sin convertir las excepciones de lectura a un error de dominio.
- save_state() reutiliza un nombre temporal predecible para el mismo destino; conviene comprobar aislamiento en guardados concurrentes.
- AndroidGameSession.load() reasigna state antes de construir la vista; si la proyección falla después, la publicación puede quedar inconsistente. La atomicidad total de la sesión es una frontera de integración separada.

Estas observaciones son lectura estática **del HEAD fijado** y no afirman incidencia en producción. Se observaron PR de corrección abiertos: #89 (guardados concurrentes y CLI), #90 (EOF y errores de guardado CLI), #92 (lectura/guardado y errores controlados, apilado sobre #89), #91 (fallo de objetivos bloqueados), y #87 (tipos inválidos de condiciones/efectos). Revisar orden de dependencias, diffs y CI antes de fusionar; una rama de PR NO equivale a corrección instalada en autoridad.

## 10. Cómo arrancarlo y comprobarlo

Desde la raíz del repositorio, **en la rama con implementación**:

    PYTHONPATH=src python -m textrpg.cli content/vertical_slice_01.json --save local_save.json

Para reanudar:

    PYTHONPATH=src python -m textrpg.cli content/vertical_slice_01.json --load-save local_save.json --save local_save.json

Pruebas Python:

    PYTHONPATH=src python -m unittest discover -s tests -v

Pruebas y compilación Android (requiere SDK/Gradle compatibles):

    gradle -p android testDebugUnitTest --stacktrace
    gradle -p android :app:assembleDebug --stacktrace

El workflow .github/workflows/android-pixel-client.yml también contiene una prueba de instrumentación en emulador con connectedDebugAndroidTest y verificaciones de APK/capturas. **Esta revisión fue un cotejo estático remoto: NO se ejecutaron aquí Python, Gradle, emulador, hardware ni la instalación de un APK.** No presentar resultados de CI de otros commits como si probaran este nuevo documento.

## 11. Protocolo de corrección de errores, sin crear características

1. Confirmar repositorio, rama y SHA; leer AGENTS.md, Bulletin y Coord. Room para evitar trabajo paralelo duplicado.
2. Reproducir el fallo con estado/contenido fijo y un test que falle; identificar módulo dueño de la regla.
3. Hacer el cambio mínimo y reversible en el módulo autoritativo; no trasladar reglas a la UI ni añadir sprites, contenido, personajes o mecánicas.
4. Añadir regresión, ejecutar Python y, si afecta Android, sus pruebas/compilación/emulador.
5. Contrastar el diff contra el HEAD de autoridad, mantener el PR como candidato hasta comprobar CI y dependencias.
6. No modificar main ni promocionar un borrador/canon sin aprobación; nunca tocar guardados de usuarios para “limpiar” un error.

## 12. Qué queda verificado y qué no

**VERIFICADO por lectura de archivos en dac5d22:** tecnologías; organización del código; modelo GameState; camino de elecciones; semilla del check; rutas Python/Android; esquema de guardado; fuentes de datos; puntos de riesgo señalados; existencia de PR abiertos.

**NO VERIFICADO en esta auditoría:** ejecución local exact-head, aprobación CI para este documento, Android en dispositivo físico, funcionamiento completo de todas las combinaciones de sistemas, integración de PR #87/#89/#90/#91/#92 o release APK. La documentación no convierte un PR abierto en código incorporado.

**Decisión de alcance:** esta entrega registra el engine **como existe**, para entenderlo y facilitar su depuración. No propone reescribirlo ni ampliar el juego.
