---
title: Exportación de escenas 3D a formato AMF comprimido
linktitle: Exportar escena a AMF comprimido
second_title: Aspose.3D API .NET
description: Aprenda a exportar escenas 3D a formato AMF comprimido usando Aspose.3D para .NET. Mejore sus habilidades de desarrollo con esta guía paso a paso.
type: docs
weight: 11
url: /es/net/loading-and-saving/amf/export-scene-compressed-amf/
---
## Introducción

En el dinámico mundo del modelado y renderizado 3D, la eficiencia y la flexibilidad son primordiales. Aspose.3D para .NET permite a los desarrolladores exportar sin problemas escenas 3D al formato comprimido AMF (archivo de fabricación aditiva), lo que garantiza un tamaño de archivo óptimo sin comprometer la calidad. Este tutorial lo guiará a través del proceso paso a paso, facilitando que tanto los principiantes como los desarrolladores experimentados aprovechen las capacidades de Aspose.3D para .NET.

## Requisitos previos

Antes de sumergirse en el tutorial, asegúrese de tener los siguientes requisitos previos:

- Comprensión básica de los conceptos de modelado 3D.
- Visual Studio instalado en su máquina
-  Aspose.3D para la biblioteca .NET. Puedes descargarlo[aquí](https://releases.aspose.com/3d/net/)
- ¡Un deseo de mejorar tus habilidades de desarrollo 3D!

## Importar espacios de nombres

En su proyecto, asegúrese de importar los espacios de nombres necesarios para aprovechar la funcionalidad de Aspose.3D para .NET:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```

## Paso 1: cargue una escena 3D

Comience cargando una escena 3D usando Aspose.3D para .NET. Cree un objeto de escena y agréguele entidades como cuadros:

```csharp
Scene scene = new Scene();
var box = new Box();
var tr = scene.RootNode.CreateChildNode(box).Transform;
tr.Scale = new Vector3(12, 12, 12);
tr.Translation = new Vector3(10, 0, 0);
```

## Paso 2: Transformación de escala

A continuación, aplique una transformación de escala a otro cuadro de la escena:

```csharp
tr = scene.RootNode.CreateChildNode(box).Transform;
tr.Scaling = new Vector3(5, 5, 5);
```

## Paso 3: Establecer los ángulos de Euler

Establezca los ángulos de Euler para la transformación:

```csharp
tr.EulerAngles = new Vector3(50, 10, 0);
```

## Paso 4: guarde el archivo AMF comprimido

Finalmente, guarde la escena 3D en un archivo AMF comprimido en el directorio de salida que desee:

```csharp
scene.Save("Your Output Directory/" + "Aspose.amf", new AmfSaveOptions() { EnableCompression = false });
```

## Conclusión

¡Felicidades! Ha exportado con éxito una escena 3D a un formato AMF comprimido utilizando Aspose.3D para .NET. Esta poderosa biblioteca abre un mundo de posibilidades para los desarrolladores 3D, permitiéndoles crear modelos eficientes y visualmente impresionantes.

## Preguntas frecuentes

### P1: ¿Aspose.3D es compatible con el popular software de modelado 3D?

R1: Aspose.3D admite varios formatos de archivo, lo que lo hace compatible con herramientas populares de modelado 3D.

### P2: ¿Puedo habilitar la compresión para otros formatos de archivo además de AMF?

R2: Sí, Aspose.3D ofrece opciones para habilitar la compresión para varios formatos de archivo.

### P3: ¿Aspose.3D es adecuado tanto para principiantes como para desarrolladores avanzados?

R3: ¡Absolutamente! Aspose.3D ofrece simplicidad para principiantes y funciones avanzadas para desarrolladores experimentados.

### P4: ¿Existe alguna limitación en el tamaño de las escenas 3D que se pueden exportar?

R4: Aspose.3D está diseñado para manejar escenas de diversa complejidad y no existen limitaciones estrictas de tamaño.

### P5: ¿Dónde puedo encontrar apoyo adicional y debates comunitarios?

 A5: Visita el[Foro Aspose.3D](https://forum.aspose.com/c/3d/18) para apoyo y discusiones.