---
date: 2026-01-09
description: Aprenda a criar cenas 3D usando Aspose.3D para .NET, incluindo exportação
  para Wavefront OBJ e como torcer o deslocamento em extrusão linear.
linktitle: Twist Offset in Linear Extrusion
second_title: Aspose.3D .NET API
title: Como criar cena 3D com deslocamento de torção em extrusão linear
url: /pt/net/3d-modeling/linear-extrusion/twist-offset-in-linear-extrusion/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Criar Cena 3D: Deslocamento de Torção em Extrusão Linear

## Introdução

## Respostas Rápidas
- **O que o “twist offset” faz?** Ele desloca o ponto inicial da torção ao longo do eixo de extrusão.  
- **Qual método exporta Wavefront OBJ?** `scene.Save(..., FileFormat.WavefrontOBJ)`.  
- **Preciso de uma licença para executar o exemplo?** Uma licença temporária funciona para testes; uma licença completa é necessária para produção.  
- **Quais versões do .NET são suportadas?** .NET Framework 4.5+, .NET Core 3.1+, .NET 5/6+.  
- **Quantas fatias são recomendadas para torções suaves?** Cerca de 100 fatias oferecem um bom equilíbrio entre qualidade e desempenho.

## O que é **create 3d scene**?

Criar uma cena 3‑D significa construir uma estrutura hierárquica que contém geometria, luzes, câmeras e transformações. Aspose.3D fornece a classe `Scene` que atua como o contêiner raiz para todos os nós que você adiciona.

## Por que usar **linear extrusion twist**?

Uma extrusão linear com torção permite transformar um perfil 2‑D em um objeto 3‑D em espiral — perfeito para parafusos, molas ou colunas decorativas. Adicionar um deslocamento de torção oferece ainda mais controle sobre o início da rotação, permitindo designs assimétricos.

## Pré-requisitos

- Biblioteca Aspose.3D for .NET: Baixe e instale a biblioteca a partir da [release page](https://releases.aspose.com/3d/net/).  
- Seu Ambiente de Desenvolvimento: Visual Studio 2022 (ou qualquer IDE C#) pronto para desenvolvimento .NET.

## Importar Namespaces

Comece importando os namespaces necessários para acessar a funcionalidade do Aspose.3D.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Guia Passo a Passo

### Etapa 1: Inicializar o Perfil Base  

Usaremos um retângulo com um pequeno raio de arredondamento como o perfil que será extrudado.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

### Etapa 2: Criar uma Cena  

Este é o contêiner onde criaremos nós **create 3d scene**.

```csharp
Scene scene = new Scene();
```

### Etapa 3: Criar Nós  

Dois nós irmãos são adicionados à raiz — um para a extrusão regular e outro para a versão com deslocamento.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(18, 0, 0);
```

### Etapa 4: Extrusão Linear no Nó da Esquerda (torção básica)  

Aqui demonstramos uma **linear extrusion twist** clássica sem nenhum deslocamento.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100 });
```

### Etapa 5: Extrusão Linear no Nó da Direita com **Twist Offset**  

Agora aplicamos a técnica **how to twist offset** fornecendo um vetor `TwistOffset`.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100, TwistOffset = new Vector3(3, 0, 0) });
```

### Etapa 6: **Export Wavefront OBJ**  

Finalmente, salve a cena montada em um arquivo OBJ para que você possa visualizá-lo em qualquer visualizador 3‑D padrão.

```csharp
scene.Save("Your Output Directory" + "TwistOffsetInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Problemas Comuns & Dicas

- **A torção parece plana?** Aumente o valor de `Slices` para uma geometria mais suave.  
- **Deslocamento não visível?** Certifique‑se de que o vetor `TwistOffset` não seja zero e esteja alinhado com a direção da extrusão.  
- **Arquivo OBJ sem texturas?** OBJ armazena apenas geometria; use arquivos MTL para definições de material, se necessário.

## Perguntas Frequentes

**Q: Posso usar Aspose.3D for .NET com outras linguagens de programação?**  
A: Aspose.3D tem como alvo principalmente linguagens .NET, mas bibliotecas equivalentes existem para Java e outras plataformas.

**Q: Como obtenho uma licença temporária para Aspose.3D for .NET?**  
A: Visite [this link](https://purchase.aspose.com/temporary-license/) para adquirir uma licença temporária para fins de teste.

**Q: Existe um fórum da comunidade para Aspose.3D for .NET?**  
A: Claro! Junte‑se à comunidade em [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) para interagir com outros desenvolvedores e buscar ajuda.

**Q: Existem exemplos e documentação adicionais disponíveis?**  
A: Explore a [documentation](https://reference.aspose.com/3d/net/) para guias e exemplos extensos.

**Q: Onde posso comprar Aspose.3D for .NET?**  
A: Acesse [this link](https://purchase.aspose.com/buy) para efetuar a compra e desbloquear todo o potencial do Aspose.3D.

## Conclusão

Neste **aspose 3d tutorial** você aprendeu como **create 3d scene**, aplicar uma **linear extrusion twist**, controlar o **twist offset** e **export Wavefront OBJ** arquivos. Essas técnicas permitem adicionar geometria sofisticada e torcida a qualquer projeto 3‑D com apenas algumas linhas de código.

---

**Última Atualização:** 2026-01-09  
**Testado com:** Aspose.3D 24.11 for .NET  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}