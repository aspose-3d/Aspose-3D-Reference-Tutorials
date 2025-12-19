---
date: 2025-12-19
description: Aprenda a criar uma cena 3D e exportar um objeto 3D usando Twist Offset
  em Extrusão Linear com Aspose.3D para Java.
linktitle: Create 3d scene with Twist Offset – Aspose.3D Java
second_title: Aspose.3D Java API
title: Criar cena 3D com Twist Offset – Aspose.3D Java
url: /pt/java/linear-extrusion/using-twist-offset/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Criar cena 3d com Twist Offset – Aspose.3D for Java

## Introdução

No mundo dinâmico dos gráficos 3D, aprender a **criar cena 3d** com extrusão linear é um divisor de águas. Com Aspose.3D for Java, você pode elevar suas habilidades de modelagem 3D incorporando o recurso Twist Offset ao seu processo de extrusão linear. Este tutorial o guiará pelos passos de utilização do Twist Offset na Extrusão Linear usando Aspose.3D for Java, fornecendo as ferramentas para criar cenas 3D impressionantes.

## Respostas Rápidas
- **O que o Twist Offset faz?** Ele desloca o início da torção ao longo do caminho de extrusão, dando a você mais controle sobre a geometria.  
- **Qual formato de arquivo é usado para exportação?** O exemplo salva o modelo como um Wavefront OBJ (`.obj`).  
- **Preciso de uma licença para desenvolvimento?** Uma avaliação gratuita funciona para testes; uma licença comercial é necessária para produção.  
- **Qual versão do Java é necessária?** Java 8 ou posterior.  
- **Posso mudar o número de fatias?** Sim – o método `setSlices` define a suavidade da torção.

## Pré-requisitos

Antes de mergulhar no tutorial, certifique‑se de que você tem os seguintes pré-requisitos em vigor:

- **Ambiente Java:** Certifique‑se de que você tem um ambiente de desenvolvimento Java configurado em seu sistema.  
- **Aspose.3D for Java:** Baixe e instale a biblioteca Aspose.3D a partir do [link de download](https://releases.aspose.com/3d/java/).  
- **Documentação:** Familiarize‑se com a [documentação do Aspose.3D for Java](https://reference.aspose.com/3d/java/).  

## Importar Pacotes

No seu projeto Java, importe os pacotes necessários para começar a usar Aspose.3D for Java. Certifique‑se de incluir as bibliotecas necessárias para uma integração perfeita.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Etapa 1: Configurar o Ambiente

Comece configurando seu ambiente de desenvolvimento Java e garantindo que o Aspose.3D for Java esteja instalado corretamente.

## Etapa 2: Inicializar o Perfil Base

Crie um perfil base para extrusão, neste caso, um `RectangleShape` com raio de arredondamento de 0.3.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
// Initialize the base profile to be extruded
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Etapa 3: Criar uma Cena 3D

Construa uma cena 3D para abrigar seus objetos extrudados.

```java
// Create a scene
Scene scene = new Scene();
```

## Etapa 4: Criar Nós

Gere nós dentro da cena para representar diferentes entidades.

```java
// Create left node
Node left = scene.getRootNode().createChildNode();
// Create right node
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Etapa 5: Executar Extrusão Linear

Utilize extrusão linear nos nós esquerdo e direito com várias propriedades.

```java
// Perform linear extrusion on left node using twist and slices property
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});

// Perform linear extrusion on right node using twist, twist offset, and slices property
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setTwistOffset(new Vector3(3, 0, 0)); }});
```

## Etapa 6: Salvar a Cena 3D

Salve sua cena 3D recém‑criada com o formato de arquivo especificado.

```java
// Save 3D scene
scene.save(MyDir + "TwistOffsetInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Como salvar modelo 3d e exportar 3d obj

A chamada `scene.save` na etapa anterior **salva o modelo 3d** como um arquivo OBJ, que é um formato **export 3d obj** amplamente suportado. Você pode mudar o nome do arquivo ou escolher outro formato suportado (por exemplo, STL, FBX) ajustando o enum `FileFormat`.

## Conclusão

Parabéns! Você implementou com sucesso o Twist Offset na Extrusão Linear usando Aspose.3D for Java. Esse recurso poderoso abre um mundo de possibilidades para seus esforços de modelagem 3D, permitindo que você **crie cena 3d** com torções e deslocamentos intricados, e então **salve modelo 3d** em um formato pronto para pipelines subsequentes.

## Perguntas Frequentes

### Q1: Posso usar Aspose.3D for Java em projetos não comerciais?

R1: Sim, Aspose.3D for Java pode ser usado tanto em projetos comerciais quanto não comerciais. Verifique as [opções de licenciamento](https://purchase.aspose.com/buy) para mais detalhes.

### Q2: Onde posso encontrar suporte para Aspose.3D for Java?

R2: Visite o [fórum Aspose.3D for Java](https://forum.aspose.com/c/3d/18) para obter assistência e conectar‑se com a comunidade.

### Q3: Existe uma avaliação gratuita disponível para Aspose.3D for Java?

R3: Sim, você pode explorar uma versão de avaliação gratuita na [página de releases](https://releases.aspose.com/).

### Q4: Como obtenho uma licença temporária para Aspose.3D for Java?

R4: Obtenha uma licença temporária para seu projeto visitando [este link](https://purchase.aspose.com/temporary-license/).

### Q5: Existem exemplos e tutoriais adicionais disponíveis?

R5: Sim, consulte a [documentação](https://reference.aspose.com/3d/java/) para mais exemplos e tutoriais aprofundados.

## Perguntas Frequentes

**Q: Este tutorial faz parte de uma série de tutoriais Aspose 3d?**  
R: Sim – é um **tutorial aspose 3d** oficial que demonstra um recurso específico da biblioteca.

**Q: Posso usar uma forma diferente em vez de um retângulo?**  
R: Absolutamente. Qualquer implementação de `IProfile` (por exemplo, `CircleShape`, `PolygonShape` personalizado) pode ser extrudada.

**Q: O que acontece se eu omitir `setTwistOffset`?**  
R: A extrusão começará a torcer a partir da origem do perfil, resultando em uma torção simétrica.

**Q: Como aumento a suavidade da torção?**  
R: Aumente o valor passado para `setSlices`; contagens de fatias maiores produzem geometria mais suave.

**Q: Quais outros formatos de arquivo posso exportar além de OBJ?**  
R: Aspose.3D suporta STL, FBX, GLTF, 3MF e vários outros via o enum `FileFormat`.

---

**Última atualização:** 2025-12-19  
**Testado com:** Aspose.3D 24.11 for Java  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}