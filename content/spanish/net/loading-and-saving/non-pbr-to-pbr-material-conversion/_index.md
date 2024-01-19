---
title: Cargando y guardando - Conversión de materiales que no son PBR a PBR
linktitle: Cargando y guardando - Conversión de materiales que no son PBR a PBR
second_title: Aspose.3D API .NET
description: Explore Aspose.3D para .NET convierta materiales que no sean PBR en PBR sin esfuerzo. Tutorial completo y potente API.
type: docs
weight: 16
url: /es/net/loading-and-saving/non-pbr-to-pbr-material-conversion/
---
## Introducción

Bienvenido a esta guía paso a paso sobre el uso de Aspose.3D para .NET para convertir materiales sin PBR (renderizado basado físicamente) en materiales PBR. Aspose.3D es una potente API que permite a los desarrolladores trabajar sin problemas con formatos de archivos 3D en sus aplicaciones .NET.

## Requisitos previos

Antes de sumergirnos en el tutorial, asegúrese de tener los siguientes requisitos previos:

-  Aspose.3D para .NET: asegúrese de tener instalada la biblioteca Aspose.3D para .NET. Puedes encontrar el enlace de descarga.[aquí](https://releases.aspose.com/3d/net/).

- Comprensión básica de C#: este tutorial asume que tiene un conocimiento fundamental de la programación en C#.

- IDE (entorno de desarrollo integrado): elija su IDE preferido para el desarrollo .NET, como Visual Studio.

## Importar espacios de nombres

En su código C#, comience importando los espacios de nombres necesarios:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
```

## Paso 1: inicializa una nueva escena 3D

Comience creando una nueva escena 3D usando el siguiente código:

```csharp
// ExInicio:Non_PBRtoPBRMaterial
// inicializar una nueva escena 3D
var scene = new Scene();
```

## Paso 2: crea un objeto 3D

A continuación, cree un objeto 3D, por ejemplo, un cuadro:

```csharp
var box = new Box();
scene.RootNode.CreateChildNode("box1", box).Material = new PhongMaterial() { DiffuseColor = new Vector3(1, 0, 1) };
```

## Paso 3: configurar la conversión de materiales

Configure opciones de conversión de materiales para la conversión de No PBR a PBR:

```csharp
GltfSaveOptions options = new GltfSaveOptions(FileFormat.GLTF2);
options.MaterialConverter = delegate (Material material)
{
    PhongMaterial phongMaterial = (PhongMaterial)material;
    return new PbrMaterial() { Albedo = new Vector3(phongMaterial.DiffuseColor.x, phongMaterial.DiffuseColor.y, phongMaterial.DiffuseColor.z) };
};
```

## Paso 4: Guardar en formato GLTF 2.0

Guarde la escena convertida en formato GLTF 2.0:

```csharp
scene.Save("Your Output Directory" + "Non_PBRtoPBRMaterial_Out.gltf", options);
// ExEnd:Non_PBRtoPBRMaterial
```

Repita estos pasos según sea necesario para su caso de uso específico, asegurándose de que cada detalle esté configurado correctamente.

## Conclusión

¡Felicidades! Ha aprendido con éxito cómo convertir materiales que no son PBR en PBR utilizando Aspose.3D para .NET. Esta poderosa herramienta abre infinitas posibilidades para la manipulación de gráficos 3D en sus aplicaciones .NET.

## Preguntas frecuentes

### P1: ¿Aspose.3D es compatible con todos los formatos de archivos 3D?

R1: Sí, Aspose.3D admite una amplia gama de formatos de archivos 3D, lo que brinda flexibilidad en sus proyectos.

### P2: ¿Puedo utilizar Aspose.3D para aplicaciones comerciales?

 R2: ¡Absolutamente! Aspose.3D es un producto comercial y puedes comprarlo[aquí](https://purchase.aspose.com/buy).

### P3: ¿Necesito una licencia temporal para realizar pruebas?

R3: Sí, puede obtener una licencia temporal para realizar pruebas.[aquí](https://purchase.aspose.com/temporary-license/).

### P4: ¿Dónde puedo encontrar soporte para Aspose.3D?

 A4: Visita el[Foro Aspose.3D](https://forum.aspose.com/c/3d/18) para apoyo y debates de la comunidad.

### P5: ¿Hay una prueba gratuita disponible?

 R5: Sí, puedes explorar una versión de prueba gratuita[aquí](https://releases.aspose.com/).