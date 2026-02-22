---
date: 2026-02-22
description: Aprende a establecer la dirección en la extrusión lineal y a exportar
  modelos 3D en formato OBJ usando Aspose.3D para Java. Sigue nuestra guía paso a
  paso.
linktitle: Setting Direction in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Cómo establecer la dirección en la extrusión lineal con Aspose.3D para Java
url: /es/java/linear-extrusion/setting-direction/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Cómo establecer la dirección en una extrusión lineal con Aspose.3D para Java

## Introducción

En este tutorial completo descubrirás **cómo establecer la dirección** al realizar una extrusión lineal con Aspose.3D para Java. Ya sea que estés construyendo una herramienta tipo CAD o generando geometría para un motor de juego, controlar la dirección de la extrusión te permite crear exactamente la forma que necesitas. Recorreremos cada paso, desde inicializar un perfil hasta guardar el resultado como un archivo OBJ, para que también puedas **exportar archivos de modelo 3d obj** directamente desde Java.

## Respuestas rápidas
- **¿Cuál es la clase principal para la extrusión lineal?** `LinearExtrusion`
- **¿Qué método define la dirección de la extrusión?** `setDirection(Vector3 direction)`
- **¿Puedo exportar el resultado como OBJ?** Sí, usando `scene.save(..., FileFormat.WAVEFRONTOBJ)`
- **¿Necesito una licencia para el desarrollo?** Está disponible una prueba gratuita; se requiere una licencia para producción.
- **¿Qué IDE de Java funciona mejor?** IntelliJ IDEA o Eclipse son ambos totalmente compatibles.

## ¿Qué es la extrusión lineal?

La extrusión lineal toma un perfil 2‑D (como un rectángulo o círculo) y lo extiende a lo largo de una línea recta para crear un sólido 3‑D. Por defecto, la extrusión sigue el eje Z positivo, pero Aspose.3D te permite cambiar esa trayectoria con la propiedad `setDirection`.

## ¿Por qué establecer la dirección en la extrusión lineal?

Establecer una dirección personalizada es útil cuando:
- Alineas la geometría con objetos existentes en una escena.
- Creas piezas inclinadas o anguladas sin pasos de transformación adicionales.
- Exportas modelos que deben coincidir con un sistema de coordenadas específico (p. ej., para impresión 3‑D o motores de juego).

## Requisitos previos

Antes de comenzar, asegúrate de tener:

- Conocimientos básicos de Java.
- Biblioteca Aspose.3D instalada. Puedes descargarla desde [aquí](https://releases.aspose.com/3d/java/).
- Un IDE como Eclipse o IntelliJ IDEA.

## Importar paquetes

Primero, importa los espacios de nombres que proporcionan las clases 3‑D principales y los tipos de utilidad.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Paso 1: Inicializar el perfil base

Crea la forma que será extruida. En este ejemplo usamos un `RectangleShape` con un pequeño radio de redondeo para dar a los bordes un aspecto suave.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Paso 2: Crear una escena

Un objeto `Scene` actúa como contenedor de todos los nodos 3‑D, luces, cámaras y materiales.

```java
Scene scene = new Scene();
```

## Paso 3: Crear nodos

Agrega dos nodos hijos a la raíz de la escena: uno para la extrusión izquierda y otro para la extrusión derecha. El nodo derecho se traslada para que los dos objetos no se superpongan.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Paso 4: Realizar la extrusión lineal en el nodo izquierdo

Extruye el perfil en el nodo izquierdo usando la dirección predeterminada del eje Z. También añadimos una torsión completa de 360° y aumentamos el recuento de segmentos para una malla más suave.

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Paso 5: Realizar la extrusión lineal en el nodo derecho con dirección

Aquí es donde **establecemos la dirección**. Al pasar un `Vector3` personalizado a `setDirection`, la extrusión sigue el vector (0.3, 0.2, 1), produciendo una forma inclinada.

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Paso 6: Guardar la escena 3D

Finalmente, exporta la escena al formato Wavefront OBJ. Este paso demuestra cómo **guardar archivos obj java** y facilita la visualización del resultado en cualquier visor 3‑D.

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Problemas comunes y soluciones

| Problema | Por qué ocurre | Solución |
|----------|----------------|----------|
| El archivo OBJ aparece vacío | El perfil no se añadió a un nodo | Asegúrate de que `createChildNode` se llame en un nodo válido |
| La dirección parece sin cambios | `setDirection` se llamó después de que la extrusión ya estaba construida | Establece la dirección dentro del inicializador de `LinearExtrusion` como se muestra |
| Malla de baja resolución | El valor de `setSlices` es demasiado bajo | Incrementa el recuento de segmentos (p. ej., 100 o más) |

## Conclusión

Ahora sabes **cómo establecer la dirección** en una extrusión lineal, cómo ajustar la torsión y los parámetros de segmentos, y cómo **exportar archivos de modelo 3d obj** usando Aspose.3D para Java. Estas técnicas te brindan un control detallado sobre la creación de geometría y facilitan la integración de activos 3‑D en flujos de trabajo más amplios.

## Preguntas frecuentes

### Q1: ¿Puedo usar Aspose.3D con otros lenguajes de programación?

A1: Aspose.3D soporta varios lenguajes de programación, incluidos .NET y Java.

### Q2: ¿Hay una prueba gratuita disponible para Aspose.3D?

A2: Sí, puedes explorar las funciones de Aspose.3D con una prueba gratuita [aquí](https://releases.aspose.com/).

### Q3: ¿Dónde puedo encontrar documentación detallada para Aspose.3D para Java?

A3: La documentación completa está disponible [aquí](https://reference.aspose.com/3d/java/).

### Q4: ¿Cómo puedo obtener soporte para Aspose.3D?

A4: Visita el [foro de Aspose.3D](https://forum.aspose.com/c/3d/18) para cualquier ayuda o consulta.

### Q5: ¿Están disponibles licencias temporales para Aspose.3D?

A5: Sí, puedes obtener una licencia temporal [aquí](https://purchase.aspose.com/temporary-license/).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Última actualización:** 2026-02-22  
**Probado con:** Aspose.3D for Java (última versión)  
**Autor:** Aspose