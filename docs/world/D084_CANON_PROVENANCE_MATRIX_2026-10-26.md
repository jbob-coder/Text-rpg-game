# D-084 — Matriz de procedencia, canon y conflictos (lote no propietario)

**Fecha de lectura:** 2026-10-26; ampliación de fuentes históricas y sincronización editorial: 2026-10-27 (AST)  
**Proyecto:** THE GAME, `jbob-coder/Text-rpg-game`  
**Rama base auditada:** `docs/master-game-development-program` @ `dac5d22cdbe211d0d35d3df98b542be2653f1b85`  
**Tipo:** contribución preparatoria/revisable de D-084; NO reclama la tarea ni activa ninguna entidad Player-AI.  
**Estado:** DRAFT / NO MERGED / NO TECHNICAL CANON PROMOTION / NO RUNTIME CHANGE.

## 1. Alcance y autoridad

Este lote remedia un desfase de fuentes: el Bulletin y el Master Task Register describen D-084 con una última directriz del **8 de octubre**, mientras que el documento narrativo prioritario de Google Drive contiene decisiones del creador hasta el **13 de octubre**, en particular **H-32 a H-36**. El documento de referencia se titula **«THE GAME — Historia original prioritaria — 2026-10-10»** y el índice posterior **«THE GAME — Centro de Historia y Canon — Leer Primero»** (v1.0, 2026-10-13). Ambos se leyeron en la sesión que produjo este lote. No se copian URL privadas ni transcripciones a un repositorio público; los títulos, fechas e IDs H-## sirven para recuperar el original mediante el índice Drive autorizado.

**Separar siempre tres planos:**
1. **Narrativa confirmada por el creador en Drive:** hechos con IDs H-##. Guía para escritura, no prueba de implementación.
2. **Implementación verificable en GitHub:** código/contenido como `content/vertical_slice_01.json` y documentos de `docs/world/`. Los detalles de Gate Twelve son hechos del prototipo, no canon final del mundo.
3. **Propuesta literaria/editorial:** recreación no aprobada de la experiencia humana y las consecuencias. No puede elevarse por sí sola a canon.

**Regla:** una fuente posterior que aclare una cuestión narrativa supera una interpretación documental anterior de esa cuestión, pero no sustituye automáticamente los contratos técnicos ni los estados de tareas. El Bulletin sigue siendo la autoridad de claims.

## 2. Matriz de evidencia narrativa

