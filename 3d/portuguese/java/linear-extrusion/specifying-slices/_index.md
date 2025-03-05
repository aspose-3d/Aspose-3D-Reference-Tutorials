---
title: Especificando fatias em extrusão linear com Aspose.3D para Java
linktitle: Especificando fatias em extrusão linear com Aspose.3D para Java
second_title: API Java Aspose.3D
description: Aprenda a especificar fatias em extrusão linear usando Aspose.3D para Java. Eleve suas habilidades de modelagem 3D com este guia passo a passo.
type: docs
weight: 13
url: /pt/java/linear-extrusion/specifying-slices/
---
## Introdução

A criação de modelos 3D complexos geralmente requer mais do que apenas criatividade; exige um conhecimento profundo das ferramentas à sua disposição. Aspose.3D para Java é uma virada de jogo nesse aspecto. Neste tutorial, focaremos em um aspecto específico – a especificação de fatias em extrusão linear.

## Pré-requisitos

Antes de mergulhar no tutorial, certifique-se de ter os seguintes pré-requisitos em vigor:

1. Ambiente Java: Certifique-se de ter um ambiente de desenvolvimento Java configurado em seu sistema.
2.  Aspose.3D para Java: Baixe e instale a biblioteca Aspose.3D. Você pode encontrar os pacotes necessários[aqui](https://releases.aspose.com/3d/java/).

## Importar pacotes

No seu projeto Java, importe a biblioteca Aspose.3D. Isto é crucial para acessar as funcionalidades com as quais trabalharemos. Adicione a seguinte instrução de importação ao seu código:

```java
import com.aspose.threed.*;

import java.io.IOException;
```

Agora, vamos dividir o exemplo em várias etapas.

## Etapa 1: configurar a cena

Inicialize o perfil base a ser extrudado, neste caso, um`RectangleShape` com um raio de arredondamento especificado. Crie uma cena 3D para trabalhar.

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

## Etapa 2: criar nós

Gere nós esquerdo e direito dentro da cena. Ajuste a translação do nó esquerdo para variação espacial.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Etapa 3: Extrusão Linear com Fatias

Execute extrusão linear em ambos os nós, especificando o número de fatias para cada um. É aqui que a mágica acontece.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

## Etapa 4: salve a cena

Salve a cena 3D no formato desejado, neste caso, um arquivo Wavefront OBJ.

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Conclusão

Parabéns! Você aprendeu com sucesso como especificar fatias em extrusão linear usando Aspose.3D para Java. Essa habilidade abre novas possibilidades em sua jornada de modelagem 3D.

## Perguntas frequentes

### Q1: Como posso baixar Aspose.3D para Java?

 A1: Você pode baixar a biblioteca[aqui](https://releases.aspose.com/3d/java/).

### Q2: Onde posso encontrar a documentação do Aspose.3D?

 A2: Consulte a documentação[aqui](https://reference.aspose.com/3d/java/).

### Q3: Existe um teste gratuito disponível?

 A3: Sim, você pode explorar uma avaliação gratuita[aqui](https://releases.aspose.com/).

### Q4: Como posso obter suporte para Aspose.3D?

 A4: Visite o fórum de suporte[aqui](https://forum.aspose.com/c/3d/18).

### P5: Posso adquirir uma licença temporária?

 A5: Sim, uma licença temporária pode ser obtida[aqui](https://purchase.aspose.com/temporary-license/).