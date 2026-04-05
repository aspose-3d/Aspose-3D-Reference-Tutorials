---
date: 2026-02-25
description: Aprende cómo invertir el sistema de coordenadas y personalizar la importación
  3D usando Aspose.3D LoadOptions en Java. Guía paso a paso para 3DS, OBJ, STL, U3D,
  glTF, PLY, X y opcionalmente FBX.
linktitle: Customize 3D File Loading in Java with Aspose.3D LoadOptions
second_title: Aspose.3D Java API
title: Voltear el sistema de coordenadas – Personaliza la carga de archivos 3D en
  Java con Aspose.3D
url: /es/java/load-and-save/customize-3d-file-loading/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Sistema de Coordenadas Invertido – Personaliza la Carga de Archivos 3D en Java con Aspose.3D

En el panorama siempre cambiante del diseño y desarrollo 3D, **invertir el sistema de coordenadas** al importar modelos es un requisito común. Ya sea que estés convirtiendo activos de un sistema derecho a uno izquierdo o necesites alinear los modelos con las convenciones de ejes de tu motor, Aspose.3D para Java te brinda un control granular. Este tutorial te guía sobre cómo **personalizar la importación 3D** usando `LoadOptions` de Aspose.3D, cubriendo los formatos más populares como 3DS, OBJ, STL, U3D, glTF, PLY, X y el opcional FBX.

## Respuestas Rápidas
- **¿Qué hace “flip coordinate system”?** Intercambia los ejes X/Y/Z para coincidir con la convención de coordenadas objetivo.  
- **¿Qué formatos admiten la inversión?** Todos los formatos principales (3DS, OBJ, STL, U3D, glTF, PLY, X, FBX) exponen una opción `setFlipCoordinateSystem`.  
- **¿Necesito bibliotecas adicionales?** Solo el JAR de Aspose.3D para Java; no se requieren convertidores externos.  
- **¿Puedo cargar materiales al mismo tiempo?** Sí—usa `setEnableMaterials(true)` para archivos OBJ.  
- **¿Se requiere una licencia para producción?** Se necesita una licencia válida de Aspose.3D para implementaciones que no sean de prueba.

## ¿Qué es “flip coordinate system”?
Invertir el sistema de coordenadas cambia la orientación de los ejes utilizados por el modelo importado. Esto es esencial cuando el archivo fuente usa una mano diferente (derecha vs. izquierda) que tu motor de renderizado, evitando que los modelos aparezcan reflejados o invertidos.

## ¿Por qué personalizar la importación 3D?
- Preservar transformaciones de animación (`setApplyAnimationTransform`).  
- Corregir el manejo de colores (`setGammaCorrectedColor`).  
- Resolver rutas de recursos externos mediante `getLookupPaths()`.  
- Optimizar el uso de memoria cargando solo lo que necesitas.

## Requisitos Previos

