---
title: Representar una escena en un mapa cúbico con seis caras
linktitle: Representar una escena en un mapa cúbico con seis caras
second_title: Aspose.3D API .NET
description: Cree impresionantes mapas de cubos con Aspose.3D para .NET. Siga nuestra guía paso a paso para renderizar escenas 3D en cautivadores mapas de cubos de seis caras.
weight: 14
url: /es/net/rendering/render-scene-cubemap/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Representar una escena en un mapa cúbico con seis caras

## Introducción
Bienvenido a esta guía paso a paso sobre cómo representar una escena en un mapa de cubos con seis caras usando Aspose.3D para .NET. En este tutorial, lo guiaremos a través del proceso de creación de un impresionante mapa de cubos renderizando una escena 3D. Aspose.3D es una potente API .NET que simplifica la manipulación de gráficos 3D y, con esta guía, aprovechará sus capacidades para crear cautivadores mapas de cubos.
## Requisitos previos
Antes de sumergirnos en el tutorial, asegúrese de tener implementados los siguientes requisitos previos:
- Un conocimiento práctico del desarrollo de C# y .NET.
-  Aspose.3D para .NET instalado. Puedes descargarlo[aquí](https://releases.aspose.com/3d/net/).
- Un archivo de escena 3D en formato GLB (por ejemplo, "VirtualCity.glb") para renderizar.
## Importar espacios de nombres
Comience importando los espacios de nombres necesarios para Aspose.3D en su código C#:
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Render;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Drawing.Imaging;
using System.Linq;
using System.Text;
```
## Paso 1: carga la escena
Cargue el archivo de escena 3D usando el siguiente código:
```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("VirtualCity.glb"));
```
## Paso 2: crea cámara y luces
Crea una cámara y dos luces para iluminar la escena:
```csharp
Camera cam = new Camera(ProjectionType.Perspective)
{
    NearPlane = 0.1,
    FarPlane = 200,
    RotationMode = RotationMode.FixedDirection
};
scene.RootNode.CreateChildNode(cam).Transform.Translation = new Vector3(5, 6, 0);
scene.RootNode.CreateChildNode(new Light() { LightType = LightType.Point }).Transform.Translation = new Vector3(-10, 7, -10);
scene.RootNode.CreateChildNode(new Light()
{
    Color = new Vector3(Color.CadetBlue)
}).Transform.Translation = new Vector3(49, 0, 49);
```
## Paso 3: crear un renderizador y un destino de renderizado
Cree un renderizador y un destino de renderizado de mapa de cubos con textura de profundidad:
```csharp
using (var renderer = Renderer.CreateRenderer())
{
    IRenderTexture rt = renderer.RenderFactory.CreateCubeRenderTexture(new RenderParameters(false), 512, 512);
    rt.CreateViewport(cam, RelativeRectangle.FromScale(0, 0, 1, 1));
    renderer.Render(rt);
    ITextureCubemap cubemap = rt.Targets[0] as ITextureCubemap;
```
## Paso 4: guardar las caras de Cubemap
Guarde cada cara del mapa de cubos en el disco con nombres de archivo específicos:
```csharp
CubeFaceData<string> fileNames = new CubeFaceData<string>()
{
    Right = "Your Output Directory" + "right.png",
    Left = "Your Output Directory" + "left.png",
    Back = "Your Output Directory" + "back.png",
    Front = "Your Output Directory" + "front.png",
    Bottom = "Your Output Directory" + "bottom.png",
    Top = "Your Output Directory" + "top.png"
};
cubemap.Save(fileNames, ImageFormat.Png);
```
## Conclusión
¡Felicidades! Ha renderizado con éxito una escena 3D en un mapa de cubos usando Aspose.3D para .NET. Explore más opciones de personalización y mejore sus proyectos de gráficos 3D con esta potente API.
## Preguntas frecuentes
### P: ¿Puedo usar Aspose.3D para .NET con otros formatos de archivos 3D?
Sí, Aspose.3D admite varios formatos de archivos 3D, lo que brinda flexibilidad en sus proyectos.
### P: ¿Cómo puedo obtener soporte para Aspose.3D?
 Visita el[Foro Aspose.3D](https://forum.aspose.com/c/3d/18) para apoyo y debates de la comunidad.
### P: ¿Hay una prueba gratuita disponible?
 Sí, puedes acceder a la prueba gratuita.[aquí](https://releases.aspose.com/).
### P: ¿Puedo renderizar escenas con animaciones usando Aspose.3D?
¡Absolutamente! Aspose.3D admite la representación de escenas animadas en 3D.
### P: ¿Dónde puedo encontrar documentación detallada?
 Referirse a[Documentación de Aspose.3D](https://reference.aspose.com/3d/net/) para obtener información detallada.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
