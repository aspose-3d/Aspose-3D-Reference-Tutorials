---
title: Centro en extrusión lineal
linktitle: Centro en extrusión lineal
second_title: Aspose.3D API .NET
description: Explore el mundo del modelado 3D con Aspose.3D para .NET. Centre técnicas de extrusión lineal, cree diseños impresionantes y dé rienda suelta a su creatividad.
weight: 10
url: /es/net/3d-modeling/linear-extrusion/center-in-linear-extrusion/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Centro en extrusión lineal

## Introducción

Bienvenido a esta guía completa sobre cómo dominar la extrusión lineal utilizando Aspose.3D para .NET. Si buscas mejorar tus habilidades de modelado 3D y crear extrusiones impresionantes, estás en el lugar correcto. En este tutorial, profundizaremos en la técnica de extrusión lineal, centrándonos específicamente en el aspecto de centrado para llevar tus diseños a un nivel completamente nuevo.

## Requisitos previos

Antes de embarcarnos en este emocionante viaje, asegúrese de cumplir con los siguientes requisitos previos:

- Conocimientos básicos del lenguaje de programación C#.
- Visual Studio instalado en su máquina.
-  Biblioteca Aspose.3D para .NET, que puede descargar desde[Documentación de Aspose.3D .NET](https://reference.aspose.com/3d/net/).
-  Asegúrese de tener acceso a la[Documentación de Aspose.3D .NET](https://reference.aspose.com/3d/net/) como referencia a lo largo del tutorial.

## Importar espacios de nombres

Para comenzar, importemos los espacios de nombres necesarios. Estos sentarán las bases de nuestra obra maestra del modelado 3D.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Paso 1: Inicializar el perfil base

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## Paso 2: crea una escena 3D

```csharp
Scene scene = new Scene();
```

## Paso 3: crear nodos izquierdo y derecho

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(5, 0, 0);
```

## Paso 4: realizar una extrusión lineal en el nodo izquierdo

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 2) { Center = false, Slices = 3 });
```

## Paso 5: Establecer el plano de tierra como referencia

```csharp
left.CreateChildNode(new Box(0.01, 3, 3));
```

## Paso 6: realizar una extrusión lineal en el nodo derecho

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 2) { Center = true, Slices = 3 });
```

## Paso 7: Establecer el plano de tierra como referencia (nodo derecho)

```csharp
right.CreateChildNode(new Box(0.01, 3, 3));
```

## Paso 8: guardar la escena 3D

```csharp
scene.Save("Your Output Directory" + "CenterInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Conclusión

¡Felicidades! Ha dominado con éxito el arte de la extrusión lineal con centrado utilizando Aspose.3D para .NET. Siéntete libre de experimentar con diferentes parámetros y explorar las amplias posibilidades que ofrece esta técnica.

## Preguntas frecuentes

### P1: ¿Puedo usar Aspose.3D para .NET con otros lenguajes de programación?

R1: Aspose.3D admite principalmente lenguajes .NET como C# y VB.NET.

### P2: ¿Dónde puedo encontrar soporte para consultas relacionadas con Aspose.3D?

 A2: Visita el[Foro Aspose.3D](https://forum.aspose.com/c/3d/18) para soporte y debates dedicados.

### P3: ¿Hay una prueba gratuita disponible de Aspose.3D para .NET?

 R3: Sí, puedes acceder a la prueba gratuita[aquí](https://releases.aspose.com/).

### P4: ¿Cómo puedo obtener una licencia temporal de Aspose.3D para .NET?

 R4: Puedes adquirir una licencia temporal[aquí](https://purchase.aspose.com/temporary-license/).

### P5: ¿Dónde puedo comprar la licencia Aspose.3D para .NET?

 R5: Compre su licencia[aquí](https://purchase.aspose.com/buy).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