| ID del paquete | Afirmación | Estado de narrativa | Fuente recuperable | Restricción de uso |
| --- | --- | --- | --- | --- |
| HC-01 | Los invasores conquistadores llegan del exterior del planeta, con inteligencia y tecnología avanzada anteriores a su llegada; ya se enfrentaron a seres celestiales. | CONFIRMADO | Historia prioritaria H-01/H-02/H-35 | No equipararlos a bestias o Hybrid Beasts; no narrar obligatoriamente la guerra cósmica. |
| HC-02 | La ayuda celestial concede un Sistema defensivo indirecto y existe en la Tierra una tableta pétrea vinculada al Sistema, desconocida para los invasores. | CONFIRMADO en lo general; mecanismo ABIERTO | H-03/H-04 | No explicar técnicas o medios de ocultación no establecidos; secreto de autor. |
| HC-03 | Un humano dispone de una habilidad principal y subhabilidades dependientes; asignación realmente aleatoria. | CONFIRMADO | H-05/H-06 | «La habilidad eligió» puede ser creencia social, no regla causal. No extrapolar fórmulas. |
| HC-04 | Portales de gran coste energético natural generan rupturas espaciales aprovechadas por los invasores. | CONFIRMADO en lo general; mecanismo ABIERTO | H-08/H-15 | No fijar energía, intención original, control total ni origen geográfico. |
| HC-05 | Las primeras aperturas, rupturas, invasores, bestias y Sistema corresponden al **mismo estallido histórico** que encuentra a la Tierra sin preparación específica. | CONFIRMADO; corrección más reciente | H-32/H-33/H-34/H-36 (2026-10-13) | La simultaneidad es histórica, no «mismo segundo» ni observación idéntica. **Supera** secuencias antiguas que ponían a las bestias después. |
| HC-06 | Las bestias llegaron con núcleos/cristales que ya portaban antes de llegar; pueden evolucionar y algunas llegar a formas humanoides e inteligencia mayor. | CONFIRMADO en general; progresión y sociedad ABIERTAS | H-09/H-10/H-16/H-17/H-18 | No asumir que los invasores evolucionan en híbridos o que los híbridos poseen política propia. |
| HC-07 | Cristal y diamante refieren al mismo material en estas conversaciones; humanos aprenden a utilizarlo y fabricar armas de estética medieval. | CONFIRMADO en general | H-07/H-11 | No inventar propiedades mágicas específicas, estadísticas o disponibilidad. |
| HC-08 | La Primera Guerra terrestre ocurre después de concederse el Sistema. | CONFIRMADO | H-12 | No atribuir fecha, duración, causas particulares o vencedor. |
| HC-09 | Una tregua territorial suspende la Primera Guerra y frena la conquista mutua; no establece paz definitiva. | CONFIRMADO en general | H-13 | Signatarios, límites, obligaciones y cronología precisos están ABIERTOS. |
| HC-10 | Forja: naturaleza del núcleo y habilidad/experiencia Smith influyen en la efectividad sin transmutación arbitraria ni duplicación automática de ventajas entre arma y portador. | CONFIRMADO en general; números ABIERTOS | H-19 a H-27 | Diseño separado; no convertir el primer volumen en un tutorial de forja. |
| HC-11 | La historia se escribe como novela-documental en tercera persona omnisciente, con foco en la civilización tras la irrupción, sus causas/efectos y zonas de incertidumbre. | CONFIRMADO | H-28/H-29/H-30 | «Tecnología como 2026» es comparación ilustrativa, no datación ni inventario de artefactos. |
| HC-12 | Existen decisiones cronológicas previas reclamadas por el creador que aún no se han localizado en las dos fuentes principales leídas. | POR VERIFICAR | H-31; Centro de Historia y Canon (2026-10-13) | No pedir arbitrariamente un nuevo lapso temporal, ni fijar comienzo del juego. |

### Cronología mínima: orden parcial, no años

- **T-antes:** enfrentamientos históricos entre invasores y celestiales, fuera del foco narrativo (H-02).
- **T-ruptura:** `{primeras aperturas, rupturas, invasores, bestias, manifestación del Sistema}` en una **fase simultánea** (H-32–H-36). Los núcleos de las bestias ya existían antes de su llegada (H-16).
- **T-guerra:** Primera Guerra **posterior** a la concesión del Sistema (H-12). Su relación con cada descubrimiento no consta.
- **T-tregua:** suspensión territorial de la Primera Guerra (H-13).
- **T-juego:** marco inicial jugable, **sin fecha/lapso verificado** (H-31).
- **T-aprendizaje [SIN POSICIÓN FIJA RESPECTO A T-guerra]:** los humanos aprenden a utilizar cristales y habilidades (H-05/H-07/H-11), pero **no está confirmado si las primeras armas de cristal aparecieron antes, durante o después del inicio de la guerra** (Dossier de la Primera Guerra, CAN-WAR-009 / R-WAR-01).

Estas relaciones **no** establecen años ni un orden total de descubrimientos. La posición editorial de T-aprendizaje en esta lista no indica precedencia temporal.

## 3. Matriz de contradicciones y cortafuegos

