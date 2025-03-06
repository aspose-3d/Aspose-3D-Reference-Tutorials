---
title: Personalize o carregamento de arquivos 3D em Java com Aspose.3D LoadOptions
linktitle: Personalize o carregamento de arquivos 3D em Java com Aspose.3D LoadOptions
second_title: API Java Aspose.3D
description: Aprimore o carregamento de arquivos 3D em Java com LoadOptions personalizáveis Aspose.3D. Aprenda a personalização passo a passo para 3DS, OBJ, STL, U3D, glTF, PLY, X e FBX opcional.
weight: 12
url: /pt/java/load-and-save/customize-3d-file-loading/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Personalize o carregamento de arquivos 3D em Java com Aspose.3D LoadOptions

## Introdução

No cenário em constante evolução do design e desenvolvimento 3D, o manuseio eficiente de formatos de arquivo 3D é crucial. Aspose.3D for Java fornece uma solução poderosa para personalizar o carregamento de vários formatos de arquivo 3D. Este tutorial irá guiá-lo através do processo de personalização do carregamento de arquivos 3D em Java usando LoadOptions do Aspose.3D.

## Pré-requisitos

Antes de mergulhar no processo de personalização, certifique-se de ter o seguinte:

- Compreensão básica de programação Java.
- Kit de desenvolvimento Java (JDK) instalado.
-  Biblioteca Aspose.3D para Java baixada. Você pode obtê-lo[aqui](https://releases.aspose.com/3d/java/).
- Familiaridade com formatos de arquivo 3D como 3DS, OBJ, STL, U3D, glTF, PLY, X e FBX.

## Importar pacotes

Em seu projeto Java, certifique-se de importar os pacotes Aspose.3D necessários:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Personalize o carregamento de arquivos 3D

### Etapa 1: personalizar o carregamento de arquivos 3DS

```java
public static void discreet3DSLoadOption() {
    String MyDir = "Your Document Directory";
    Discreet3dsLoadOptions loadOpts = new Discreet3dsLoadOptions();
    loadOpts.setApplyAnimationTransform(true);
    loadOpts.setFlipCoordinateSystem(true);
    loadOpts.setGammaCorrectedColor(true);
    loadOpts.getLookupPaths().add(MyDir);
}
```

### Etapa 2: personalizar o carregamento do arquivo OBJ

```java
public static void objLoadOption() {
    String MyDir = "Your Document Directory";
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();
    loadObjOpts.setEnableMaterials(true);
    loadObjOpts.setFlipCoordinateSystem(true);
    loadObjOpts.getLookupPaths().add(MyDir);
}
```

### Etapa 3: personalizar o carregamento de arquivo STL

```java
public static void stlLoadOption() {
    String MyDir = "Your Document Directory";
    StlLoadOptions loadSTLOpts = new StlLoadOptions();
    loadSTLOpts.setFlipCoordinateSystem(true);
    loadSTLOpts.getLookupPaths().add(MyDir);
}
```

### Etapa 4: personalizar o carregamento de arquivos U3D

```java
public static void u3dLoadOption() {
    String MyDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();
    loadU3DOpts.setFlipCoordinateSystem(true);
    loadU3DOpts.getLookupPaths().add(MyDir);
}
```

### Etapa 5: personalizar o carregamento do arquivo glTF

```java
public static void gltfLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();
    loadOpt.setFlipTexCoordV(true);
    scene.open(MyDir + "Duck.gltf", loadOpt);
}
```

### Etapa 6: personalizar o carregamento do arquivo PLY

```java
public static void plyLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();
    loadPLYOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "vase-v2.ply", loadPLYOpts);
}
```

### Etapa 7: personalizar o carregamento do arquivo X

```java
public static void xLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    XLoadOptions loadXOpts = new XLoadOptions(FileContentType.ASCII);
    loadXOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "warrior.x", loadXOpts);
}
```

### Etapa 8: personalizar o carregamento de arquivos FBX (opcional)

```java
private static void FBXLoadOptions() throws IOException {
    String dataDir = "Your Document Directory";
    Scene scene = new Scene();
    FbxLoadOptions opt = new FbxLoadOptions();
    opt.setKeepBuiltinGlobalSettings(true);
    scene.open(dataDir + "test.FBX", opt);
    for(Property property:scene.getRootNode().getAssetInfo().getProperties()) {
        System.out.println(property);
    }
}
```

## Conclusão

Personalizar o carregamento de arquivos 3D em Java com LoadOptions do Aspose.3D permite que os desenvolvedores adaptem o processo de importação a requisitos específicos. Seja ajustando transformações de animação, invertendo sistemas de coordenadas ou lidando com dependências externas, o Aspose.3D oferece a flexibilidade necessária para uma integração perfeita.

## Perguntas frequentes

### Q1: Onde posso encontrar a documentação do Aspose.3D para Java?

 A1: A documentação está disponível[aqui](https://reference.aspose.com/3d/java/).

### Q2: Como posso baixar Aspose.3D para Java?

 A2: Você pode baixá-lo[aqui](https://releases.aspose.com/3d/java/).

### Q3: Existe um teste gratuito disponível?

 A3: Sim, você pode acessar a avaliação gratuita[aqui](https://releases.aspose.com/).

### Q4: Onde posso obter suporte para Aspose.3D para Java?

 A4: Visite o fórum de suporte[aqui](https://forum.aspose.com/c/3d/18).

### P5: Preciso de uma licença temporária para testes?

 A5: Sim, obtenha uma licença temporária[aqui](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
