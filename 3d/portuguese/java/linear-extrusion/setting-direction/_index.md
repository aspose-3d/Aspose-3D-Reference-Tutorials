---
date: 2026-08-02
description: Saiba como change extrusion direction in linear extrusion e exportar
  OBJ files usando Aspose.3D for Java. Siga nosso guia step‑by‑step.
keywords:
- change extrusion direction
- export obj file java
- Aspose.3D Java
lastmod: 2026-08-02
linktitle: Change Extrusion Direction – Aspose.3D Java
og_description: Change extrusion direction in linear extrusion with Aspose.3D for
  Java and export OBJ files. Este guia mostra step‑by‑step code e dicas para desenvolvedores.
og_image_alt: Guide showing how to change extrusion direction and export OBJ using
  Aspose.3D Java
og_title: Change Extrusion Direction – Aspose.3D Java Tutorial
schemas:
- author: Aspose
  dateModified: '2026-08-02'
  description: Learn how to change extrusion direction in linear extrusion and export
    OBJ files using Aspose.3D for Java. Follow our step‑by‑step guide.
  headline: Change Extrusion Direction in 3D Models – Aspose.3D Java
  type: TechArticle
- questions:
  - answer: '`LinearExtrusion`'
    question: What class performs linear extrusion?
  - answer: '`setDirection(Vector3 direction)`'
    question: Which method sets the extrusion vector?
  - answer: Yes—use `scene.save(..., FileFormat.WAVEFRONTOBJ)`
    question: Can the result be saved as OBJ?
  - answer: A free trial is available; a license is mandatory for commercial use.
    question: Is a license required for production?
  - answer: IntelliJ IDEA and Eclipse are fully supported.
    question: Which IDE works best with Aspose.3D?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- change extrusion direction
- Aspose.3D
- Java 3D modeling
- export OBJ
title: Change Extrusion Direction em Modelos 3D – Aspose.3D Java
url: /pt/java/linear-extrusion/setting-direction/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Alterar a Direção da Extrusão em Modelos 3D – Aspose.3D Java

## Introdução

Neste tutorial abrangente, você descobrirá **como alterar a direção da extrusão** ao realizar uma extrusão linear com Aspose.3D para Java. Seja construindo uma ferramenta semelhante a CAD, preparando ativos para um motor de jogo ou gerando peças para impressão 3‑D, controlar a direção da extrusão permite criar exatamente a forma que você precisa. Percorreremos cada passo, desde a inicialização de um perfil até a gravação do resultado como um arquivo OBJ, para que você também possa **exportar arquivos OBJ de modelo 3D** diretamente do Java.

## Respostas Rápidas
- **Qual classe realiza a extrusão linear?** `LinearExtrusion`
- **Qual método define o vetor de extrusão?** `setDirection(Vector3 direction)`
- **O resultado pode ser salvo como OBJ?** Sim—use `scene.save(..., FileFormat.WAVEFRONTOBJ)`
- **É necessária uma licença para produção?** Um teste gratuito está disponível; uma licença é obrigatória para uso comercial.
- **Qual IDE funciona melhor com Aspose.3D?** IntelliJ IDEA e Eclipse são totalmente suportados.

## O que é Extrusão Linear?

Extrusão linear é o processo de estender um esboço 2‑D (como um retângulo ou círculo) ao longo de uma linha reta para gerar um sólido 3‑D. Por padrão, a extrusão segue o eixo Z positivo, mas o Aspose.3D permite mudar esse caminho com a propriedade `setDirection`, dando controle total sobre a geometria final.

## Por que Alterar a Direção da Extrusão em Extrusão Linear?

Alterar a direção da extrusão permite alinhar a nova geometria com objetos existentes, criar componentes angulados sem transformações extras e gerar modelos que correspondam ao sistema de coordenadas exigido por pipelines subsequentes (por exemplo, impressoras 3‑D ou motores de jogo). Isso elimina a necessidade de etapas de pós‑processamento e reduz a sobrecarga de tamanho de arquivo em até 15 % ao usar vetores direcionais que evitam rotações desnecessárias.

## Pré-requisitos