| ID | Fuente / conflicto | Disposición |
| --- | --- | --- |
| CX-01 | El Bulletin y el Master Register de 2026-10-08 no incorporaban H-36. | **Actualizar mediante revisión:** prevalece la simultaneidad de los cinco fenómenos (H-36); no marcar todavía integrado hasta revisión/merge. |
| CX-02 | `AC` fue erróneamente leído como *After Crystal* en material antiguo. | **CORRECCIÓN YA APROBADA en Bulletin:** `AC = Antes del Crystal`. La etiqueta posterior, fecha exacta del evento, «2010 AC» y «2000 BC» siguen pendientes de procedencia. |
| CX-03 | La directriz del repositorio llama al entorno **mundo ficticio original**, pero H-01/H-04/H-33/H-36 hablan explícitamente de **Tierra**. | **CONFLICTO DE ALCANCE, NO RESUELTO.** No renombrar el planeta ni decidir si «Tierra» es nombre literal, nombre provisional o etapa de continuidad. Conservar ambos contextos y pedir resolución solo para promover identidad planetaria final. |
| CX-04 | `docs/world/WORLD_CANON_DECISION_QUEUE.md` identifica Gate Twelve, mapas y personajes como contenido jugable `provisional_canon`; D-084 exige una sociedad de cristales. | **PENDIENTE DE ADAPTACIÓN.** No insertar retrospectivamente cristales en escenas sin diseño/contrato de migración. Gate Twelve prueba una región local, no el origen del mundo. |
| CX-05 | La habilidad Steal de Jack Wilson aparece en antecedentes del creador; Gate Twelve usa Trace Echo. | **INDEPENDIENTES / SIN MIGRACIÓN APROBADA.** No sustituir ni combinar habilidades o protagonistas. |
| CX-06 | `world_vantiel.txt` de la antigua continuidad describe Tres Murallas, Fractura y Pacto Radiante. | **HISTÓRICO / OTRO UNIVERSO.** No usar nombres, geografías, guerras ni magia como canon de THE GAME. |
| CX-07 | My Vampire System inspira el proyecto, pero sus instituciones/híbridos no son el canon original. | **REFERENCIA, NO IMPORTACIÓN.** No trasplantar personajes ni equivalencias de especies. |
| CX-08 | Una cronología vieja ponía llegada de bestias después de la manifestación del Sistema o les atribuía el pronombre «ellos». | **SUPERADO por H-34/H-35/H-36.** Invasores y bestias son categorías distintas, contemporáneas en la crisis. |
| CX-09 | Atlas antiguo 2670: guerra intermundial 2645–2659, acuerdo de 2660 y partida del 2670; H-12/H-13 no ofrecen fechas ni demuestran mismos bandos. | **VERIFICADO EN EL ATLAS ORIGINAL / NO PROMOVIDO.** Los años son válidos solo como contenidos de la fuente antigua; identidad de guerra, tratado y cronología con THE GAME actual por verificar. |
| CX-10 | Plan antiguo de 2010 AC explícitamente glosaba AC como *After Crystal* y describía cristales como motores de la sociedad en 2010 AC. | **SUPERADO POR LA CORRECCIÓN DEL CREADOR (2026-10-08):** AC significa *Antes del Crystal*. El plan histórico de desarrollo no fija la edad del presente jugable. |

## 4. Control de revelaciones: autor frente a jugador

| Materia | Conocimiento del autor | Presentación segura al jugador |
| --- | --- | --- |
| Ser celestial y tableta | H-03/H-04: origen general de la ayuda; tableta existe y permanece oculta a invasores | **NO PUBLICAR** como dato inicial del jugador. Descubrimiento narrativo por diseñar. |
| Aleatoriedad de habilidades | H-06: mecanismo real aleatorio | Pueden circular creencias sociales distintas, pero ninguna ha sido formalizada como diálogo canónico. |
| Rupturas e invasores | H-08/H-15/H-36: simultaneidad histórica, aprovechamiento de fisuras | Personajes solo pueden afirmar lo que su posición, época y conocimiento justifican; no darles omnisciencia. |
| Bestias y núcleos | H-16: poseen núcleos antes de llegar | No es automáticamente un dato público en los primeros días; debe establecerse su descubrimiento. |
| Tregua | H-13: acuerdo territorial general | Tratado literal, fronteras y experiencia de habitantes aún abiertos. |

**Nota editorial:** omnisciencia de la *obra histórica* no equivale a omnisciencia de NPCs ni autoriza spoilers de la *interfaz del juego*. Toda traducción a escenas necesita un contrato de revelación.

## 5. Índice de volúmenes y desarrollo acotado

