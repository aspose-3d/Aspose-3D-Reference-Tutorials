---
date: 2025-12-18
description: Aprende cómo agregar un plano de referencia y establecer la propiedad
  de centro en la extrusión lineal usando Aspose.3D para Java, con ejemplos de código
  paso a paso.
linktitle: Controlling Center in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Cómo añadir plano de base y centro de control en extrusión lineal con Aspose.3D
  para Java
url: /es/java/linear-extrusion/controlling-center/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Control del centro en extrusión lineal con Aspose.3D para Java

## Introducción

Cuando construyes escenas 3D en Java, la capacidad de **añadir plano de suelo** mientras estableces con precisión la **propiedad de centro** en una extrusión lineal puede marcar la diferencia entre un prototipo plano y una visualización pulida. En este tutorial recorreremos el proceso completo de controlar el centro de la extrusión y añadir un plano de suelo usando Aspose.3D para Java. Verás por qué es importante, cómo configurarlo y obtendrás un ejemplo de código listo‑para‑ejecutar que podrás adaptar a tus propios proyectos.

## Respuestas rápidas
- **¿Qué hace “add ground plane”?** Crea una geometría de referencia delgada que ayuda a ver la posición de la extrusión respecto a los ejes del mundo.  
- **¿Cómo establezco el centro de una extrusión lineal?** Usa el método `setCenter(boolean)` en el objeto `LinearExtrusion`.  
- **¿Necesito una licencia para ejecutar el ejemplo?** Una licencia temporal funciona para pruebas; se requiere una licencia completa para producción.  
- **¿Qué formato de archivo se usa para guardar?** El ejemplo guarda en Wavefront OBJ (`.obj`).  
- **¿Qué versión de Java se requiere?** Java 8 o posterior es suficiente.

## Qué es “add ground plane” en una escena 3D?

Añadir un plano de suelo significa insertar una geometría rectangular delgada (a menudo una caja con grosor mínimo) que se sitúa en el plano X‑Z. Actúa como un piso visual, facilitando la evaluación de la altura y alineación de otros objetos, especialmente cuando se experimenta con centros de extrusión.

## ¿Por qué establecer la propiedad de centro en una extrusión lineal?

Por defecto, una extrusión lineal comienza desde el origen del perfil. Establecer la propiedad de centro (`setCenter(true)`) desplaza el perfil de modo que la extrusión quede centrada alrededor del origen, lo que es útil para diseños simétricos o cuando se necesita una alineación consistente entre varios objetos.

## Requisitos previos

Antes de iniciar este tutorial, asegúrate de cumplir los siguientes requisitos:

1. **Entorno de desarrollo Java** – Asegúrate de tener un entorno de desarrollo Java configurado en tu máquina.  
2. **Aspose.3D for Java** – Descarga e instala la biblioteca Aspose.3D. Puedes encontrar la biblioteca y su documentación [aquí](https://reference.aspose.com/3d/java/).  
3. **Directorio de documentos** – Crea un directorio para almacenar tus documentos Java. Llamémoslo “Your Document Directory.”

## Importar paquetes

En tu entorno de desarrollo Java, importa los paquetes necesarios para Aspose.3D. Esto garantiza que tu código tenga acceso a las funcionalidades proporcionadas por la biblioteca.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Paso 1: Configurar el perfil base

Inicializa el perfil base que se extruirá. En este ejemplo, usaremos una forma rectangular con un radio de redondeo de 0.3.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Paso 2: Crear una escena 3D

Construye la base de tu mundo 3D creando una escena.

```java
Scene scene = new Scene();
```

## Paso 3: Crear nodos izquierdo y derecho

Establece nodos izquierdo y derecho dentro de tu escena. Estos nodos sirven como lienzo para tus objetos 3D.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Paso 4: Extrusión lineal con propiedad de centro (nodo izquierdo)

Realiza una extrusión lineal en el nodo izquierdo **sin centrar** y establece el número de secciones en 3. Observa la llamada `setCenter(false)` – aquí es donde **establecemos la propiedad de centro** a *false*.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

## Paso 5: Añadir plano de suelo como referencia (nodo izquierdo)

Mejora la representación visual **añadiendo un plano de suelo** al nodo izquierdo. La caja delgada actúa como un piso para que puedas ver claramente la altura de la extrusión.

```java
left.createChildNode(new Box(0.01, 3, 3));
```

## Paso 6: Extrusión lineal con propiedad de centro (nodo derecho)

Ahora realiza una extrusión lineal en el nodo derecho, esta vez **centrando la extrusión**. La llamada `setCenter(true)` muestra cómo **establecer la propiedad de centro** a *true*.

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

## Paso 7: Añadir plano de suelo como referencia (nodo derecho)

Al igual que en el lado izquierdo, añade un plano de suelo al nodo derecho para una base visual consistente.

```java
right.createChildNode(new Box(0.01, 3, 3));
```

## Paso 8: Guardar la escena 3D

Guarda tu escena 3D en formato Wavefront OBJ para que puedas verla en cualquier visor 3D estándar.

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Problemas comunes y soluciones

| Problema | Por qué ocurre | Solución |
|----------|----------------|----------|
| El plano de suelo no es visible | El grosor de la caja es demasiado pequeño para la escala del visor. | Aumenta el grosor (primer parámetro de `Box`) o aleja el zoom en el visor. |
| La extrusión aparece desplazada | El valor de `setCenter` no se estableció como se pretendía. | Verifica el booleano pasado a `setCenter`. |
| El archivo no se guarda | Ruta del directorio incorrecta o faltan permisos de escritura. | Verifica que `MyDir` apunte a una carpeta existente con acceso de escritura. |

## Preguntas frecuentes

**Q1: ¿Puedo usar Aspose.3D for Java en proyectos comerciales?**  
A1: Sí, Aspose.3D for Java está disponible para uso comercial. Para detalles de licenciamiento, visita [aquí](https://purchase.aspose.com/buy).

**Q2: ¿Hay una prueba gratuita disponible?**  
A2: Sí, puedes probar una versión de prueba gratuita de Aspose.3D for Java [aquí](https://releases.aspose.com/).

**Q3: ¿Dónde puedo encontrar soporte para Aspose.3D for Java?**  
A3: El foro de la comunidad Aspose.3D es un excelente lugar para buscar soporte y compartir experiencias. Visita el foro [aquí](https://forum.aspose.com/c/3d/18).

**Q4: ¿Necesito una licencia temporal para pruebas?**  
A4: Sí, si necesitas una licencia temporal para propósitos de prueba, puedes obtener una [aquí](https://purchase.aspose.com/temporary-license/).

**Q5: ¿Dónde puedo encontrar la documentación?**  
A5: La documentación de Aspose.3D for Java está disponible [aquí](https://reference.aspose.com/3d/java/).

## Conclusión

Controlar el centro en una extrusión lineal **y** aprender a **añadir un plano de suelo** con Aspose.3D para Java abre emocionantes posibilidades en el desarrollo de gráficos 3D. Siguiendo los pasos anteriores ahora dispones de unizable para crear extrusiones centradas, planos de referencia visual y exportar el resultado a OBJ. Siéntete libre de experimentar con diferentes perfiles, recuentos de secciones y transformaciones para adaptarlos a las necesidades de tu proyecto.

---

**Last Updated:** 2025-12-18  
**Tested With:** Aspose.3D 24.11 for Java (latest at time of writing)  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}