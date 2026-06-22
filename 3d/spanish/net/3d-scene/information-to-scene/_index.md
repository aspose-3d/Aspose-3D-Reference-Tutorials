---
date: 2026-03-26
description: Aprende cómo agregar información del proveedor a una escena 3D y cómo
  guardar archivos FBX usando Aspose.3D para .NET. Sigue esta guía paso a paso con
  código listo para ejecutar.
linktitle: Extracting Information to Scene Assets
second_title: Aspose.3D .NET API
title: Cómo agregar información del proveedor y guardar la escena FBX usando Aspose.3D
url: /es/net/3d-scene/information-to-scene/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Cómo agregar información del proveedor y guardar la escena FBX usando Aspose.3D

## Introducción

Bienvenido a este tutorial completo que muestra **cómo agregar información del proveedor** a una escena 3D y luego **cómo guardar archivos FBX** con Aspose.3D para .NET. Ya sea que esté creando visualizaciones arquitectónicas, activos para juegos o modelos de ingeniería, incrustar metadatos del proveedor y de la aplicación hace que sus escenas sean más informativas y más fáciles de gestionar en etapas posteriores. Repasemos el proceso paso a paso.

## Respuestas rápidas
- **¿Qué significa “add vendor”?** Almacena los nombres de la aplicación y del proveedor dentro del bloque AssetInfo de la escena.  
- **¿Qué formato admite información del proveedor?** FBX (ASCII o binario) conserva los metadatos al guardarse.  
- **¿Cómo guardar FBX?** Use `scene.Save(path, FileFormat.FBX7500ASCII)` o el equivalente binario.  
- **¿Necesito una licencia?** Una prueba gratuita funciona para desarrollo; se requiere una licencia comercial para producción.  
- **¿Puedo cambiar las unidades de medida?** Sí, establezca `AssetInfo.UnitName` y `AssetInfo.UnitScaleFactor`.

## ¿Qué es “how to add vendor” en una escena 3D?
Agregar información del proveedor significa rellenar las propiedades `AssetInfo` de un objeto `Scene`. Estas propiedades viajan con el archivo, permitiendo que cualquier consumidor del archivo FBX vea qué aplicación lo creó y quién es el proveedor.

## ¿Por qué agregar información del proveedor?
- **Rastreabilidad:** Identificar rápidamente la fuente de un modelo en grandes flujos de trabajo.  
- **Cumplimiento:** Algunas industrias requieren etiquetado explícito del proveedor para la gestión de activos.  
- **Automatización:** Los scripts pueden filtrar o procesar archivos basados en los metadatos del proveedor.

## Requisitos previos

- Aspose.3D for .NET instalado. Puede descargarlo desde la [página de Aspose.3D for .NET](https://releases.aspose.com/3d/net/).

## Importar espacios de nombres

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
```

## Cómo agregar información del proveedor

### Paso 1: Inicializar una escena 3D

```csharp
Scene scene = new Scene();
```

Crear una nueva `Scene` le brinda un lienzo limpio para trabajar.

### Paso 2: Establecer la información de la aplicación y del proveedor

```csharp
scene.AssetInfo.ApplicationName = "Egypt";
scene.AssetInfo.ApplicationVendor = "Manualdesk";
```

Aquí demostramos **cómo agregar información del proveedor** asignando cadenas significativas a `ApplicationName` y `ApplicationVendor`.

### Paso 3: Definir unidades de medida

```csharp
scene.AssetInfo.UnitName = "pole";
scene.AssetInfo.UnitScaleFactor = 0.6;
```

Especificar el sistema de unidades garantiza que cualquiera que abra el archivo FBX interprete correctamente las dimensiones. En este ejemplo, un “pole” equivale a 60 cm.

## Cómo guardar la escena FBX

### Paso 4: Guardar la escena (cómo guardar fbx)

```csharp
var output = "Your Output Directory" + "InformationToScene.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

Esta línea muestra **cómo guardar fbx** usando la versión ASCII de FBX 7.5.0. Si prefiere binario, reemplace `FBX7500ASCII` por `FBX7500Binary`.

> **Consejo profesional:** Mantenga la extensión de archivo `.fbx` coherente con el formato que elija; de lo contrario, algunos visores pueden interpretar incorrectamente el contenido.

### Paso 5: Mostrar mensaje de éxito

```csharp
Console.WriteLine("\nAsset information added successfully to Scene.\nFile saved at " + output);
```

Un mensaje amigable en la consola confirma que la escena, completa con los metadatos del proveedor, se ha escrito en el disco.

## Problemas comunes y soluciones

| Problema | Solución |
|----------|----------|
| **La información del proveedor no aparece en el visor** | Asegúrese de haber guardado el archivo como **FBX ASCII** o **Binary**; algunos visores antiguos solo leen un formato. |
| **La ruta contiene espacios** | Encierre la ruta entre comillas o use `Path.Combine` para crear una ruta segura. |
| **La escala de la unidad parece incorrecta** | Verifique `UnitScaleFactor`; es un multiplicador relativo a metros. |
| **Excepción de licencia** | Use la prueba gratuita para pruebas; obtenga una licencia completa para compilaciones de producción. |

## Preguntas frecuentes

**P: ¿Puedo usar Aspose.3D for .NET con otros lenguajes de programación?**  
R: Aspose.3D admite principalmente lenguajes .NET, pero puede explorar opciones de interoperabilidad para otros lenguajes.

**P: ¿Hay una prueba gratuita disponible para Aspose.3D for .NET?**  
R: Sí, puede acceder a la prueba gratuita [aquí](https://releases.aspose.com/).

**P: ¿Cómo obtengo soporte para consultas relacionadas con Aspose.3D?**  
R: Visite el [foro de Aspose.3D](https://forum.aspose.com/c/3d/18) para la comunidad y soporte.

**P: ¿Puedo comprar una licencia temporal para Aspose.3D for .NET?**  
R: Sí, puede adquirir una licencia temporal [aquí](https://purchase.aspose.com/temporary-license/).

**P: ¿Dónde puedo encontrar documentación detallada para Aspose.3D for .NET?**  
R: Consulte la [documentación](https://reference.aspose.com/3d/net/) para información detallada.

---

**Última actualización:** 2026-03-26  
**Probado con:** Aspose.3D 24.11 for .NET  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}