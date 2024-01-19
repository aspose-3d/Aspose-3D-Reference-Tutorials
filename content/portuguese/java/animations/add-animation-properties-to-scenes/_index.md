---
title: Adicionar propriedades de animação a cenas 3D em Java | Tutorial Aspose.3D
linktitle: Adicionar propriedades de animação a cenas 3D em Java | Tutorial Aspose.3D
second_title: API Java Aspose.3D
description: Aprimore seus projetos 3D baseados em Java com Aspose.3D. Siga nosso tutorial para adicionar propriedades de animação perfeitamente.
type: docs
weight: 10
url: /pt/java/animations/add-animation-properties-to-scenes/
---
## Introdução

Bem-vindo a este tutorial passo a passo sobre como adicionar propriedades de animação a cenas 3D em Java usando Aspose.3D. Se você deseja aprimorar seus projetos 3D com animações dinâmicas, você está no lugar certo. Neste guia, orientaremos você durante o processo, detalhando cada etapa para uma experiência perfeita.

## Pré-requisitos

Antes de mergulharmos no tutorial, certifique-se de ter os seguintes pré-requisitos em vigor:

- Conhecimento básico de programação Java.
-  Biblioteca Aspose.3D instalada. Caso contrário, baixe-o do[página de lançamento](https://releases.aspose.com/3d/java/).

## Importar pacotes

Em seu projeto Java, certifique-se de importar os pacotes necessários para aproveitar as funcionalidades do Aspose.3D:

```java
import com.aspose.threed.*;

import examples.geometry.Common;
```

Agora, vamos passar para o guia passo a passo.

## Etapa 1: inicializar a cena

```java
// Inicializar objeto de cena
Scene scene = new Scene();
```

## Etapa 2: criar malha usando Polygon Builder

```java
// Chame a classe Common para criar malha usando o método construtor de polígono para definir a instância da malha
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## Etapa 3: Criar nó de cubo com tradução

```java
// Cada nó do cubo tem sua própria tradução
Node cube1 = scene.getRootNode().createChildNode("cube1", mesh);
```

## Etapa 4: Encontre a propriedade de tradução

```java
// Encontre a propriedade de tradução no objeto de transformação do nó
Property translation = cube1.getTransform().findProperty("Translation");
```

## Etapa 5: criar ponto de vinculação

```java
// Crie um ponto de ligação com base na propriedade de tradução
BindPoint bindPoint = new BindPoint(scene, translation);
```

## Passo 6: Criar Curva de Animação

```java
// Crie a curva de animação no componente X da escala
KeyframeSequence kfs = new KeyframeSequence();

// Adicionar quadros-chave para o componente X
kfs.add(0, 10.0f, Interpolation.BEZIER);
kfs.add(3, 20.0f, Interpolation.BEZIER);
kfs.add(5, 30.0f, Interpolation.LINEAR);

// Vincule a sequência de quadros-chave ao componente X
bindPoint.bindKeyframeSequence("X", kfs);
```

## Etapa 7: Repita para o componente Z

```java
// Repita o processo para o componente Z
kfs = new KeyframeSequence();
kfs.add(0, 10.0f, Interpolation.BEZIER);
kfs.add(3, -10.0f, Interpolation.BEZIER);
kfs.add(5, 0.0f, Interpolation.LINEAR);

bindPoint.bindKeyframeSequence("Z", kfs);
```

## Passo 8: Salve a cena 3D

```java
// Especifique o diretório para salvar a cena 3D
String MyDir = "Your Document Directory";
MyDir = MyDir + "PropertyToDocument.fbx";

//Salve cenas 3D nos formatos de arquivo suportados
scene.save(MyDir, FileFormat.FBX7500ASCII);
```

## Conclusão

Parabéns! Você adicionou propriedades de animação à sua cena 3D com sucesso usando Aspose.3D em Java. Experimente diferentes parâmetros para obter as animações desejadas para seus projetos.

## Perguntas frequentes

### Q1: Posso usar Aspose.3D para projetos comerciais?

 A1: Sim, você pode. Visite a[página de compra](https://purchase.aspose.com/buy) para detalhes de licenciamento.

### P2: Existe um teste gratuito disponível?

 A2: Certamente! Pegue o seu[teste grátis](https://releases.aspose.com/) antes de tomar uma decisão de compra.

### Q3: Onde posso encontrar suporte para Aspose.3D?

 A3: Junte-se à comunidade em[Fórum Aspose.3D](https://forum.aspose.com/c/3d/18) para assistência.

### Q4: Como posso obter uma licença temporária?

 A4: Obtenha um[licença temporária](https://purchase.aspose.com/temporary-license/) para o seu período de avaliação.

### Q5: Existem mais tutoriais disponíveis?

 A5: Explore o abrangente[documentação](https://reference.aspose.com/3d/java/) para tutoriais adicionais.