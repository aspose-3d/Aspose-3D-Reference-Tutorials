---
title: Dirección en extrusión lineal
linktitle: Dirección en extrusión lineal
second_title: Aspose.3D API .NET
description: Desbloquee el mundo del modelado 3D con Aspose.3D para .NET. Aprenda a dirigir la extrusión lineal, impulse la creatividad y cree aplicaciones inmersivas sin esfuerzo.
type: docs
weight: 11
url: /es/net/linear-extrusion/direction-in-linear-extrusion/
---
## Introducción

En el dinámico mundo del desarrollo de software, crear modelos 3D inmersivos es una habilidad indispensable. Aspose.3D para .NET proporciona a los desarrolladores un sólido conjunto de herramientas para aprovechar el potencial del modelado 3D en sus aplicaciones. En este tutorial, profundizaremos en el intrigante mundo de la extrusión lineal y exploraremos los matices de la función "Dirección en extrusión lineal".

## Requisitos previos

Antes de embarcarnos en este emocionante viaje, asegúrese de cumplir con los siguientes requisitos previos:

-  Aspose.3D para .NET: descargue e instale la biblioteca desde[Documentación de Aspose.3D .NET](https://reference.aspose.com/3d/net/).

- Entorno de desarrollo: asegúrese de tener configurado un entorno de desarrollo .NET que funcione.

## Importar espacios de nombres

En su proyecto .NET, importe los espacios de nombres necesarios para acceder a la funcionalidad de Aspose.3D. Agregue las siguientes líneas al comienzo de su código:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Paso 1: Inicializar el perfil base

Comience inicializando el perfil base que se va a extruir. En este ejemplo, creamos una forma de rectángulo con un radio de redondeo de 0,3.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## Paso 2: crea una escena 3D

Construye las bases para tu obra maestra en 3D creando una escena.

```csharp
Scene scene = new Scene();
```

## Paso 3: crear nodos

Genere nodos dentro de la escena para representar diferentes componentes de su entorno 3D.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(8, 0, 0);
```

## Paso 4: Extrusión lineal sin dirección

 Realice una extrusión lineal en el nodo izquierdo usando el`Twist` y`Slices` propiedades.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100 });
```

## Paso 5: Extrusión lineal con dirección

 Amplíe las capacidades de extrusión incorporando la`Direction` propiedad en el nodo derecho.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100, Direction = new Vector3(0.3, 0.2, 1) });
```

## Paso 6: guarde la escena 3D

 Conserva tu creación guardando la escena 3D. Reemplazar`"Your Output Directory"` con el directorio deseado.

```csharp
scene.Save("Your Output Directory" + "DirectionInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

¡Felicidades! Ha implementado con éxito la extrusión lineal con Aspose.3D para .NET, explorando tanto el enfoque tradicional como el direccional.

## Conclusión

En este tutorial, navegamos por el fascinante ámbito del modelado 3D utilizando Aspose.3D para .NET. La extrusión lineal, con y sin dirección, abre infinitas posibilidades para los desarrolladores que buscan crear aplicaciones visualmente impresionantes. Con Aspose.3D, el poder del modelado 3D está a tu alcance.

## Preguntas frecuentes

### P1: ¿Cómo puedo obtener una licencia temporal de Aspose.3D para .NET?

 A1: Visita[Aspose Licencia Temporal](https://purchase.aspose.com/temporary-license/) para obtener una licencia temporal.

### P2: ¿Dónde puedo encontrar soporte para Aspose.3D?

 A2: Únete a la[Foro Aspose.3D](https://forum.aspose.com/c/3d/18) para buscar ayuda y conectarse con la comunidad.

### P3: ¿Hay una prueba gratuita disponible?

 R3: Sí, explore las funciones con una prueba gratuita en[Lanzamientos de Aspose.3D](https://releases.aspose.com/).

### P4: ¿Cómo compro Aspose.3D para .NET?

 A4: Navegue hasta el[Aspose Página de compra](https://purchase.aspose.com/buy) para opciones de licencia y detalles de compra.

### P5: ¿Dónde puedo encontrar documentación detallada de Aspose.3D para .NET?

 A5: Consulte la información completa[Documentación de Aspose.3D .NET](https://reference.aspose.com/3d/net/) para obtener información detallada.