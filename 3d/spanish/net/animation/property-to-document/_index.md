---
date: 2026-01-14
description: Aprenda a animar un cubo en escenas 3D usando Aspose.3D para .NET. Esta
  guía muestra cómo crear una curva de animación, vincular fotogramas clave y animar
  propiedades 3D.
linktitle: Animating Properties to Document in 3D Scenes
second_title: Aspose.3D .NET API
title: Cómo animar un cubo en escenas 3D con Aspose.3D para .NET
url: /es/net/animation/property-to-document/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Cómo animar un cubo en escenas 3D con Aspose.3D para .NET

## Introducción

Si te estás adentrando en el mundo de la creación y animación de escenas 3D en .NET, Aspose.3D es tu herramienta de referencia. En esta guía paso a paso, exploraremos **cómo animar un cubo** mediante la animación de sus propiedades, la creación de curvas de animación y la vinculación de fotogramas clave. Al final, tendrás un cubo completamente animado que podrás exportar a formatos 3D populares.

## Respuestas rápidas
- **¿Qué biblioteca se utiliza?** Aspose.3D for .NET  
- **¿Qué tarea principal cubre este tutorial?** Cómo animar un cubo en una escena 3D  
- **¿Pasos clave?** Importar espacios de nombres, crear una escena, vincular fotogramas clave, guardar el archivo  
- **¿Necesito una licencia?** Una prueba gratuita sirve para aprender; se requiere una licencia comercial para producción  
- **¿Formato de salida compatible?** FBX (ASCII 7500) y otros compatibles con Aspose.3D  

## ¿Qué es “cómo animar un cubo” en Aspose.3D?

Animar un cubo significa modificar sus propiedades de transformación (como Translación, Rotación o Escala) a lo largo del tiempo usando datos de fotogramas clave. Aspose.3D ofrece una API clara para crear **curvas de animación**, **vincular fotogramas clave** y **animar propiedades 3D** directamente en los nodos de la escena.

## ¿Por qué animar un cubo con Aspose.3D?

- **Integración completa con .NET** – funciona con .NET Framework, .NET Core y .NET 5/6.  
- **Sin dependencias externas** – no se necesita Unity u otros motores para animaciones simples.  
- **Flexibilidad de exportación** – las escenas animadas pueden guardarse como FBX, OBJ, GLTF, etc., para flujos de trabajo posteriores.

## Requisitos previos

Antes de embarcarnos en este emocionante viaje, asegúrate de contar con los siguientes requisitos:

