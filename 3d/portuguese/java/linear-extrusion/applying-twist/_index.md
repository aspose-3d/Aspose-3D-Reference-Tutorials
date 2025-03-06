---
title: Aplicando Torção em Extrusão Linear com Aspose.3D para Java
linktitle: Aplicando Torção em Extrusão Linear com Aspose.3D para Java
second_title: API Java Aspose.3D
description: Aprenda como adicionar um toque especial aos seus modelos 3D usando Aspose.3D para Java. Siga nosso guia passo a passo para obter efeitos de extrusão linear aprimorados.
weight: 14
url: /pt/java/linear-extrusion/applying-twist/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aplicando Torção em Extrusão Linear com Aspose.3D para Java

## Introdução

Bem-vindo a este tutorial passo a passo sobre como aplicar uma torção na extrusão linear usando Aspose.3D para Java. Aspose.3D é uma biblioteca Java poderosa que permite aos desenvolvedores trabalhar com formatos de arquivo 3D, oferecendo funcionalidade robusta para criar, manipular e renderizar cenas 3D. Neste tutorial, exploraremos como aplicar um efeito de torção durante o processo de extrusão linear para aprimorar seus modelos 3D.

## Pré-requisitos

Antes de mergulhar no tutorial, certifique-se de ter os seguintes pré-requisitos em vigor:

- Ambiente de Desenvolvimento Java: Certifique-se de ter o Java instalado em seu sistema.
-  Biblioteca Aspose.3D: Baixe e instale a biblioteca Aspose.3D para Java do[Link para Download](https://releases.aspose.com/3d/java/).
-  Documentação: Consulte o[Documentação Aspose.3D](https://reference.aspose.com/3d/java/) para orientação abrangente.

## Importar pacotes

Antes de iniciar o processo de codificação, importe os pacotes necessários para o seu projeto Java. Aqui está um exemplo de como fazer isso:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Etapa 1: definir diretório de documentos

Comece definindo o diretório do documento onde sua cena 3D será salva.

```java
// ExStart:SetDocumentDirectory
String MyDir = "Your Document Directory";
// ExEnd:SetDocumentDirectory
```

## Etapa 2: inicializar o perfil base

Inicialize o perfil base a ser extrudado. Neste exemplo, usamos uma forma retangular com raio de arredondamento.

```java
// ExStart:InitializeBaseProfile
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
// ExEnd:InitializeBaseProfile
```

## Etapa 3: crie uma cena

Crie uma cena 3D para hospedar os nós extrudados.

```java
// ExStart:CreateScene
Scene scene = new Scene();
// ExEnd:CreateScene
```

## Etapa 4: criar nós

Crie nós esquerdo e direito na cena. Ajuste a translação do nó esquerdo.

```java
// ExStart:CriarNodes
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
// ExEnd:CriarNodes
```

## Etapa 5: Execute a extrusão linear com torção

Execute extrusão linear nos nós esquerdo e direito, aplicando propriedades de torção e fatias.

```java
// ExStart:Extrusão LinearComTorção
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(0); setSlices(100); }});
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(90); setSlices(100); }});
// ExEnd:Extrusão LinearComTorção
```

## Etapa 6: Salvar cena 3D

Salve a cena 3D no formato de arquivo Wavefront OBJ.

```java
// ExStart:Salvar3DScene
scene.save(MyDir + "TwistInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
//ExEnd:Save3DScene
```

## Conclusão

Parabéns! Você aplicou com sucesso uma torção na extrusão linear usando Aspose.3D para Java. Este tutorial forneceu um guia passo a passo detalhado para ajudá-lo a aprimorar seus recursos de modelagem 3D.

## Perguntas frequentes

### Q1: Posso usar Aspose.3D for Java para trabalhar com outros formatos de arquivo 3D?

A1: Sim, Aspose.3D suporta vários formatos de arquivo 3D, permitindo importar, exportar e manipular diversos tipos de arquivos.

### P2: Onde posso encontrar suporte para Aspose.3D para Java?

 A2: Visite o[Fórum Aspose.3D](https://forum.aspose.com/c/3d/18) para apoio e discussões da comunidade.

### Q3: Existe uma avaliação gratuita disponível para Aspose.3D para Java?

 A3: Sim, você pode acessar a versão de avaliação gratuita em[aqui](https://releases.aspose.com/).

### Q4: Como posso obter uma licença temporária do Aspose.3D para Java?

 A4: Obtenha uma licença temporária do[página de licença temporária](https://purchase.aspose.com/temporary-license/).

### Q5: Onde posso comprar Aspose.3D para Java?

 A5: Compre Aspose.3D para Java no site[página de compra](https://purchase.aspose.com/buy).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
