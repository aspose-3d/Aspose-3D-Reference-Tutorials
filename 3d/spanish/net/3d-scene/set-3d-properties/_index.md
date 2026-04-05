---
date: 2026-03-28
description: Aprende a enumerar las propiedades del material, cambiar el color difuso
  y modificar los atributos del material 3D usando Aspose.3D para .NET. Se incluyen
  ejemplos de código paso a paso.
linktitle: List Material Properties in 3D Scenes with Aspose.3D
second_title: Aspose.3D .NET API
title: Listar propiedades de material en escenas 3D con Aspose.3D
url: /es/net/3d-scene/set-3d-properties/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Listar propiedades de materiales en escenas 3D con Aspose.3D

## Introducción

Si necesitas **listar propiedades de material** de un modelo 3D y luego ajustar cosas como el color difuso, estás en el lugar correcto. Aspose.3D for .NET te brinda una API limpia y orientada a objetos que te permite inspeccionar, recuperar y modificar atributos de material sin salir de tu código C#. En este tutorial recorreremos la carga de una escena, la enumeración de sus propiedades de material y el cambio de valores como el componente difuso, para que puedas dar a tus modelos el aspecto exacto que deseas.

## Respuestas rápidas
- **¿Cuál es el objetivo principal?** Listar propiedades de material y modificarlas (p. ej., color difuso).  
- **¿Qué biblioteca se requiere?** Aspose.3D for .NET.  
- **¿Necesito una licencia?** Se requiere una licencia temporal o completa para uso en producción.  
- **¿Formatos de archivo compatibles?** FBX, OBJ, STL, STL‑ASCII, 3MF y más.  
- **¿Tiempo típico de implementación?** Aproximadamente 10‑15 minutos para un script básico de listado de propiedades.

## Qué es **listar propiedades de material**?
Listar propiedades de material significa iterar sobre el `PropertyCollection` de un material para leer cada nombre de propiedad y su valor actual. Esto es útil para depuración, inspección visual o la creación de controles UI que permitan a los usuarios ajustar la configuración del material en tiempo de ejecución.

## Por qué usar Aspose.3D para **acceder a propiedades de material**?
- **Sin convertidores externos** – trabaja directamente con objetos nativos de .NET.  
- **Modelo de propiedades rico** – soporta atributos personalizados específicos de FBX además de los valores PBR estándar.  
- **Multiplataforma** – funciona en .NET Framework, .NET Core y .NET 5/6+.  

## Requisitos previos

