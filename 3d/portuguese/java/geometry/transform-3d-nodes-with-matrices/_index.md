---
title: Transforme nós 3D com matrizes de transformação usando Aspose.3D
linktitle: Transforme nós 3D com matrizes de transformação em Java usando Aspose.3D
second_title: API Java Aspose.3D
description: Explore o mundo dos gráficos 3D em Java com Aspose.3D. Aprenda a transformar nós sem esforço usando matrizes de transformação.
weight: 21
url: /pt/java/geometry/transform-3d-nodes-with-matrices/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Transforme nós 3D com matrizes de transformação usando Aspose.3D

## Introdução

Bem-vindo a este guia passo a passo sobre como transformar nós 3D com matrizes de transformação em Java usando Aspose.3D. Se você é um desenvolvedor Java e deseja aprimorar seus gráficos 3D e habilidades de modelagem, você está no lugar certo. Neste tutorial, mergulharemos no processo de aplicação de transformações a nós 3D dentro da estrutura Aspose.3D.

## Pré-requisitos

Antes de começarmos, certifique-se de ter os seguintes pré-requisitos:

- Conhecimento básico de programação Java.
-  Biblioteca Aspose.3D instalada. Você pode baixá-lo em[aqui](https://releases.aspose.com/3d/java/).
- Um ambiente de desenvolvimento integrado (IDE) funcional para desenvolvimento Java.

## Importar pacotes

No seu projeto Java, importe os pacotes necessários do Aspose.3D. Certifique-se de que seu projeto esteja configurado corretamente para usar a biblioteca Aspose.3D. Aqui está um exemplo de instrução de importação:

```java
import com.aspose.threed.*;

```

## Transformando nós 3D

### Etapa 1: inicializar o objeto de cena

Comece inicializando um objeto de cena, que serve como contêiner para elementos 3D.

```java
Scene scene = new Scene();
```

### Etapa 2: inicializar o objeto de classe do nó

Crie um objeto da classe Node, como um cubo, que passará por transformação.

```java
Node cubeNode = new Node("cube");
```

### Etapa 3: criar malha usando o Polygon Builder

Utilize a classe Common para criar uma malha usando o método construtor de polígonos. Isso define a instância de malha do cubo.

```java
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

### Etapa 4: apontar o nó para a geometria da malha

Atribua a malha criada ao nó do cubo.

```java
cubeNode.setEntity(mesh);
```

### Etapa 5: definir matriz de tradução personalizada

Aplique uma matriz de tradução customizada ao nó do cubo. Este exemplo define uma matriz de transformação para tradução.

```java
cubeNode.getTransform().setTransformMatrix(new Matrix4(
    1, -0.3, 0, 0,
    0.4, 1, 0.3, 0,
    0, 0, 1, 0,
    0, 20, 0, 1
));
```

### Etapa 6: adicionar cubo à cena

Inclua o nó do cubo no nó raiz da cena.

```java
scene.getRootNode().addChildNode(cubeNode);
```

### Etapa 7: Salvar cena 3D

Especifique o diretório e o nome do arquivo para salvar a cena 3D em formatos de arquivo suportados, como FBX.

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "TransformationToNode.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nTransformation added successfully to node.\nFile saved at " + MyDir);
```

## Conclusão

Parabéns! Você aprendeu com sucesso como transformar nós 3D usando Aspose.3D em Java. Experimente diferentes matrizes e explore as infinitas possibilidades dos gráficos 3D.

## Perguntas frequentes

### Q1: Posso aplicar múltiplas transformações a um único nó 3D?

A1: Sim, você pode concatenar múltiplas matrizes de transformação para transformações complexas.

### Q2: Como posso girar um objeto 3D no Aspose.3D?

A2: Use a matriz de rotação apropriada na matriz de transformação para a rotação desejada.

### P3: Existe um limite para o tamanho das cenas 3D que posso criar?

R3: O tamanho de suas cenas 3D pode ser limitado pelos recursos do sistema, mas o Aspose.3D foi projetado para ser eficiente.

### P4: Onde posso encontrar exemplos e documentação adicionais?

 A4: Visite o[Documentação Aspose.3D](https://reference.aspose.com/3d/java/) para mais exemplos e detalhes.

### Q5: Como obtenho uma licença temporária para Aspose.3D?

 A5: Você pode obter uma licença temporária[aqui](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