- **Volumen I (YA EXISTE EN DRIVE):** «THE GAME — Historia novelada — Volumen I: La era de las rupturas — BORRADOR v0.9.1», verificado el **2026-10-27**, doce secciones narrativas I–XII y XIII «Nota del archivo histórico»; trabajo literario en revisión, no canon final. El capítulo XII es «El oficio de volver a vivir» y contiene una adaptación puntual y expresamente *ficticia* de la escena compuesta DR-06. La fuente independiente «Lo que debía seguir funcionando» permanece intacta, no es un capítulo segundo ni un evento validado. No crear otro Volumen I. Véase el [puente narración→juego](D084_DRIVE_TO_GAME_INTEGRATION_BOUNDARY_2026-10-26.md).
- **Volumen II (pendiente):** estudio humano de cristales, aprendizaje, resistencia y reorganización alrededor de la crisis y la guerra, **sin fijar anticipadamente cuándo ocurrió la primera forja**. Requiere fuentes concretas para evitar inventar eventos.
- **Volumen III (pendiente):** desarrollo de la Primera Guerra, bandos y consecuencias. Requiere eventos y participantes comprobados.
- **Volumen IV (pendiente):** tregua y normalización en la época jugable. Requiere cronología y contexto de sociedades/territorios.
- **Anexos pendientes:** arcos de facciones/personajes, reglas de conocimiento de NPCs, atlas, cronología absoluta y tabla de decisiones.

### Próxima secuencia verificable para D-084

1. La fuente primaria antigua del calendario **2670 ya se encontró en la biblioteca**: verificar ahora su *linaje y adopción* frente a H-36 antes de reutilizar años; el lugar exacto del archivo original no se publica en este repositorio. Buscar aún la fuente cronológica que gobierna la continuidad narrativa actual, si es distinta.
2. Reconciliar CX-03 (mundo ficticio frente a Tierra) sin silenciosamente reescribir H-01/H-36.
3. Examinar cómo integrar, si procede, la prueba de Gate Twelve a la civilización de cristales; preservar save/quest IDs y Trace Echo.
4. Continuar editorialmente el **manuscrito Drive v0.9.1 ya existente** (I–XII narrativo + XIII nota histórica), cruzándolo con REL y preguntas pendientes. Conservar los identificadores de procedencia NOV-XII-MANUSCRITO-v0.9.1 y NOV-XII-DR06-BORRADOR-v0.1; no crear una novela competidora ni promover la escena DR-06 a hecho histórico.
5. Solo tras claim legítimo y revisión: sincronizar D-084, índice de mundo, Master Documentation Record, Brag/Learning y el Bulletin. Nunca marcar **DONE** sin los entregables y aceptación completos.

## 5A. Nueva evidencia recuperada en Drive (26 de octubre)

El trabajo editorial avanzó fuera del repositorio: el manuscrito se había identificado originalmente como **Volumen I BORRADOR v0.8**, pero fue releído el **2026-10-27** ya en **v0.9.1** (12 secciones narrativas + nota XIII), junto a un **Registro histórico relacional** (v1.6 y adiciones del 2026-10-27), una **Matriz de divulgación**, el **Cuestionario QH** y el **Dossier de la Primera Guerra**. No duplicar sus capítulos ni su estructura de eventos en un archivo nuevo. En especial, el dossier localizó referencias al antiguo `WORLD_CAUSALITY_ATLAS_2670_V1` con guerra 2645–2659, acuerdo en 2660 y escenario 2670: son datos **HISTÓRICOS/DE PROCEDENCIA PENDIENTE**, no fechas aprobadas para la línea H-36. El atlas usa una secuencia previa que puede entrar en conflicto con H-36. **Actualización 2026-10-27:** el JSON y el Markdown del atlas original ya fueron encontrados y leídos en la biblioteca; resta comprobar **identidad de continuidad** y autoridad de adopción, no la existencia del archivo. El objetivo es comparar linaje y conservar divergencias explícitas. Véase el [contrato de integración narrativa al juego](D084_DRIVE_TO_GAME_INTEGRATION_BOUNDARY_2026-10-26.md).

## 5B. Auditoría directa del atlas anterior, 2026-10-27

