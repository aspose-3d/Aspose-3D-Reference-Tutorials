---
date: 2026-08-02
description: Aprenda cómo cambiar la dirección de extrusión en extrusión lineal y
  exportar archivos OBJ usando Aspose.3D para Java. Siga nuestra guía paso a paso.
keywords:
- change extrusion direction
- export obj file java
- Aspose.3D Java
lastmod: 2026-08-02
linktitle: Cambiar la dirección de extrusión – Aspose.3D Java
og_description: Cambie la dirección de extrusión en extrusión lineal con Aspose.3D
  para Java y exporte archivos OBJ. Esta guía muestra código paso a paso y consejos
  para desarrolladores.
og_image_alt: Guide showing how to change extrusion direction and export OBJ using
  Aspose.3D Java
og_title: Cambiar la dirección de extrusión – Tutorial de Aspose.3D Java
schemas:
- author: Aspose
  dateModified: '2026-08-02'
  description: Learn how to change extrusion direction in linear extrusion and export
    OBJ files using Aspose.3D for Java. Follow our step‑by‑step guide.
  headline: Change Extrusion Direction in 3D Models – Aspose.3D Java
  type: TechArticle
- questions:
  - answer: '`LinearExtrusion`'
    question: What class performs linear extrusion?
  - answer: '`setDirection(Vector3 direction)`'
    question: Which method sets the extrusion vector?
  - answer: Yes—use `scene.save(..., FileFormat.WAVEFRONTOBJ)`
    question: Can the result be saved as OBJ?
  - answer: A free trial is available; a license is mandatory for commercial use.
    question: Is a license required for production?
  - answer: IntelliJ IDEA and Eclipse are fully supported.
    question: Which IDE works best with Aspose.3D?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- change extrusion direction
- Aspose.3D
- Java 3D modeling
- export OBJ
title: Cambiar la dirección de extrusión en modelos 3D – Aspose.3D Java
url: /es/java/linear-extrusion/setting-direction/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Cambiar la dirección de extrusión en modelos 3D – Aspose.3D Java

## Introducción

En este tutorial exhaustivo descubrirás **cómo cambiar la dirección de extrusión** al realizar una extrusión lineal con Aspose.3D para Java. Ya sea que estés construyendo una herramienta tipo CAD, preparando recursos para un motor de juego, o generando piezas para impresión 3‑D, controlar la dirección de extrusión te permite crear exactamente la forma que necesitas. Repasaremos cada paso, desde inicializar un perfil hasta guardar el resultado como un archivo OBJ, para que también puedas **exportar archivos OBJ de modelo 3D** directamente desde Java.

## Respuestas rápidas
- **¿Qué clase realiza la extrusión lineal?** `LinearExtrusion`
- **¿Qué método establece el vector de extrusión?** `setDirection(Vector3 direction)`
- **¿Se puede guardar el resultado como OBJ?** Sí—use `scene.save(..., FileFormat.WAVEFRONTOBJ)`
- **¿Se requiere una licencia para producción?** Hay una prueba gratuita disponible; una licencia es obligatoria para uso comercial.
- **¿Qué IDE funciona mejor con Aspose.3D?** IntelliJ IDEA y Eclipse son totalmente compatibles.

## ¿Qué es la extrusión lineal?

La extrusión lineal es el proceso de extender un boceto 2‑D (como un rectángulo o círculo) a lo largo de una línea recta para generar un sólido 3‑D. Por defecto, la extrusión sigue el eje Z positivo, pero Aspose.3D te permite cambiar esa trayectoria con la propiedad `setDirection`, dándote control total sobre la geometría final.

## ¿Por qué cambiar la dirección de extrusión en la extrusión lineal?

Cambiar la dirección de extrusión te permite alinear la nueva geometría con objetos existentes, crear componentes angulados sin transformaciones adicionales y generar modelos que coincidan con el sistema de coordenadas requerido por las canalizaciones posteriores (p. ej., impresoras 3‑D o motores de juego). Esto elimina la necesidad de pasos de post‑procesamiento y reduce la sobrecarga del tamaño de archivo hasta un 15 % al usar vectores direccionales que evitan rotaciones innecesarias.

## Requisitos previos

