---
date: 2026-03-26
description: Aprende a crear un cilindro y exportar un archivo OBJ usando Aspose.3D
  para .NET. Esta guía para principiantes cubre la configuración de la escena 3D y
  la exportación a OBJ.
linktitle: Customized Shear Bottom Cylinder
second_title: Aspose.3D .NET API
title: Cómo crear un cilindro con base sesgada – Aspose.3D para .NET
url: /es/net/3d-modeling/working-with-cylinder/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Cómo crear un cilindro con base sesgada – Aspose.3D para .NET

## Introducción
Si te preguntas **cómo crear cilindro** objetos con una base sesgada personalizada en un entorno .NET, has llegado al lugar correcto. En este tutorial recorreremos cada paso—from setting up a 3‑D scene to exporting the final model as an OBJ file—para que puedas mejorar tus *habilidades de modelado 3D para principiantes* usando **Aspose.3D for .NET**.

## Respuestas rápidas
- **¿Cuál es la clase principal para iniciar un modelo 3D?** `Scene` crea el contenedor raíz para toda la geometría.  
- **¿Qué método exporta el modelo a OBJ?** `scene.Save(..., FileFormat.WavefrontOBJ)`.  
- **¿Necesito una licencia para pruebas?** Hay una prueba gratuita disponible — consulta el enlace de prueba en las Preguntas frecuentes.  
- **¿Puedo cambiar el ángulo de sesgo?** Sí, modifica `ShearBottom` con un valor `Vector2`.  
- **¿Es adecuado para principiantes?** Absolutamente; la API abstrae el manejo de mallas de bajo nivel.

## ¿Qué es una escena 3D?
Una *escena 3D* es un contenedor jerárquico que contiene todas las entidades geométricas, luces, cámaras y transformaciones. En Aspose.3D la clase `Scene` proporciona una forma limpia de organizar y luego exportar tus modelos.

## ¿Por qué exportar OBJ?
OBJ es un formato basado en texto, ampliamente compatible, que muchas aplicaciones 3‑D (Blender, Maya, Unity) pueden importar. Exportar a OBJ te permite compartir o editar más tus modelos de cilindro fuera de .NET.

## Requisitos previos
Antes de sumergirnos, asegúrate de tener:

- Conocimientos básicos de C# y desarrollo .NET.  
- **Aspose.3D for .NET** instalado – puedes descargarlo **[aquí](https://releases.aspose.com/3d/net/)**.  
- Un IDE .NET (Visual Studio, Rider o VS Code) listo para programar.

## Importar espacios de nombres
Primero, trae los espacios de nombres requeridos al alcance para que los tipos de la API sean reconocidos.

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

## Paso 1: Crear una escena 3D
El objeto `Scene` actúa como la raíz de la jerarquía de tu modelo.

```csharp
Scene scene = new Scene();
```

## Paso 2: Crear Cylinder 1
Generamos el primer cilindro con un radio de 2, altura 10 y 20 segmentos radiales.

```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```

## Paso 3: Personalizar Shear Bottom para Cylinder 1
Aplicamos una transformación de sesgo, habilitamos la generación de cilindro‑fan, y ajustamos otras propiedades para lograr la forma deseada.

```csharp
// Shear 47.5deg in the xy plane (z-axis)
cylinder1.ShearBottom = new Vector2(0, 0.83); 

// Set GenerateFanCylinder to true
cylinder1.GenerateFanCylinder = true;
// Set ThetaLength
cylinder1.ThetaLength = MathUtils.ToRadian(270);

// Set OffsetTop
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```

## Paso 4: Añadir Cylinder 1 a la escena
Colocamos el primer cilindro en una ubicación conveniente usando una transformación de traslación.

```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```

## Paso 5: Crear Cylinder 2
Se crea un segundo cilindro con las mismas dimensiones base pero sin sesgo personalizado—perfecto para una comparación lado a lado.

```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```

## Paso 6: Añadir Cylinder 2 a la escena
Simplemente adjuntamos el segundo cilindro al grafo de la escena.

```csharp
scene.RootNode.CreateChildNode(cylinder2);
```

## Paso 7: Exportar la escena como archivo OBJ
Finalmente, guardamos toda la escena en un archivo OBJ para que pueda abrirse en cualquier visor 3‑D estándar.

```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```

## Problemas comunes y soluciones
| Problema | Por qué ocurre | Solución |
|----------|----------------|----------|
| **El archivo OBJ está vacío** | La escena no tiene geometría adjunta. | Asegúrate de que ambos cilindros se añadan a `scene.RootNode`. |
| **El sesgo se ve incorrecto** | `ShearBottom` espera la tangente del ángulo. | Usa `Math.Tan(angleInRadians)` o el valor `0.83` proporcionado para ~47.5°. |
| **Errores de ruta de archivo** | Directorio inválido o ausente. | Usa `Path.Combine(Environment.CurrentDirectory, "CustomizedShearBottomCylinder.obj")`. |

## Preguntas frecuentes
### ¿Aspose.3D for .NET es adecuado para principiantes?
¡Absolutamente! Aspose.3D for .NET ofrece una API de alto nivel que abstrae las partes matemáticas intensivas del modelado 3‑D, haciéndola accesible para desarrolladores de cualquier nivel de habilidad.

### ¿Puedo aplicar diferentes ángulos de sesgo a los cilindros?
Sí, cada instancia de `Cylinder` tiene su propia propiedad `ShearBottom`, por lo que puedes asignar un ángulo único a cada objeto.

### ¿Hay una versión de prueba disponible?
Sí, puedes explorar la versión de prueba gratuita **[aquí](https://releases.aspose.com/)**.

### ¿Dónde puedo encontrar soporte adicional?
Visita el **[foro de Aspose.3D](https://forum.aspose.com/c/3d/18)** para obtener ayuda de la comunidad, ejemplos de código y discusión.

### ¿Cómo puedo obtener una licencia temporal?
Obtén tu licencia temporal **[aquí](https://purchase.aspose.com/temporary-license/)**.

**Preguntas y respuestas adicionales**

**P: ¿Cómo exporto el modelo en un formato diferente, como STL?**  
R: Reemplaza `FileFormat.WavefrontOBJ` por `FileFormat.STL` en la llamada a `scene.Save`.

**P: ¿Puedo animar los cilindros después de crearlos?**  
R: Sí, puedes añadir animaciones de fotogramas clave a las transformaciones de nodos usando las clases `Animation` proporcionadas por Aspose.3D.

**P: ¿La API es compatible con .NET Core?**  
R: La biblioteca es totalmente compatible con .NET Core, .NET 5+ y .NET 6+.

---

**Última actualización:** 2026-03-26  
**Probado con:** Aspose.3D for .NET (última versión)  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}