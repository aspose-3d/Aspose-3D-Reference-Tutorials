---
title: Transforme nós 3D com quaternions em Java usando Aspose.3D
linktitle: Transforme nós 3D com quaternions em Java usando Aspose.3D
second_title: API Java Aspose.3D
description: Aprimore seus aplicativos Java com Aspose.3D para transformações 3D poderosas. Aprenda a transformar nós usando quatérnios neste guia passo a passo.
type: docs
weight: 20
url: /pt/java/geometry/transform-3d-nodes-with-quaternions/
---
## Introdução

Bem-vindo a este guia passo a passo sobre como transformar nós 3D com quaternions em Java usando Aspose.3D. Se você deseja aprimorar seu aplicativo Java com transformações 3D poderosas, este tutorial é para você. Aspose.3D for Java fornece um conjunto robusto de recursos para trabalhar com gráficos 3D e, neste tutorial, vamos nos concentrar na transformação de nós 3D usando quaternions.

## Pré-requisitos

Antes de mergulharmos no tutorial, certifique-se de ter os seguintes pré-requisitos em vigor:

- Conhecimento básico de programação Java.
- Aspose.3D para Java instalado. Você pode baixá-lo[aqui](https://releases.aspose.com/3d/java/).
- Um diretório de documentos configurado para salvar suas cenas 3D.

## Importar pacotes

Nesta seção, importaremos os pacotes necessários para iniciar as transformações 3D usando Aspose.3D.

```java
import com.aspose.threed.*;
```

## Etapa 1: inicializar o objeto de cena

Para começar, crie um objeto de cena que servirá como contêiner para seus elementos 3D.

```java
Scene scene = new Scene();
```

## Etapa 2: inicializar o objeto de classe do nó

Agora, crie um objeto de classe de nó, neste caso, representando um cubo.

```java
Node cubeNode = new Node("cube");
```

## Etapa 3: Criar malha usando Polygon Builder

Utilize a classe comum para criar uma malha usando o método construtor de polígonos.

```java
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## Etapa 4: definir a geometria da malha

Atribua a malha criada ao nó do cubo.

```java
cubeNode.setEntity(mesh);
```

## Etapa 5: definir rotação com Quaternion

Aplique rotação ao nó do cubo usando quaternions.

```java
cubeNode.getTransform().setRotation(Quaternion.fromRotation(new Vector3(0, 1, 0), new Vector3(0.3, 0.5, 0.1)));
```

## Etapa 6: definir a tradução

Especifique a conversão para o nó do cubo.

```java
cubeNode.getTransform().setTranslation(new Vector3(0, 0, 20));
```

## Passo 7: Adicionar Cubo à Cena

Inclua o nó do cubo na cena.

```java
scene.getRootNode().getChildNodes().add(cubeNode);
```

## Etapa 8: Salvar cena 3D

Salve a cena 3D em um formato de arquivo compatível, por exemplo, FBX7500ASCII.

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "TransformationToNode.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nTransformation added successfully to node.\nFile saved at " + MyDir);
```

## Conclusão

Parabéns! Você aprendeu com sucesso como transformar nós 3D usando quaternions em Java com Aspose.3D. Experimente diferentes transformações para dar vida às suas aplicações 3D.

## Perguntas frequentes

### Q1: Posso usar Aspose.3D para Java gratuitamente?

A1: Aspose.3D for Java oferece uma avaliação gratuita. Você pode encontrá lo[aqui](https://releases.aspose.com/).

### P2: Onde posso encontrar a documentação do Aspose.3D para Java?

 A2: A documentação está disponível[aqui](https://reference.aspose.com/3d/java/).

### Q3: Como obtenho suporte para Aspose.3D para Java?

 A3: Visite o[Fórum Aspose.3D](https://forum.aspose.com/c/3d/18) para suporte.

### P4: As licenças temporárias estão disponíveis?

 A4: Sim, você pode obter uma licença temporária[aqui](https://purchase.aspose.com/temporary-license/).

### Q5: Onde posso comprar Aspose.3D para Java?

 A5: Você pode comprá-lo[aqui](https://purchase.aspose.com/buy).