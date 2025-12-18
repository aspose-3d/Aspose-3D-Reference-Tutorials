---
date: 2025-12-18
description: Aprende a crear una escena 3D y guardar un archivo OBJ usando Aspose.3D
  para Java. Sigue nuestra guía paso a paso para la dirección de extrusión lineal.
linktitle: Setting Direction in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Crear escena 3D – Establecer dirección de extrusión Aspose.3D Java
url: /es/java/linear-extrusion/setting-direction/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Crear escena 3D – Establecer dirección de extrusión Aspose.3D Java

## Introducción

En este tutorial aprenderá **cómo crear escena 3d** objetos y controlar la dirección de extrusión con Aspose.3D para Java. Ya sea que esté creando visualizaciones arquitectónicas, prototipos de productos o recursos para juegos, dominar la extrusión lineal le brinda la flexibilidad para modelar formas complejas rápidamente. Recorreremos cada paso, desde agregar nodos en Java hasta **exportar modelo 3d obj** archivos, para que pueda ver el resultado al instante.

## Respuestas rápidas
- **¿Qué significa “crear escena 3d”?** Significa inicializar un objeto `Scene` de Aspose.3D que contendrá toda la geometría, luces y cámaras.  
- **¿Cómo establezco la dirección de extrusión?** Use el método `setDirection(Vector3)` en una instancia de `LinearExtrusion`.  
- **¿Qué formato debo usar para exportar?** El formato OBJ (`FileFormat.WAVEFRONTOBJ`) es ampliamente compatible para flujos de trabajo 3‑D.  
- **¿Necesito una licencia para Aspose.3D?** Una prueba gratuita funciona para desarrollo; se requiere una licencia comercial para producción.  
- **¿Puedo agregar más nodos en Java?** Sí—use `scene.getRootNode().createChildNode()` para agregar tantos objetos como necesite.

## ¿Qué es un flujo de trabajo de “crear escena 3d”?

Un flujo de trabajo de **crear escena 3d** comienza con un objeto `Scene` vacío, agrega geometría (como perfiles extruidos), lo posiciona con transformaciones y finalmente guarda la escena en un formato de archivo como OBJ. Este patrón es la columna vertebral de la mayoría de aplicaciones 3‑D construidas con Aspose.3D.

## ¿Por qué establecer la dirección de extrusión?

Establecer la dirección de extrusión le permite inclinar, rotar o sesgar la forma mientras se extruye, dándole control sobre la geometría final sin procesamiento posterior adicional. Es especialmente útil para:

- Crear columnas cónicas o tuberías de forma personalizada.  
- Alinear extrusiones con ejes no estándar en piezas mecánicas.  
- Generar formas artísticas para efectos visuales.

## Requisitos previos

- Conocimientos básicos de Java.  
- Biblioteca Aspose.3D instalada – descárguela desde [here](https://releases.aspose.com/3d/java/).  
- Un IDE como Eclipse o IntelliJ IDEA.

## Importar paquetes

Primero, importe las clases de Aspose.3D requeridas:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Paso 1: Inicializar perfil base

Cree el perfil 2‑D que será extruido. En este ejemplo usamos un rectángulo con esquinas redondeadas:

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

> **Consejo profesional:** Ajuste el radio de redondeo para controlar cuán afiladas o suaves aparecen las esquinas del rectángulo antes de la extrusión.

## Paso 2: Crear una escena

Ahora **creamos escena 3d** que alojará nuestros objetos:

```java
Scene scene = new Scene();
```

## Paso 3: Agregar nodos Java – Posicionar los objetos

Agregaremos dos nodos hijos (izquierdo y derecho) al nodo raíz de la escena y moveremos el izquierdo un poco a un lado:

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Paso 4: Cómo extruir – Nodo izquierdo (dirección predeterminada)

Extruya el perfil en el nodo izquierdo usando la dirección predeterminada del eje Z. También establecemos una torsión completa de 360° y aumentamos el recuento de segmentos para mayor suavidad:

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Paso 5: Cómo establecer dirección – Nodo derecho

Aquí **cómo establecer dirección** proporcionando un `Vector3` personalizado. Esto inclina la extrusión hacia el vector (0.3, 0.2, 1):

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Paso 6: Guardar archivo OBJ – Exportar modelo 3D

Finalmente, **guardamos archivo obj** para ver el resultado en cualquier visor 3‑D:

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

Al abrir el archivo OBJ generado, verá dos rectángulos extruidos: uno con la dirección predeterminada y otro inclinado según el vector que establecimos.

## Problemas comunes y soluciones

| Problema | Razón | Solución |
|----------|-------|----------|
| El archivo OBJ aparece vacío | Escena no guardada o ruta incorrecta | Verifique que `MyDir` apunte a una carpeta con permisos de escritura y que el nombre del archivo termine con `.obj`. |
| La extrusión parece plana | `setSlices` demasiado bajo | Aumente `setSlices` (p.ej., 200) para una geometría más suave. |
| La dirección parece sin cambios | Vector no normalizado | Use un `Vector3` normalizado o ajuste los valores para reflejar la inclinación deseada. |

## Preguntas frecuentes

### P1: ¿Puedo usar Aspose.3D con otros lenguajes de programación?
A1: Aspose.3D admite varios lenguajes, incluidos .NET y Java.

### P2: ¿Hay una prueba gratuita disponible para Aspose.3D?
A2: Sí, puede explorar las funciones de Aspose.3D con una prueba gratuita [here](https://releases.aspose.com/).

### P3: ¿Dónde puedo encontrar documentación detallada para Aspose.3D para Java?
A3: La documentación completa está disponible [here](https://reference.aspose.com/3d/java/).

### P4: ¿Cómo puedo obtener soporte para Aspose.3D?
A4: Visite el [foro de Aspose.3D](https://forum.aspose.com/c/3d/18) para cualquier ayuda o consulta.

### P5: ¿Hay licencias temporales disponibles para Aspose.3D?
A5: Sí, puede obtener una licencia temporal [here](https://purchase.aspose.com/temporary-license/).

**Última actualización:** 2025-12-18  
**Probado con:** Aspose.3D 24.11 para Java  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}