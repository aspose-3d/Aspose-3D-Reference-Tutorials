---
date: 2026-09-08
description: Aprenda cómo definir unidades y exportar una escena a FBX en Java usando
  Aspose.3D. Esta guía paso a paso muestra cómo establecer el nombre de la aplicación,
  las unidades de medida y obtener información de la escena 3D.
keywords:
- how to define units
- export scene to fbx
- how to set application name
- define measurement units
lastmod: 2026-09-08
linktitle: Cómo guardar FBX y obtener información de la escena 3D en Java
og_description: Aprenda cómo definir unidades y exportar una escena a FBX en Java
  con Aspose.3D. La guía cubre la configuración del nombre de la aplicación, las unidades
  de medida y la obtención de información de la escena 3D en unos pocos pasos.
og_image_alt: Guide showing how to define units and export a 3D scene to FBX using
  Aspose.3D Java
og_title: Cómo definir unidades y exportar escena a FBX en Java
schemas:
- author: Aspose
  dateModified: '2026-09-08'
  description: Learn how to define units and export a scene to FBX in Java using Aspose.3D.
    This step‑by‑step guide shows setting the application name, measurement units,
    and retrieving 3D scene information.
  headline: How to define units and export scene to FBX in Java
  type: TechArticle
- description: Learn how to define units and export a scene to FBX in Java using Aspose.3D.
    This step‑by‑step guide shows setting the application name, measurement units,
    and retrieving 3D scene information.
  name: How to define units and export scene to FBX in Java
  steps:
  - name: initialize a 3D scene
    text: The `Scene` class is Aspose.3D's top‑level container that represents an
      entire 3D scene, including geometry, lights, cameras, and metadata. First, create
      an empty `Scene` object. This will be the container for all geometry, lights,
      cameras, and asset metadata.
  - name: define measurement units
    text: The unit system determines the real‑world scale of the scene; Aspose.3D
      lets you specify a unit name and a scale factor relative to meters. In this
      example we use an ancient Egyptian unit called “pole” with a custom scale factor.
      > **Tip:** Adjust `unitScaleFactor` to match the real‑world size of yo
  - name: export scene to FBX
    text: Now that the asset information is attached, we save the scene as an FBX
      file. The `FileFormat.FBX7500ASCII` option produces a human‑readable ASCII FBX,
      which is handy for debugging. > **Remember:** Replace `"Your Document Directory"`
      with an absolute path or a path relative to your project's working
  type: HowTo
- questions:
  - answer: Replace `FileFormat.FBX7500ASCII` with `FileFormat.FBX7500` when calling
      `scene.save(...)`.
    question: How do I change the output format to binary FBX?
  - answer: Yes, use `scene.getUserData().add("Key", "Value")` to embed additional
      key‑value pairs.
    question: Can I add custom user‑defined metadata beyond the built‑in asset fields?
  - answer: It does. Simply change the `FileFormat` enum to `OBJ` or `GLTF2` as needed.
    question: Does Aspose.3D support other export formats like OBJ or GLTF?
  - answer: Aspose.3D for Java supports Java 8 and later.
    question: What version of Java is required?
  - answer: Absolutely. Load the file with `new Scene("input.fbx")`, modify `scene.getAssetInfo()`,
      then save.
    question: Is it possible to load an existing FBX, modify its asset info, and resave?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- export scene to fbx
- Aspose.3D
- Java 3D
- define units
- 3D asset metadata
title: Cómo definir unidades y exportar escena a FBX en Java
url: /es/java/3d-scenes-and-models/get-scene-information/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Cómo definir unidades y exportar una escena a FBX en Java

## Introducción

