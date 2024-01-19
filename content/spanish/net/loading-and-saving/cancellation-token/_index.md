---
title: Cargando y guardando - Usando CancellationToken
linktitle: Cargando y guardando - Usando CancellationToken
second_title: Aspose.3D API .NET
description: Explore el perfecto mundo del modelado 3D con Aspose.3D para .NET. Aprenda a cargar y guardar documentos 3D de manera eficiente usando CancellationToken.
type: docs
weight: 10
url: /es/net/loading-and-saving/cancellation-token/
---
## Introducción

Bienvenido a nuestra guía completa sobre cómo utilizar Aspose.3D para .NET para mejorar sus proyectos de modelado y renderizado 3D. Aspose.3D es una potente biblioteca que permite a los desarrolladores .NET trabajar sin problemas con archivos 3D. En este tutorial, profundizaremos en los aspectos de carga y guardado, centrándonos específicamente en el uso de CancellationToken para una gestión eficiente de tareas asincrónicas.

## Requisitos previos

Antes de embarcarnos en este viaje, asegúrese de contar con los siguientes requisitos previos:

-  Aspose.3D para .NET: descargue e instale la biblioteca desde[aquí](https://releases.aspose.com/3d/net/).
- Entorno .NET: asegúrese de tener configurado un entorno de desarrollo .NET compatible.
- Conocimientos básicos de C#: se recomienda estar familiarizado con el lenguaje de programación C#.

## Importar espacios de nombres

Para comenzar, asegúrese de incluir los espacios de nombres necesarios en su proyecto. Estos espacios de nombres proporcionarán acceso a las funcionalidades necesarias para la manipulación de archivos 3D.

```csharp
using Aspose.ThreeD;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
```

## Cargando y guardando - Usando CancellationToken

### Paso 1: crear CancellationTokenSource

```csharp
// ExStart:CancelaciónTokenFuente

CancellationTokenSource cts = new CancellationTokenSource();
```

Aquí, creamos una instancia de CancellationTokenSource, un componente crucial para gestionar la cancelación en operaciones asincrónicas.

### Paso 2: Inicializar la escena 3D

```csharp
Scene scene = new Scene();
```

Crea una instancia de la clase Escena. Este será el lienzo para tus actividades de modelado 3D.

### Paso 3: Establecer el tiempo de espera del token de cancelación

```csharp
cts.CancelAfter(1000);
```

 Establezca el tiempo de espera de cancelación usando el`CancelAfter` método. En este ejemplo, el tiempo de espera se establece en 1000 milisegundos (1 segundo).

### Paso 4: abrir documento 3D

```csharp
try
{
    scene.Open("Your Output Directory" + "document.fbx", cts.Token);
    Console.WriteLine("Import is done within 1000ms");
}
catch (ImportException e)
{
    if (e.InnerException is OperationCanceledException)
    {
        Console.WriteLine("It takes too long time to import, import has been canceled.");
    }
}
```

 Intente abrir el documento 3D dentro del período de tiempo especificado. El`cts.Token`El parámetro garantiza que la operación se pueda cancelar si excede el tiempo de espera establecido.

### Paso 5: Manejar la excepción de importación

En caso de una ImportException, manéjela correctamente comprobando si fue causada por una OperationCanceledException.

```csharp
catch (ImportException e)
{
    if (e.InnerException is OperationCanceledException)
    {
        Console.WriteLine("It takes too long time to import, import has been canceled.");
    }
}
// ExEnd:CancelaciónTokenFuente
```

## Conclusión

¡Felicidades! Ha navegado con éxito por el proceso de uso de Aspose.3D para .NET con CancellationToken para administrar la carga de documentos 3D. Esta técnica garantiza operaciones de importación eficientes y oportunas, mejorando el rendimiento general de sus aplicaciones 3D.

## Preguntas frecuentes

### P1: ¿Aspose.3D es compatible con todos los formatos de archivos 3D?

 R1: Aspose.3D admite una amplia gama de formatos de archivos 3D, incluidos FBX, STL, OBJ y más. Referirse a[documentación](https://reference.aspose.com/3d/net/) para la lista completa.

### P2: ¿Cómo puedo obtener una licencia temporal para Aspose.3D?

 A2: Obtenga una licencia temporal visitando[este enlace](https://purchase.aspose.com/temporary-license/).

### P3: ¿Dónde puedo encontrar soporte para Aspose.3D?

 A3: Únase a la discusión comunitaria en el[Foro Aspose.3D](https://forum.aspose.com/c/3d/18).

### P4: ¿Puedo probar Aspose.3D gratis antes de comprarlo?

 R4: Sí, explore las funciones con una prueba gratuita disponible[aquí](https://releases.aspose.com/).

### P5: ¿Cuál es la última versión de Aspose.3D para .NET?

 R5: Manténgase actualizado consultando la[pagina de descarga](https://releases.aspose.com/3d/net/) para la última versión.