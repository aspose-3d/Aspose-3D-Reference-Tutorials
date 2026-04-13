---
date: 2026-02-22
description: Aprenda a criar extrusão 3D com fatias usando Aspose.3D para Java. Este
  guia passo a passo aborda extrusão linear, definição do raio de arredondamento e
  exportação de OBJ.
linktitle: Create 3D Extrusion with Slices – Aspose.3D for Java
second_title: Aspose.3D Java API
title: Criar extrusão 3D com fatias – Aspose.3D para Java
url: /pt/java/linear-extrusion/specifying-slices/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Criar Extrusão 3D com Fatias – Aspose.3D para Java

## Introdução

Se você precisa **criar extrusão 3d** objetos que pareçam suaves e precisos, controlar o número de fatias é fundamental. Neste tutorial, vamos percorrer como especificar fatias ao realizar uma extrusão linear com Aspose.3D para Java. Você verá por que a contagem de fatias importa, como definir um raio de arredondamento e como exportar o resultado como um arquivo OBJ que pode ser usado em qualquer pipeline 3D.

## Respostas Rápidas
- **O que as “fatias” controlam?** O número de seções transversais intermediárias usadas para aproximar a superfície da extrusão.  
- **Qual método define a contagem de fatias?** `LinearExtrusion.setSlices(int)`  
- **Posso mudar o raio de arredondamento do perfil?** Sim, via `RectangleShape.setRoundingRadius(double)`  
- **Qual formato de arquivo é usado neste exemplo?** Wavefront OBJ (`FileFormat.WAVEFRONTOBJ`)  
- **Preciso de licença para executar o código?** Uma avaliação gratuita funciona para teste; uma licença comercial é necessária para produção.

## O que é uma extrusão linear com fatias?

A extrusão linear pega um perfil 2‑D (como um retângulo) e o estica ao longo de uma linha reta para formar um sólido 3‑D. Ao especificar **fatias**, você informa ao Aspose.3D quantas etapas intermediárias gerar, o que influencia diretamente a suavidade de bordas curvas, como um retângulo arredondado.

## Por que usar Aspose.3D para Java para criar extrusão 3d?

* **Controle total** – Você pode ajustar a contagem de fatias, o raio de arredondamento e o formato de exportação programaticamente.  
* **Multiplataforma** – Funciona em qualquer ambiente com suporte a Java sem dependências nativas.  
* **Flexibilidade de exportação** – Salve diretamente em OBJ, FBX, STL e muitos outros formatos.

## Pré-requisitos

1. **Java Development Kit** – JDK 8 ou superior instalado.  
2. **Aspose.3D para Java** – Baixe a biblioteca no site oficial [aqui](https://releases.aspose.com/3d/java/).  
3. Uma IDE ou editor de texto de sua escolha.

## Importar Pacotes

Adicione o namespace Aspose.3D ao seu projeto para que você possa acessar as classes de modelagem 3‑D.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Guia Passo a Passo

### Etapa 1: Configurar a cena e definir o perfil

Primeiro criamos um `RectangleShape` e atribuímos a ele um **raio de arredondamento** para que os cantos fiquem suaves. Em seguida, inicializamos uma nova `Scene` que conterá toda a geometria.

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

### Etapa 2: **Criar objetos child node** para cada extrusão

Cada peça de geometria reside sob um `Node`. Aqui geramos dois nós irmãos – um para uma extrusão de baixa quantidade de fatias e outro para uma extrusão de alta quantidade de fatias – e movemos o nó da esquerda um pouco para o lado para que os resultados sejam fáceis de comparar.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Etapa 3: Executar extrusão linear e **definir fatias**

Agora realmente **criamos objetos de extrusão 3d**. O construtor `LinearExtrusion` recebe o perfil e a profundidade da extrusão. Usando uma **classe interna anônima** chamamos `setSlices` para controlar a suavidade. O nó da esquerda recebe apenas 2 fatias (grosseira), enquanto o nó da direita recebe 10 fatias (suave).

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

### Etapa 4: **Exportar OBJ** – salvar a cena

Finalmente gravamos a cena em um arquivo Wavefront OBJ, um formato amplamente suportado por editores 3‑D e motores de jogos. Isso demonstra a capacidade de **export obj java** do Aspose.3D.

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Problemas Comuns e Soluções

| Problema | Por que acontece | Correção |
|----------|------------------|----------|
| **Extrusão parece plana** | Contagem de fatias definida como 1 ou 0 | Garanta que `setSlices` seja chamado com um valor ≥ 2. |
| **Cantos arredondados parecem serrilhados** | Raio de arredondamento muito pequeno em relação à contagem de fatias | Aumente o raio ou a contagem de fatias para curvas mais suaves. |
| **Arquivo não encontrado ao salvar** | `MyDir` aponta para uma pasta inexistente | Crie o diretório antes ou use um caminho absoluto. |

## Perguntas Frequentes

**Q: Como posso baixar Aspose.3D para Java?**  
A: Você pode baixar a biblioteca [aqui](https://releases.aspose.com/3d/java/).

**Q: Onde posso encontrar a documentação do Aspose.3D?**  
A: Consulte a documentação [aqui](https://reference.aspose.com/3d/java/).

**Q: Existe uma avaliação gratuita disponível?**  
A: Sim, você pode explorar uma avaliação gratuita [aqui](https://releases.aspose.com/).

**Q: Como posso obter suporte para Aspose.3D?**  
A: Visite o fórum de suporte [aqui](https://forum.aspose.com/c/3d/18).

**Q: Posso comprar uma licença temporária?**  
A: Sim, uma licença temporária pode ser obtida [aqui](https://purchase.aspose.com/temporary-license/).

---

**Última atualização:** 2026-02-22  
**Testado com:** Aspose.3D para Java 24.11 (mais recente no momento da escrita)  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}