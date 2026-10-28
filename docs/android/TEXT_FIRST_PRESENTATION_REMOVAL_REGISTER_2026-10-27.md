# THE GAME — Retirada controlada de presentación pixel art
**Revisión:** 2026-10-27 (Puerto Rico)  
**Repositorio:** `jbob-coder/Text-rpg-game`  
**Autoridad vigente al inventario:** `docs/master-game-development-program` @ `369621af7469175fdc3ddf964f470fcc8fa6b295`  
**Propuesta:** PR #97, rama `fix/remove-unwanted-pixel-presentation-20261027`; NO integrada en autoridad ni en `main`.

## 1. Instrucción actual del dueño y alcance
THE GAME sigue siendo un RPG de elecciones y narrativa de texto. El **mapa es la excepción visual funcional**, para mostrar lugares descubiertos, conexiones, ubicación actual, rutas disponibles y selección de viaje. **No deben renderizarse ilustraciones de escenas, personajes o equipamiento ni sprites generados sin autorización**. El texto, estadísticas, inventario, misiones y controles existentes se conservan. No agregar ninguna mecánica, nueva animación, contenido o cambio de motor.

Las directivas y bíblicas visuales antiguas del repositorio que exigen sprites/pixel art contradicen esta instrucción posterior del dueño: se consideran antecedentes históricos y **NO autorizan volver a introducir arte**. Este documento evita que futuros agentes interpreten su mera existencia como aprobación.

## 2. Qué modificó realmente PR #97 (NO fusiones)
- `GameScreen.kt`: las escenas dejan de invocar `SceneIllustration`/`PlayerAvatarPanel`; narrativa, opciones, voz, navegación y estados siguen operativos en la capa UI.
- `GameScreen.kt`: el mapa sustituye el fondo y marcadores de sprites por nodos y líneas vectoriales; mantiene datos y acciones `map.nodes`, `map.edges`, `reachable`, `onTravel(selected.id)` del snapshot.
- `GameScreen.kt` y `CharacterSection.kt`: retiran iconos pixelados de inventario, equipo, misiones y navegación; conservan equipar, desequipar, estadísticas y pantallas de texto.
- `PixelComponents.kt`: los paneles y tarjetas de decisiones activas dejan de llamar al pintado de marcos pixel art.
- `PixelMapTravelTransition.kt`: reemplaza fotogramas de sprites animados por texto para la notificación breve de viaje, sin cambiar el resultado autoritativo del viaje.
- `tests/test_d064_android_scene_projection_source.py` y pruebas Android: sustituyen las aserciones de arte en las pantallas activas por aserciones del flujo de texto y del mapa.
- NO se ha modificado ningún archivo de `src/textrpg/`, `content/`, guardados ni estado de canon.

## 3. Archivos heredados AÚN PRESENTES; no alegar retirada total
### 3.1 PNG: 24 archivos rastreados en el árbol de autoridad
- `android/app/src/main/res/drawable-nodpi/pixel_district_archive_default_scene.png`
- `android/app/src/main/res/drawable-nodpi/pixel_district_plaza_open_scene.png`
- `android/app/src/main/res/drawable-nodpi/pixel_evac_stair_default_scene.png`
- `android/app/src/main/res/drawable-nodpi/pixel_gate_twelve_sealed_scene.png`
- `android/app/src/main/res/drawable-nodpi/pixel_item_courier_necktag_icon.png`
- `android/app/src/main/res/drawable-nodpi/pixel_item_courier_necktag_paperdoll.png`
- `android/app/src/main/res/drawable-nodpi/pixel_item_dead_relay_damaged.png`
- `android/app/src/main/res/drawable-nodpi/pixel_item_dead_relay_icon.png`
- `android/app/src/main/res/drawable-nodpi/pixel_item_dead_relay_opened.png`
- `android/app/src/main/res/drawable-nodpi/pixel_item_dead_relay_signal_lost.png`
- `android/app/src/main/res/drawable-nodpi/pixel_item_depot_jacket_icon.png`
- `android/app/src/main/res/drawable-nodpi/pixel_item_depot_jacket_paperdoll.png`
- `android/app/src/main/res/drawable-nodpi/pixel_item_maintenance_seal_icon.png`
- `android/app/src/main/res/drawable-nodpi/pixel_item_signal_ring_icon.png`
- `android/app/src/main/res/drawable-nodpi/pixel_item_signal_ring_paperdoll.png`
- `android/app/src/main/res/drawable-nodpi/pixel_item_work_gloves_icon.png`
- `android/app/src/main/res/drawable-nodpi/pixel_item_work_gloves_paperdoll.png`
- `android/app/src/main/res/drawable-nodpi/pixel_platform_nine_blackout_scene.png`
- `android/app/src/main/res/drawable-nodpi/pixel_player_gameplay_front_base.png`
- `android/app/src/main/res/drawable-nodpi/pixel_player_hair_tech_placeholder.png`
- `android/app/src/main/res/drawable-nodpi/pixel_relay_workbench_default_scene.png`
- `android/app/src/main/res/drawable-nodpi/pixel_service_tunnel_default_scene.png`
- `android/app/src/main/res/drawable-nodpi/pixel_trace_chamber_idle_scene.png`
- `android/app/src/main/res/drawable-nodpi/pixel_workshop_row_default_scene.png`

