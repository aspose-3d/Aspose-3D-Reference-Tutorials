---
title: Transformación de nodo por matriz de transformación
linktitle: Transformación de nodo por matriz de transformación
second_title: Aspose.3D API .NET
description: Transforme nodos sin esfuerzo en escenas 3D usando Aspose.3D para .NET. Aprenda las transformaciones de nodos paso a paso con un tutorial.
weight: 21
url: /es/net/geometry-and-hierarchy/transformation-node-matrix/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Transformación de nodo por matriz de transformación

## Introducción

En el ámbito dinámico de las visualizaciones y gráficos 3D, la capacidad de manipular objetos dentro de una escena es un aspecto crucial. Aspose.3D para .NET permite a los desarrolladores transformar nodos sin problemas utilizando matrices de transformación, agregando una capa de creatividad y control a las escenas 3D. Este tutorial lo guiará a través del proceso de transformar un nodo en una escena 3D paso a paso.

## Requisitos previos

Antes de sumergirse en el tutorial, asegúrese de cumplir con los siguientes requisitos previos:

1.  Aspose.3D para la biblioteca .NET: asegúrese de tener la biblioteca Aspose.3D instalada en su proyecto .NET. Puedes descargarlo[aquí](https://releases.aspose.com/3d/net/).

2. Entorno de desarrollo: configure un entorno de desarrollo .NET que funcione y, si aún no lo ha hecho, cree un nuevo proyecto donde implementará las transformaciones.

## Importar espacios de nombres

Comience importando los espacios de nombres necesarios a su proyecto .NET. Estos espacios de nombres proporcionan las clases y métodos esenciales para la manipulación de escenas 3D.

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

Ahora que hemos cubierto los conceptos básicos, analicemos el proceso de transformación en una guía paso a paso.

## Paso 1: inicializar la escena

```csharp
// ExStart: Agregar transformación a nodo por matriz de transformación
// Inicializar objeto de escena
Scene scene = new Scene();

```

En este paso, creamos una nueva escena 3D vacía.

## Paso 2: crear malla y adjuntarla a la escena

```csharp
// Llame a la clase común para crear malla utilizando el método de creación de polígonos para establecer una instancia de malla
Mesh mesh = (new Box()).ToMesh();

// Cree un nodo contenedor para la malla.
Node cubeNode = scene.RootNode.CreateChildNode(mesh);
```

Aquí, generamos una malla usando el método de construcción de polígonos y la asignamos al nodo, estableciendo la geometría de nuestro cubo.

## Paso 3: Establecer una matriz de traducción personalizada

```csharp
// Establecer matriz de traducción personalizada
cubeNode.Transform.TransformMatrix = new Matrix4(
    1, -0.3, 0, 0,
    0.4, 1, 0.3, 0,
    0, 0, 1, 0,
    0, 20, 0, 1
);        
```

Defina una matriz de traducción personalizada para determinar la transformación específica aplicada al nodo. Ajuste los valores de la matriz según sea necesario para la transformación deseada.

Incluya el nodo del cubo en la escena, haciéndolo parte del entorno 3D general.

## Paso 4: guarda la escena

```csharp
// La ruta al directorio de documentos.
var output = "TransformationToNode.fbx";

// Guarde la escena 3D en los formatos de archivo compatibles
scene.Save(output);
// ExEnd:AddTransformationToNodeByTransformationMatrix
Console.WriteLine("\nTransformation added successfully to node.\nFile saved at " + output);
```

Especifique el directorio de salida y el nombre del archivo, luego guarde la escena 3D en el formato de archivo deseado. En este ejemplo, lo guardaremos en el formato FBX7500ASCII.

## Conclusión

¡Felicidades! Ha transformado exitosamente un nodo usando una matriz de transformación en una escena 3D con Aspose.3D para .NET. Esta capacidad abre las puertas a aplicaciones 3D diversas y visualmente cautivadoras.

## Preguntas frecuentes

### P1: ¿Qué es una matriz de transformación en gráficos 3D?

R1: Una matriz de transformación es una representación matemática que se utiliza para aplicar varias transformaciones (traslación, rotación, escala) a objetos en el espacio 3D.

### P2: ¿Puedo aplicar múltiples transformaciones a un solo nodo?

R2: Sí, puedes combinar múltiples transformaciones multiplicando sus respectivas matrices y aplicando el resultado al nodo.

### P3: ¿Existen otros formatos de archivo compatibles para guardar escenas 3D?

 R3: Aspose.3D para .NET admite varios formatos de archivo, incluidos STL, GLTF, OBJ y más. Referirse a[documentación](https://reference.aspose.com/3d/net/) para obtener una lista completa.

### P4: ¿Cómo puedo obtener una licencia temporal de Aspose.3D para .NET?

 A4: Visita el[página de licencia temporal](https://purchase.aspose.com/temporary-license/)en el sitio web de Aspose para obtener una licencia temporal con fines de evaluación.

### P5: ¿Dónde puedo buscar ayuda o conectarme con la comunidad Aspose.3D?

 A5: Visita el[Foro Aspose.3D](https://forum.aspose.com/c/3d/18) para hacer preguntas, compartir experiencias y conectarse con otros desarrolladores que utilizan Aspose.3D.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
