---
date: 2026-02-22
description: Aprende a crear extrusión 3D con rebanadas usando Aspose.3D para Java.
  Esta guía paso a paso cubre la extrusión lineal, establecer el radio de redondeo
  y la exportación a OBJ.
linktitle: Create 3D Extrusion with Slices – Aspose.3D for Java
second_title: Aspose.3D Java API
title: Crear extrusión 3D con cortes – Aspose.3D para Java
url: /es/java/linear-extrusion/specifying-slices/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Crear extrusión 3D con rebanadas – Aspose.3D para Java

## Introducción

Si necesitas **crear extrusión 3d** objetos que se vean suaves y precisos, controlar el número de rebanadas es la clave. En este tutorial recorreremos cómo especificar rebanadas al realizar una extrusión lineal con Aspose.3D para Java. Verás por qué el recuento de rebanadas importa, cómo establecer un radio de redondeo y cómo exportar el resultado como un archivo OBJ que puede usarse en cualquier flujo de trabajo 3D.

## Respuestas rápidas
- **¿Qué controla “rebanadas”?** El número de secciones transversales intermedias usadas para aproximar la superficie de la extrusión.  
- **¿Qué método establece el recuento de rebanadas?** `LinearExtrusion.setSlices(int)`  
- **¿Puedo cambiar el radio de redondeo del perfil?** Sí, mediante `RectangleShape.setRoundingRadius(double)`  
- **¿Qué formato de archivo se usa en este ejemplo?** Wavefront OBJ (`FileFormat.WAVEFRONTOBJ`)  
- **¿Necesito una licencia para ejecutar el código?** Una prueba gratuita funciona para evaluación; se requiere una licencia comercial para producción.

## ¿Qué es una extrusión lineal con rebanadas?

La extrusión lineal toma un perfil 2‑D (como un rectángulo) y lo estira a lo largo de una línea recta para formar un sólido 3‑D. Al especificar **rebanadas**, le indicas a Aspose.3D cuántos pasos intermedios generar, lo que influye directamente en la suavidad de los bordes curvos, como un rectángulo redondeado.

## ¿Por qué usar Aspose.3D para Java para crear extrusión 3d?

* **Control total** – Puedes ajustar el recuento de rebanadas, el radio de redondeo y el formato de exportación de forma programática.  
* **Multiplataforma** – Funciona en cualquier entorno con Java sin dependencias nativas.  
* **Flexibilidad de exportación** – Guarda directamente en OBJ, FBX, STL y muchos otros formatos.

## Requisitos previos

1. **Java Development Kit** – JDK 8 o superior instalado.  
2. **Aspose.3D para Java** – Descarga la biblioteca desde el sitio oficial [aquí](https://releases.aspose.com/3d/java/).  
3. Un IDE o editor de texto de tu preferencia.

## Importar paquetes

Añade el espacio de nombres de Aspose.3D a tu proyecto para que puedas acceder a las clases de modelado 3‑D.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Guía paso a paso

### Paso 1: Configurar la escena y definir el perfil

Primero creamos un `RectangleShape` y le damos un **radio de redondeo** para que las esquinas sean suaves. Luego inicializamos una nueva `Scene` que contendrá toda la geometría.

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

### Paso 2: **Crear objetos nodo hijo** para cada extrusión

Cada pieza de geometría vive bajo un `Node`. Aquí generamos dos nodos hermanos – uno para una extrusión de baja rebanada y otro para una extrusión de alta rebanada – y movemos el nodo izquierdo un poco a un lado para que los resultados sean fáciles de comparar.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Paso 3: Realizar la extrusión lineal y **establecer rebanadas**

Ahora realmente **creamos objetos de extrusión 3d**. El constructor `LinearExtrusion` recibe el perfil y la profundidad de la extrusión. Usando una **clase interna anónima** llamamos a `setSlices` para controlar la suavidad. El nodo izquierdo obtiene solo 2 rebanadas (baja resolución), mientras que el nodo derecho obtiene 10 rebanadas (alta resolución).

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

### Paso 4: **Exportar OBJ** – guardar la escena

Finalmente escribimos la escena a un archivo Wavefront OBJ, un formato ampliamente soportado por editores 3‑D y motores de juego. Esto demuestra la capacidad **export obj java** de Aspose.3D.

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Problemas comunes y soluciones

| Problema | Por qué ocurre | Solución |
|----------|----------------|----------|
| **La extrusión parece plana** | El recuento de rebanadas está establecido en 1 o 0 | Asegúrate de que `setSlices` se llame con un valor ≥ 2. |
| **Las esquinas redondeadas se ven dentadas** | El radio de redondeo es demasiado pequeño respecto al recuento de rebanadas | Incrementa el radio o el recuento de rebanadas para curvas más suaves. |
| **Archivo no encontrado al guardar** | `MyDir` apunta a una carpeta inexistente | Crea el directorio previamente o usa una ruta absoluta. |

## Preguntas frecuentes

**P: ¿Cómo puedo descargar Aspose.3D para Java?**  
R: Puedes descargar la biblioteca [aquí](https://releases.aspose.com/3d/java/).

**P: ¿Dónde puedo encontrar la documentación de Aspose.3D?**  
R: Consulta la documentación [aquí](https://reference.aspose.com/3d/java/).

**P: ¿Hay una prueba gratuita disponible?**  
R: Sí, puedes explorar una prueba gratuita [aquí](https://releases.aspose.com/).

**P: ¿Cómo puedo obtener soporte para Aspose.3D?**  
R: Visita el foro de soporte [aquí](https://forum.aspose.com/c/3d/18).

**P: ¿Puedo comprar una licencia temporal?**  
R: Sí, una licencia temporal se puede obtener [aquí](https://purchase.aspose.com/temporary-license/).

---

**Última actualización:** 2026-02-22  
**Probado con:** Aspose.3D para Java 24.11 (última versión al momento de escribir)  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}