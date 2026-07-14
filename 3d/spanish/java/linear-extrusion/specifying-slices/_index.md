---
date: 2026-05-24
description: Aprenda cómo crear una extrusión 3D con cortes usando Aspose.3D for Java.
  Esta guía paso a paso cubre la extrusión lineal, establecer el radio de redondeo
  y la exportación a OBJ.
keywords:
- create 3d extrusion java
- Aspose 3D slices
- linear extrusion Java
linktitle: Crear extrusión 3D con cortes – Aspose.3D for Java
schemas:
- author: Aspose
  dateModified: '2026-05-24'
  description: Learn how to create 3d extrusion with slices using Aspose.3D for Java.
    This step‑by‑step guide covers linear extrusion, set rounding radius, and exporting
    OBJ.
  headline: Create 3D Extrusion with Slices – Aspose.3D for Java
  type: TechArticle
- description: Learn how to create 3d extrusion with slices using Aspose.3D for Java.
    This step‑by‑step guide covers linear extrusion, set rounding radius, and exporting
    OBJ.
  name: Create 3D Extrusion with Slices – Aspose.3D for Java
  steps:
  - name: Set up the scene and define the profile
    text: '`RectangleShape` is a class that defines a 2‑D rectangle profile. First
      we create a `RectangleShape` and give it a **rounding radius** so the corners
      are smooth. `Scene` is the root container for all nodes and geometry. Then we
      initialise a new `Scene` that will hold all geometry.'
  - name: Create child node objects for each extrusion
    text: '`Node` represents an element in the scene graph that can hold geometry
      and transformations. Every piece of geometry lives under a `Node`. Here we generate
      two sibling nodes – one for a low‑slice extrusion and another for a high‑slice
      extrusion – and move the left node a little to the side so the res'
  - name: Perform linear extrusion and set slices
    text: '`LinearExtrusion` is the class that creates a solid by sweeping a profile
      linearly. `LinearExtrusion` is Aspose.3D''s class that generates a solid by
      extruding a 2‑D profile along a straight line. Using an **anonymous inner class**
      we call `setSlices` to control the smoothness. The left node gets onl'
  - name: Export OBJ – save the scene
    text: Finally we write the scene to a Wavefront OBJ file, a format widely supported
      by 3‑D editors and game engines. This demonstrates the **export OBJ Java** capability
      of Aspose.3D.
  type: HowTo
