---
date: 2026-01-07
description: Aprenda a extrusar linearmente um perfil 2D e exportar o modelo 3D OBJ
  usando Aspose.3D para .NET. Este tutorial de extrusão linear orienta você passo
  a passo.
linktitle: Performing Linear Extrusion
second_title: Aspose.3D .NET API
title: Como extrudir linearmente com Aspose.3D para .NET
url: /pt/net/3d-modeling/linear-extrusion/performing-linear-extrusion/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# How to Linear Extrude with Aspose.3D for .NET

## Introdução

Bem‑vindo ao nosso **tutorial de extrusão linear**! Neste guia você descobrirá **como fazer linear extrude** um perfil 2‑D e transformá‑lo em um objeto 3‑D completo usando Aspose.3D para .NET. Seja você quem está construindo uma aplicação no estilo CAD ou apenas precisa **exportar 3d model obj** para processamento posterior, este passo a passo lhe dará a confiança necessária para adicionar criação de geometria poderosa aos seus projetos.

## Respostas Rápidas
- **O que é extrusão linear?** Extender uma forma 2‑D ao longo de um caminho reto para criar um sólido 3‑D.  
- **Qual biblioteca usamos?** Aspose.3D para .NET.  
- **Preciso de licença?** Uma licença temporária funciona para testes; uma licença completa é necessária para produção.  
- **Posso exportar para OBJ?** Sim – a cena final é salva como um arquivo Wavefront OBJ.  
- **Quantas linhas de código?** Menos de 30 linhas de C# mais comentários explicativos.

## O que é Extrusão Linear?

A extrusão linear pega um perfil plano (como um retângulo ou círculo) e o varre ao longo de uma linha reta, opcionalmente adicionando torções, escalonamentos ou deslocamentos. O resultado é um sólido que pode ser renderizado, editado ou exportado para uso em outras ferramentas 3‑D.

## Por que usar Aspose.3D para Extrusão Linear?

* **Zero dependência:** Não há necessidade de kernels CAD externos.  
* **Suporte total ao .NET:** Funciona com .NET Framework, .NET Core e .NET 5/6+.  
* **Flexibilidade de exportação:** Salve diretamente em OBJ, STL, FBX e muitos outros formatos.  
* **API rica:** Controle fatias, torção e deslocamentos com apenas algumas propriedades.

## Pré‑requisitos

Antes de começar, certifique‑se de que você tem:

