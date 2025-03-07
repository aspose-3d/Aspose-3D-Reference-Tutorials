---
title: Realizar extrusión lineal
linktitle: Realizar extrusión lineal
second_title: Aspose.3D API .NET
description: Explore el mundo de los gráficos 3D con Aspose.3D para .NET. Realización de extrusión lineal en esta guía paso a paso.
weight: 12
url: /es/net/3d-modeling/linear-extrusion/performing-linear-extrusion/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Realizar extrusión lineal

## Introducción:

Embárquese en un emocionante viaje al reino de los gráficos 3D con Aspose.3D para .NET, una potencia que eleva su juego de desarrollo. En este tutorial, profundizaremos en las complejidades de la extrusión lineal, una técnica fascinante que da vida a perfiles 2D estáticos, impulsándolos al mundo dinámico del 3D. ¡Abramos la puerta a la creatividad y la innovación usando Aspose.3D!

## Requisitos previos:

Antes de sumergirse en el encantador mundo de la manipulación 3D, asegúrese de cumplir con los siguientes requisitos previos:

1. Instalación de Aspose.3D:
   -  Comience descargando e instalando Aspose.3D para .NET desde[aquí](https://releases.aspose.com/3d/net/).
   -  Siga las instrucciones de instalación proporcionadas en la documentación.[aquí](https://reference.aspose.com/3d/net/).

2. Configurando su entorno de desarrollo:
   - Asegúrese de que su entorno de desarrollo esté configurado correctamente con los espacios de nombres necesarios para Aspose.3D.

Ahora que estás preparado, ¡saltemos a la magia de Aspose.3D!

## Importar espacios de nombres:

Incluya los espacios de nombres esenciales para iniciar su aventura 3D:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

Estos espacios de nombres sientan las bases para su viaje de codificación 3D, brindando acceso a las herramientas necesarias para una integración perfecta de las funcionalidades de Aspose.3D.

## Realización de extrusión lineal:

Creemos un objeto 3D fascinante a través de extrusión lineal usando Aspose.3D. Sigue estos pasos:

## Paso 1: Inicializar el perfil base
```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

Este paso configura el perfil 2D que servirá como base para nuestra obra maestra 3D. Ajuste los parámetros según sea necesario para lograr la forma deseada.

## Paso 2: Extrusión lineal
```csharp
var extrusion = new LinearExtrusion(profile, 10) { Slices = 100, Center = true, Twist = 360, TwistOffset = new Vector3(10, 0, 0) };
```

Aquí se realiza la Extrusión Lineal, tomando el perfil 2D y extendiéndolo en la tercera dimensión. Experimente con parámetros como 'Slices' y 'Twist' para moldear su creación.

## Paso 3: crea una escena
```csharp
Scene scene = new Scene();
```

Se crea un lienzo en blanco: una escena donde su objeto 3D cobrará vida.

## Paso 4: agregue extrusión a la escena
```csharp
scene.RootNode.CreateChildNode(extrusion);
```

Su obra maestra extruida se agrega como un nodo secundario a la escena.

## Paso 5: guarde la escena 3D
```csharp
scene.Save(RunExamples.GetOutputFilePath("LinearExtrusion.obj"), FileFormat.WavefrontOBJ);
```

Finalmente, guarde su creación en el formato deseado. En este ejemplo, se guarda como un archivo Wavefront OBJ.

¡Ahora contempla tu maravilla 3D!

## Conclusión:

¡Felicidades! Acabas de arañar la superficie del potencial de Aspose.3D. Este tutorial simplemente da una idea del vasto paisaje que espera su exploración. Sumérgete en la documentación, experimenta con varias formas y desbloquea todo el espectro de posibilidades con Aspose.3D para .NET.

## Preguntas frecuentes:

### P1: ¿Aspose.3D es adecuado para principiantes?

R1: ¡Absolutamente! Aspose.3D ofrece un entorno fácil de usar y nuestro tutorial lo guiará a través de los conceptos básicos.

### P2: ¿Puedo utilizar Aspose.3D para proyectos comerciales?

 R2: Sí, Aspose.3D viene con opciones de licencia para uso personal y comercial. Controlar[aquí](https://purchase.aspose.com/buy) para detalles.

### P3: ¿Cómo puedo obtener licencias temporales para realizar pruebas?

 A3: Visita[este enlace](https://purchase.aspose.com/temporary-license/) para obtener licencias temporales con fines de prueba.

### P4: ¿Dónde puedo encontrar apoyo comunitario?

 A4: Únase a la[Foro Aspose.3D](https://forum.aspose.com/c/3d/18) para conectarse con una comunidad vibrante y buscar ayuda.

### P5: ¿Hay una prueba gratuita disponible?

 R5: ¡Por supuesto! Descargue la versión de prueba gratuita[aquí](https://releases.aspose.com/) para experimentar las capacidades de Aspose.3D de primera mano.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
