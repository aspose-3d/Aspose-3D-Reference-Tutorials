---
title: Transforme nós 3D com ângulos de Euler em Java usando Aspose.3D
linktitle: Transforme nós 3D com ângulos de Euler em Java usando Aspose.3D
second_title: API Java Aspose.3D
description: Explore o mundo das transformações 3D em Java com Aspose.3D. Siga nosso guia passo a passo para adicionar ângulos de Euler dinâmicos aos seus nós 3D.
type: docs
weight: 19
url: /pt/java/geometry/transform-3d-nodes-with-euler-angles/
---
## Introdução

Bem-vindo a este tutorial passo a passo sobre como transformar nós 3D com ângulos de Euler em Java usando Aspose.3D. Neste guia, nos aprofundaremos no processo de adição de transformações a um nó 3D, usando ângulos de Euler para obter posicionamento e orientação dinâmicos.

## Pré-requisitos

Antes de mergulharmos no tutorial, certifique-se de ter os seguintes pré-requisitos em vigor:

- Conhecimento básico de programação Java.
- Java Development Kit (JDK) instalado em sua máquina.
-  Biblioteca Aspose.3D, que você pode obter em[Documentação Java Aspose.3D](https://reference.aspose.com/3d/java/).

## Importar pacotes

 Comece importando os pacotes necessários para o seu projeto Java. Certifique-se de que a biblioteca Aspose.3D foi adicionada corretamente ao seu caminho de classe. Se você ainda não baixou, você pode encontrar o link para download[aqui](https://releases.aspose.com/3d/java/).

```java
import com.aspose.threed.*;
```

## Etapa 1. Inicializar cena e nó

```java
// ExStart: AddTransformationToNodeByEulerAngles
// Inicializar objeto de cena
Scene scene = new Scene();

// Inicializar objeto de classe Node
Node cubeNode = new Node("cube");
```

## Passo 2. Criar Malha e Definir Geometria

```java
// Chame a classe Common para criar malha usando o método construtor de polígono para definir a instância da malha
Mesh mesh = Common.createMeshUsingPolygonBuilder();

// Aponte o nó para a geometria da malha
cubeNode.setEntity(mesh);
```

## Etapa 3. Definir ângulos e translação de Euler

```java
// Ângulos de Euler
cubeNode.getTransform().setEulerAngles(new Vector3(0.3, 0.1, -0.5));

// Definir tradução
cubeNode.getTransform().setTranslation(new Vector3(0, 0, 20));
```

## Etapa 4. Adicionar nó à cena

```java
// Adicione um cubo à cena
scene.getRootNode().getChildNodes().add(cubeNode);
```

## Passo 5. Salvar cena 3D

```java
// O caminho para o diretório de documentos.
String MyDir = "Your Document Directory";
MyDir = MyDir + "TransformationToNode.fbx";

//Salve cenas 3D nos formatos de arquivo suportados
scene.save(MyDir, FileFormat.FBX7500ASCII);
// ExEnd: AddTransformationToNodeByEulerAngles
System.out.println("\nTransformation added successfully to node.\nFile saved at " + MyDir);
```

Certifique-se de substituir “Seu diretório de documentos” pelo caminho apropriado em sua máquina.

## Conclusão

Parabéns! Você transformou nós 3D com sucesso usando ângulos de Euler em Java com Aspose.3D. Experimente diferentes ângulos e traduções para criar cenas 3D dinâmicas e envolventes.

## Perguntas frequentes

### Q1: Posso usar Aspose.3D para Java em projetos comerciais?

 A1: Sim, você pode. Visite a[página de compra](https://purchase.aspose.com/buy) para detalhes de licenciamento.

### P2: Onde posso encontrar suporte para Aspose.3D?

 A2: O[Fórum Aspose.3D](https://forum.aspose.com/c/3d/18) é o lugar para buscar assistência e se conectar com a comunidade.

### Q3: Existe um teste gratuito disponível?

 A3: Sim, você pode explorar o[teste grátis](https://releases.aspose.com/) para experimentar os recursos do Aspose.3D.

### P4: Como posso obter uma licença temporária?

 A4: Você pode obter uma licença temporária[aqui](https://purchase.aspose.com/temporary-license/).

### P5: Onde posso encontrar a documentação?

 A5: O[documentação](https://reference.aspose.com/3d/java/) fornece orientação abrangente sobre como usar Aspose.3D para Java.