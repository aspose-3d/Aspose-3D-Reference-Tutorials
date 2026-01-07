---
date: 2026-01-07
description: Aprende a agregar un plano de referencia mientras realizas una extrusión
  lineal con Aspose.3D para .NET y exportas archivos Wavefront OBJ. Domina las técnicas
  de centrado y puesta a tierra en el modelado 3‑D.
linktitle: Add Ground Plane and Center in Linear Extrusion
second_title: Aspose.3D .NET API
title: Añadir plano de base y centro en extrusión lineal
url: /es/net/3d-modeling/linear-extrusion/center-in-linear-extrusion/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Agregar plano base y centrar en extrusión lineal

## Introducción

Bienvenido a esta guía completa para dominar la extrusión lineal usando Aspose.3D para .NET. Si deseas **agregar un plano base** a tus modelos y **exportar archivos Wavefront OBJ** manteniendo la extrusión centrada, estás en el lugar correcto. En este tutorial profundizaremos en la técnica de extrusión lineal, enfocándonos específicamente en el aspecto del centrado y en cómo un plano base te ayuda a visualizar el resultado con mayor claridad.

## Respuestas rápidas
- **¿Qué logra “agregar plano base”?** Proporciona una referencia visual que facilita ver dónde se sitúa la extrusión en el plano X‑Z.  
- **¿Qué formato se usa para exportar el modelo?** La escena se guarda como un archivo Wavefront OBJ (`FileFormat.WavefrontOBJ`).  
- **¿Necesito una licencia para ejecutar el código?** Una prueba gratuita funciona para desarrollo; se requiere una licencia permanente para producción.  
- **¿Puedo cambiar la longitud de la extrusión?** Sí – modifica el segundo parámetro de `LinearExtrusion`.  
- **¿El centrado es opcional?** Establecer `Center = true` centra la extrusión alrededor del perfil; `false` la alinea a un lado.

## Requisitos previos

Antes de embarcarnos en este emocionante viaje, asegúrate de contar con los siguientes requisitos:

- Comprensión básica del lenguaje de programación C#.  
- Visual Studio instalado en tu máquina.  
- Biblioteca Aspose.3D para .NET, que puedes descargar desde la [Documentación de Aspose.3D .NET](https://reference.aspose.com/3d/net/).  
- Asegúrate de tener acceso a la [Documentación de Aspose.3D .NET](https://reference.aspose.com/3d/net/) para referencia a lo largo del tutorial.

## Importar espacios de nombres

Para comenzar, importemos los espacios de nombres necesarios. Estos sentarán las bases de nuestra obra maestra de modelado 3D.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Paso 1: Inicializar el perfil base

Comenzamos definiendo un perfil rectangular que será extruido. `RoundingRadius` agrega un sutil filete a las esquinas.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## Paso 2: Crear una escena 3D

Un objeto `Scene` actúa como contenedor de toda la geometría, luces y cámaras.

```csharp
Scene scene = new Scene();
```

## Paso 3: Crear nodos izquierdo y derecho

Se crean dos nodos hermanos bajo la raíz. Uno demostrará la extrusión **sin** centrado, el otro **con** centrado. También trasladamos el nodo izquierdo para que los dos ejemplos no se superpongan.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(5, 0, 0);
```

## Paso 4: Realizar extrusión lineal en el nodo izquierdo (Sin centro)

Aquí extruimos el perfil sin centrado. Observa la bandera `Center = false`.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 2) { Center = false, Slices = 3 });
```

## Paso 5: Agregar plano base como referencia (Nodo izquierdo)

Agregar una caja delgada actúa como **plano base** para que puedas ver claramente cómo la extrusión se asienta sobre la base.

```csharp
left.CreateChildNode(new Box(0.01, 3, 3));
```

## Paso 6: Realizar extrusión lineal en el nodo derecho (Con centro)

Ahora extruimos el mismo perfil pero habilitando el centrado. La geometría se colocará de forma simétrica alrededor del origen del perfil.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 2) { Center = true, Slices = 3 });
```

## Paso 7: Agregar plano base como referencia (Nodo derecho)

Se agrega un segundo plano base al nodo derecho para mantener la comparación visual consistente.

```csharp
right.CreateChildNode(new Box(0.01, 3, 3));
```

## Paso 8: Exportar archivo Wavefront OBJ

Finalmente, **exportamos Wavefront OBJ** para que el resultado pueda abrirse en cualquier visor 3‑D estándar.

```csharp
scene.Save("Your Output Directory" + "CenterInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## ¿Por qué agregar un plano base?

Agregar un plano base te brinda una pista visual inmediata sobre la altura y alineación de la extrusión. Es especialmente útil cuando necesitas comparar resultados centrados vs. no centrados, como se muestra en este tutorial.

## Problemas comunes y consejos

- **Plano base no visible:** Asegúrate de que el grosor del plano (`0.01` en el constructor `Box`) sea lo suficientemente pequeño como para no ocultar la extrusión, pero lo suficientemente grande para ser renderizado.  
- **Exportación falla:** Verifica que el directorio de salida exista y que tengas permisos de escritura.  
- **Extrusión centrada aparece desplazada:** Revisa la propiedad `Center`; `true` centra el perfil, `false` lo alinea a un lado.

## Preguntas frecuentes

### Q1: ¿Puedo usar Aspose.3D para .NET con otros lenguajes de programación?

A1: Aspose.3D soporta principalmente lenguajes .NET como C# y VB.NET.

### Q2: ¿Dónde puedo encontrar soporte para consultas relacionadas con Aspose.3D?

A2: Visita el [Foro de Aspose.3D](https://forum.aspose.com/c/3d/18) para soporte dedicado y discusiones.

### Q3: ¿Hay una prueba gratuita disponible para Aspose.3D para .NET?

A3: Sí, puedes acceder a la prueba gratuita [aquí](https://releases.aspose.com/).

### Q4: ¿Cómo puedo obtener una licencia temporal para Aspose.3D para .NET?

A4: Puedes adquirir una licencia temporal [aquí](https://purchase.aspose.com/temporary-license/).

### Q5: ¿Dónde puedo comprar la licencia de Aspose.3D para .NET?

A5: Compra tu licencia [aquí](https://purchase.aspose.com/buy).

### Q6: ¿Puedo exportar la escena a otros formatos además de OBJ?

A6: Sí, Aspose.3D soporta muchos formatos como STL, FBX y GLTF. Simplemente cambia el valor del enum `FileFormat` en el método `Save`.

### Q7: ¿Cómo cambio el número de segmentos de la extrusión?

A7: Ajusta la propiedad `Slices` en el constructor de `LinearExtrusion` para controlar la densidad de la malla.

---

**Última actualización:** 2026-01-07  
**Probado con:** Aspose.3D para .NET última versión  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}