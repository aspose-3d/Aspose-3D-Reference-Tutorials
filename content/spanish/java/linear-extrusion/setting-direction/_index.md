---
title: Establecer dirección en extrusión lineal con Aspose.3D para Java
linktitle: Establecer dirección en extrusión lineal con Aspose.3D para Java
second_title: API de Java Aspose.3D
description: ¡Domina la extrusión lineal con Aspose.3D para Java! Siga nuestra guía para una programación 3D perfecta. Descárguelo ahora para vivir una experiencia cautivadora.
type: docs
weight: 12
url: /es/java/linear-extrusion/setting-direction/
---
## Introducción

Bienvenido a nuestra guía paso a paso sobre cómo establecer la dirección en extrusión lineal usando Aspose.3D para Java. Aspose.3D es una potente biblioteca Java que permite a los desarrolladores trabajar sin problemas con archivos y escenas 3D. En este tutorial, nos centraremos en la tarea específica de establecer la dirección en la extrusión lineal, mejorando su competencia en programación 3D.

## Requisitos previos

Antes de sumergirnos en el tutorial, asegúrese de cumplir con los siguientes requisitos previos:

- Conocimientos básicos del lenguaje de programación Java.
-  Biblioteca Aspose.3D instalada. Puedes descargarlo desde[aquí](https://releases.aspose.com/3d/java/).
- Un entorno de desarrollo integrado (IDE) para Java, como Eclipse o IntelliJ.

## Importar paquetes

Asegúrese de importar los paquetes necesarios para iniciar su proyecto:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Paso 1: inicializar el perfil base

 Comience inicializando el perfil base que se va a extruir. En este ejemplo, utilizamos un`RectangleShape` con un radio de redondeo de 0,3:

```java
// La ruta al directorio de documentos.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Paso 2: crea una escena

A continuación, cree una escena 3D para contener los objetos extruidos:

```java
Scene scene = new Scene();
```

## Paso 3: crear nodos

Crea nodos izquierdo y derecho dentro de la escena:

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Paso 4: realizar una extrusión lineal en el nodo izquierdo

 Realice una extrusión lineal en el nodo izquierdo usando el`LinearExtrusion`clase con parámetros especificados como giros y cortes:

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Paso 5: realizar una extrusión lineal en el nodo derecho con dirección

 Realizar una extrusión lineal en el nodo derecho, introduciendo el`setDirection` Propiedad para definir la dirección de extrusión:

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Paso 6: guardar la escena 3D

Guarde la escena 3D en el formato de archivo deseado. En este ejemplo, lo guardamos como un archivo Wavefront OBJ:

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Conclusión

¡Felicidades! Ha aprendido con éxito cómo establecer la dirección en la extrusión lineal usando Aspose.3D para Java. Este tutorial mejora tus habilidades en programación 3D y abre nuevas posibilidades para proyectos creativos.

## Preguntas frecuentes

### P1: ¿Puedo usar Aspose.3D con otros lenguajes de programación?

R1: Aspose.3D admite varios lenguajes de programación, incluidos .NET y Java.

### P2. ¿Hay una prueba gratuita disponible para Aspose.3D?

 R2: Sí, puedes explorar las funciones de Aspose.3D con una prueba gratuita[aquí](https://releases.aspose.com/).

### P3: ¿Dónde puedo encontrar documentación detallada de Aspose.3D para Java?

 A3: La documentación completa está disponible[aquí](https://reference.aspose.com/3d/java/).

### P4: ¿Cómo puedo obtener soporte para Aspose.3D?

 A4: Visita el[Foro Aspose.3D](https://forum.aspose.com/c/3d/18) para cualquier ayuda o consulta.

### P5: ¿Hay licencias temporales disponibles para Aspose.3D?

 R5: Sí, puedes obtener una licencia temporal[aquí](https://purchase.aspose.com/temporary-license/).