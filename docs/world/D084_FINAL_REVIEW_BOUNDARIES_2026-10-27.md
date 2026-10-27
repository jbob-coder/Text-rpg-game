# D-084 — Gate de adopción histórica y divulgación (revisión no propietaria)

**Fecha de contraste:** 2026-10-27 AST. **Estado:** REVIEW-READY / PROPOSED / NOT CANON-PROMOTED.
**Repositorio:** `jbob-coder/Text-rpg-game`; PR #85, rama `docs/d084-canon-provenance-volume1-20261026`.
**Límite de esta aportación:** cierra criterios revisables de cronología, divulgación y adopción. **No** reclama D-084, no activa Player-AIs, no reescribe narrativa en Drive y no realiza migración de `content/`, saves, motor ni Android. D-084 integral continúa sujeto a gobernanza, aceptación narrativa y decisiones de autor.

## 1. Fuentes cotejadas y precedencia

1. **Decisión expresa del creador:** mundo de ficción original centrado en cristales, portales y consecuencias sociales (Bulletin/Master Register, 2026-10-08). `AC = Antes del Crystal` confirmado. No es necesario volver a preguntar si el mundo es ficticio.
2. **Hechos históricos:** Drive, `THE GAME - Historia original prioritaria - 2026-10-10`, entradas H-01–H-36, con actualizaciones hasta 2026-10-13. Hechos narrativos `CONFIRMADO` no equivalen a contenido ya migrado.
3. **Visibilidad por perspectiva:** Drive, `THE GAME — MATRIZ DE CONOCIMIENTO Y DIVULGACIÓN DEL ESTALLIDO — v1.0 — PROPUESTAS`, M-01..M-08: observación humana e interpretación editorial pueden permanecer desconocidas. La matriz es instrumento, no canon independiente.
4. **Puente editorial contemporáneo:** Drive, `THE GAME — CAP-15 — Puente hacia la época jugable — Escaleta y contrato narrativo — PROPUESTA v0.1 — 2026-10-27`. Ocho secuencias propuestas y tres capas C/K/I; **CAP-15 no renumera el Volumen I ni habilita escenas de juego**.
5. **Novela:** Drive, `THE GAME - Historia novelada - Volumen I - BORRADOR v0.9.1`; I–XII y nota XIII, con adaptación compuesta DR-06 identificada y alternativa NOV-XII preservada. Una escena propuesta no es acontecimiento histórico.
6. **Implementación:** `content/vertical_slice_01.json` en `docs/master-game-development-program`, `CONTENT_VERTICAL_SLICE_01`, `provisional_canon`; `NPC_TAMSIN`, `KNOW_RELAY_DESTINATION_SERVICE_GATE_12`, `TRACK_RELAY_CASE` son IDs persistentes del producto. `docs/systems/SOCIAL_SCHEMA_API_MIGRATION_PACKET.md` define separación de conocimiento/estado (diseño; no licencia de migración).

Precedencia por dominio: instrucciones explícitas posteriores del creador > inferencias editoriales anteriores; hechos H-## > reconstrucción literaria; para runtime y saves, **código y contrato técnico verificados** > descripción narrativa. Nunca usar una fuente histórica de otra campaña como puente de autoridad por coincidencia temática.

## 2. Clasificación cerrada de hechos y conflictos

