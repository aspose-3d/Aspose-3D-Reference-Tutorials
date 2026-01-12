---
date: 2026-01-12
description: Aprende cómo crear un cilindro de corte inferior y cómo exportar un modelo
  3D en formato OBJ usando Aspose.3D para .NET. Sigue esta guía paso a paso para dominar
  el modelado 3D.
linktitle: Customized Shear Bottom Cylinder
second_title: Aspose.3D .NET API
title: Cómo crear un cilindro con base de corte usando Aspose.3D para .NET
url: /es/net/3d-modeling/working-with-cylinder/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Cilindro con Base Cortada Personalizado

## Introducción
Bienvenido a nuestra guía completa donde **aprenderás a crear modelos de cilindro con base cortada** con Aspose.3D para .NET. Ya sea que estés creando un activo para un juego, una pieza mecánica o una demostración visual, este tutorial te muestra exactamente cómo dar forma a la base de un cilindro, aplicar un corte y, finalmente, **exportar el archivo OBJ del modelo 3D** para usarlo en cualquier flujo de trabajo posterior. Recorremos cada paso juntos, para que puedas comenzar a producir geometría personalizada en minutos.

## Respuestas rápidas
- **¿Qué es un cilindro con base cortada?** Un cilindro cuya cara inferior está inclinada (cortada) en lugar de plana.  
- **¿Qué biblioteca se utiliza?** Aspose.3D para .NET.  
- **¿Cómo exporto el modelo?** Usa `scene.Save(..., FileFormat.WavefrontOBJ)`.  
- **¿Necesito una licencia?** Hay una versión de prueba disponible; se requiere una licencia comercial para producción.  
- **¿Qué requisitos previos son necesarios?** Entorno de desarrollo .NET y el paquete NuGet Aspose.3D.

## ¿Qué es un cilindro con base cortada?
Un cilindro con base cortada es una malla cilíndrica estándar cuya cara inferior ha sido transformada mediante una operación de corte. Esto te permite crear bases anguladas, rampas o conectores personalizados sin editar manualmente los vértices.

## ¿Por qué usar Aspose.3D para esta tarea?
- **Control total** sobre los parámetros de la geometría (radio, altura, segmentos).  
- **Soporte integrado de corte** mediante la propiedad `ShearBottom`, lo que te evita manipulaciones de malla de bajo nivel.  
- **Exportación con un clic** a formatos populares como OBJ, FBX y STL, facilitando la integración con otras herramientas.

## Requisitos previos
Antes de comenzar, asegúrate de tener:

- Conocimientos básicos de C# y .NET.  
- Aspose.3D para .NET instalado. Puedes descargarlo **[aquí](https://releases.aspose.com/3d/net/)**.  
- Un IDE compatible con .NET (Visual Studio, Rider o VS Code).

## Importar espacios de nombres
En tu archivo C#, comienza importando los espacios de nombres necesarios:

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

## Paso 1: Crear una escena
Primero, instancia una nueva escena 3‑D que contendrá todos nuestros objetos.

```csharp
Scene scene = new Scene();
```

## Paso 2: Crear el Cilindro 1
Crea el cilindro principal que personalizaremos con una base cortada.

```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```

## Paso 3: Personalizar la base cortada para el Cilindro 1
Aplica el corte, habilita la generación de fan y ajusta otras propiedades para lograr la forma deseada.

```csharp
// Shear 47.5deg in the xy plane (z‑axis)
cylinder1.ShearBottom = new Vector2(0, 0.83); 

// Set GenerateFanCylinder to true
cylinder1.GenerateFanCylinder = true;
// Set ThetaLength
cylinder1.ThetaLength = MathUtils.ToRadian(270);

// Set OffsetTop
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```

## Paso 4: Añadir el Cilindro 1 a la escena
Coloca el cilindro personalizado en la escena y muévelo un poco a la derecha para poder ver ambos objetos lado a lado.

```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```

## Paso 5: Crear el Cilindro 2
Crea un segundo cilindro simple para comparación.

```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```

## Paso 6: Añadir el Cilindro 2 a la escena
Añade el segundo cilindro sin ningún corte personalizado; esto ayuda a ilustrar el efecto de los pasos anteriores.

```csharp
scene.RootNode.CreateChildNode(cylinder2);
```

## Paso 7: Guardar la escena
Finalmente, exporta toda la escena como un archivo OBJ para que puedas abrirlo en Blender, Maya o cualquier otro visor 3‑D.

```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```

## Problemas comunes y consejos
- **Valores de corte**: El `Vector2` recibe los factores de corte X y Y. Un valor de `0.83` corresponde aproximadamente a 47.5°, pero puedes ajustarlo para obtener diferentes ángulos.  
- **Ruta de exportación**: Asegúrate de que la carpeta que especificas exista y tengas permisos de escritura; de lo contrario `scene.Save` lanzará una excepción.  
- **Rendimiento**: Para cilindros con muchos segmentos, considera reducir el recuento de segmentos (`20` en el ejemplo) para mantener el tamaño del archivo OBJ manejable.

## Preguntas frecuentes

### ¿Es Aspose.3D para .NET adecuado para principiantes?
¡Absolutamente! Aspose.3D para .NET ofrece una API fácil de usar, lo que lo hace accesible tanto para principiantes como para desarrolladores experimentados.

### ¿Puedo aplicar diferentes ángulos de corte a los cilindros?
Sí, puedes personalizar la propiedad `ShearBottom` de cada cilindro individualmente, lo que te permite lograr efectos únicos.

### ¿Hay una versión de prueba disponible?
Sí, puedes explorar la versión de prueba gratuita **[aquí](https://releases.aspose.com/)**.

### ¿Dónde puedo encontrar soporte adicional?
Visita el **[foro de Aspose.3D](https://forum.aspose.com/c/3d/18)** para obtener soporte de la comunidad y participar en discusiones.

### ¿Cómo puedo obtener una licencia temporal?
Obtén tu licencia temporal **[aquí](https://purchase.aspose.com/temporary-license/)**.

**Preguntas y respuestas adicionales**

**P: ¿Cómo cambio el formato de exportación a FBX?**  
R: Reemplaza `FileFormat.WavefrontOBJ` por `FileFormat.FBX` en la llamada a `scene.Save`.

**P: ¿Puedo animar el cilindro después de exportarlo?**  
R: OBJ no soporta animación; usa FBX o GLTF si necesitas datos animados.

**P: ¿Qué hago si necesito un radio de cilindro mayor?**  
R: Ajusta los dos primeros parámetros del constructor `Cylinder` (por ejemplo, `new Cylinder(4, 4, …)`).

## Conclusión
Ahora dominas cómo **crear modelos de cilindro con base cortada** y exportarlos como archivos OBJ usando Aspose.3D para .NET. Experimenta con diferentes valores de corte, recuentos de segmentos y formatos de exportación para adaptarlos a las necesidades de tu proyecto. ¡Feliz modelado!

---

**Última actualización:** 2026-01-12  
**Probado con:** Aspose.3D para .NET 24.11 (última versión al momento de escribir)  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}