- Conocimientos básicos de Java.
- Biblioteca Aspose.3D instalada. Puedes descargarla desde [aquí](https://releases.aspose.com/3d/java/). También puedes explorar todas las versiones de Aspose en la página principal [aquí](https://releases.aspose.com/).
- Un IDE como Eclipse o IntelliJ IDEA.

## Importar paquetes

El espacio de nombres `com.aspose.threed` proporciona las clases 3‑D centrales y los tipos de utilidad.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Paso 1: Inicializar el perfil base

La clase `RectangleShape` crea el perfil 2‑D que será extruido. Un pequeño radio de redondeo da a los bordes un aspecto suave.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Paso 2: Crear una escena

La clase `Scene` es el contenedor de nivel superior de Aspose.3D que contiene todos los nodos 3‑D, luces, cámaras y materiales.

```java
Scene scene = new Scene();
```

## Paso 3: Crear nodos

Un `Node` representa un objeto en el grafo de la escena, permitiéndote adjuntar geometría, transformaciones y otras propiedades.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Paso 4: Realizar extrusión lineal en el nodo izquierdo

`LinearExtrusion` realiza la operación de extrusión, convirtiendo un perfil 2‑D en una malla 3‑D.

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Paso 5: Realizar extrusión lineal en el nodo derecho con dirección

Aquí **cambiamos la dirección de extrusión**. Al pasar un `Vector3` personalizado a `setDirection`, la extrusión sigue el vector (0.3, 0.2, 1), produciendo una forma inclinada que se alinea con el sistema de coordenadas de la escena.

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Paso 6: Guardar la escena 3D

El método `save` escribe la escena en un archivo con el formato especificado.

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Problemas comunes y soluciones

| Problema | Por qué ocurre | Solución |
|----------|----------------|----------|
| El archivo OBJ aparece vacío | El perfil no se añadió a un nodo | Asegúrate de que `createChildNode` se llame en un nodo válido |
| La dirección parece sin cambios | `setDirection` se llamó después de que la extrusión ya estaba construida | Establece la dirección dentro del inicializador de `LinearExtrusion` como se muestra |
| Malla de baja resolución | El valor de `setSlices` es demasiado bajo | Incrementa el número de cortes (por ejemplo, 100 o más) |

## Conclusión

Ahora sabes **cómo cambiar la dirección de extrusión** en una extrusión lineal, cómo ajustar la torsión y los parámetros de cortes, y cómo **exportar archivos OBJ de modelo 3D** usando Aspose.3D para Java. Estas técnicas te brindan un control granular sobre la creación de geometría y facilitan la integración de recursos 3‑D en canalizaciones más grandes.

## Preguntas frecuentes

**P:** ¿Puedo usar Aspose.3D con otros lenguajes de programación?  
**R:** Sí—Aspose.3D proporciona APIs para .NET y Java, permitiendo desarrollo multiplataforma.

**P:** ¿Hay una prueba gratuita disponible para Aspose.3D?  
**R:** Por supuesto. Puedes explorar el conjunto completo de funciones con una prueba gratuita [aquí](https://releases.aspose.com/).

**P:** ¿Dónde puedo encontrar documentación detallada para Aspose.3D para Java?  
**R:** La referencia completa está disponible [aquí](https://reference.aspose.com/3d/java/).

**P:** ¿Cómo obtengo soporte para Aspose.3D?  
**R:** Visita el [foro oficial de Aspose.3D](https://forum.aspose.com/c/3d/18) para recibir ayuda de la comunidad y del equipo del producto.

**P:** ¿Están disponibles licencias temporales para pruebas?  
**R:** Sí—las licencias temporales pueden obtenerse [aquí](https://purchase.aspose.com/temporary-license/).

---

**Última actualización:** 2026-08-02  
**Probado con:** Aspose.3D para Java (última versión)  
**Autor:** Aspose

{{< blocks/products/products-backtop-button >}}

## Tutoriales relacionados

- [Cómo extruir una forma - Creación de modelos 3D con extrusión lineal en Java](/3d/java/linear-extrusion/)
- [Crear extrusión 3D Java con Aspose.3D](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [Tutorial de gráficos 3D Java – Centro en extrusión lineal](/3d/java/linear-extrusion/controlling-center/)

{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}