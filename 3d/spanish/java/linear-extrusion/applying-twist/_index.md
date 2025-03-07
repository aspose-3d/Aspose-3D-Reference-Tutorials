---
title: Aplicación de torsión en extrusión lineal con Aspose.3D para Java
linktitle: Aplicación de torsión en extrusión lineal con Aspose.3D para Java
second_title: API de Java Aspose.3D
description: Aprenda cómo darle un toque diferente a sus modelos 3D usando Aspose.3D para Java. Siga nuestra guía paso a paso para obtener efectos de extrusión lineal mejorados.
weight: 14
url: /es/java/linear-extrusion/applying-twist/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aplicación de torsión en extrusión lineal con Aspose.3D para Java

## Introducción

Bienvenido a este tutorial paso a paso sobre cómo aplicar un giro en extrusión lineal usando Aspose.3D para Java. Aspose.3D es una potente biblioteca Java que permite a los desarrolladores trabajar con formatos de archivos 3D y ofrece una funcionalidad sólida para crear, manipular y renderizar escenas 3D. En este tutorial, exploraremos cómo aplicar un efecto de torsión durante el proceso de extrusión lineal para mejorar sus modelos 3D.

## Requisitos previos

Antes de sumergirse en el tutorial, asegúrese de cumplir con los siguientes requisitos previos:

- Entorno de desarrollo de Java: asegúrese de tener Java instalado en su sistema.
-  Biblioteca Aspose.3D: descargue e instale la biblioteca Aspose.3D para Java desde[enlace de descarga](https://releases.aspose.com/3d/java/).
-  Documentación: Consulte la[Documentación de Aspose.3D](https://reference.aspose.com/3d/java/) para una orientación integral.

## Importar paquetes

Antes de comenzar el proceso de codificación, importe los paquetes necesarios a su proyecto Java. A continuación se muestra un ejemplo de cómo hacer esto:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Paso 1: configurar el directorio de documentos

Comience configurando el directorio de documentos donde se guardará su escena 3D.

```java
// ExInicio:EstablecerDirectorioDeDocumentos
String MyDir = "Your Document Directory";
// ExEnd:EstablecerDirectorioDeDocumentos
```

## Paso 2: inicializar el perfil base

Inicialice el perfil base que se va a extruir. En este ejemplo, utilizamos una forma de rectángulo con un radio de redondeo.

```java
// ExStart: Inicializar perfil base
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
// ExEnd: Inicializar perfil base
```

## Paso 3: crea una escena

Cree una escena 3D para albergar los nodos extruidos.

```java
// ExInicio:CrearEscena
Scene scene = new Scene();
// ExEnd:CrearEscena
```

## Paso 4: crear nodos

Crea nodos izquierdo y derecho dentro de la escena. Ajusta la traducción del nodo izquierdo.

```java
// ExInicio:CrearNodos
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
// ExEnd:CrearNodos
```

## Paso 5: realizar una extrusión lineal con giro

Realice una extrusión lineal en los nodos izquierdo y derecho, aplicando propiedades de torsión y cortes.

```java
// ExStart: Extrusión lineal con giro
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(0); setSlices(100); }});
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(90); setSlices(100); }});
// ExEnd: Extrusión lineal con giro
```

## Paso 6: guardar la escena 3D

Guarde la escena 3D en el formato de archivo Wavefront OBJ.

```java
// ExInicio:GuardarEscena3DS
scene.save(MyDir + "TwistInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
//ExEnd:GuardarEscena 3DS
```

## Conclusión

¡Felicidades! Ha aplicado con éxito un giro en la extrusión lineal utilizando Aspose.3D para Java. Este tutorial proporciona una guía detallada paso a paso para ayudarle a mejorar sus capacidades de modelado 3D.

## Preguntas frecuentes

### P1: ¿Puedo usar Aspose.3D para Java para trabajar con otros formatos de archivos 3D?

R1: Sí, Aspose.3D admite varios formatos de archivos 3D, lo que le permite importar, exportar y manipular diversos tipos de archivos.

### P2: ¿Dónde puedo encontrar soporte para Aspose.3D para Java?

 A2: Visita el[Foro Aspose.3D](https://forum.aspose.com/c/3d/18) para apoyo y debates de la comunidad.

### P3: ¿Hay una prueba gratuita disponible para Aspose.3D para Java?

 R3: Sí, puedes acceder a la versión de prueba gratuita desde[aquí](https://releases.aspose.com/).

### P4: ¿Cómo puedo obtener una licencia temporal de Aspose.3D para Java?

 R4: Obtenga una licencia temporal del[página de licencia temporal](https://purchase.aspose.com/temporary-license/).

### P5: ¿Dónde puedo comprar Aspose.3D para Java?

 R5: Compre Aspose.3D para Java en el[pagina de compra](https://purchase.aspose.com/buy).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
