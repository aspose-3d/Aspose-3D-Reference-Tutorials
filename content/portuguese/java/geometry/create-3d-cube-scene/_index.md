---
title: Crie uma cena de cubo 3D em Java com Aspose.3D
linktitle: Crie uma cena de cubo 3D em Java com Aspose.3D
second_title: API Java Aspose.3D
description: Explore as maravilhas dos gráficos de cena de cubo 3D com Aspose.3D para Java. Crie cenas impressionantes sem esforço.
type: docs
weight: 12
url: /pt/java/geometry/create-3d-cube-scene/
---
## Introdução

Bem-vindo ao fascinante mundo dos gráficos 3D em Java usando Aspose.3D! Neste tutorial, iremos guiá-lo através do processo de criação de uma impressionante cena de cubo 3D usando Aspose.3D para Java. Aspose.3D é uma biblioteca Java poderosa que fornece funcionalidades abrangentes para trabalhar com modelos e cenas 3D.

## Pré-requisitos

Antes de nos aprofundarmos na criação da cena do cubo 3D, certifique-se de ter os seguintes pré-requisitos em vigor:

1.  Java Development Kit (JDK): Certifique-se de ter o Java instalado em seu sistema. Você pode baixar a versão mais recente em[Site da Oracle](https://www.oracle.com/java/).

2.  Biblioteca Aspose.3D para Java: Baixe e instale a biblioteca Aspose.3D. Você pode encontrar o link para download[aqui](https://releases.aspose.com/3d/java/).

## Importar pacotes

Comece importando os pacotes necessários para o seu projeto Java:

```java
import java.io.File;

import com.aspose.threed.Box;
import com.aspose.threed.Cylinder;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Mesh;
import com.aspose.threed.Node;
import com.aspose.threed.Scene;
```

Agora, vamos dividir o processo de criação de uma cena de cubo 3D em várias etapas.

## Etapa 1: inicializar a cena

```java
// Inicializar objeto de cena
Scene scene = new Scene();
```

## Etapa 2: inicializar o nó e a malha

```java
// Inicializar objeto de classe Node
Node cubeNode = new Node("box");

// Chame a classe Common para criar malha usando o método construtor de polígono para definir a instância da malha
Mesh mesh = Common.createMeshUsingPolygonBuilder();

// Aponte o nó para a geometria da malha
cubeNode.setEntity(mesh);
```

## Etapa 3: adicionar nó à cena

```java
// Adicionar nó a uma cena
scene.getRootNode().getChildNodes().add(cubeNode);
```

## Passo 4: Salve a cena 3D

```java
// O caminho para o diretório de documentos.
String MyDir = "Your Document Directory";
MyDir = MyDir + "CubeScene.fbx";

// Salve cenas 3D nos formatos de arquivo suportados
scene.save(MyDir, FileFormat.FBX7400ASCII);
```

## Etapa 5: Imprimir mensagem de sucesso

```java
System.out.println("\nCube Scene created successfully.\nFile saved at " + MyDir);
```

## Conclusão

Parabéns! Você criou com sucesso uma cena de cubo 3D usando Aspose.3D para Java. Este tutorial fornece uma base sólida para explorar recursos mais avançados e liberar sua criatividade no mundo dos gráficos 3D.

## Perguntas frequentes

### Q1: Posso usar Aspose.3D para projetos comerciais?

 A1: Sim, você pode. Verifica a[página de compra](https://purchase.aspose.com/buy) para detalhes de licenciamento.

### Q2: Como posso obter suporte para Aspose.3D?

 A2: Visite o[Fórum Aspose.3D](https://forum.aspose.com/c/3d/18) para apoio comunitário.

### Q3: Existe um teste gratuito disponível?

 A3: Sim, você pode obter uma avaliação gratuita[aqui](https://releases.aspose.com/).

### Q4: Onde posso encontrar a documentação do Aspose.3D?

 A4: Consulte o[Documentação Aspose.3D](https://reference.aspose.com/3d/java/) para obter informações detalhadas.

### Q5: Como obter uma licença temporária para Aspose.3D?

 A5: Você pode obter uma licença temporária[aqui](https://purchase.aspose.com/temporary-license/).