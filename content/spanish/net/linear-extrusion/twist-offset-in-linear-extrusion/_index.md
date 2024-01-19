---
title: Desplazamiento de torsión en extrusión lineal
linktitle: Desplazamiento de torsión en extrusión lineal
second_title: Aspose.3D API .NET
description: Explore la magia de Aspose.3D para .NET con nuestra guía paso a paso sobre Twist Offset en Linear Extrusion. Eleva tus proyectos 3D sin esfuerzo.
type: docs
weight: 15
url: /es/net/linear-extrusion/twist-offset-in-linear-extrusion/
---
## Introducción

Bienvenido al mundo de Aspose.3D para .NET, una biblioteca versátil que permite a los desarrolladores manejar la manipulación 3D con facilidad. En este tutorial, profundizaremos en una de las funciones más interesantes: el "Desplazamiento de torsión en extrusión lineal". Si está listo para mejorar sus habilidades de programación 3D, ¡vamos a sumergirnos!

## Requisitos previos

Antes de embarcarnos en este emocionante viaje, asegúrese de cumplir con los siguientes requisitos previos:

-  Aspose.3D para la biblioteca .NET: descargue e instale la biblioteca desde[página de lanzamiento](https://releases.aspose.com/3d/net/).

- Su entorno de desarrollo: asegúrese de que su entorno de desarrollo esté configurado y listo para funcionar.

## Importar espacios de nombres

Comience importando los espacios de nombres necesarios para acceder a la funcionalidad proporcionada por Aspose.3D para .NET. En su código, esto podría verse así:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

Ahora, dividamos el ejemplo en pasos manejables para dominar el desplazamiento de torsión en extrusión lineal:

## Paso 1: Inicializar el perfil base

Comience creando un perfil base, ejemplificado aquí por una forma de rectángulo con un radio de redondeo específico.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## Paso 2: crea una escena

Genere una escena 3D para albergar sus nodos y formas.

```csharp
Scene scene = new Scene();
```

## Paso 3: crear nodos

Construya nodos dentro de la escena, tanto a la izquierda como a la derecha.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(18, 0, 0);
```

## Paso 4: Extrusión lineal en el nodo izquierdo

Realice una extrusión lineal en el nodo izquierdo usando la propiedad de giro y cortes.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100 });
```

## Paso 5: Extrusión lineal en el nodo derecho con compensación de giro

En el nodo derecho, realice una extrusión lineal usando las propiedades de giro, desplazamiento de giro y cortes.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100, TwistOffset = new Vector3(3, 0, 0) });
```

## Paso 6: guardar la escena 3D

Guarde la escena 3D en el directorio de salida que desee, especificando el formato de archivo como WavefrontOBJ.

```csharp
scene.Save("Your Output Directory" + "TwistOffsetInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

¡Felicidades! Ha implementado con éxito el desplazamiento de torsión en extrusión lineal utilizando Aspose.3D para .NET.

## Conclusión

En este tutorial, exploramos las poderosas capacidades de Aspose.3D para .NET, centrándonos específicamente en Twist Offset en Linear Extrusion. Con estas nuevas habilidades, estará bien equipado para infundir dinamismo a sus proyectos 3D.

## Preguntas frecuentes

### P1: ¿Puedo usar Aspose.3D para .NET con otros lenguajes de programación?

R1: Aspose.3D admite principalmente lenguajes .NET, pero Aspose proporciona bibliotecas similares para Java y otras plataformas.

### P2: ¿Cómo obtengo una licencia temporal de Aspose.3D para .NET?

 A2: Visita[este enlace](https://purchase.aspose.com/temporary-license/) adquirir una licencia temporal para fines de prueba.

### P3: ¿Existe un foro comunitario para Aspose.3D para .NET?

R3: ¡Absolutamente! Únase a la comunidad en[Foro Aspose.3D](https://forum.aspose.com/c/3d/18) para interactuar con otros desarrolladores y buscar ayuda.

### P4: ¿Hay ejemplos y documentación adicionales disponibles?

 A4: Explora el[documentación](https://reference.aspose.com/3d/net/) para guías y ejemplos extensos.

### P5: ¿Dónde puedo comprar Aspose.3D para .NET?

 A5: Dirígete a[este enlace](https://purchase.aspose.com/buy) para realizar una compra y desbloquear todo el potencial de Aspose.3D.