**Fuentes recuperadas en la biblioteca personal (leídas, no importadas ni republicadas):**
- `WORLD_CAUSALITY_ATLAS_2670_V1.json`, 542 líneas de texto en el registro; `schema_version: 1.0.0`, `revision: 2`, `updated_at: 2026-08-23T20:18:00-04:00`. El campo `authority` se limita a **USER_DIRECTIVE_PLUS_ORIGINAL_CAMPAIGN_CANON_DERIVED_FROM_ACTIVE_WORLD_RECORDS** y `status` a **READY_FOR_CHAT_GAME_CAUSAL_REFERENCE**. Son atribuciones de **esa campaña**, no de esta rama de GitHub.
- `WORLD_CAUSALITY_ATLAS_2670_V1.md`: resumen explicativo del mismo atlas. Declara un encadenamiento local de Veinfall, economía de cristales, posterior expansión portal, guerra y reconstrucción de Asterline/Riverbend, sin afirmación de que sea el corpus de H-36.
- `Pasted text(48).txt`, transcripción histórica de un archivo de planificación Godot separado. Su pasaje `HIGH-LEVEL THEME` afirma `2010 AC` y `AC means After Crystal`; también planeaba `2000 BC gateway opening`. **Esa definición AC está expresamente anulada por la decisión más reciente del creador citada en CX-02**. No se adjudica esa planificación de Godot al juego actual.

**Cotejo de hechos en dos capas (la primera describe el contenido auténtico del atlas; la segunda evalúa su posible adopción):**

| ID | Qué afirma el artefacto antiguo | Relación con H-## vigente | Dictamen |
| --- | --- | --- | --- |
| LA-01 | `snapshot_world_datetime: 2670-08-31T06:00:00-04:00`; uso como referencia causal de una partida centrada en Jack | H-31 dice que falta comprobar el lapso de la historia original actual | **FUENTE ORIGINAL VERIFICADA, IDENTIDAD DE CONTINUIDAD NO VERIFICADA**. No cambiar la fecha del RPG ni inferir equivalencia con el protagonista provisional del slice. |
| LA-02 | `CAUSE_VEINFALL` (cristales/experiencia de habilidades/ecología bestial), seguido por `CAUSE_PORTAL_EXPANSION` (ciencia portal y expansión hacia recursos exteriores) | H-36 declara simultaneidad de **primeras aperturas**, rupturas, invasores, bestias y Sistema | **RELACIÓN INDETERMINADA**: una *expansión posterior* puede seguir a primeras aperturas sin contradicción. Sí sería conflicto afirmar que **los primeros portales** surgieron después de años de Sistema/cristales; el atlas no lo prueba por sí solo. |
| LA-03 | `CAUSE_FIRST_INTERWORLD_WAR`: conflicto humano/Kharvori 2645–2659 | H-12 confirma Primera Guerra terrestre posterior al Sistema, sin años, bandos ni identidad con Kharvori | **NO EQUIVALENCIA DEMOSTRADA**. Evitar copiar nombre, fechas o resultado. |
| LA-04 | `CAUSE_HALCYON`: acuerdo de 2660 que pone fin a guerra a gran escala sin eliminar tensión | H-13 confirma tregua territorial, sin fecha ni texto de tratado | **COMPATIBILIDAD TEMÁTICA, NO IDENTIDAD**. No rebautizar la tregua como Halcyon. |
| LA-05 | Tierra como Bastión humano; Asterline, siete wards, Eastbank/Riverbend; ruta de estudio de Jack a Ravelin | WD-001/WD-002 mantienen pendiente el lugar/tecnología global; Gate Twelve es `provisional_canon` | **GEOGRAFÍA Y PERSONAJE DE OTRA CAPA HISTÓRICA**. No inyectar barrios/coordenadas, política de residencia ni edad/academia en Gate Twelve. |
| LA-06 | Una planificación Godot antigua equipara `AC` con `After Crystal` y describe `2010 AC` como sociedad cristalina | Directiva posterior del propietario: `AC = Antes del Crystal` | **RECTIFICADO**. No usar `2010 AC` de esa propuesta para fechar una civilización posterior al cristal. |

### Regla formal de migración de datos temporales

