---
title: Executando extrusão linear em Aspose.3D para Java
linktitle: Executando extrusão linear em Aspose.3D para Java
second_title: API Java Aspose.3D
description: Explore o mundo da modelagem 3D com Aspose.3D para Java. Aprenda a realizar extrusão linear sem esforço.
weight: 10
url: /pt/java/linear-extrusion/performing-linear-extrusion/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Executando extrusão linear em Aspose.3D para Java

## Introdução

Bem-vindo a este tutorial abrangente sobre como realizar extrusão linear em Aspose.3D para Java! Se você deseja aprimorar suas habilidades de modelagem 3D usando Java, você está no lugar certo. Neste tutorial, orientaremos você no processo de execução de extrusão linear usando Aspose.3D, uma poderosa biblioteca Java para modelagem 3D.

## Pré-requisitos

Antes de mergulhar no tutorial, certifique-se de ter os seguintes pré-requisitos em vigor:

1. Ambiente de Desenvolvimento Java: Certifique-se de ter um ambiente de desenvolvimento Java configurado em sua máquina.

2.  Biblioteca Aspose.3D: Baixe e instale a biblioteca Aspose.3D. Você pode encontrar a biblioteca[aqui](https://releases.aspose.com/3d/java/).

## Importar pacotes

Depois de configurar seu ambiente de desenvolvimento e instalar a biblioteca Aspose.3D, é hora de importar os pacotes necessários. Em seu código Java, inclua o seguinte:

```java
import com.aspose.threed.*;
```

Vamos detalhar cada etapa para garantir um entendimento claro.

## Etapa 1: definir diretório de documentos

Defina o caminho para o diretório do seu documento:

```java
String MyDir = "Your Document Directory";
```

Isto garante que o modelo 3D gerado será salvo no diretório especificado.

## Etapa 2: inicializar a forma base

Crie uma forma retangular como perfil base para extrusão:

```java
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

Ajuste o raio de arredondamento conforme necessário para personalizar a forma.

## Etapa 3: realizar extrusão linear

Execute a extrusão linear no perfil base:

```java
LinearExtrusion extrusion = new LinearExtrusion(profile, 10) {{ setSlices(100); setCenter(true); setTwist(360); setTwistOffset(new Vector3(10, 0, 0));}};
```

Aqui, extrudamos a forma em 10 unidades, definimos o número de fatias, habilitamos a centralização e aplicamos torção e deslocamento de torção.

## Etapa 4: criar cena 3D

Crie uma cena 3D e adicione a extrusão como nó filho:

```java
Scene scene = new Scene();
scene.getRootNode().createChildNode(extrusion);
```

## Etapa 5: salvar cena 3D

Salve a cena 3D gerada como um arquivo Wavefront OBJ:

```java
scene.save(MyDir +  "LinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

Agora, você executou com sucesso a extrusão linear usando Aspose.3D para Java!

## Conclusão

Parabéns! Você aprendeu como aproveitar o Aspose.3D for Java para realizar extrusão linear. Esta poderosa biblioteca abre um mundo de possibilidades para seus projetos de modelagem 3D.

## Perguntas frequentes

### Q1: O Aspose.3D é compatível com todas as versões Java?

A1: Aspose.3D foi projetado para funcionar com Java 1.6 e versões posteriores.

### Q2: Posso usar Aspose.3D para projetos comerciais?

A2: Sim, o Aspose.3D pode ser usado para projetos pessoais e comerciais. Verifique os detalhes do licenciamento[aqui](https://purchase.aspose.com/buy).

### Q3: Como posso obter suporte para Aspose.3D?

 A3: Visite o[Fórum Aspose.3D](https://forum.aspose.com/c/3d/18) para apoio da comunidade ou considere comprar um[licença temporária](https://purchase.aspose.com/temporary-license/) para suporte premium.

### Q4: Existem outros recursos de modelagem 3D no Aspose.3D?

 A4: Com certeza! Explore a extensa documentação[aqui](https://reference.aspose.com/3d/java/) para obter uma lista abrangente de recursos e exemplos.

### Q5: Existe uma avaliação gratuita disponível para Aspose.3D?

 A5: Sim, você pode acessar uma avaliação gratuita[aqui](https://releases.aspose.com/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