| Clave | Lo que se puede afirmar | Lo que **no** se puede afirmar / decisión necesaria | Tratamiento |
| --- | --- | --- | --- |
| B-01 | Las primeras aperturas de portales, rupturas, invasores inteligentes, bestias y Sistema pertenecen al mismo estallido histórico (H-32..H-36). | Mismo segundo, microorden, lugar, fecha, testigo común. | Una fase, cinco tipos; no cinco años. |
| B-02 | Sistema previo a la Primera Guerra (H-12) y tregua territorial posterior (H-13). | Vencedor, firmantes, fronteras, época jugable o fecha absoluta. | Orden parcial y campos nulos. |
| B-03 | Las bestias traían cores antes de llegar (H-16); no son invasores ni Hybrid Beasts por defecto (H-10/H-14/H-35). | Subordinación política, alianza, fisiología inventada, fecha de primera forja. | Taxonomías separadas; progresión/forja sin cifras. |
| B-04 | Un ser celestial otorgó el Sistema; la tableta existe y los invasores la desconocen (H-03/H-04). | Ubicación exacta, mecanismo, descubridores, conocimiento inicial de humano, NPC o jugador. | Hecho de autor; no conocimiento público automático. |
| B-05 | Asignación verdaderamente aleatoria de una habilidad principal y posibles subhabilidades (H-05/H-06). | Varias habilidades principales, 'la habilidad eligió' como ley causal, equivalencia con Trace Echo/Steal. | Creencia y regla objetiva separadas. |
| B-06 | `AC` significa `Antes del Crystal` (decisión del 8/10). | `After Crystal`, nombre de era posterior, año del evento, cronología 2010 AC como posterior. | Interpretación histórica revocada, no renombrar era. |
| B-07 | La directiva del juego establece mundo ficticio original; H-01..H-36 utiliza a veces 'Tierra'. | Que 'Tierra' sea ya el topónimo final o una segunda Tierra; cambiar palabras del autor silenciosamente. | **PENDIENTE** reconciliación de designación planetaria (WD-001); no reabrir la naturaleza ficticia del mundo. |
| B-08 | Atlas `WORLD_CAUSALITY_ATLAS_2670_V1` pertenece a una campaña anterior, sin vínculo de adopción. | Trasladar años 2645–2659/2660/2670, acuerdos o facciones. Expansión posterior de portales ≠ apertura inicial por definición. | HISTORICAL_UNLINKED. |
| B-09 | El manuscrito XI/XII y DR-06 son borradores editoriales. | Convertir escena compuesta, instituciones, suministros, rutas o nombres en hechos/quests. | Editorial, no `content/`. |
| B-10 | Gate Twelve/Trace Echo existe como `provisional_canon`; Jack/Steal tiene línea histórica del creador. | Fusionarlos, escoger uno o reescribir saves sin decisión de continuidad. | Bloqueo de promoción de historia→juego. |

## 3. Contrato mínimo de conocimiento: autor != personaje

Para cualquier hecho `fact_id` evaluado como contenido futuro, exigir antes de uso en diálogo, journal, escena o proyección:

- **Verdad de autor:** `fact_id`, fuente H-## y estado `confirmed / proposed / unresolved`.
- **Titular del conocimiento:** protagonista/jugador, NPC por ID, grupo o narrador; nunca asumir `all`.
- **Adquisición:** observación, enseñanza, documento, recuerdo o evento **realmente autorizado**, con referencia de fuente/escena. Si no existe, dejar `unknown`, no `true`.
- **Nivel de revelación:** hecho verificable, rumor, creencia, interpretación retrospectiva o secreto de autor; separe lo verdadero de lo conocido.
- **Persistencia:** conservar `state.knowledge` como conocimiento del jugador y `state.npcs[id].knowledge`/memories/goals/story_state como estado privado; no generar claves durables nuevas por narrativa.
- **Proyección Android:** pasar solo información explícitamente permitida en la vista que consume el usuario; nunca el mapa bruto de NPC ni información de omnisciencia del manuscrito.

Caso concreto `SYSTEM_TABLET_EXISTS` (identificador **solo del revisor**, no un ID runtime): hecho verdadero H-04; `invader_knowledge = DOES_NOT_KNOW`; jugador inicial/NPC inicial **no especificados**. No autorizar pantalla, pista, recompensa, flag ni diálogo inicial hasta tener transmisión authored. Tampoco basta con ocultarlo de la UI si una API devuelve el secreto en `view.meta` o en serialización pública.

## 4. Adopción de un acontecimiento al juego: puertas independientes

**A — Identidad:** decisión explícita de continuidad entre la sociedad de cristales, la ubicación Gate Twelve y la trayectoria Jack/Steal vs Trace Echo; referencia/versión trazable. Si no: rechazar integración, conservar slice actual.

**B — Tiempo:** usar precedencia parcial `REVIEW_INITIAL_BURST -> FIRST_WAR -> TERRITORIAL_TRUCE`; permitir solapamientos de percepción, nunca inventar años/microorden ni adoptar atlas antiguo. La forja no adquiere una ubicación temporal inventada.

**C — Perspectiva:** para cada escena, marcar cuál personaje sabe qué hecho y por qué. El narrador retrospectivo puede saber más que jugador/NPC; invasores no conocen tableta.

**D — Save y entidad:** preparar migración versionada si se cambia contenido durable. Sin consentimiento, conservar `NPC_TAMSIN`, `TRACK_RELAY_CASE`, `KNOW_RELAY_DESTINATION_SERVICE_GATE_12`, saves schema v1 y rutas actuales. No generar NPC/locations/routes/quests/items/abilities desde propuestas literarias.

