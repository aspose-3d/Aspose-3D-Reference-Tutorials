---
title: Capturar ventanas gráficas en escenas 3D
linktitle: Capturar ventanas gráficas en escenas 3D
second_title: Aspose.3D API .NET
description: Aprenda a capturar impresionantes ventanas gráficas 3D utilizando Aspose.3D para .NET. Guía paso a paso para renderizar escenas con flexibilidad.
weight: 11
url: /es/net/rendering/capture-viewport/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Capturar ventanas gráficas en escenas 3D

## Introducción

En el ámbito de la visualización y los gráficos 3D, capturar ventanas gráficas es una habilidad esencial que mejora la profundidad y el detalle de sus escenas. Aspose.3D para .NET proporciona una solución sólida para renderizar y manipular escenas 3D. Este tutorial lo guiará a través del proceso de captura de ventanas gráficas en escenas 3D usando Aspose.3D, permitiéndole crear visualizaciones impresionantes con facilidad.

## Requisitos previos

Antes de sumergirse en el tutorial, asegúrese de cumplir con los siguientes requisitos previos:

-  Aspose.3D para la biblioteca .NET: asegúrese de tener instalada la biblioteca Aspose.3D. Puedes descargarlo desde[aquí](https://releases.aspose.com/3d/net/).

## Importar espacios de nombres

Para comenzar, importe los espacios de nombres necesarios a su proyecto .NET:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using System.Drawing;
using System.Drawing.Imaging;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Render;
using Aspose.ThreeD.Utilities;
```

## Paso 1: cargue una escena 3D existente

Comience cargando una escena 3D existente en su proyecto. El siguiente fragmento de código demuestra esto:

```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("scene.obj"));
```

## Paso 2: crea una cámara

A continuación, cree una instancia de la cámara y establezca su posición y objetivo:

```csharp
Camera camera = new Camera();
scene.RootNode.CreateChildNode("camera", camera).Transform.Translation = new Vector3(2, 44, 66);
camera.LookAt = new Vector3(50, 12, 0);
```

## Paso 3: agregue iluminación a la escena

Mejore su escena agregando una fuente de luz. El siguiente fragmento de código muestra cómo crear un punto de luz:

```csharp
scene.RootNode.CreateChildNode("light", new Light() { Color = new Vector3(Color.White), LightType = LightType.Point }).Transform.Translation = new Vector3(26, 57, 43);
```

## Paso 4: configurar el renderizador y el destino de renderizado

Configure el renderizador y cree un objetivo de renderizado para capturar la escena:

```csharp
using (var renderer = Renderer.CreateRenderer())
{
    renderer.EnableShadows = false;

    using (IRenderTexture rt = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(), 1, 1024, 1024))
    {
        // ... (continuación en los siguientes pasos)
    }
}
```

## Paso 5: definir ventanas gráficas y renderizar

Defina ventanas gráficas y renderice la escena para generar imágenes de salida:

```csharp
Viewport vp = rt.CreateViewport(camera, new RelativeRectangle() { ScaleWidth = 1, ScaleHeight = 1 });
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "file-1viewports_out.png", ImageFormat.Png);
```

## Paso 6: modifique las ventanas gráficas y vuelva a renderizar

Modifique las ventanas gráficas y renderice la escena una vez más, demostrando la flexibilidad de Aspose.3D:

```csharp
vp.Area = new RelativeRectangle() { ScaleWidth = 0.5f, ScaleHeight = 1 };
rt.CreateViewport(camera, new RelativeRectangle() { ScaleX = 0.5f, ScaleWidth = 0.5f, ScaleHeight = 1 });
camera.FieldOfView = 90;
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "file-2viewports_out.png", ImageFormat.Png);
```

Continúe experimentando con diferentes configuraciones para lograr los efectos visuales deseados.

## Conclusión

En este tutorial, exploramos el proceso de captura de ventanas gráficas en escenas 3D usando Aspose.3D para .NET. Aprovechando sus poderosas funciones, puede elevar sus proyectos de gráficos 3D a nuevas alturas, brindando experiencias visuales cautivadoras.

## Preguntas frecuentes

### P1: ¿Aspose.3D es compatible con otros formatos de archivos 3D?

R1: Sí, Aspose.3D admite varios formatos de archivos 3D, lo que garantiza la compatibilidad con una amplia gama de herramientas de diseño.

### P2: ¿Puedo usar Aspose.3D para desarrollar juegos?

R2: Si bien Aspose.3D está diseñado principalmente para gráficos y visualización, sus funcionalidades pueden complementar ciertos aspectos del desarrollo de juegos.

### P3: ¿Dónde puedo encontrar ejemplos y documentación adicionales?

 A3: Explore lo completo[Documentación de Aspose.3D](https://reference.aspose.com/3d/net/) para más ejemplos e información detallada.

### P4: ¿Hay una prueba gratuita disponible?

 R4: Sí, puedes acceder a una prueba gratuita[aquí](https://releases.aspose.com/).

### P5: ¿Cómo puedo buscar ayuda o participar en la comunidad?

 A5: Únase a la comunidad Aspose.3D en el[Foro de soporte](https://forum.aspose.com/c/3d/18) para asistencia y colaboración.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
