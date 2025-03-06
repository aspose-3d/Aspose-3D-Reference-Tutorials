---
title: Guardar 3D en PDF
linktitle: Guardar 3D en PDF
second_title: Aspose.3D API .NET
description: Explore Aspose.3D para .NET. Su biblioteca de referencia para modelado y renderizado 3D perfectos. Guarde modelos 3D en PDF sin esfuerzo.
weight: 19
url: /es/net/loading-and-saving/pdf/save-3d-in-pdf/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Guardar 3D en PDF

## Introducción

¡Bienvenido a nuestra guía completa sobre el uso de Aspose.3D para .NET! En este tutorial, lo guiaremos a través del proceso de cargar y guardar modelos 3D, centrándonos en la tarea específica de guardar un modelo 3D en formato PDF. Aspose.3D para .NET es una poderosa biblioteca que proporciona herramientas eficientes para trabajar con archivos 3D, lo que la convierte en un recurso esencial para desarrolladores y entusiastas en este campo.

## Requisitos previos

Antes de sumergirnos en el tutorial, asegúrese de cumplir con los siguientes requisitos previos:

-  Aspose.3D para .NET: asegúrese de tener la biblioteca instalada. Si no, puedes descargarlo desde[Aspose.3D para documentación .NET](https://reference.aspose.com/3d/net/).

- Entorno de desarrollo: configure su entorno de desarrollo .NET preferido.

- Comprensión básica de los conceptos 3D: familiarícese con los conceptos 3D fundamentales, ya que esta guía asume un conocimiento básico del modelado 3D.

## Importar espacios de nombres

En su proyecto .NET, asegúrese de importar los espacios de nombres necesarios para acceder a las funcionalidades proporcionadas por Aspose.3D:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Formats;
using System.Drawing;
```

## Paso 1: crea una nueva escena

Comience inicializando una nueva escena 3D usando la biblioteca Aspose.3D. Esto sirve como base para su modelo 3D.

```csharp
Scene scene = new Scene();
```

## Paso 2: agregar un nodo secundario de cilindro

Para demostrar el proceso de guardar, creemos un modelo 3D simple: un cilindro. Agregue un cilindro como nodo secundario a la escena.

```csharp
scene.RootNode.CreateChildNode("cylinder", new Cylinder()).Material = new PhongMaterial() { DiffuseColor = new Vector3(Color.DarkCyan) };
```

## Paso 3: configurar el modo de renderizado y el esquema de iluminación

Defina el modo de renderizado y el esquema de iluminación para su escena 3D. Este paso le permite personalizar la apariencia visual de su modelo.

```csharp
PdfSaveOptions opt = new PdfSaveOptions();
opt.LightingScheme = PdfLightingScheme.CAD;
opt.RenderMode = PdfRenderMode.ShadedIllustration;
```

## Paso 4: guardar en formato PDF

Finalmente, ejecute el proceso de guardado especificando el directorio de salida y el nombre del archivo. En este caso, guardaremos el modelo 3D en formato PDF.

```csharp
scene.Save("Your Output Directory" + "output_out.pdf", opt);
```

Asegúrese de reemplazar "Su directorio de salida" con la ruta deseada.

## Conclusión

 ¡Felicidades! Ha aprendido con éxito cómo utilizar Aspose.3D para .NET para crear un modelo 3D simple y guardarlo en formato PDF. Esto es sólo el comienzo de lo que puedes lograr con esta poderosa biblioteca. Explora más características y posibilidades en el[Documentación de Aspose.3D](https://reference.aspose.com/3d/net/).

## Preguntas frecuentes

### P1: ¿Aspose.3D para .NET es compatible con todos los formatos de archivos 3D?

R1: Sí, Aspose.3D para .NET admite una amplia gama de formatos de archivos 3D, lo que garantiza la compatibilidad con varios estándares de la industria.

### P2: ¿Puedo personalizar los aspectos visuales de mi modelo 3D durante el proceso de guardado?

R2: ¡Absolutamente! Como se muestra en el tutorial, puede ajustar los modos de renderizado, los esquemas de iluminación y más para lograr el resultado visual deseado.

### P3: ¿Dónde puedo encontrar soporte para Aspose.3D para .NET?

 A3: Visita el[Foro Aspose.3D](https://forum.aspose.com/c/3d/18) para soporte de la comunidad y discusiones relacionadas con Aspose.3D para .NET.

### P4: ¿Hay una prueba gratuita disponible de Aspose.3D para .NET?

 R4: Sí, puedes acceder al[prueba gratis](https://releases.aspose.com/) para explorar las capacidades de Aspose.3D para .NET antes de realizar una compra.

### P5: ¿Cómo puedo obtener una licencia temporal de Aspose.3D para .NET?

 R5: Para obtener una licencia temporal, visite[este enlace](https://purchase.aspose.com/temporary-license/) y siga las instrucciones proporcionadas.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
