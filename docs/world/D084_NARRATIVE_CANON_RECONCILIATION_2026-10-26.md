# D-084 — Cruce de canon narrativo, procedencia y límites de integración

**Corte de revisión:** 2026-10-26 AST  
**Estado:** REVIEW / NO CANON PROMOTION / NON-OWNING D-084 SUPPORT  
**Rama de origen revisada:** `docs/master-game-development-program@dac5d22cdbe211d0d35d3df98b542be2653f1b85`  
**Responsabilidad:** auditoría de integración de las fuentes narrativas posteriores al 2026-10-08; no equivale a reclamar D-084 ni a reactivar ninguna entidad de Drive.

## 1. Resultado y autoridad

La directiva D-084 del repositorio (8 de octubre) es anterior a decisiones expresas del creador (9–13 de octubre), una narrativa prioritaria H-01–H-36, un registro relacional, un dossier de guerra y un manuscrito literario v0.9. **El expediente narrativo ya existe en Drive y se ha ampliado con NOV-XII (27 oct.); D-084 no debe reiniciarse como si no hubiese texto.** Tampoco está integrada ni aceptada automáticamente su semántica en los contratos técnicos del repositorio.

La autoridad de lectura para esta integración es:

| Código | Fuente verificada | Papel y frontera |
| --- | --- | --- |
| G-01 | Historia original prioritaria, H-01–H-36 [fuente Drive: recuperar por título en el Centro de Historia y Canon] (actualizada 14 oct.) | Decisiones narrativas expresas; el propio documento avisa que su integración formal en el repositorio está **pendiente** |
| G-02 | Centro de Historia y Canon [fuente Drive: recuperar por título en el Centro de Historia y Canon] | Índice y reglas de autoridad; informa que el manuscrito literario, actualizado actualmente a v0.9, no equivale a canon |
| G-03 | Registro histórico relacional v1.6 [fuente Drive: recuperar por título en el Centro de Historia y Canon] (sincronizado 26 oct., v1.6) | EVT/ENT/TEC/REL/CAP, cronología parcial y dependencias; registro **subordinado** a G-01 |
| G-04 | Manuscrito Volumen I v0.9 [fuente Drive: recuperar por título en el Centro de Historia y Canon] (27 oct.) | Doce secciones + nota y apéndices; **BORRADOR**, incluye escenas compuestas DR-01 y DR-05 |
| G-05 | Dossier de la Primera Guerra [fuente Drive: recuperar por título en el Centro de Historia y Canon] | Advertencias R-WAR-01–10; cuarentena de la cronología 2670/Veinfall/Halcyon |
| G-06 | Cuestionario maestro QH-01–28 [fuente Drive: recuperar por título en el Centro de Historia y Canon] | QH-01 está resuelta por H-36; las demás preguntas históricas continúan abiertas salvo evidencia posterior |
| R-01 | [Bulletin](../AI_TASK_BULLETIN_BOARD.md), [Master Task Register](../THE_GAME_MASTER_TASK_REGISTER.md) | D-084 READY/unclaimed en la rama inspeccionada; reglas de coordinación y aceptación |
| R-02 | [World Canon Decision Queue](WORLD_CANON_DECISION_QUEUE.md), [World Master Index](WORLD_DEVELOPMENT_MASTER_INDEX.md), [Gate Twelve](../../content/vertical_slice_01.json) | World-parent por decidir, esquemas técnicos y contenido jugable provisional, sin canon global aprobado |
| R-03 | [AGENTS](../../AGENTS.md) y Drive entity registry [fuente Drive: recuperar por título en el Centro de Historia y Canon] (última modificación 8 oct. AST) | Separan autorización de trabajo, activación, claim, integración y despliegue. Las siete entidades canónicas aparecen INACTIVE/null sesión al leerlas aquí |