- Aspose.3D for .NET instalado en tu proyecto. Descárgalo [aquí](https://releases.aspose.com/3d/net/).
- Una carpeta en el disco para almacenar tus archivos fuente 3D (p. ej., un archivo FBX con texturas incrustadas).

Ahora que tienes lo básico listo, sumérgete en el código.

## Importar espacios de nombres

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```

## Paso 1: Cargar escena 3D

```csharp
//ExStart: Load3DScene
string dataDir = "Your Document Directory";
Scene scene = new Scene(dataDir + "EmbeddedTexture.fbx");
//ExEnd: Load3DScene
```

## Paso 2: **Acceder a propiedades de material** del primer nodo

```csharp
//ExStart: AccessMaterialProperties
Material material = scene.RootNode.ChildNodes[0].Material;
PropertyCollection props = material.Properties;
//ExEnd: AccessMaterialProperties
```

## Paso 3: **Listar propiedades de material** – ver cada par nombre/valor

```csharp
//ExStart: ListAllProperties
foreach (var prop in props)
{
    Console.WriteLine("{0} = {1}", prop.Name, prop.Value);
}

//or using ordinal for loop
for (int i = 0; i < props.Count; i++)
{
    var prop = props[i];
    Console.WriteLine("{0} = {1}", prop.Name, prop.Value);
}
//ExEnd: ListAllProperties
```

## Paso 4: **Cómo cambiar el difuso** – modificar la propiedad Diffuse

```csharp
//ExStart: GetModifyPropertyByName
var diffuse = props["Diffuse"];
Console.WriteLine(diffuse);

//modify property value by name
props["Diffuse"] = new Vector3(1, 0, 1); // sets a magenta diffuse color
//ExEnd: GetModifyPropertyByName
```

## Paso 5: **Recuperar propiedad por nombre** – obtener una instancia fuertemente tipada

```csharp
//ExStart: GetPropertyInstanceByName
Property pdiffuse = props.FindProperty("Diffuse");
Console.WriteLine(pdiffuse);
//ExEnd: GetPropertyInstanceByName
```

## Paso 6: Recorrer las propias propiedades de una propiedad (avanzado)

```csharp
//ExStart: TraversePropertyProperties
Console.WriteLine("Property flags = {0}", pdiffuse.GetProperty("flags"));

//and some properties that only defined in FBX file:
Console.WriteLine("Label = {0}", pdiffuse.GetProperty("label"));
Console.WriteLine("Type Name = {0}", pdiffuse.GetProperty("typeName"));

//traversal on property's property is possible
foreach (var pp in pdiffuse.Properties)
{
    Console.WriteLine("Diffuse.{0} = {1}", pp.Name, pp.Value);
}
//ExEnd: TraversePropertyProperties
```

## Cómo **cambiar el color del material 3D** más allá del difuso
Si necesitas afectar los colores especular, ambiental o emisivo, simplemente reemplaza `"Diffuse"` por `"Specular"` o `"Ambient"` en la asignación `props["..."]` anterior. Se aplican las mismas estructuras `Vector3` o `Vector4`.

## Cómo **actualizar el color del material en C#**
Cambiar la apariencia visual de un material se reduce a actualizar la propiedad adecuada en el `PropertyCollection`. Ya sea que quieras modificar el difuso, especular o cualquier atributo de color personalizado, el patrón sigue siendo el mismo:

1. Recupera la propiedad por su nombre exacto (sensible a mayúsculas/minúsculas).  
2. Asigna un nuevo valor `Vector3` (RGB) o `Vector4` (RGBA).  

Debido a que la API trabaja directamente con objetos C#, puedes **actualizar el color del material C#** sin archivos intermedios ni convertidores. Esto lo hace perfecto para editores en tiempo real o pipelines de procesamiento por lotes.

## Problemas comunes y consejos
- **Sensibilidad a mayúsculas en el nombre de la propiedad** – las claves de propiedades de Aspose.3D distinguen mayúsculas/minúsculas; usa el nombre exacto que se muestra en la salida del listado.  
- **Propiedad ausente** – No todos los materiales exponen cada atributo PBR. Verifica `props.ContainsKey("Specular")` antes de acceder.  
- **Guardar cambios** – Después de modificar propiedades, llama a `scene.Save("output.fbx");` para persistir los cambios.

## Conclusión

Ahora sabes cómo **listar propiedades de material**, **recuperar una propiedad por nombre** y **cambiar el color difuso** (o cualquier otro atributo del material) usando Aspose.3D para .NET. Experimenta con diferentes tipos de propiedades para afinar el aspecto de tus activos 3D, y recuerda que puedes **actualizar el color del material C#** con una sola línea de código.

## Preguntas frecuentes

### P1: ¿Puedo usar Aspose.3D para .NET con otros formatos de archivo 3D?
A1: Sí, Aspose.3D soporta varios formatos de archivo 3D, incluyendo FBX, STL y muchos más.

### P2: ¿Cómo puedo obtener una licencia temporal para Aspose.3D para .NET?
A2: Visita [aquí](https://purchase.aspose.com/temporary-license/) para obtener una licencia temporal.

### P3: ¿Existe un foro comunitario para usuarios de Aspose.3D?
A3: Sí, puedes encontrar soporte y discusiones en el [foro de Aspose.3D](https://forum.aspose.com/c/3d/18).

### P4: ¿Dónde puedo encontrar documentación detallada para Aspose.3D para .NET?
A4: Consulta la [documentación](https://reference.aspose.com/3d/net/) para una guía completa.

### P5: ¿Puedo probar Aspose.3D para .NET gratis antes de comprar?
A5: ¡Claro! Descarga la [versión de prueba gratuita](https://releases.aspose.com/) para explorar sus funciones.

## Preguntas frecuentes

**P: ¿Qué representa `Vector3(1, 0, 1)`?**  
R: Establece el color difuso a magenta (rojo = 1, verde = 0, azul = 1) en espacio de color lineal.

**P: ¿Necesito llamar a `scene.Save` después de cambiar propiedades?**  
R: Sí, guardar la escena escribe tus modificaciones en disco; de lo contrario los cambios permanecen solo en memoria.

**P: ¿Puedo enumerar atributos FBX personalizados?**  
R: Por supuesto. El `PropertyCollection` incluirá cualquier atributo personalizado, al que puedes acceder mediante `GetProperty("customName")`.

**P: ¿Hay una forma de actualizar por lotes varios materiales?**  
R: Recorre `scene.RootNode.ChildNodes` y repite los pasos de modificación de propiedades para cada material.

**P: ¿Aspose.3D soporta .NET 6?**  
R: Sí, la biblioteca es totalmente compatible con .NET 6 y versiones posteriores.

**Última actualización:** 2026-03-28  
**Probado con:** Aspose.3D 24.11 for .NET  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}