- questions:
  - answer: You can download the library [here](https://releases.aspose.com/3d/java/).
    question: How can I download Aspose.3D for Java?
  - answer: Refer to the documentation [here](https://reference.aspose.com/3d/java/).
    question: Where can I find the documentation for Aspose.3D?
  - answer: Yes, you can explore a free trial [here](https://releases.aspose.com/).
    question: Is there a free trial available?
  - answer: Visit the support forum [here](https://forum.aspose.com/c/3d/18).
    question: How can I get support for Aspose.3D?
  - answer: Yes, a temporary license can be obtained [here](https://purchase.aspose.com/temporary-license/).
    question: Can I purchase a temporary license?
  type: FAQPage
second_title: Aspose.3D Java API
title: Crear extrusión 3D con cortes – Aspose.3D for Java
url: /es/java/linear-extrusion/specifying-slices/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Crear Extrusión 3D con Rebanadas – Aspose.3D para Java

## Introducción

Si necesitas **crear extrusión 3D** objetos que se vean suaves y precisos, controlar el número de rebanadas es la clave. En este tutorial recorreremos cómo especificar las rebanadas al realizar una extrusión lineal con Aspose.3D para Java. Verás por qué el recuento de rebanadas importa, cómo establecer un radio de redondeo y cómo exportar el resultado como un archivo OBJ que puede usarse en cualquier canal 3‑D.

## Respuestas Rápidas
- **¿Qué controla “slices”?** El número de secciones transversales intermedias usadas para aproximar la superficie de la extrusión.  
- **¿Qué método establece el recuento de rebanadas?** `LinearExtrusion.setSlices(int)`  
- **¿Puedo cambiar el radio de redondeo del perfil?** Sí, a través de `RectangleShape.setRoundingRadius(double)`  
- **¿Qué formato de archivo se usa en este ejemplo?** Wavefront OBJ (`FileFormat.WAVEFRONTOBJ`)  
- **¿Necesito una licencia para ejecutar el código?** Una prueba gratuita funciona para evaluación; se requiere una licencia comercial para producción.

`LinearExtrusion.setSlices(int)` establece cuántas rebanadas intermedias generará la extrusión.  
`RectangleShape.setRoundingRadius(double)` define el radio de esquina de un perfil rectangular.

## Cómo crear extrusión 3D en Java con rebanadas?

Carga tu perfil 2‑D, elige un recuento de rebanadas, establece el radio de redondeo y llama a `save` – todo el flujo de trabajo cabe en unas pocas líneas. Aspose.3D para Java maneja la creación de geometría, la interpolación de rebanadas y la exportación OBJ automáticamente, para que puedas enfocarte en la calidad visual en lugar de cálculos de malla de bajo nivel.

## Qué es una extrusión lineal con rebanadas?

Una extrusión lineal con rebanadas convierte una forma plana 2‑D en un sólido 3‑D al barrerla a lo largo de una línea recta mientras genera un número configurable de secciones transversales intermedias. El recuento de rebanadas influye directamente en cuán suavemente se renderizan los bordes curvos, como las esquinas redondeadas.

## Por qué usar Aspose.3D para Java para crear extrusión 3D?

Aspose.3D ofrece **control programático completo** sobre cada parámetro de extrusión, soporta **más de 50 formatos de entrada y salida** (incluidos OBJ, FBX, STL y GLTF), y puede procesar **modelos de cientos de páginas** sin cargar todo el archivo en memoria. Se ejecuta en cualquier plataforma con Java, no requiere DLLs nativas y garantiza resultados determinísticos en Windows, Linux y macOS.

## Requisitos Previos

1. **Java Development Kit** – JDK 8 o superior instalado.  
2. **Aspose.3D for Java** – Descarga la biblioteca desde el sitio oficial [aquí](https://releases.aspose.com/3d/java/).  
3. Un IDE o editor de texto de tu elección.

## Importar Paquetes

Agrega el espacio de nombres de Aspose.3D a tu proyecto para que puedas acceder a las clases de modelado 3‑D.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Guía Paso a Paso

### Paso 1: Configurar la escena y definir el perfil

`RectangleShape` es una clase que define un perfil rectangular 2‑D.  
Primero creamos un `RectangleShape` y le damos un **radio de redondeo** para que las esquinas sean suaves.  
`Scene` es el contenedor raíz para todos los nodos y la geometría.  
Luego inicializamos una nueva `Scene` que contendrá toda la geometría.

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

### Paso 2: Crear objetos nodo hijo para cada extrusión

`Node` representa un elemento en el grafo de escena que puede contener geometría y transformaciones.  
Cada pieza de geometría vive bajo un `Node`. Aquí generamos dos nodos hermanos – uno para una extrusión de baja cantidad de rebanadas y otro para una extrusión de alta cantidad de rebanadas – y movemos el nodo izquierdo un poco a un lado para que los resultados sean fáciles de comparar.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Paso 3: Realizar extrusión lineal y establecer rebanadas

`LinearExtrusion` es la clase que crea un sólido al barrer un perfil linealmente.  
`LinearExtrusion` es la clase de Aspose.3D que genera un sólido extruyendo un perfil 2‑D a lo largo de una línea recta. Usando una **clase interna anónima** llamamos a `setSlices` para controlar la suavidad. El nodo izquierdo recibe solo 2 rebanadas (bajo detalle), mientras que el nodo derecho recibe 10 rebanadas (suave).

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

### Paso 4: Exportar OBJ – guardar la escena

Finalmente escribimos la escena a un archivo Wavefront OBJ, un formato ampliamente soportado por editores 3‑D y motores de juego. Esto demuestra la capacidad de **exportar OBJ Java** de Aspose.3D.

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Problemas Comunes y Soluciones

| Problema | Por qué ocurre | Solución |
|----------|----------------|----------|
| **La extrusión parece plana** | Recuento de rebanadas establecido en 1 o 0 | Asegúrate de que `setSlices` se llame con un valor ≥ 2. |
| **Las esquinas redondeadas se ven dentadas** | Radio de redondeo demasiado pequeño en relación con el recuento de rebanadas | Aumenta el radio o el recuento de rebanadas para curvas más suaves. |
| **Archivo no encontrado al guardar** | `MyDir` apunta a una carpeta inexistente | Crea el directorio previamente o usa una ruta absoluta. |

## Preguntas Frecuentes

**Q: ¿Cómo puedo descargar Aspose.3D para Java?**  
A: Puedes descargar la biblioteca [aquí](https://releases.aspose.com/3d/java/).

**Q: ¿Dónde puedo encontrar la documentación de Aspose.3D?**  
A: Consulta la documentación [aquí](https://reference.aspose.com/3d/java/).

**Q: ¿Hay una prueba gratuita disponible?**  
A: Sí, puedes explorar una prueba gratuita [aquí](https://releases.aspose.com/).

**Q: ¿Cómo puedo obtener soporte para Aspose.3D?**  
A: Visita el foro de soporte [aquí](https://forum.aspose.com/c/3d/18).

**Q: ¿Puedo comprar una licencia temporal?**  
A: Sí, una licencia temporal se puede obtener [aquí](https://purchase.aspose.com/temporary-license/).

---

**Última actualización:** 2026-05-24  
**Probado con:** Aspose.3D for Java 24.11 (latest at time of writing)  
**Autor:** Aspose

## Tutoriales Relacionados

- [Crear Extrusión 3D Java con Aspose.3D](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [Cómo establecer la dirección en la extrusión lineal con Aspose.3D para Java](/3d/java/linear-extrusion/setting-direction/)
- [Crear escena 3D con torsión en la extrusión lineal – Aspose.3D para Java](/3d/java/linear-extrusion/applying-twist/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}