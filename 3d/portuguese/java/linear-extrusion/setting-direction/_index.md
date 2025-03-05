---
title: Definindo direção em extrusão linear com Aspose.3D para Java
linktitle: Definindo direção em extrusão linear com Aspose.3D para Java
second_title: API Java Aspose.3D
description: Domine a extrusão linear com Aspose.3D para Java! Siga nosso guia para uma programação 3D perfeita. Baixe agora para uma experiência cativante.
type: docs
weight: 12
url: /pt/java/linear-extrusion/setting-direction/
---
## Introdução

Bem-vindo ao nosso guia passo a passo sobre como definir a direção na extrusão linear usando Aspose.3D para Java. Aspose.3D é uma biblioteca Java poderosa que permite aos desenvolvedores trabalhar perfeitamente com arquivos e cenas 3D. Neste tutorial, focaremos na tarefa específica de definir a direção na extrusão linear, aprimorando sua proficiência em programação 3D.

## Pré-requisitos

Antes de mergulharmos no tutorial, certifique-se de ter os seguintes pré-requisitos em vigor:

- Conhecimento básico da linguagem de programação Java.
-  Biblioteca Aspose.3D instalada. Você pode baixá-lo em[aqui](https://releases.aspose.com/3d/java/).
- Um ambiente de desenvolvimento integrado (IDE) para Java, como Eclipse ou IntelliJ.

## Importar pacotes

Certifique-se de importar os pacotes necessários para iniciar seu projeto:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Etapa 1: inicializar o perfil base

 Comece inicializando o perfil base a ser extrudado. Neste exemplo, usamos um`RectangleShape` com um raio de arredondamento de 0,3:

```java
// O caminho para o diretório de documentos.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Etapa 2: crie uma cena

A seguir, crie uma cena 3D para conter os objetos extrudados:

```java
Scene scene = new Scene();
```

## Etapa 3: criar nós

Crie nós esquerdo e direito dentro da cena:

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Etapa 4: Execute a extrusão linear no nó esquerdo

 Execute a extrusão linear no nó esquerdo usando o`LinearExtrusion`classe com parâmetros especificados, como twist e slices:

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Etapa 5: Execute a extrusão linear no nó direito com direção

 Execute a extrusão linear no nó direito, introduzindo o`setDirection` propriedade para definir a direção da extrusão:

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Etapa 6: Salvar cena 3D

Salve a cena 3D no formato de arquivo desejado. Neste exemplo, salvamos como um arquivo Wavefront OBJ:

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Conclusão

Parabéns! Você aprendeu com sucesso como definir a direção na extrusão linear usando Aspose.3D para Java. Este tutorial aprimora suas habilidades em programação 3D e abre novas possibilidades para projetos criativos.

## Perguntas frequentes

### Q1: Posso usar Aspose.3D com outras linguagens de programação?

A1: Aspose.3D oferece suporte a várias linguagens de programação, incluindo .NET e Java.

### Q2. Existe um teste gratuito disponível para Aspose.3D?

 A2: Sim, você pode explorar os recursos do Aspose.3D com uma avaliação gratuita[aqui](https://releases.aspose.com/).

### Q3: Onde posso encontrar documentação detalhada para Aspose.3D para Java?

 A3: A documentação abrangente está disponível[aqui](https://reference.aspose.com/3d/java/).

### Q4: Como posso obter suporte para Aspose.3D?

 A4: Visite o[Fórum Aspose.3D](https://forum.aspose.com/c/3d/18) para qualquer assistência ou dúvida.

### Q5: Estão disponíveis licenças temporárias para Aspose.3D?

 A5: Sim, você pode obter uma licença temporária[aqui](https://purchase.aspose.com/temporary-license/).