Si buscas una guía clara y práctica sobre **cómo definir unidades** y **exportar una escena a FBX** mientras extraes metadatos útiles de tus escenas 3D, has llegado al lugar correcto. En este tutorial recorreremos cada paso usando la biblioteca **Aspose.3D for Java**: desde crear una escena, **establecer el nombre de la aplicación**, **definir unidades de medida**, hasta finalmente **exportar la escena a FBX**. Al final tendrás un archivo FBX listo para usar que lleva la información de activos que necesitas para los flujos de trabajo posteriores.

## Respuestas rápidas
- **¿Cuál es el objetivo principal?** Exportar una escena a FBX que contenga información de activos personalizada.  
- **¿Qué biblioteca se utiliza?** Aspose.3D for Java.  
- **¿Necesito una licencia?** Una prueba gratuita funciona para desarrollo; se requiere una licencia comercial para producción.  
- **¿Puedo cambiar las unidades de medida?** Sí – usa `setUnitName` y `setUnitScaleFactor`.  
- **¿Dónde se guarda la salida?** En la ruta que especifiques en `scene.save(...)`.  

## Requisitos previos

Antes de comenzar, asegúrate de tener:

- Un buen dominio de la sintaxis básica de Java.  
- **Aspose.3D for Java** descargado y añadido a tu proyecto (puedes obtenerlo en la página oficial) [Página de descarga de Aspose 3D](https://releases.aspose.com/3d/java/).  
- Tu IDE favorito de Java (IntelliJ IDEA, Eclipse, NetBeans, etc.) correctamente configurado.

## Importar paquetes

En tu archivo fuente Java, importa las clases de Aspose.3D que proporcionan manejo de escenas y soporte de formatos de archivo.

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
```

> **Consejo profesional:** Mantén la lista de importaciones mínima para evitar dependencias innecesarias y mejorar los tiempos de compilación.

## ¿Cuál es el proceso para guardar un archivo FBX?

Para guardar una escena como archivo FBX, creas un `Scene`, estableces los metadatos de activo deseados, defines la unidad de medida y luego llamas a `scene.save(path, FileFormat.FBX7500ASCII)`. Esta secuencia escribe geometría, materiales y metadatos en un FBX ASCII que puede inspeccionarse o importarse por herramientas posteriores.

### Paso 1: inicializar una escena 3D

La clase `Scene` es el contenedor de nivel superior de Aspose.3D que representa una escena 3D completa, incluyendo geometría, luces, cámaras y metadatos. Primero, crea un objeto `Scene` vacío. Este será el contenedor para toda la geometría, luces, cámaras y metadatos de activo.

```java
// ExStart:AddAssetInformationToScene
Scene scene = new Scene();
```

### Cómo establecer el nombre de la aplicación en Java

El objeto `AssetInfo` almacena metadatos como el nombre de la aplicación, el proveedor y la versión de la escena. Añadir metadatos personalizados ayuda a las herramientas posteriores a identificar el origen del archivo. Usa el objeto `AssetInfo` para **establecer el nombre de la aplicación** (y el proveedor) antes de guardar el archivo.

```java
scene.getAssetInfo().setApplicationName("Egypt");
scene.getAssetInfo().setApplicationVendor("Manualdesk");
```

> **Por qué es importante:** Muchos flujos de trabajo filtran o etiquetan activos según la aplicación de origen, lo que hace que este paso sea esencial para proyectos grandes.

### Paso 3: definir unidades de medida

El sistema de unidades determina la escala del mundo real de la escena; Aspose.3D te permite especificar un nombre de unidad y un factor de escala relativo a metros. En este ejemplo usamos una unidad egipcia antigua llamada “pole” con un factor de escala personalizado.

```java
scene.getAssetInfo().setUnitName("pole");
scene.getAssetInfo().setUnitScaleFactor(0.6);
```

> **Consejo:** Ajusta `unitScaleFactor` para que coincida con el tamaño real de tus modelos; 1.0 representa una correspondencia 1‑a‑1 con la unidad elegida.

### Paso 4: exportar la escena a FBX

Ahora que la información del activo está adjunta, guardamos la escena como archivo FBX. La opción `FileFormat.FBX7500ASCII` produce un FBX ASCII legible por humanos, lo cual es útil para depuración.

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "InformationToScene.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nAsset information added successfully to Scene.\nFile saved at " + MyDir);
// ExEnd:AddAssetInformationToScene
```

> **Recuerda:** Reemplaza `"Your Document Directory"` con una ruta absoluta o una ruta relativa al directorio de trabajo de tu proyecto.

## ¿Por qué exportar la escena a FBX con Aspose.3D?

Aspose.3D soporta **más de 50 formatos de entrada y salida** y puede procesar escenas de cientos de páginas sin cargar todo el archivo en memoria, dándote control total sobre el archivo exportado—metadatos, unidades y geometría—sin necesidad de una aplicación de autoría 3D pesada. Esto hace que la generación automática de activos, el procesamiento por lotes y las conversiones del lado del servidor sean rápidas y fiables.

## Casos de uso comunes

- **Pipelines de activos para juegos** – incrusta información del creador directamente en archivos FBX para el seguimiento de versiones.  
- **Visualización arquitectónica** – almacena unidades específicas del proyecto para evitar errores de escala al importar en motores de renderizado.  
- **Informes automatizados** – genera archivos FBX sobre la marcha con metadatos que las herramientas de análisis posteriores pueden leer.  
- **Servicios 3D basados en la nube** – crea y exporta escenas programáticamente sin GUI, perfecto para plataformas SaaS.

## Solución de problemas y consejos

| Problema | Solución |
|----------|----------|
| **Archivo no encontrado después de guardar** | Verifica que `MyDir` apunte a una carpeta existente y que tu aplicación tenga permisos de escritura. |
| **Las unidades aparecen incorrectas en el visor externo** | Revisa `unitScaleFactor`; algunos visores esperan metros como unidad base. |
| **Metadatos del activo ausentes** | Asegúrate de llamar a `scene.getAssetInfo()` **antes** de guardar; los cambios realizados después de `save()` no se conservarán. |
| **Cuello de botella de rendimiento en escenas grandes** | Usa `scene.optimize()` antes de guardar para reducir el uso de memoria. |
| **El FBX ASCII es demasiado grande** | Cambia a FBX binario usando `FileFormat.FBX7500` (ver FAQ). |

## Preguntas frecuentes

**P: ¿Cómo cambio el formato de salida a FBX binario?**  
R: Reemplaza `FileFormat.FBX7500ASCII` por `FileFormat.FBX7500` al llamar a `scene.save(...)`.

**P: ¿Puedo añadir metadatos definidos por el usuario más allá de los campos de activo incorporados?**  
R: Sí, usa `scene.getUserData().add("Key", "Value")` para incrustar pares clave‑valor adicionales.

**P: ¿Aspose.3D soporta otros formatos de exportación como OBJ o GLTF?**  
R: Lo hace. Simplemente cambia el enum `FileFormat` a `OBJ` o `GLTF2` según sea necesario.

**P: ¿Qué versión de Java se requiere?**  
R: Aspose.3D for Java soporta Java 8 y versiones posteriores.

**P: ¿Es posible cargar un FBX existente, modificar su información de activo y volver a guardarlo?**  
R: Absolutamente. Carga el archivo con `new Scene("input.fbx")`, modifica `scene.getAssetInfo()`, luego guarda.

---

**Última actualización:** 2026-09-08  
**Probado con:** Aspose.3D for Java 24.11  
**Autor:** Aspose

## Tutoriales relacionados

- [Reducir el tamaño de archivos 3D – Comprimir escenas con Aspose.3D for Java](/3d/java/3d-scenes-and-models/compress-3d-scenes/)
- [Cómo establecer color vector3 en Java: Cambiar color difuso y gestionar propiedades 3D en escenas Java usando Aspose.3D](/3d/java/3d-scenes-and-models/managing-3d-properties-scenes/)

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}