1. **Aspose.3D instalado** – faça o download a partir de [aqui](https://releases.aspose.com/3d/net/).  
2. **Acesso à documentação** – siga o guia de configuração [aqui](https://reference.aspose.com/3d/net/).  
3. Um ambiente de desenvolvimento .NET (Visual Studio, VS Code ou Rider) com os namespaces necessários referenciados.

## Importar Namespaces

Inclua os namespaces essenciais para desbloquear a funcionalidade do Aspose.3D:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

Esses namespaces dão acesso a `Scene`, `LinearExtrusion`, `RectangleShape` e classes utilitárias como `Vector3`.

## Executando a Extrusão Linear

A seguir está o fluxo de trabalho completo. Cada passo é explicado em linguagem simples antes do bloco de código correspondente, para que você possa acompanhar sem adivinhar o que o código faz.

### Passo 1: Inicializar o Perfil Base

Primeiro, crie a forma 2‑D que será extrudada. Neste exemplo usamos um retângulo com um pequeno raio de arredondamento.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

*Por que isso importa:* O perfil define a seção transversal do objeto 3‑D final. Ajuste `RoundingRadius`, largura ou altura para obter silhuetas diferentes.

### Passo 2: Aplicar Extrusão Linear

Agora varremos o perfil 10 unidades ao longo do eixo Z, adicionando 100 fatias para suavidade, centralizando a geometria e aplicando uma torção completa de 360° com um deslocamento.

```csharp
var extrusion = new LinearExtrusion(profile, 10) { Slices = 100, Center = true, Twist = 360, TwistOffset = new Vector3(10, 0, 0) };
```

*Dica profissional:* Brinque com `Slices` para equilibrar desempenho vs. qualidade visual e experimente `Twist` para efeitos espirais.

### Passo 3: Criar uma Cena

Um `Scene` atua como o contêiner para todas as entidades 3‑D — pense nele como a tela.

```csharp
Scene scene = new Scene();
```

### Passo 4: Adicionar a Extrusão à Cena

Anexe a geometria extrudada ao nó raiz da cena para que ela faça parte da hierarquia renderizável.

```csharp
scene.RootNode.CreateChildNode(extrusion);
```

### Passo 5: Salvar o Modelo 3‑D

Finalmente, exporte a cena para um arquivo OBJ amplamente suportado. Isso demonstra a capacidade de **export 3d model obj** do Aspose.3D.

```csharp
scene.Save(RunExamples.GetOutputFilePath("LinearExtrusion.obj"), FileFormat.WavefrontOBJ);
```

Ao abrir o `LinearExtrusion.obj` resultante em qualquer visualizador 3‑D, você verá um prisma retangular torcido — exatamente o que o código descreve.

## Armadilhas Comuns & Dicas

| Problema | Por que acontece | Como corrigir |
|----------|------------------|---------------|
| **Perfil não visível** | Esquecendo de adicionar a extrusão à cena. | Garanta que `CreateChildNode` seja chamado. |
| **Torção parece plana** | `Slices` muito baixo, gerando geometria grosseira. | Aumente `Slices` (ex.: 200) para uma torção mais suave. |
| **Exportação falha** | Pasta de saída não existe ou falta permissão de gravação. | Use `RunExamples.GetOutputFilePath` ou crie o diretório manualmente. |
| **Escala inesperada** | `Center` definido como `false` desloca a geometria. | Defina `Center = true` a menos que precise de offset. |

## Perguntas Frequentes

### Q1: O Aspose.3D é adequado para iniciantes?

R1: Absolutamente! Aspose.3D oferece uma API amigável, e este tutorial orienta você pelos fundamentos da extrusão linear.

### Q2: Posso usar Aspose.3D em projetos comerciais?

R2: Sim, o Aspose.3D possui opções de licenciamento tanto para uso pessoal quanto comercial. Consulte [aqui](https://purchase.aspose.com/buy) para detalhes.

### Q3: Como obter licenças temporárias para testes?

R3: Visite [este link](https://purchase.aspose.com/temporary-license/) para obter licenças temporárias para fins de teste.

### Q4: Onde encontrar suporte da comunidade?

R4: Junte‑se ao [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) para conectar‑se com uma comunidade vibrante e buscar assistência.

### Q5: Existe uma versão de avaliação gratuita?

R5: Claro! Baixe a versão de avaliação gratuita [aqui](https://releases.aspose.com/) para experimentar as capacidades do Aspose.3D em primeira mão.

---

**Última atualização:** 2026-01-07  
**Testado com:** Aspose.3D 24.11 para .NET  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

## PALAVRAS‑CHAVE‑ALVO:

**Palavra‑chave principal (MAIOR PRIORIDADE):**
how to linear extrude

**Palavras‑chave secundárias (SUPORTE):**
export 3d model obj, linear extrusion tutorial

**Estratégia de Integração de Palavras‑chave:**
1. Palavra‑chave principal: Use 3‑5 vezes (título, meta, primeiro parágrafo, cabeçalho H2, corpo)  
2. Palavras‑chave secundárias: Use 1‑2 vezes cada (cabeçalhos, texto do corpo)  
3. Todas as palavras‑chave devem ser integradas naturalmente — priorize a legibilidade sobre a contagem  
4. Se uma palavra‑chave não se encaixar naturalmente, use uma variação semântica ou omita