**E — Verificación:** pruebas de parser/revisión independientes de tests de runtime. Cuando exista adopción real, añadir fixtures de jugador nuevo, NPC ignorante, jugador con descubrimiento, save viejo/new roundtrip, proyección Android, simultaneidad por fase, progresión de habilidad y no duplicación de contenido. No confundir un validador editorial PASS con aprobación de jugabilidad.

## 5. Qué queda decidido, qué está bloqueado y cierre del lote

**Cerrado a nivel de revisión:** fuente prioritaria identificada, corrección AC, evento H-36 sin microorden, guerra/tregua sin fechas, diferenciación invasor/bestia/Hybrid, tableta como secreto, identidad de capítulos NOV-XII, rol propositivo de CAP-15, preservación de la continuidad Gate Twelve y atlas como histórico no adoptado.

**Bloquea la aceptación total D-084 (no se resuelve automáticamente):**
1. Nombre/destinación de la palabra 'Tierra' en la continuidad de ficción (no la decisión ya tomada de que el mundo es ficticio).
2. Época jugable, nomenclatura posterior al Crystal, geografía macro y vínculos con el slice (WD-001/002).
3. Elección de continuidad de protagonista y habilidad principal: Jack/Steal frente a Gate Twelve/Trace Echo.
4. Tratamiento aprobado de las fuentes/editoriales pendientes y ratificación del volumen/biblia para producción.
5. Designación/CLAIM legítima y registro de aprobación según Bulletin, Master Register y control de cambios.

**Salida comprobable en esta PR:** `D084_EVENT_KNOWLEDGE_REVIEW_MANIFEST_2026-10-27.json` y `tools/validate_d084_review_manifest.py` verifican que el manifiesto sea cerrado, no importable, no auto-revele conocimiento y conserve el baseline. `tests/test_d084_review_manifest.py` contiene ahora **33 pruebas definidas**: las 26 del ciclo anterior (con ejecución confirmada en el flujo remoto #411), más **7 regresiones añadidas** en este ciclo contra filtración de identificadores editoriales dentro del contenido inicial, diálogo, claves JSON y tipos inválidos de conocimiento de NPCs. El control recorre el `content/vertical_slice_01.json` real y no se limita a inspeccionar el manifiesto. **Las siete pruebas nuevas requieren comprobar el CI del commit actual**; no atribuirles por anticipado el resultado del flujo #411. Ninguna sustituye futuras pruebas de saves, Android o contenido autorizado.

**Decisión de seguridad:** PR #85 permanece **DRAFT, NO MERGE, NO CLAIM D-084**, hasta revisión legítima. Este lote evita trabajo duplicado, deja especificado el camino de aceptación y no fabrica decisiones del creador.


## 6. Cierre de hueco del validador: contenido real (revisión 2026-10-27)

**Riesgo verificado por inspección del validador previo:** el revisor comprobaba la etiqueta declarativa «no conceder el secreto», pero no recorría el `content/vertical_slice_01.json` para comprobar si un identificador interno de D-084 había sido introducido accidentalmente en diálogos, escenas, conocimiento inicial de jugador/NPC, claves o metadatos. Ausencia de cobertura no prueba una filtración existente.

**Cambio de esta rama:** `tools/validate_d084_review_manifest.py` recorre recursivamente claves y valores del contenido real para rechazar cuatro identificadores exclusivos de revisión (`SYSTEM_TABLET_EXISTS`, `REVIEW_INITIAL_BURST`, `FIRST_WAR`, `TERRITORIAL_TRUCE`). Comprueba además el tipo de los contenedores de conocimiento inicial y del estado social de Tamsin. `tests/test_d084_review_manifest.py` incluye siete pruebas negativas específicas para ese límite.

**Alcance:** este control detecta esos identificadores textuales únicamente; no es un análisis semántico de todos los spoilers posibles. Una descripción equivalente con otras palabras exigiría revisión editorial y futuros tests de proyección. No se implementa el secreto ni una ruta de importación al motor.

**Ejecución pendiente de precisar:** el flujo #411 pasó antes de las siete pruebas nuevas. La evidencia del cambio corresponderá al flujo #413 o al posterior de un HEAD que lo contenga. No inferir PASS hasta que termine.