- Aspose.3D for .NET: Asegúrate de tener la biblioteca instalada. Puedes descargarla desde el [sitio web de Aspose.3D](https://releases.aspose.com/3d/net/).
- Conocimiento de C#: Familiaridad con el lenguaje de programación C# es esencial para comprender e implementar los ejemplos.
- Entorno de Desarrollo Integrado (IDE): Usa tu IDE preferido, como Visual Studio, para codificar junto con los ejemplos.
- Conceptos básicos de escena 3D: Tener una comprensión de los conceptos básicos de escena 3D hará que tu proceso de aprendizaje sea más fluido.

## Importar espacios de nombres

En tu código C#, asegúrate de importar los espacios de nombres necesarios para Aspose.3D. Aquí está el conjunto requerido:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using Aspose._3D.Examples.CSharp.Geometry_Hierarchy;
```

## Paso 1: Inicializar el objeto Scene

Crea una escena vacía que contendrá todos nuestros nodos y animaciones.

```csharp
Scene scene = new Scene();
```

## Paso 2: Crear malla usando Polygon Builder

Generamos una malla de cubo simple usando el método auxiliar `Common.CreateMeshUsingPolygonBuilder()`.

```csharp
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
```

## Paso 3: Crear nodos de cubo

Agrega la malla del cubo a la escena como un nodo hijo de la raíz. El nombre del nodo **cube1** se usará más adelante cuando vinculamos los fotogramas clave.

```csharp
Node cube1 = scene.RootNode.CreateChildNode("cube1", mesh);
```

## Paso 4: Encontrar la propiedad Translation

Para animar la posición del cubo, necesitamos localizar su propiedad **Translation** en la transformación del nodo.

```csharp
Property translation = cube1.Transform.FindProperty("Translation");
```

## Paso 5: Crear un Bind Point

Un `BindPoint` vincula una propiedad de la escena a una curva de animación. Aquí vinculamos la propiedad de translación.

```csharp
BindPoint bindPoint = new BindPoint(scene, translation);
```

## Paso 6: Vincular curva de animación en el componente X

Ahora creamos una curva de animación para el eje **X**. Esto demuestra el paso de **crear curva de animación** y muestra cómo **vincular fotogramas clave**.

```csharp
bindPoint.BindKeyframeSequence("X", new KeyframeSequence()
{
    {0, 10.0f, Interpolation.Bezier},
    {3, 20.0f, Interpolation.Bezier},
    {5, 30.0f, Interpolation.Linear},
});
```

## Paso 7: Vincular curva de animación en el componente Z

De manera similar, animamos el eje **Z** para dar al cubo una trayectoria de movimiento más dinámica.

```csharp
bindPoint.BindKeyframeSequence("Z", new KeyframeSequence()
{
    {0, 10.0f, Interpolation.Bezier},
    {3, -10.0f, Interpolation.Bezier},
    {5, 0.0f, Interpolation.Linear},
});
```

## Paso 8: Guardar la escena 3D

Exporta la escena animada a un archivo FBX. El formato `FBX7500ASCII` es ampliamente compatible con herramientas 3D.

```csharp
string output = "Your Output Directory" + "PropertyToDocument.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

## Paso 9: Mostrar mensaje de éxito

Proporciona al usuario una retroalimentación de que la animación se añadió correctamente.

```csharp
Console.WriteLine("\nAnimation property added successfully to document.\nFile saved at " + output);
```

## Problemas comunes y soluciones

| Problema | Razón | Solución |
|----------|-------|----------|
| No se observa movimiento | Los tiempos de los fotogramas clave no coinciden con el rango de reproducción | Asegúrate de que la línea de tiempo de animación de la escena cubra los tiempos de los fotogramas clave (0‑5 segundos en este ejemplo). |
| Ruta de archivo incorrecta | `output` apunta a un directorio que no existe | Crea el directorio primero o usa una ruta absoluta. |
| Excepción de licencia | Ejecutar sin una licencia válida en producción | Aplica tu licencia de Aspose.3D antes de crear el `Scene`. |

## Preguntas frecuentes

### P1: ¿Dónde puedo encontrar la documentación de Aspose.3D?

R1: La documentación está disponible [aquí](https://reference.aspose.com/3d/net/).

### P2: ¿Cómo descargo Aspose.3D para .NET?

R2: Puedes descargarlo desde la [página de lanzamientos](https://releases.aspose.com/3d/net/).

### P3: ¿Hay una prueba gratuita disponible?

R3: Sí, puedes obtener una prueba gratuita [aquí](https://releases.aspose.com/).

### P4: ¿Dónde puedo obtener soporte para Aspose.3D?

R4: Visita el [foro de Aspose.3D](https://forum.aspose.com/c/3d/18) para obtener soporte.

### P5: ¿Puedo obtener una licencia temporal?

R5: Sí, puedes obtener una licencia temporal [aquí](https://purchase.aspose.com/temporary-license/).

## Preguntas frecuentes adicionales (optimizado por IA)

**P: ¿Puedo animar otras propiedades como rotación o escala?**  
R: Por supuesto. Usa `cube1.Transform.FindProperty("Rotation")` o `"Scale"` y vincula secuencias de fotogramas clave de la misma manera.

**P: ¿Aspose.3D admite tipos de interpolación de fotogramas clave diferentes a Bezier y Linear?**  
R: Sí, también admite `Interpolation.Step` y `Interpolation.Cubic` para mayor control.

**P: ¿Cómo puedo previsualizar la animación antes de exportar?**  
R: Aspose.3D ofrece un visor simple en su API; alternativamente, carga el FBX exportado en un visor 3D como Autodesk FBX Review.

**P: ¿Es posible animar varios cubos simultáneamente?**  
R: Crea nodos separados para cada cubo, recupera sus respectivas propiedades y vincula secuencias de fotogramas clave independientes.

## Conclusión

¡Felicidades! Acabas de dominar **cómo animar un cubo** en una escena 3D usando Aspose.3D para .NET. Ahora sabes cómo **crear curvas de animación**, **vincular fotogramas clave** y **animar propiedades 3D** para dar vida a la geometría estática. Siéntete libre de experimentar con rotaciones, escalado o incluso objetivos de morph para ampliar tu conjunto de herramientas de animación.

---

**Última actualización:** 2026-01-14  
**Probado con:** Aspose.3D 24.11 for .NET  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}