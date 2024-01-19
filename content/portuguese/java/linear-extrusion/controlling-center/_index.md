---
title: Centro de Controle em Extrusão Linear com Aspose.3D para Java
linktitle: Centro de Controle em Extrusão Linear com Aspose.3D para Java
second_title: API Java Aspose.3D
description: Explore o mundo dos gráficos 3D em Java com Aspose.3D. Controle o centro na extrusão linear sem esforço.
type: docs
weight: 11
url: /pt/java/linear-extrusion/controlling-center/
---
## Introdução

No mundo dos gráficos 3D e da programação Java, o controle do centro na extrusão linear desempenha um papel crucial para alcançar os efeitos desejados em seus projetos. Aspose.3D for Java fornece um kit de ferramentas poderoso para lidar com essas tarefas perfeitamente. Neste tutorial, mergulharemos no processo de controle do centro na extrusão linear usando Aspose.3D para Java, detalhando cada etapa para garantir uma compreensão suave e abrangente.

## Pré-requisitos

Antes de embarcarmos nesta jornada tutorial, certifique-se de ter os seguintes pré-requisitos em vigor:

1. Ambiente de Desenvolvimento Java: Certifique-se de ter um ambiente de desenvolvimento Java configurado em sua máquina.

2.  Aspose.3D para Java: Baixe e instale a biblioteca Aspose.3D. Você pode encontrar a biblioteca e sua documentação[aqui](https://reference.aspose.com/3d/java/).

3. Diretório de documentos: crie um diretório para armazenar seus documentos Java. Vamos chamá-lo de “Seu diretório de documentos”.

## Importar pacotes

Em seu ambiente de desenvolvimento Java, importe os pacotes necessários para Aspose.3D. Isso garante que seu código tenha acesso às funcionalidades fornecidas pela biblioteca.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Etapa 1: configurar o perfil base

Inicialize o perfil base a ser extrudado. Neste exemplo, usaremos uma forma retangular com raio de arredondamento de 0,3.

```java
// O caminho para o diretório de documentos.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Passo 2: Crie uma cena 3D

Construa a base do seu mundo 3D criando uma cena.

```java
Scene scene = new Scene();
```

## Etapa 3: criar nós esquerdo e direito

Estabeleça nós esquerdo e direito em sua cena. Esses nós servem como tela para seus objetos 3D.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Etapa 4: Extrusão Linear com Propriedade Central

Execute a extrusão linear no nó esquerdo sem centralizar e defina o número de fatias como 3.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

## Etapa 5: definir plano de solo para referência

Aprimore a representação visual adicionando um plano de solo ao nó esquerdo.

```java
left.createChildNode(new Box(0.01, 3, 3));
```

## Etapa 6: Extrusão Linear com Propriedade Central (Nó Direito)

Execute a extrusão linear no nó direito, desta vez centralizando a extrusão, e novamente defina o número de fatias para 3.

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

## Etapa 7: definir plano de solo para referência (nó direito)

Semelhante ao nó esquerdo, adicione um plano de terra ao nó direito para referência.

```java
right.createChildNode(new Box(0.01, 3, 3));
```

## Passo 8: Salve a cena 3D

Salve sua cena 3D no formato Wavefront OBJ.

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Conclusão

Controlar o centro na extrusão linear com Aspose.3D para Java abre possibilidades interessantes no desenvolvimento de gráficos 3D. Seguindo este guia passo a passo, você aprendeu como manipular a propriedade center, permitindo obter os efeitos visuais desejados em seus projetos Java.

## Perguntas frequentes

### Q1: Posso usar Aspose.3D para Java em projetos comerciais?

 A1: Sim, Aspose.3D for Java está disponível para uso comercial. Para detalhes de licenciamento, visite[aqui](https://purchase.aspose.com/buy).

### P2: Existe um teste gratuito disponível?

 A2: Sim, você pode explorar uma avaliação gratuita do Aspose.3D para Java[aqui](https://releases.aspose.com/).

### Q3: Onde posso encontrar suporte para Aspose.3D para Java?

 A3: O fórum da comunidade Aspose.3D é um ótimo lugar para buscar suporte e compartilhar suas experiências. Visite o fórum[aqui](https://forum.aspose.com/c/3d/18).

### P4: Preciso de uma licença temporária para testes?

A4: Sim, se você precisar de uma licença temporária para fins de teste, poderá obter uma[aqui](https://purchase.aspose.com/temporary-license/).

### P5: Onde posso encontrar a documentação?

 A5: A documentação do Aspose.3D para Java está disponível[aqui](https://reference.aspose.com/3d/java/).