- Comprensión básica de la programación en Java.  
- JDK (Java Development Kit) instalado.  
- Biblioteca Aspose.3D para Java descargada. Puedes obtenerla [aquí](https://releases.aspose.com/3d/java/).  
- Familiaridad con formatos de archivo 3D como 3DS, OBJ, STL, U3D, glTF, PLY, X y FBX.

## Importar Paquetes

En tu proyecto Java, asegúrate de importar los paquetes necesarios de Aspose.3D:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Cómo personalizar la importación 3D con LoadOptions

A continuación se presentan fragmentos de código paso a paso que demuestran cómo habilitar la opción **flip coordinate system** para cada formato compatible. Los fragmentos están listos para copiar en tu proyecto; solo reemplaza `"Your Document Directory"` con la ruta real a tus recursos.

### Paso 1: Personalizar la Carga de Archivo 3DS

```java
public static void discreet3DSLoadOption() {
    String MyDir = "Your Document Directory";
    Discreet3dsLoadOptions loadOpts = new Discreet3dsLoadOptions();
    loadOpts.setApplyAnimationTransform(true);
    loadOpts.setFlipCoordinateSystem(true);
    loadOpts.setGammaCorrectedColor(true);
    loadOpts.getLookupPaths().add(MyDir);
}
```

### Paso 2: Personalizar la Carga de Archivo OBJ

```java
public static void objLoadOption() {
    String MyDir = "Your Document Directory";
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();
    loadObjOpts.setEnableMaterials(true);
    loadObjOpts.setFlipCoordinateSystem(true);
    loadObjOpts.getLookupPaths().add(MyDir);
}
```

### Paso 3: Personalizar la Carga de Archivo STL

```java
public static void stlLoadOption() {
    String MyDir = "Your Document Directory";
    StlLoadOptions loadSTLOpts = new StlLoadOptions();
    loadSTLOpts.setFlipCoordinateSystem(true);
    loadSTLOpts.getLookupPaths().add(MyDir);
}
```

### Paso 4: Personalizar la Carga de Archivo U3D

```java
public static void u3dLoadOption() {
    String MyDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();
    loadU3DOpts.setFlipCoordinateSystem(true);
    loadU3DOpts.getLookupPaths().add(MyDir);
}
```

### Paso 5: Personalizar la Carga de Archivo glTF

```java
public static void gltfLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();
    loadOpt.setFlipTexCoordV(true);
    scene.open(MyDir + "Duck.gltf", loadOpt);
}
```

### Paso 6: Personalizar la Carga de Archivo PLY

```java
public static void plyLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();
    loadPLYOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "vase-v2.ply", loadPLYOpts);
}
```

### Paso 7: Personalizar la Carga de Archivo X

```java
public static void xLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    XLoadOptions loadXOpts = new XLoadOptions(FileContentType.ASCII);
    loadXOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "warrior.x", loadXOpts);
}
```

### Paso 8: Personalizar la Carga de Archivo FBX (Opcional)

```java
private static void FBXLoadOptions() throws IOException {
    String dataDir = "Your Document Directory";
    Scene scene = new Scene();
    FbxLoadOptions opt = new FbxLoadOptions();
    opt.setKeepBuiltinGlobalSettings(true);
    scene.open(dataDir + "test.FBX", opt);
    for(Property property:scene.getRootNode().getAssetInfo().getProperties()) {
        System.out.println(property);
    }
}
```

## Problemas Comunes y Soluciones
- **El modelo aparece reflejado después de cargar** – Verifica que `setFlipCoordinateSystem(true)` esté configurado para el formato correcto.  
- **Faltan materiales** – Para archivos OBJ, asegúrate de `setEnableMaterials(true)` y de que los archivos de material (.mtl) estén ubicados en una de las rutas de búsqueda.  
- **Las coordenadas de textura están al revés** – Para glTF, puede que necesites `setFlipTexCoordV(true)` además de invertir los ejes.  
- **Errores de archivo no encontrado** – Añade el directorio que contiene recursos externos (texturas, archivos auxiliares) a `loadOpts.getLookupPaths()`.

## Conclusión

Al aprovechar `LoadOptions` de Aspose.3D, puedes **invertir el sistema de coordenadas** y **personalizar la importación 3D** para prácticamente todos los formatos principales. Este nivel de control elimina la necesidad de scripts de post‑procesamiento y garantiza que tus recursos se rendericen correctamente desde la primera vez.

## Preguntas Frecuentes

### Q1: ¿Dónde puedo encontrar la documentación de Aspose.3D para Java?
A1: La documentación está disponible [aquí](https://reference.aspose.com/3d/java/).

### Q2: ¿Cómo puedo descargar Aspose.3D para Java?
A2: Puedes descargarla [aquí](https://releases.aspose.com/3d/java/).

### Q3: ¿Hay una prueba gratuita disponible?
A3: Sí, puedes acceder a la prueba gratuita [aquí](https://releases.aspose.com/).

### Q4: ¿Dónde puedo obtener soporte para Aspose.3D para Java?
A4: Visita el foro de soporte [aquí](https://forum.aspose.com/c/3d/18).

### Q5: ¿Necesito una licencia temporal para pruebas?
A5: Sí, obtén una licencia temporal [aquí](https://purchase.aspose.com/temporary-license/).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Última actualización:** 2026-02-25  
**Probado con:** Aspose.3D for Java 24.11 (latest)  
**Autor:** Aspose