# D-084 — Puente de continuidad: canon de Drive → THE GAME jugable

**Fecha:** 2026-10-26 (AST)  
**Clase:** análisis de integración documental, **NO implementación**.  
**Estado:** PROPUESTA / revisión; no reemplaza el manuscrito ni crea canon.  
**Paquete hermano:** [matriz de procedencia D-084](D084_CANON_PROVENANCE_MATRIX_2026-10-26.md).  
**Base GitHub inspeccionada:** `docs/master-game-development-program` @ `dac5d22cdbe211d0d35d3df98b542be2653f1b85`.

## 1. Hallazgo que cambia el plan

En Google Drive **ya existe** la historia literaria original en `THE GAME — Historia novelada — Volumen I: La era de las rupturas — BORRADOR v0.8` (documento de ~115 mil caracteres recuperado; encabezado actualizado 2026-10-15, notas de continuidad agregadas posteriormente). **No escribir un nuevo Volumen I paralelo en GitHub.** Este documento no compite con ese manuscrito: define cómo podría alimentarse el diseño del videojuego una vez resueltos canon, conocimiento del jugador, identidad y compatibilidad de contenido.

Fuentes narrativas recuperadas, con función distinta y sin copiar URL privadas al repositorio público:

| Etiqueta | Fuente Drive (título identificable) | Papel | Estado de autoridad |
| --- | --- | --- | --- |
| CAN | THE GAME — Historia original prioritaria — 2026-10-10, con H-01–H-36 hasta 13 de octubre | Hechos expresos del creador | Prioridad narrativa; canon técnico aún sin migración formal |
| CEN | THE GAME — Centro de Historia y Canon — Leer Primero (2026-10-13) | Lectura/decisiones/procedencia | Índice, no canon paralelo |
| REL | THE GAME — Registro histórico relacional — Eventos, entidades, vínculos y capítulos (v1.6, entrada 2026-10-26) | ENT, EVT, REL, CAP y estado temporal | Trazabilidad de la novela |
| NOV | THE GAME — Historia novelada — Volumen I — BORRADOR v0.8 | Narración literaria extensa | **BORRADOR**, no contenido jugable aprobado |
| WAR | THE GAME — Dossier de la Primera Guerra — fuentes y continuidad (2026-10-15) | Riesgos R-WAR y continuidad bélica | Investigación, no canon |
| DISC | THE GAME — Matriz de conocimiento y divulgación del estallido (2026-10-14) | Narrador/seres humanos/invasores/secretos | Propuesta editorial, no acceso de NPCs confirmado |
| QH | THE GAME — Cuestionario maestro de historia — Q&A por etapas | Preguntas aún no resueltas | Herramienta, no decisiones nuevas |
| ♾ | THE GAME — Continuidad contextual, permisos y retoma — Leer Primero (2026-10-13) | Interpretación de continuidad autónoma | Permisos/retoma; no habilita identidad Player-AI suspendida |

**Hallazgo sobre calendario — verificado con fuente primaria 2026-10-27:** WAR condujo al original `WORLD_CAUSALITY_ATLAS_2670_V1.json` y su par `.md`, localizados y leídos directamente en la biblioteca del usuario. El JSON consta de 542 líneas, revisión 2 del 2026-08-23, y se autodefine como **referencia causal de una campaña original de chat**, no como canon técnico de este repositorio. Contiene una guerra intermundial humano/Kharvori 2645–2659, el acuerdo Halcyon de 2660 y snapshot de 2670. **Esas fechas existen en esa fuente, pero su pertenencia a H-36 no está probada.** Importa distinguir *primera apertura* (H-36) de *expansión posterior de portales* (atlas): una secuencia de expansión posterior no contradice por sí sola la simultaneidad inicial. **No migrar** fechas, bandos, nombres, coordenadas, población ni relaciones de Jack a este juego por parecido. Restan pruebas de identidad y adopción, no buscar el archivo otra vez. Véase auditoría LA-01..LA-06 en la matriz hermana.

## 2. Reconciliación con el producto actual

Lectura puntual real de `content/vertical_slice_01.json` en la rama autoritativa:

- `content_id = CONTENT_VERTICAL_SLICE_01`; `canon_status = provisional_canon`.
- Apertura `OPENING_DEPOT_BLACKOUT` con flags de estado `world.trace_echo_quest_started` y otros flags locales.
- Contiene `NPC_TAMSIN` con `knowledge`, `memories`, `goals` y `story_state` separadas en el estado inicial.
- `docs/world/WORLD_CANON_DECISION_QUEUE.md` registra Gate Twelve y lugares del distrito, además de WD-001 (identidad y emplazamiento), WD-002 (tecnología/física global) y decisiones relacionadas sin resolver.
- `docs/systems/SOCIAL_SCHEMA_API_MIGRATION_PACKET.md` (D-062) define separación de conocimiento de jugador/NPC, persistencia, visibilidad y migración **como diseño**, no como permiso de reescribir la historia de Tamsin.

**Conclusión operativa:** la ficción original del mundo de cristales no está incorporada automáticamente en esa apertura. No es válido tratar escenas Gate Twelve como evidencia de H-01–H-36 o inyectar el nuevo canon mediante una búsqueda/sustitución de strings. Hace falta un contrato de migración o una separación explícita de campañas, según decisión editorial.

## 3. Matriz de consumidores y límites de implementación

| Dependencia narrativa | Contrato a acordar primero | Consumidor futuro (propuesta, no código confirmado) | Criterio de protección |
| --- | --- | --- | --- |
| H-36: estallido simultáneo | `STORY_EVENT` estable con cinco subeventos concurrentes y una **etiqueta de fase**, sin inventar fecha, lugar o microorden | Referencias de historia, lector de lore, contenido de quests | No generar cinco timestamps necesariamente diferentes o secuencias no aprobadas |
| H-03/H-04: origen Sistema/tableta | Identidad de `secret_fact` y política de revelación por progresión | Player projection, journal, NPC knowledge | La tableta no aparece en HUD/diálogo/inventario inicial sin descubrimiento autorizado |
| H-05/H-06: habilidad principal aleatoria | Autoridad de asignación, subhabilidades y migración de progreso definida por D-032 / D-061 y padres | Motor de progresión, Android Stats | No convertir Trace Echo/Steal en una equivalencia sin decisión; no sumar habilidades principales |
| H-09/H-10/H-16: bestias y núcleos | Taxonomía de bestia separada de invasores, provenance del core, evolución propuesta | Bestiario, loot, crafting, NPCs | No adjudicar humanoides automáticamente a invasores ni instanciar etapas numéricas no aprobadas |
| H-11/H-19–H-27: forja | Destino de atributo, tipo de core, habilidad Smith, guardarraíl de duplicación de buffs | Ítems/recetas/balance | No escribir formulas ni craft instantáneo sin diseño aprobado |
| H-12/H-13: Primera Guerra y tregua | Timeline parcial de estado de mundo y facciones; años solo con fuente propia | Quest history, mapas políticos, codex | No firmantes, vencedor, mapa de fronteras o cronología derivados de otro proyecto |
| H-28–H-31: presentación histórica | Política `author_known` / `public_known` / `player_discovered` / `npc_known` | Contenido narrativo, bridge, Android UI | Omnisciencia literaria != conocimiento del jugador |

La tabla es una **agenda de contratos**, no afirma que las estructuras o claves propuestas (`STORY_EVENT`, `secret_fact`, etc.) existan ya en el motor.

## 4. Grafo mínimo de dependencias para el programa

```mermaid
flowchart TD
    CAN["Decisiones H-01..H-36 · fuente Drive"] --> REL["Registro relacional ENT / EVT / CAP"]
    CAN --> CON["Matriz de conflictos D-084"]
    REL --> NOV["Manuscrito v0.8 · BORRADOR"]
    CON --> DEC{"Canon de mundo y alcance definidos?"}
    NOV --> REV["Revisión editorial y secretos"]
    REV --> DEC
    DEC -->|No| HOLD["Conservar Gate Twelve provisional"]
    DEC -->|Sí| MIG["Contrato de migración de contenido + saves"]
    MIG --> TEST["Pruebas de exposición / compatibilidad"]
    TEST --> GAME["Contenido jugable validado"]
```

**Precondición de esta ruta:** el historial del Drive no sustituye la autoridad de implementación actual del repositorio. Las decisiones editoriales deben atravesar revisión de estado, schemas y pruebas antes de crear mecánicas.

## 5. Pruebas futuras especificadas, NO ejecutadas

