# D-084 — Matriz de procedencia, canon y conflictos (lote no propietario)

**Fecha de lectura:** 2026-10-26 (AST)  
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
- **T-adaptación:** los humanos aprenden a emplear cristales y el Sistema, en una secuencia interna todavía no cerrada (H-05/H-07/H-11).
- **T-guerra:** Primera Guerra **posterior** a la concesión del Sistema (H-12). Su relación puntual con cada descubrimiento no consta.
- **T-tregua:** suspensión territorial de la Primera Guerra (H-13).
- **T-juego:** marco inicial jugable, **sin fecha/lapso verificado** (H-31).

Estas relaciones **no** establecen cuántos años median entre etapas.

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

- **Volumen I (YA EXISTE EN DRIVE):** «THE GAME — Historia novelada — Volumen I — BORRADOR v0.8», manuscrito extenso en continua revisión, no canon final. No crear otro Volumen I paralelo. Véase el [puente narración→juego](D084_DRIVE_TO_GAME_INTEGRATION_BOUNDARY_2026-10-26.md).
- **Volumen II (pendiente):** estudio humano de cristales, aprendizaje, resistencia y reorganización antes de la guerra. Requiere fuentes concretas para evitar inventar eventos.
- **Volumen III (pendiente):** desarrollo de la Primera Guerra, bandos y consecuencias. Requiere eventos y participantes comprobados.
- **Volumen IV (pendiente):** tregua y normalización en la época jugable. Requiere cronología y contexto de sociedades/territorios.
- **Anexos pendientes:** arcos de facciones/personajes, reglas de conocimiento de NPCs, atlas, cronología absoluta y tabla de decisiones.

### Próxima secuencia verificable para D-084

1. Recuperar del Centro Drive la fuente cronológica original que sustenta el lapso ya decidido; registrar **archivo y evidencia**, no pedir una fecha nueva por defecto.
2. Reconciliar CX-03 (mundo ficticio frente a Tierra) sin silenciosamente reescribir H-01/H-36.
3. Examinar cómo integrar, si procede, la prueba de Gate Twelve a la civilización de cristales; preservar save/quest IDs y Trace Echo.
4. Continuar editorialmente el **manuscrito Drive v0.8 ya existente**, cruzándolo con los registros de continuidad y preguntas pendientes. No crear una novela competidora en el repositorio ni promover propuestas a hechos aprobados.
5. Solo tras claim legítimo y revisión: sincronizar D-084, índice de mundo, Master Documentation Record, Brag/Learning y el Bulletin. Nunca marcar **DONE** sin los entregables y aceptación completos.

## 5A. Nueva evidencia recuperada en Drive (26 de octubre)

El trabajo editorial avanzó fuera del repositorio: ya existe en Drive el manuscrito **Volumen I BORRADOR v0.8**, un **Registro histórico relacional** (v1.6, actualización 2026-10-26), una **Matriz de divulgación**, el **Cuestionario QH** y el **Dossier de la Primera Guerra**. No duplicar sus capítulos ni su estructura de eventos en un archivo nuevo. En especial, el dossier localizó referencias al antiguo `WORLD_CAUSALITY_ATLAS_2670_V1` con guerra 2645–2659, acuerdo en 2660 y escenario 2670: son datos **HISTÓRICOS/DE PROCEDENCIA PENDIENTE**, no fechas aprobadas para la línea H-36. El atlas usa una secuencia previa que puede entrar en conflicto con H-36. El objetivo es rastrear el documento matriz, comparar linaje y conservar divergencias explícitas. Véase el [contrato de integración narrativa al juego](D084_DRIVE_TO_GAME_INTEGRATION_BOUNDARY_2026-10-26.md).

## 6. Verificación y límites de este lote

**Se leyó:** Bulletin Board, Master Task Register (entrada D-084), `AGENTS.md`, Mission Control, `docs/world/WORLD_CANON_DECISION_QUEUE.md`, `docs/world/WORLD_DEVELOPMENT_MASTER_INDEX.md`, Historia original prioritaria y Centro de Historia y Canon, el manuscrito existente Volumen I v0.8, Dossier de la Primera Guerra (2026-10-15), Matriz de divulgación del estallido (2026-10-14), Cuestionario maestro de historia y Registro histórico relacional con sincronización del 2026-10-26 (Drive), registry de Player-AIs; `world_vantiel.txt` solo para frontera histórica.

**No ejecutado:** suite Python, Android, CI, emulador ni dispositivo; no hay cambios de runtime. **Sin claim:** las siete entidades canónicas permanecían `INACTIVE` al consultar el registry; ninguna fue activada, prestada ni suplantada. Este lote vive en rama de revisión separada y no cambia la autoridad hasta merge explícito.