**Regla de actualización:** las decisiones expresas más recientes del creador gobiernan el diseño narrativo; el código y la rama de autoridad prueban únicamente **qué está implementado**. Una decisión narrativa no migra por sí misma saves, clases, escenas, NPCs ni mundo jugable.

## 2. Estado del canon: matriz de reconciliación

| ID | Hecho o conflicto | Clasificación a 26 oct. | Acción segura |
| --- | --- | --- | --- |
| CW-01 | H-36: primeras aperturas, rupturas, llegada de invasores, primeras bestias y manifestación del Sistema pertenecen al **mismo estallido histórico**, sin simultaneidad de segundos obligatoria | DECISIÓN DEL CREADOR, G-01; rectifica órdenes anteriores | Conservar un **evento conjunto** con subeventos sin orden interno total; no representar una llegada tardía de las primeras bestias |
| CW-02 | H-01/H-34/H-35: invasores extraplanetarios inteligentes/tecnológicos **antes** de llegar, distintos de bestias con evolución potencial H-09/H-10/H-17 | DECISIÓN DEL CREADOR, G-01 | Distintas entidades e IDs, sin asumir que híbridos son invasores o firmantes de tregua |
| CW-03 | H-03–H-06/H-32–H-33: ayuda celestial indirecta, tableta oculta a invasores; Sistema de una habilidad principal aleatoria + derivadas, manifestado en crisis | DECISIÓN DEL CREADOR; mecanismo privado aún ABIERTO | Mantener el trasfondo oculto fuera de proyecciones públicas; no implementar concesión anticipada del Sistema |
| CW-04 | H-07/H-11/H-16: cristales ya presentes en bestias **antes** de llegar a Tierra; existen aplicaciones humanas y armas, pero fecha de descubrimiento/forja frente a guerra no fijada | DECISIÓN con orden parcial, G-01/G-05 | No colocar armas cristalinas obligatoriamente antes de Primera Guerra |
| CW-05 | H-12/H-13: Primera Guerra después del Sistema; termina en tregua territorial, **no paz** ni victoria confirmada | DECISIÓN con actores/fronteras/fechas ABIERTOS | No inventar vencedores, tratados, campañas, ejércitos o países |
| CW-06 | H-28–H-31: novela-documental omnisciente en tercera persona, larga y causal, con zonas grises | DECISIÓN EDITORIAL, G-01 | Reusar G-04 como borrador activo, no regenerar una segunda biblia contradictoria |
| CW-07 | `AC` = **Antes del Crystal**, según corrección explícita del 8 oct.; eras post-Evento, evento ancla y fechas exactas no validadas | DIRECTIVA EN REPO; cotejo de calendarios ABIERTO | No invertir AC ni equiparar automáticamente “Cristal” calendario a H-36 |
| CW-08 | Directiva 8 oct.: **mundo ficticio original**; H-01/H-28/H-36 posteriores hablan literalmente de **Tierra** y humanidad | CONFLICTO DE MODELO / MIGRACIÓN NO AUTORIZADA | Registrar ambas fuentes y pedir decisión de pertenencia/continuidad antes de convertir WORLD_*, mapas o fechas en hechos |
| CW-09 | El protagonista previo Jack Wilson/Steal y el vertical slice Gate Twelve/Trace Echo | DOS CONTINUIDADES SIN EQUIVALENCIA VALIDADA | Preservar IDs y evitar retcon automático, sustitución o fusión de poderes |
| CW-10 | `WORLD_CAUSALITY_ATLAS_2670_V1.json` y su par `.md`, “Veinfall”, 2645–2659 y “Halcyon Gate Concord” | EXISTENCIA ORIGINAL RECUPERADA EN BIBLIOTECA / CONTINUIDAD AÚN EN CUARENTENA, G-05/G-06 | Los archivos originales están localizados y fueron examinados por la revisión PR #85; queda por probar el vínculo de continuidad y adopción. No inferir equivalencia con H-12/H-13 |
| CW-11 | G-04 v0.9: escenas DR-01 (depósito de provisiones) y DR-05 (noticia de tregua) | ESCENAS COMPUESTAS, NO HECHOS | No crear localidades, NPCs, quests, rutas o leyes a partir de sus detalles |
| CW-12 | Gate Twelve: 9 nodos/8 aristas y `provisional_canon`; parent city/world no confirmado | REALIDAD DE IMPLEMENTACIÓN, NO WORLD CANON | No reescribir `content/vertical_slice_01.json` ni ruta del jugador al aceptar fuentes narrativas |

