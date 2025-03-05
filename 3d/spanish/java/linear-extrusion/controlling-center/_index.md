---
title: Centro de Control en Extrusión Lineal con Aspose.3D para Java
linktitle: Centro de Control en Extrusión Lineal con Aspose.3D para Java
second_title: API de Java Aspose.3D
description: Explora el mundo de los gráficos 3D en Java con Aspose.3D. Controle el centro en extrusión lineal sin esfuerzo.
type: docs
weight: 11
url: /es/java/linear-extrusion/controlling-center/
---
## Introducción

En el mundo de los gráficos 3D y la programación Java, controlar el centro en extrusión lineal juega un papel crucial para conseguir los efectos deseados en tus proyectos. Aspose.3D para Java proporciona un potente conjunto de herramientas para realizar este tipo de tareas sin problemas. En este tutorial, nos sumergiremos en el proceso de control del centro en extrusión lineal usando Aspose.3D para Java, desglosando cada paso para garantizar una comprensión completa y fluida.

## Requisitos previos

Antes de embarcarnos en este viaje tutorial, asegúrese de cumplir con los siguientes requisitos previos:

1. Entorno de desarrollo Java: asegúrese de tener un entorno de desarrollo Java configurado en su máquina.

2.  Aspose.3D para Java: descargue e instale la biblioteca Aspose.3D. Puedes encontrar la biblioteca y su documentación.[aquí](https://reference.aspose.com/3d/java/).

3. Directorio de documentos: cree un directorio para almacenar sus documentos Java. Llamémoslo "Su directorio de documentos".

## Importar paquetes

En su entorno de desarrollo Java, importe los paquetes necesarios para Aspose.3D. Esto garantiza que su código tenga acceso a las funcionalidades proporcionadas por la biblioteca.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Paso 1: configurar el perfil base

Inicialice el perfil base que se va a extruir. En este ejemplo, usaremos una forma de rectángulo con un radio de redondeo de 0,3.

```java
// La ruta al directorio de documentos.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Paso 2: crea una escena 3D

Construye las bases de tu mundo 3D creando una escena.

```java
Scene scene = new Scene();
```

## Paso 3: crear nodos izquierdo y derecho

Establece nodos izquierdo y derecho dentro de tu escena. Estos nodos sirven como lienzo para sus objetos 3D.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Paso 4: Extrusión lineal con propiedad central

Realice una extrusión lineal en el nodo izquierdo sin centrar y establezca el número de cortes en 3.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

## Paso 5: Establecer el plano de tierra como referencia

Mejore la representación visual agregando un plano de tierra al nodo izquierdo.

```java
left.createChildNode(new Box(0.01, 3, 3));
```

## Paso 6: Extrusión lineal con propiedad central (nodo derecho)

Realice una extrusión lineal en el nodo derecho, esta vez centrando la extrusión y nuevamente establezca el número de cortes en 3.

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

## Paso 7: Establecer el plano de tierra como referencia (nodo derecho)

De manera similar al nodo izquierdo, agregue un plano de tierra al nodo derecho como referencia.

```java
right.createChildNode(new Box(0.01, 3, 3));
```

## Paso 8: guarde la escena 3D

Guarde su escena 3D en formato Wavefront OBJ.

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Conclusión

Controlar el centro en extrusión lineal con Aspose.3D para Java abre posibilidades interesantes en el desarrollo de gráficos 3D. Siguiendo esta guía paso a paso, habrá aprendido cómo manipular la propiedad central, lo que le permitirá lograr los efectos visuales deseados en sus proyectos Java.

## Preguntas frecuentes

### P1: ¿Puedo utilizar Aspose.3D para Java en proyectos comerciales?

 R1: Sí, Aspose.3D para Java está disponible para uso comercial. Para obtener detalles sobre la licencia, visite[aquí](https://purchase.aspose.com/buy).

### P2: ¿Hay una prueba gratuita disponible?

 R2: Sí, puedes explorar una prueba gratuita de Aspose.3D para Java[aquí](https://releases.aspose.com/).

### P3: ¿Dónde puedo encontrar soporte para Aspose.3D para Java?

 R3: El foro de la comunidad Aspose.3D es un gran lugar para buscar apoyo y compartir sus experiencias. visita el foro[aquí](https://forum.aspose.com/c/3d/18).

### P4: ¿Necesito una licencia temporal para realizar pruebas?

R4: Sí, si necesita una licencia temporal para fines de prueba, puede obtener una[aquí](https://purchase.aspose.com/temporary-license/).

### P5: ¿Dónde puedo encontrar la documentación?

 R5: La documentación de Aspose.3D para Java está disponible[aquí](https://reference.aspose.com/3d/java/).