---
title: Crear un documento 3D vacío
linktitle: Crear un documento 3D vacío
second_title: Aspose.3D API .NET
description: Explore el mundo de la creación de documentos 3D con Aspose.3D para .NET. Crea, edita y guarda impresionantes escenas 3D sin esfuerzo.
type: docs
weight: 11
url: /es/net/loading-and-saving/create-empty-3d-document/
---
## Introducción

¡Bienvenido al mundo de la creación de documentos 3D utilizando Aspose.3D para .NET! En este tutorial, exploraremos los conceptos básicos de cargar y guardar documentos 3D. Aspose.3D para .NET proporciona un poderoso conjunto de herramientas para trabajar con escenas 3D y lo guiaremos en cada paso para ayudarlo a comenzar sin problemas.

## Requisitos previos

Antes de sumergirnos en el tutorial, asegúrese de cumplir con los siguientes requisitos previos:

-  Aspose.3D para .NET: asegúrese de tener la biblioteca instalada. Puedes descargarlo desde[aquí](https://releases.aspose.com/3d/net/).

## Importar espacios de nombres

Para comenzar, importe los espacios de nombres necesarios en su proyecto .NET:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
```

## Cargar y guardar: crear un documento 3D vacío

### Paso 1: configure su directorio de salida

```csharp
// La ruta al directorio de documentos.
var output = "Your Output Directory" + "document.fbx";
```

### Paso 2: crea un documento 3D vacío

```csharp
// ExStart: Crear documento 3DD vacío

// Crear un objeto de la clase Escena.
Scene scene = new Scene();

// Guarde el documento de escena 3D en formato FBX
scene.Save(output);

// ExEnd: Crear documento 3DD vacío
```

### Paso 3: mostrar el resultado

```csharp
Console.WriteLine("\nAn empty 3D document created successfully.\nFile saved at " + output);
```

¡Felicidades! Acaba de crear su primer documento 3D vacío usando Aspose.3D para .NET. No dude en explorar más características y funcionalidades para liberar todo el potencial de esta biblioteca.

## Conclusión

 En este tutorial, cubrimos los conceptos básicos de la creación de un documento 3D vacío usando Aspose.3D para .NET. A medida que continúa su viaje con el desarrollo 3D, consulte la[documentación](https://reference.aspose.com/3d/net/) para obtener información detallada y funciones avanzadas.

## Preguntas frecuentes

### P1: ¿Aspose.3D para .NET es adecuado para principiantes?

R1: Sí, Aspose.3D para .NET proporciona una interfaz fácil de usar, lo que la hace accesible tanto para principiantes como para desarrolladores experimentados.

### P2: ¿Puedo probar Aspose.3D para .NET antes de comprarlo?

 R2: ¡Absolutamente! Puedes acceder a una prueba gratuita[aquí](https://releases.aspose.com/).

### P3: ¿Cómo puedo obtener soporte para Aspose.3D para .NET?

 A3: Visita el[Foro Aspose.3D](https://forum.aspose.com/c/3d/18) para buscar ayuda y conectarse con la comunidad.

### P4: ¿Hay licencias temporales disponibles para Aspose.3D para .NET?

 R4: Sí, puedes obtener una licencia temporal[aquí](https://purchase.aspose.com/temporary-license/).

### P5: ¿Dónde puedo comprar Aspose.3D para .NET?

 A5: Puedes comprar la biblioteca.[aquí](https://purchase.aspose.com/buy).