No hay evidencia de que un capítulo literario, el grafo de Drive o el D-084 de octubre estén formalmente unidos al runtime del repositorio. La rama registrada sigue siendo la autoridad técnica.

## 3. Grafo mínimo de causalidad — orden parcial, no línea temporal inventada

Companion machine-readable: [D084_CAUSALITY_GRAPH_2026-10-26.json](D084_CAUSALITY_GRAPH_2026-10-26.json).

- **Fuera del foco / antes:** invasores y seres celestiales tienen un antecedente de conflicto (H-02). No fijar sus fechas.
- **Estallido T0 (simultaneidad histórica):** `PORTAL_INITIAL_OPENING`, `SPATIAL_RUPTURES`, `INVADERS_INITIAL_ARRIVAL`, `BEASTS_INITIAL_ARRIVAL`, `SYSTEM_MANIFESTATION` (H-36). Las aperturas implican gran gasto de poder natural y causan rupturas (H-08); las bestias ya llevaban núcleos (H-16).
- **Transformaciones sin orden absoluto:** descubrimiento/aprovechamiento humano de cristales (H-11/H-19–H-27), aprendizaje del Sistema, evolución posible de bestias (H-10/H-17), movilización social. Sus posiciones exactas respecto al inicio y desarrollo de guerra no se deducen de H-36.
- **Secuencia inequívoca:** `SYSTEM_MANIFESTATION -> PRECEDES -> FIRST_TERRESTRIAL_WAR -> PRECEDES -> TERRITORIAL_TRUCE` (H-12/H-13). La tregua no resuelve todas las amenazas. El contexto jugable posterior tiene fecha/relación aún no confirmada.

**Principio:** causalidad no equivale a cronología universal; simultaneidad del suceso no obliga a conocimiento público simultáneo. Una narración puede exponer retrospectivamente algo que ocurrió a T0.

## 4. Límite mundo / reglas / conocimiento

| Capa | Fuente de autoridad | No hacer |
| --- | --- | --- |
| Historia **ocurrida** | G-01 decisiones H y G-03 relaciones validadas | Promover escenas dramáticas a hechos, asignar años sin ancla |
| Historia **divulgada** a habitantes | Solo hechos que tenga derecho a conocer cada observador; matriz de divulgación [fuente Drive: recuperar por título en el Centro de Historia y Canon] es PROPUESTA | Filtrar tableta/causas cósmicas a todos los NPCs o UI |
| **Narrador** documental | G-04, sujeto a G-01 y revisión editorial | Confundir omnisciencia literaria con verdad cerrada de preguntas abiertas |
| **Estado jugable** | `src/textrpg/`, `content/`, tests y contratos del repositorio | Añadir System, crystals, beasts, facciones o nuevos save fields sin schema/fixture/test/PR autorizado |
| **Mundo propuesto** | R-02, WD-001–WD-012 y contratos | Nombrar de oficio un país, convertir Gate Twelve en capital o imponer mapas en metros |

Ejemplo de **secreto narrativo confirmado**: la tableta vinculada al Sistema existe, pero los invasores la desconocen (H-04). Que el narrador pueda decirlo no autoriza a `build_scene_view`, NPC memory o Android a revelarlo a un personaje. Requiere política explícita de divulgación, conocimiento por actor y prueba de proyección player-safe.

## 5. Unidades de avance verificables (sin duplicar el manuscrito)