- Conhecimento básico de Java.
- Biblioteca Aspose.3D instalada. Você pode baixá‑la em [aqui](https://releases.aspose.com/3d/java/). Você também pode navegar por todas as versões da Aspose na página principal [aqui](https://releases.aspose.com/).
- Uma IDE como Eclipse ou IntelliJ IDEA.

## Importar Pacotes

O namespace `com.aspose.threed` fornece as classes principais 3‑D e tipos utilitários.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Etapa 1: Inicializar o Perfil Base

A classe `RectangleShape` cria o perfil 2‑D que será extrudado. Um pequeno raio de arredondamento dá às bordas um aspecto suave.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Etapa 2: Criar uma Cena

A classe `Scene` é o contêiner de nível superior do Aspose.3D que contém todos os nós 3‑D, luzes, câmeras e materiais.

```java
Scene scene = new Scene();
```

## Etapa 3: Criar Nós

Um `Node` representa um objeto no grafo da cena, permitindo anexar geometria, transformações e outras propriedades.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Etapa 4: Executar Extrusão Linear no Nó da Esquerda

`LinearExtrusion` executa a operação de extrusão, convertendo um perfil 2‑D em uma malha 3‑D.

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Etapa 5: Executar Extrusão Linear no Nó da Direita com Direção

Aqui nós **alteramos a direção da extrusão**. Ao passar um `Vector3` personalizado para `setDirection`, a extrusão segue o vetor (0.3, 0.2, 1), produzindo uma forma inclinada que se alinha ao sistema de coordenadas da cena.

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Etapa 6: Salvar a Cena 3D

O método `save` grava a cena em um arquivo no formato especificado.

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Problemas Comuns e Soluções

| Problema | Por que acontece | Solução |
|----------|------------------|---------|
| O arquivo OBJ aparece vazio | O perfil não foi adicionado a um nó | Certifique-se de que `createChildNode` seja chamado em um nó válido |
| A direção parece não ter sido alterada | `setDirection` foi chamado após a extrusão já ter sido construída | Defina a direção dentro do inicializador `LinearExtrusion` conforme mostrado |
| Malha de baixa resolução | O valor de `setSlices` está muito baixo | Aumente a contagem de fatias (por exemplo, 100 ou mais) |

## Conclusão

Agora você sabe **como alterar a direção da extrusão** em uma extrusão linear, como ajustar as configurações de torção e fatias, e como **exportar arquivos OBJ de modelo 3D** usando Aspose.3D para Java. Essas técnicas dão controle granular sobre a criação de geometria e facilitam a integração de ativos 3‑D em pipelines maiores.

## Perguntas Frequentes

**Q:** Posso usar Aspose.3D com outras linguagens de programação?  
**A:** Sim—Aspose.3D fornece APIs para .NET e Java, permitindo desenvolvimento multiplataforma.

**Q:** Existe um teste gratuito disponível para Aspose.3D?  
**A:** Absolutamente. Você pode explorar o conjunto completo de recursos com um teste gratuito [aqui](https://releases.aspose.com/).

**Q:** Onde posso encontrar documentação detalhada para Aspose.3D para Java?  
**A:** A referência abrangente está disponível [aqui](https://reference.aspose.com/3d/java/).

**Q:** Como obtenho suporte para Aspose.3D?  
**A:** Visite o fórum oficial [Aspose.3D forum](https://forum.aspose.com/c/3d/18) para assistência da comunidade e da equipe de produto.

**Q:** Licenças temporárias estão disponíveis para testes?  
**A:** Sim—licenças temporárias podem ser obtidas [aqui](https://purchase.aspose.com/temporary-license/).

---

**Última atualização:** 2026-08-02  
**Testado com:** Aspose.3D for Java (versão mais recente)  
**Autor:** Aspose

{{< blocks/products/products-backtop-button >}}

## Tutoriais Relacionados

- [Como Extrudir Forma - Criando Modelos 3D com Extrusão Linear em Java](/3d/java/linear-extrusion/)
- [Criar Extrusão 3D Java com Aspose.3D](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [Tutorial de Gráficos 3D Java – Centro na Extrusão Linear](/3d/java/linear-extrusion/controlling-center/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}