Una fecha o topónimo del atlas solo puede promocionarse si se demuestra, en ese orden: **(1)** identidad del proyecto y universo, **(2)** misma continuidad/evento/personaje, **(3)** compatibilidad con decisiones expresas posteriores H-##, **(4)** aprobación o evidencia clara de adopción en la autoridad narrativa actual, y **(5)** mapeo de implementación independiente si afecta al juego. En ausencia de uno de esos eslabones, conservar el registro como **HISTÓRICO / CANDIDATO** y no marcar el evento como canon.

**Resultado:** la tarea anterior «localizar atlas» queda cerrada a nivel de existencia de fuente. La tarea nueva es **demostrar vínculo de continuidad**, sin inventar fechas. No se modificó la biblioteca ni el atlas, ni se transfirieron datos privados al repositorio público.

## 5C. Sincronización del manuscrito vivo y colisión NOV-XII, 2026-10-27

**Nueva fuente comprobada en Drive:** el Volumen I ya no termina en v0.8. Su encabezado actual es **BORRADOR LITERARIO v0.9.1**, con **doce secciones narrativas I–XII** y una **nota editorial/histórica XIII**. Se leyeron el encabezado, la tabla visible de títulos, el capítulo XII y el apéndice de conciliación fechado 2026-10-27. El registro histórico relacional conserva antecedentes de versiones inferiores y un cotejo editorial; **esos párrafos antiguos son historial, no el estado actual del manuscrito**.

- **ID único de la obra activa:** `NOV-XII-MANUSCRITO-v0.9.1` — sección XII de Volumen I, «El oficio de volver a vivir», con síntesis de continuidad material/civil tras la tregua. Estado: **BORRADOR / editorial**, no H-canon.
- **ID de fuente alternativa:** `NOV-XII-DR06-BORRADOR-v0.1` — «Lo que debía seguir funcionando», un borrador independiente de 22 párrafos registrado en Drive y **no eliminado**.
- **Integración comprobada:** los párrafos del capítulo XII después del apartado de normas cotidianas incluyen una **adaptación acotada** de la escena logística `DR-06`: material, reparaciones, solicitudes, prueba de objetos y disputa de reservas; etiquetada expresamente como **escena compuesta**, sin localidades/personajes/órganos oficiales o acontecimientos canónicos. El apéndice final confirma `DR-06-ADAPTADO` y conservación de la fuente independiente.
- **Regla de identidad:** `NOV-XII` sin calificador es ambiguo en registro histórico. No crear una segunda sección XII ni importar `DR-06` como mapa, NPC, quest, institución, ítems o ruta del juego. Nada en la descripción del episodio prueba que esos sucesos acontecieran literalmente.
- **Regla de autoridad:** el registro REL puede retener un cotejo de una versión anterior a la adaptación; ante divergencia documental se lee la versión **actual** del manuscrito y se conserva el registro antiguo como historial, sin alterar H-01–H-36.

**Consecuencia concreta para el RPG:** el tema de abastecimiento podría justificar un **futuro diseño** de recursos y actividades; **no** autoriza a generar automáticamente una economía, taller, NPC dedicado a reparaciones o misiones de `DR-06`. El puente de integración hermana añade gates y casos INT-12–INT-14. La próxima revisión debe verificar la versión Drive fresca y su continuidad antes de planificar nuevas escenas.

## 6. Verificación y límites de este lote

**Se leyó:** Bulletin Board, Master Task Register (entrada D-084), `AGENTS.md`, Mission Control, `docs/world/WORLD_CANON_DECISION_QUEUE.md`, `docs/world/WORLD_DEVELOPMENT_MASTER_INDEX.md`, Historia original prioritaria y Centro de Historia y Canon, el manuscrito existente Volumen I v0.8, Dossier de la Primera Guerra (2026-10-15), Matriz de divulgación del estallido (2026-10-14), Cuestionario maestro de historia y Registro histórico relacional con sincronización del 2026-10-26 (Drive), registry de Player-AIs; `world_vantiel.txt` solo para frontera histórica.

**No ejecutado:** suite Python, Android, CI, emulador ni dispositivo; no hay cambios de runtime. **Sin claim:** las siete entidades canónicas permanecían `INACTIVE` al consultar el registry; ninguna fue activada, prestada ni suplantada. Este lote vive en rama de revisión separada y no cambia la autoridad hasta merge explícito.