| ID | Escenario a convertir en prueba cuando exista implementación | Resultado esperado |
| --- | --- | --- |
| INT-01 | Importación de cinco eventos H-36 del mismo estallido | Pertenecen a una fase común y no se les asigna orden histórico ficticio |
| INT-02 | Proyección inicial de nuevo jugador sin conocimiento secreto | Tableta y origen oculto no filtrados en vistas públicas/Android |
| INT-03 | NPC sin conocimiento de tableta realiza diálogo habitual | No puede revelar lo no aprendido; otro campo privado tampoco se expone |
| INT-04 | Save antiguo de Gate Twelve antes/después de migración consensuada | IDs previos preservados o migrados explícitamente; no pérdida silenciosa |
| INT-05 | Habilidad principal preexistente | No se duplica ni fusiona con otra identidad al aplicar H-05 |
| INT-06 | Registro de invasor y criatura evolucionada | Son tipos separados; no comparten por defecto rol político ni progresión |
| INT-07 | Evento guerra/tregua con campos desconocidos | Falta de año, firmantes o coordenadas no se rellena con valores inventados |
| INT-08 | Borrador NOV v0.8 en corpus de contenido | No se expone automáticamente como escena/journal canon; revisión requerida |
| INT-09 | Ingesta de atlas viejo con fechas de guerra 2645–2659/2660 y metadatos de campaña | Debe permanecer HISTORICAL/UNLINKED hasta comprobación de continuidad; ni años ni bandos se convierten en hechos H-12/H-13 |
| INT-10 | Atlas menciona expansión de portales, canon H-36 exige primer estallido simultáneo | La validación distingue ‘initial opening’ de ‘later expansion’ y no infiere contradicción automática ni altera el orden de H-36 |
| INT-11 | Entrada legada interpreta AC = After Crystal | Debe quedar marcada SUPERSEDED ante directiva del creador AC = Antes del Crystal, sin calcular años del presente jugable |

Estas pruebas son **criterios propuestos**, no archivos test añadidos ni reportes PASS de ejecución.

## 6. Riesgos y próximos pasos sin solapamientos

1. **Calendario:** los archivos principales `WORLD_CAUSALITY_ATLAS_2670_V1.json` / `.md` están **localizados y leídos** en la biblioteca; rastrear ahora el vínculo de continuidad que justificaría adoptar sus fechas en H-36. Si no existe evidencia suficiente, conservar sus fechas solo como cronología de la campaña antigua.
2. **Manuscrito:** seguir trabajando en NOV v0.8 y REL v1.6 en su continuidad Drive autorizada; **no** crear un segundo Volumen I en GitHub.
3. **Identidad planetaria:** conciliar el uso reiterado «Tierra» de H-## con la directriz de «mundo ficticio original» en el Master Register.
4. **Producto:** una vez validados conceptos narrativos, preparar un contrato para conectar historias al slice jugable sin perder saves/quests ni filtrar secretos; no intervenir en D-072/Silex ni en claims inactivos.
5. **Gobernanza:** D-084 seguía READY/UNCLAIMED en el Bulletin inspeccionado. La contribución es **no propietaria**; requiere claimant legítimo, revisión, sincronización del Master Register/Bulletin/índices y aprobación de canon antes de promoverse a terminado.

## 7. Evidencia de revisión

**Leídos:** `AGENTS.md`, `docs/AI_TASK_BULLETIN_BOARD.md`, D-084 del master register, `docs/world/WORLD_CANON_DECISION_QUEUE.md`, `docs/world/WORLD_DEVELOPMENT_MASTER_INDEX.md`, `content/vertical_slice_01.json`, `docs/systems/SOCIAL_SCHEMA_API_MIGRATION_PACKET.md`, fuentes CAN/CEN/REL/NOV/WAR/DISC/QH/♾ de Drive y, en biblioteca personal, los **dos archivos originales** `WORLD_CAUSALITY_ATLAS_2670_V1` junto a una antigua planificación Godot con interpretación errónea de AC. No se copiaron fuentes de la biblioteca al repositorio público.

**Sin cambios:** runtime, APK, tests, estado de jugadores, reclamaciones de tarea, GitHub authority branch y canon aprobado. La lectura de documentos y el diff GitHub son verificaciones documentales; ninguna suite de pruebas de juego fue ejecutada.