### 3.2 Componentes y catálogos de Kotlin potencialmente heredados (25 archivos)
- `android/app/src/main/java/com/thegame/rpg/ui/PixelAssetCatalog.kt`
- `android/app/src/main/java/com/thegame/rpg/ui/PixelCharacterStagingCatalog.kt`
- `android/app/src/main/java/com/thegame/rpg/ui/PixelComponents.kt`
- `android/app/src/main/java/com/thegame/rpg/ui/PixelEnvironmentDecalCatalog.kt`
- `android/app/src/main/java/com/thegame/rpg/ui/PixelEnvironmentModuleCatalog.kt`
- `android/app/src/main/java/com/thegame/rpg/ui/PixelEnvironmentOverlayCatalog.kt`
- `android/app/src/main/java/com/thegame/rpg/ui/PixelEnvironmentPreview.kt`
- `android/app/src/main/java/com/thegame/rpg/ui/PixelEnvironmentPropCatalog.kt`
- `android/app/src/main/java/com/thegame/rpg/ui/PixelEquipmentSlotCatalog.kt`
- `android/app/src/main/java/com/thegame/rpg/ui/PixelItemQualityFrameCatalog.kt`
- `android/app/src/main/java/com/thegame/rpg/ui/PixelMapArtCatalog.kt`
- `android/app/src/main/java/com/thegame/rpg/ui/PixelMapMarkerCatalog.kt`
- `android/app/src/main/java/com/thegame/rpg/ui/PixelMapTravelTransition.kt`
- `android/app/src/main/java/com/thegame/rpg/ui/PixelRasterCatalog.kt`
- `android/app/src/main/java/com/thegame/rpg/ui/PixelSceneCatalog.kt`
- `android/app/src/main/java/com/thegame/rpg/ui/PixelSceneOverlayCatalog.kt`
- `android/app/src/main/java/com/thegame/rpg/ui/PixelStoryActorCatalog.kt`
- `android/app/src/main/java/com/thegame/rpg/ui/PixelStoryActorPlacementResolver.kt`
- `android/app/src/main/java/com/thegame/rpg/ui/PixelTheme.kt`
- `android/app/src/main/java/com/thegame/rpg/ui/PixelTraceFxCatalog.kt`
- `android/app/src/main/java/com/thegame/rpg/ui/PixelTraceStrainCatalog.kt`
- `android/app/src/main/java/com/thegame/rpg/ui/PixelUiChromeCatalog.kt`
- `android/app/src/main/java/com/thegame/rpg/ui/PixelUiIconCatalog.kt`
- `android/app/src/main/java/com/thegame/rpg/ui/PixelUiUtilityCatalog.kt`
- `android/app/src/main/java/com/thegame/rpg/ui/SceneIllustration.kt`

**Nota:** `PixelComponents.kt` y `PixelTheme.kt` siguen siendo usados, aunque sus paneles activos cambien a superficies de texto. No borrarlos por nombre. `PixelMapTravelTransition.kt` sigue siendo usado como aviso de texto. `PixelMapArtCatalog.kt`, `PixelMapMarkerCatalog.kt` y `SceneIllustration.kt` aún existen como código pero ya no son llamados desde la pantalla principal modificada. La presencia de archivos no prueba que sigan renderizados.

### 3.3 Herramientas, pruebas y documentos con expectativas antiguas
- `tools/verify_pixel_raster_equivalence.py` y `tests/test_pixel_raster_equivalence_tool.py` siguen exigiendo 24 PNG; **retirarlos o adaptar su contrato solo después de cerrar todas las dependencias**, no solo para producir CI verde.
- `android/app/src/test/java/com/thegame/rpg/ui/PixelRasterCatalogTest.kt` y pruebas especializadas pueden requerir activos gráficos todavía existentes.
- `docs/VISUAL_BIBLE.md`, `docs/assets/` y registros de decisiones heredadas deben conservar evidencia histórica distinguible de la instrucción nueva; un documento viejo no es licencia para regenerar sprites.
- `.github/workflows/android-pixel-client.yml` conserva nombre de pixel client y comprobaciones de compilación; renombrarlo solo después de verificar consumidores, sin quitar controles de seguridad/QA.

## 4. Dependencias antes de suprimir archivos
1. Buscar referencias en `android/app/src/main/java`, `src/textrpg/`, tests Kotlin/Python, assets y Gradle. La eliminación debe demostrar **cero consumidores activos**.
2. Preservar interfaces de texto, `GameSnapshot`, `worldMap`, selección, viajes, lectura de narrativa, interacción con NPC, guardados y puentes Chaquopy; nunca cambiar reglas ni contenidos para esconder un error de UI.
3. Retirar visuales fuera del shell principal (por ejemplo `StatusComponents.kt` y pruebas del raster), cuando exista reemplazo de texto y test real.
4. Solo entonces eliminar catálogos sin consumidores, los PNG y pruebas antiguas que exigen pixel art. No borrar archivos de documentación histórica sin política de conservación.
5. Ejecutar `PYTHONPATH=src python -m unittest discover -s tests -v`, tests JVM/Compose y smoke en emulador en **el mismo HEAD**. Hardware físico sigue sin verificar.

## 5. Evidencia de ejecución y límites
El run GitHub Actions #440 del PR #97 aprobó Python; falló `android-unit-and-assemble` por una referencia Kotlin `maxWidth` fuera del alcance de `BoxWithConstraints` en `CharacterSection.kt`. Se corrigió en el commit `e137077f64236021fea4731baf77046d6a4765f7`. Los commits posteriores añadieron transición de viaje exclusivamente textual y su test.

**CI de la última revisión de PR #97:** todavía PENDIENTE al redactar este registro; no afirmar APK probado, emulador aprobado ni limpieza completa. `main` NO fue modificado.

## 6. Criterio final de aceptación
No quedan sprites de escena, avatar, equipamiento o marcadores artísticos ni archivos de pixel art sin consumidor que permanezcan en el árbol activo. El mapa de rutas y todas las interacciones de texto funcionan. La suite exact-head de Python, Android y emulador pasa. Los archivos históricos y decisiones reemplazadas están marcados inequívocamente como obsoletos. Solo entonces se puede marcar la retirada completa.
