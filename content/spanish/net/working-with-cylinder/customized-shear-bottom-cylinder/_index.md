---
title: Cilindro de fondo de corte personalizado
linktitle: Cilindro de fondo de corte personalizado
second_title: Aspose.3D API .NET
description: Aprenda a crear cilindros de fondo cortante personalizados utilizando Aspose.3D para .NET con nuestra guía detallada paso a paso. ¡Mejora tus habilidades de modelado 3D hoy!
type: docs
weight: 12
url: /es/net/working-with-cylinder/customized-shear-bottom-cylinder/
---
## Introducción
Bienvenido a nuestra guía completa sobre la creación de un cilindro de fondo cortante personalizado utilizando Aspose.3D para .NET. Si buscas mejorar tus habilidades de modelado 3D y agregar características únicas a tus proyectos, estás en el lugar correcto. En este tutorial, lo guiaremos a través del proceso paso a paso, utilizando explicaciones claras y fragmentos de código.
## Requisitos previos
Antes de sumergirnos en el tutorial, asegúrese de tener lo siguiente:
- Conocimientos básicos de programación en C# y .NET.
-  Aspose.3D para la biblioteca .NET instalada. Puedes descargarlo[aquí](https://releases.aspose.com/3d/net/).
- Un entorno de desarrollo configurado para programación .NET.
## Importar espacios de nombres
En su código C#, comience importando los espacios de nombres necesarios:
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```
## Paso 1: crea una escena
Comience creando una escena 3D usando Aspose.3D:
```csharp
Scene scene = new Scene();
```
## Paso 2: crear el cilindro 1
Genere el primer cilindro y establezca sus propiedades:
```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```
## Paso 3: Personalice la parte inferior de corte para el cilindro 1
Aplique un fondo de corte personalizado al primer cilindro:
```csharp
cylinder1.ShearBottom = new Vector2(0, 0.83); // Corte 47,5 grados en el plano xy (eje z)
```
## Paso 4: agregue el cilindro 1 a la escena
Añade el primer cilindro a la escena y establece su traducción:
```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```
## Paso 5: crear el cilindro 2
Genere un segundo cilindro con propiedades similares:
```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```
## Paso 6: agregue el cilindro 2 a la escena
Agregue el segundo cilindro a la escena sin fondo cortante:
```csharp
scene.RootNode.CreateChildNode(cylinder2);
```
## Paso 7: guarde la escena
Guarde la escena como un archivo Wavefront OBJ en su directorio de documentos:
```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```
## Conclusión
¡Felicidades! Ha creado con éxito un cilindro de fondo cortante personalizado utilizando Aspose.3D para .NET. Este tutorial tenía como objetivo proporcionar una guía paso a paso para usuarios con distintos niveles de experiencia en modelado y programación 3D.
## Preguntas frecuentes
### ¿Aspose.3D para .NET es adecuado para principiantes?
¡Absolutamente! Aspose.3D para .NET ofrece una interfaz fácil de usar, lo que la hace accesible tanto para principiantes como para desarrolladores experimentados.
### ¿Puedo aplicar diferentes ángulos de corte a los cilindros?
Sí, puede personalizar el fondo de corte para cada cilindro individualmente, lo que le permitirá lograr efectos únicos.
### ¿Hay una versión de prueba disponible?
 Sí, puedes explorar la versión de prueba gratuita.[aquí](https://releases.aspose.com/).
### ¿Dónde puedo encontrar soporte adicional?
 Visita el[Foro Aspose.3D](https://forum.aspose.com/c/3d/18) para apoyo y debates de la comunidad.
### ¿Cómo puedo obtener una licencia temporal?
Obtenga su licencia temporal[aquí](https://purchase.aspose.com/temporary-license/).