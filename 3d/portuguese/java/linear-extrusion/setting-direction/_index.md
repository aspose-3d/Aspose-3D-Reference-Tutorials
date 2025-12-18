---
date: 2025-12-18
description: Aprenda a criar cenas 3D e salvar arquivos OBJ usando Aspose.3D para
  Java. Siga nosso guia passo a passo para a direção de extrusão linear.
linktitle: Setting Direction in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Criar Cena 3D – Definir Direção de Extrusão Aspose.3D Java
url: /pt/java/linear-extrusion/setting-direction/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Criar Cena 3D – Definir Direção de Extrusão Aspose.3D Java

## Introdução

Neste tutorial você aprenderá **como criar cena 3d** objetos e controlar a direção da extrusão com Aspose.3D para Java. Seja construindo visualizações arquitetônicas, protótipos de produtos ou ativos de jogos, dominar a extrusão linear lhe dá a flexibilidade de modelar formas complexas rapidamente. Percorreremos cada passo, desde a adição de nós em Java até **exportar modelo 3d obj**, para que você possa ver o resultado instantaneamente.

## Respostas Rápidas
- **O que significa “create 3d scene”?** Significa inicializar um objeto Aspose.3D `Scene` que conterá toda a geometria, luzes e câmeras.  
- **Como definir a direção da extrusão?** Use o método `setDirection(Vector3)` em uma instância `LinearExtrusion`.  
- **Qual formato devo usar para exportar?** O formato OBJ (`FileFormat.WAVEFRONTOBJ`) é amplamente suportado para fluxos de trabalho 3‑D.  
- **Preciso de uma licença para Aspose.3D?** Um teste gratuito funciona para desenvolvimento; uma licença comercial é necessária para produção.  
- **Posso adicionar mais nós em Java?** Sim—use `scene.getRootNode().createChildNode()` para adicionar quantos objetos forem necessários.

## O que é um fluxo de trabalho “create 3d scene”?

Um fluxo de trabalho **create 3d scene** começa com um objeto `Scene` vazio, adiciona geometria (como perfis extrudados), posiciona‑a com transformações e, finalmente, salva a cena em um formato de arquivo como OBJ. Esse padrão é a espinha dorsal da maioria das aplicações 3‑D construídas com Aspose.3D.

## Por que definir a direção da extrusão?

Definir a direção da extrusão permite inclinar, girar ou distorcer a forma enquanto ela é extrudada, dando-lhe controle sobre a geometria final sem pós‑processamento extra. É especialmente útil para:

- Criar colunas afuniladas ou tubos de forma personalizada.  
- Alinhar extrusões com eixos não‑padrão em peças mecânicas.  
- Gerar formas artísticas para efeitos visuais.

## Pré-requisitos

- Conhecimento básico de Java.  
- Biblioteca Aspose.3D instalada – faça o download a partir de [here](https://releases.aspose.com/3d/java/).  
- Uma IDE como Eclipse ou IntelliJ IDEA.

## Importar Pacotes

Primeiro, importe as classes necessárias do Aspose.3D:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Etapa 1: Inicializar Perfil Base

Crie o perfil 2‑D que será extrudado. Neste exemplo usamos um retângulo arredondado:

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

> **Dica profissional:** Ajuste o raio de arredondamento para controlar quão afiadas ou suaves os cantos do retângulo aparecem antes da extrusão.

## Etapa 2: Criar uma Cena

Agora nós **create 3d scene** que hospedará nossos objetos:

```java
Scene scene = new Scene();
```

## Etapa 3: Adicionar Nós Java – Posicionando os Objetos

Vamos adicionar dois nós filhos (esquerda e direita) ao nó raiz da cena e mover o da esquerda um pouco para o lado:

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Etapa 4: Como extrudar – Nó Esquerdo (direção padrão)

Extruda o perfil no nó esquerdo usando a direção padrão do eixo Z. Também definimos uma torção completa de 360° e aumentamos a contagem de fatias para suavidade:

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Etapa 5: Como definir a direção – Nó Direito

Aqui nós **how to set direction** fornecendo um `Vector3` personalizado. Isso inclina a extrusão em direção ao vetor (0.3, 0.2, 1):

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Etapa 6: Salvar arquivo OBJ – Exportar modelo 3D

Finalmente, nós **save obj file** para ver o resultado em qualquer visualizador 3‑D:

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

Ao abrir o arquivo OBJ gerado, você verá dois retângulos extrudados: um com a direção padrão e outro inclinado de acordo com o vetor que definimos.

## Problemas Comuns e Soluções

| Problema | Motivo | Correção |
|----------|--------|----------|
| Arquivo OBJ aparece vazio | Cena não salva ou caminho incorreto | Verifique se `MyDir` aponta para uma pasta gravável e se o nome do arquivo termina com `.obj`. |
| Extrusão parece plana | `setSlices` muito baixo | Aumente `setSlices` (ex.: 200) para uma geometria mais suave. |
| Direção parece não alterada | Vetor não normalizado | Use um `Vector3` normalizado ou ajuste os valores para refletir a inclinação desejada. |

## Perguntas Frequentes

### Q1: Posso usar Aspose.3D com outras linguagens de programação?
**R1:** Aspose.3D suporta várias linguagens, incluindo .NET e Java.

### Q2: Existe uma versão de teste gratuita disponível para Aspose.3D?
**R2:** Sim, você pode explorar os recursos do Aspose.3D com uma versão de teste gratuita [here](https://releases.aspose.com/).

### Q3: Onde posso encontrar documentação detalhada para Aspose.3D para Java?
**R3:** A documentação abrangente está disponível [here](https://reference.aspose.com/3d/java/).

### Q4: Como posso obter suporte para Aspose.3D?
**R4:** Visite o [Aspose.3D forum](https://forum.aspose.com/c/3d/18) para qualquer assistência ou dúvidas.

### Q5: Licenças temporárias estão disponíveis para Aspose.3D?
**R5:** Sim, você pode obter uma licença temporária [here](https://purchase.aspose.com/temporary-license/).

**Última Atualização:** 2025-12-18  
**Testado com:** Aspose.3D 24.11 for Java  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}