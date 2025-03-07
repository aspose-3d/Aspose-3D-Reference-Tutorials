---
title: Opciones de carga personalizadas
linktitle: Opciones de carga personalizadas
second_title: Aspose.3D API .NET
description: Explore Aspose.3D para .NET, la solución definitiva para cargar y guardar modelos 3D sin problemas.
weight: 15
url: /es/net/loading-and-saving/custom-load-options/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Opciones de carga personalizadas

## Introducción

Bienvenido al mundo de Aspose.3D para .NET, una potente biblioteca que permite a los desarrolladores trabajar sin problemas con archivos 3D. En este tutorial, profundizaremos en las complejidades de cargar y guardar modelos 3D, centrándonos en las opciones de carga personalizadas. Ya sea que sea un desarrollador experimentado o un recién llegado, esta guía lo guiará a través del proceso paso a paso, asegurándose de que aproveche todo el potencial de Aspose.3D para .NET.

## Requisitos previos

Antes de embarcarnos en este viaje, asegúrese de cumplir con los siguientes requisitos previos:

-  Aspose.3D para .NET: asegúrese de tener la biblioteca instalada. Puedes descargarlo[aquí](https://releases.aspose.com/3d/net/).

- Directorio de documentos: cree un directorio para almacenar sus archivos de modelo 3D.

Ahora que tienes lo esencial, ¡sumergámonos en el apasionante mundo de la manipulación de modelos 3D!

## Importar espacios de nombres

Primero lo primero, importemos los espacios de nombres necesarios. Esto preparará el escenario para nuestro viaje al reino de Aspose.3D.

```csharp
using System;
using System.IO;
using System.Collections.Generic;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Formats;
```

## Cargar y guardar: opciones de carga personalizadas

### Paso 1: cargar archivos Discreet3DS

```csharp
private static void Discreet3DSLoadOption()
{
    Discreet3dsLoadOptions loadOpts = new Discreet3dsLoadOptions();

    //Establecer opciones personalizadas
    loadOpts.ApplyAnimationTransform = true;
    loadOpts.FlipCoordinateSystem = true;
    loadOpts.GammaCorrectedColor = true;
    loadOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //Cargar archivo con las opciones de carga.
    var scene = Scene.FromFile("test.3ds", loadOpts);
}
```

### Paso 2: cargar archivos OBJ

```csharp
private static void ObjLoadOption()
{
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();

    //Establecer opciones personalizadas
    loadObjOpts.EnableMaterials = true;
    loadObjOpts.FlipCoordinateSystem = true;
    loadObjOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //Cargar archivo con las opciones de carga.
    var scene = Scene.FromFile("test.obj", loadObjOpts);

}
```

### Paso 3: cargar archivos STL

```csharp
private static void STLLoadOption()
{
    // La ruta al directorio de documentos.
    StlLoadOptions loadSTLOpts = new StlLoadOptions();

    //Establecer opciones personalizadas
    loadSTLOpts.FlipCoordinateSystem = true;
    loadSTLOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //Cargar archivo con las opciones de carga.
    var scene = Scene.FromFile("test.stl", loadSTLOpts);
}
```

### Paso 4: cargar archivos U3D

```csharp
private static void U3DLoadOption()
{
    // La ruta al directorio de documentos.
    string dataDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();

    //Establecer opciones personalizadas
    loadU3DOpts.FlipCoordinateSystem = true;
    loadU3DOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //Cargar archivo con las opciones de carga.
    var scene = Scene.FromFile("test.u3d", loadU3DOpts);
}
```

### Paso 5: Cargando archivos glTF

```csharp
private static void glTFLoadOptions()
{
    // La ruta al directorio de documentos.
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();

    //Establecer opciones personalizadas
    loadOpt.FlipTexCoordV = true;
    scene.Open("Duck.gltf", loadOpt);
}
```

### Paso 6: cargar archivos PLY

```csharp
private static void PlyLoadOptions()
{
    // La ruta al directorio de documentos.
    string dataDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();

    //Establecer opciones personalizadas
    loadPLYOpts.FlipCoordinateSystem = true;
    scene.Open("vase-v2.ply", loadPLYOpts);
}
```

### Paso 7: cargar archivos FBX

```csharp
private static void FBXLoadOptions()
{
    // La ruta al directorio de documentos.
    Scene scene = new Scene();
    FbxLoadOptions opt = new FbxLoadOptions() { KeepBuiltinGlobalSettings = true };

    //Establecer opciones personalizadas
    scene.Open("test.FBX", opt);

    // Propiedades de salida definidas en GlobalSettings en el archivo FBX
    foreach (Property property in scene.RootNode.AssetInfo.Properties)
    {
        Console.WriteLine(property);
    }
}
```

## Conclusión

¡Felicidades! Ha navegado con éxito por el intrincado mundo de cargar y guardar modelos 3D utilizando Aspose.3D para .NET. Este tutorial cubrió varios formatos de archivo y sus opciones de carga personalizadas, lo que le permitirá manipular recursos 3D con facilidad.

## Preguntas frecuentes

### P1: ¿Aspose.3D para .NET es adecuado para principiantes?

R1: ¡Absolutamente! Aspose.3D para .NET proporciona una interfaz fácil de usar, lo que la hace accesible para desarrolladores de todos los niveles.

### P2: ¿Puedo utilizar Aspose.3D para proyectos comerciales?

R2: Sí, Aspose.3D para .NET viene con una licencia comercial, lo que le permite utilizarlo en sus proyectos.

### P3: ¿Existe alguna limitación en los formatos de archivo admitidos?

 R3: Aspose.3D para .NET admite una amplia gama de formatos de archivos 3D populares, incluidos OBJ, STL, FBX y más. Referirse a[documentación](https://reference.aspose.com/3d/net/) para obtener una lista completa.

### P4: ¿Hay una versión de prueba disponible?

R4: Sí, puede explorar las capacidades de Aspose.3D para .NET descargando el[prueba gratis](https://releases.aspose.com/).

### P5: ¿Dónde puedo buscar soporte para Aspose.3D para .NET?

 A5: Visita el[Foro Aspose.3D](https://forum.aspose.com/c/3d/18) para el apoyo y asistencia de la comunidad.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