1. **Cruce editorial de D-084 con G-01–G-06.** Llevar a la autoridad técnica una decisión explícita sobre qué hechos narrativos se incorporan como canon de producción; mantener CW-07–CW-10 abiertos. No declarar D-084 DONE solo por este documento.
2. **Grafo estable y reversible.** Revisar nodos/aristas del JSON adjunto contra los H-IDs; resolver QH-25 solo tras hallar archivo matriz y procedencia. No forzar orden total ni año cero.
3. **Novela ya en curso.** Continuar CAP-14/15 sobre instituciones y cotidianeidad después de la tregua con escenas y extrapolaciones etiquetadas PROPUESTA; G-04 ha avanzado a v0.9 con NOV-XII «El oficio de volver a vivir», que trata la transición civil posterior a la tregua. No repetir ese capítulo: continuar la conexión hacia el escenario de los personajes solo desde decisiones y hechos verificables. No inventar instituciones “canónicas”.
4. **Protocolo de incorporación futura.** Tras aprobación del mundo/protagonista, escribir un mapa `narrative_fact_id -> authoritative_content_id -> state_owner -> projection_policy -> test`; no tocar código antes de esta puerta.
5. **Coordinación:** el registro de entidades leído muestra siete Player-AIs INACTIVE y ninguna sesión activa; no fingir activación, task claim, puntuación ni progreso de Silex D-072. Un agente habilitado puede reclamar D-084 por el Bulletin al retomar.

## 6. Verificación y handoff de esta entrega

- **Leído:** programa `AGENTS.md`, Bulletin, Register (D-084), Mission Control, Coordination, world index/canon queue, README y fuentes G-01–G-06.
- **Evidencia de revisión:** títulos de las fuentes Drive recuperables desde el Centro autorizado, H-ID/EVT/REL/WD y enlaces de navegación del propio repositorio; no se conservan enlaces directos a Drive en el archivo actual. No se obtuvo ninguna prueba de finalización de D-084.
- **No ejecutado:** motor Python, Android, CI, emulador o device; `git clone` local no estuvo disponible por resolución DNS.
- **Archivos afectados por esta propuesta:** únicamente este cruce documental y JSON causal; sin cambio de implementación ni Drive.
- **Siguiente acción segura:** no repetir NOV-XII; contrastar el nuevo capítulo con H-01–H-36 y la matriz de conocimiento, completar relaciones editoriales que falten para NOV-XII en el registro v1.6 mediante revisión y continuar la preparación documentada del escenario de los personajes solo con fuentes verificables.

**No modificar el Bulletin, el estado de Drive o el Master Register como DONE desde este expediente no propietario.**

## 7. Actualización de continuidad y visibilidad — 2026-10-27

**Fuentes posteriores al corte original:** el manuscrito de Drive ahora es **Volumen I v0.9**, con **NOV-XII «El oficio de volver a vivir»** insertado antes de la nota de archivo, que pasó a XIII. El Registro histórico relacional contiene sincronización **v1.6** de NOV-X/NOV-XI; no asumir que NOV-XII esté incorporado a dicho grafo sin lectura posterior. El nuevo pasaje trata recursos civiles, habilidades, suministros, memoria y recuperación bajo la tregua, con todas las extrapolaciones explícitamente **BORRADOR**. No se agregó otro capítulo en esta rama para evitar duplicación.

**Complemento no redundante:** el [PR #83](https://github.com/jbob-coder/Text-rpg-game/pull/83) conserva un puente documental de fuentes; el [PR #85](https://github.com/jbob-coder/Text-rpg-game/pull/85) aporta matriz de procedencia, frontera Drive→runtime y comprobación de existencia de los originales del atlas 2670. Este PR #84 aporta especialmente el **grafo JSON de orden parcial** y su índice WD; antes de fusionar propuestas se debe reconciliar la superposición para evitar tres autoridades de D-084.

**Privacidad de referencias:** se quitaron los enlaces directos a IDs de archivos privados de Google Drive de la versión actual de este documento. Localizar las fuentes mediante sus títulos verificables y el Centro de Historia y Canon en el Drive conectado. Esta corrección de contenido **no borra los commits anteriores del historial Git**; cualquier purga histórica requeriría una decisión distinta de reescritura de historial y su revisión de impacto. No copiar IDs de Drive a nuevos expedientes públicos.

**Estado:** propuesta no propietaria; ninguna activación de Player-AI, modificación de Bulletin o promoción de canon; sin pruebas Python/Android/device en esta intervención.

## 8. NOV-XII collision comparison — 2026-10-27, register readback verified

The Google Drive **Registro histórico relacional** now has a live, revision-guarded comparison record **CMP-XII-20261027**, verified by native document readback (not only by intended edit). Two different drafts share the provisional bare token `NOV-XII`:

- **NOV-XII-MANUSCRITO-v0.9** = «El oficio de volver a vivir», 16 narrative paragraphs embedded in the existing Volumen I, before the XIII archival note. Covers return to home, legitimacy and ability, education, civic memory, reconstruction.
- **NOV-XII-DR06-BORRADOR-v0.1** = «Lo que debía seguir funcionando», 22 narrative paragraphs in a distinct Drive document. Has a composed **DR-06** repair/inventory scene and more explicit logistical dependencies (source → transit → reception → use, material reserves, repeated deliveries, verification of repairs).

**Result:** comparison confirmed **distinct texts**, shared subject matter and complementary emphasis; do not silently overwrite, concatenate, import DR-06 into playable content, or allocate the same unqualified identifier to both. Retain the manuscript v0.9 as the current **literary** chapter XII and the other piece as a **separate proposal** until editor/owner chooses whether a limited logistics passage warrants revision. The register's labeled comparison is an **editorial recommendation only**, not approval, canon migration or task DONE. H-01–H-36, AC calendar, character continuity and runtime remain unchanged.

**Privacy:** locate the comparison under its exact ID in the connected Drive register; no private Drive file URLs/IDs are copied into this public repository proposal. This note does not correct earlier Git history that contained such links.

## 9. CAP-15 / DR-06 continuity QA — 2026-10-27

**Current revision supersedes earlier current-state observations in sections 5–8.** The connected-Drive Volumen I is now **v0.9.1**. After the source comparison CMP-XII-20261027, a separate editor incorporated an **adaptation of exactly three paragraphs** from fictional scene DR-06 after «Las normas que permiten convivir» into the chapter XII «El oficio de volver a vivir». The source NOV-XII-DR06-FUENTE-v0.1 remains unchanged. The relational register contains an explicit post-comparison correction, so the earlier statement that chapter XII does not yet contain DR-06 was correct only for manuscript v0.9.

**Further authoritative source review.** The connected Drive Knowledge and Disclosure Matrix contains B-PLAY-01–06 and six proposed integration gates: G1 creator provenance, G2 H/EVT causal evidence, G3 actor-specific knowledge/disclosure, G4 WD domain decisions, G5 existing content/IDs/save ownership, G6 executed tests. This proposal is **not** an implemented interface. The repository `content/vertical_slice_01.json` was independently read at source blob `3eeeb9d684ef31759eb11aa595e4d111b16c4c82`, with `CONTENT_VERTICAL_SLICE_01`, `canon_status=provisional_canon`, `The Dead Relay`, one `NPC_TAMSIN`, four quest entries, `ABILITY_TRACE_ECHO`, nine map nodes and eight map edges. The existing initial NPC state contains separate `knowledge`, `memories`, `goals`, `story_state` fields; these facts are about the prototype, not about historical lore.

| Audit ID | Source-backed constraint | Assessment and acceptance boundary |
| --- | --- | --- |
| QA-01 | H-36 concurrent initial openings, ruptures, invader/beast arrival, System | **SOURCE VERIFIED.** Do not place first beasts in a later chronological era, force exact-second simultaneity or imply everyone knew the facts immediately. |
| QA-02 | H-35 distinction of intelligent invaders and potentially evolving beasts | **SOURCE VERIFIED.** No automatic equivalence of invaders, beasts, Hybrid Beasts or treaty signatories. |
| QA-03 | H-04 celestial tablet unknown to invaders; general public awareness undetermined | **DISCLOSURE BLOCKED.** No HUD, NPC, dialog, quest or initial save may reveal tablet origin as public knowledge without authorized character-specific discovery. |
| QA-04 | H-11/H-16 human uses of pre-existing beast crystals, time of first forge still open | **ORDER OPEN.** No prewar-forging timeline edge or first Smith guild inferred. |
| QA-05 | H-12/H-13 First War after System, territorial truce without peace or confirmed victor | **SOURCE VERIFIED.** No fabricated battle, signatory, peace year, borders, or bestial participation. |
| QA-06 | Repository owner AC means `Antes del Crystal`; original 2645–2670 atlas exists but its lineage is unproven | **CALENDAR BLOCKED.** Do not use AC as After Crystal or import Halcyon/Kharvori/dates into present canon automatically. |
| QA-07 | NOV-XII manuscript v0.9.1 adapts three DR-06 paragraphs from standalone v0.1 | **TEXT READBACK VERIFIED; NONCANON.** No invented repair bench, people, stock ledger, deliveries or workshop from composite illustration in the game world. |
| QA-08 | `The Dead Relay` actual provisional content: `NPC_TAMSIN`, `ABILITY_TRACE_ECHO`, mission keys and map IDs | **REPO JSON PARSED; MIGRATION BLOCKED.** Preserve save keys and gameplay identity; later runtime changes require real Python/Android tests and verified ownership. |
| QA-09 | D-084 fictional crystal society vs H-history literal Earth | **PROVENANCE CONFLICT.** G1 must demonstrate the same world or receive an explicit owner direction. No retcon by paraphrase. |
| QA-10 | P-TRUCE-01..06 civilian economy, education, social customs, institutions and generations | **EDITORIAL PROPOSALS.** Use `[C]/[P]/[A]` markers; none establishes actual historical law, NPC lore, world map or classes. |

**Executed here:** fresh connected Google Docs text reads for current manuscript and relational register; connected-drive matrix excerpt; direct JSON parse of `content/vertical_slice_01.json`; crosscheck of the adapted scene with the source collision record. **Not executed:** Python engine suite, device playthrough, Android build, emulator, CI, APK, or any world migration. This is *source verification*, not production QA success.

**Next action:** keep the current v0.9.1 chapter rather than producing a duplicate XII, and proceed toward CAP-15 only through documented knowledge and provenance gates. PR #84 remains non-owning DRAFT; no activation, claim, merge or canon approval follows from this review.

## 10. CAP-15 editorial source handoff — 2026-10-27

The connected-Drive historical relational register now contains **`NOV-XIII-v0.2-DRIVE-INDEX`**, verified by native readback (exactly one entry). It locates the separate Google Doc **«THE GAME — CAP-15 / NOV-XIII — El mundo que todavía se descubre — BORRADOR v0.2»** without placing any private document ID in this public repository. The literary draft contains a 31-paragraph narrative and source/knowledge annotations for all eight `P-15-01` through `P-15-08` editorial sequences. It is **NOT part of the current Volumen I v0.9.1**, whose XIII is still «Nota del archivo histórico».

**Review condition:** keep the novel and the independently stored CAP-15 proposal separate unless a revision-guarded, reviewed literary integration explicitly replaces the archival-note numbering and preserves the original draft's canon disclaimers. D-084, WD-001, AC calendar, Jack/Steal vs Gate Twelve/Trace Echo, knowledge of the celestial tablet, and runtime G1–G6 gates remain unresolved. No new NPC, quest, saved knowledge flag, first forge date, or history event is authorized by this cross-reference. No Python/Android/runtime tests were executed here.
