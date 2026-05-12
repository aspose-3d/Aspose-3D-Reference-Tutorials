---
date: 2026-03-23
description: Aprenda a criar extrusão com torção usando Aspose.3D para .NET. Este
  guia passo a passo cobre técnicas de extrusão linear com torção.
linktitle: Twist in Linear Extrusion
second_title: Aspose.3D .NET API
title: Como criar extrusão com torção em extrusão linear
url: /pt/net/3d-modeling/linear-extrusion/twist-in-linear-extrusion/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Como Criar Extrusão com Torção em Extrusão Linear

## Introdução

Se você está desenvolvendo aplicações .NET que precisam de visuais 3D impressionantes, logo descobrirá que **como criar extrusão** é uma habilidade fundamental. Aspose.3D for .NET oferece uma API limpa e de alto desempenho para transformar perfis 2‑D simples em modelos 3‑D sofisticados — especialmente quando você adiciona uma torção. Neste tutorial, percorreremos cada passo, desde a configuração da cena até a gravação do arquivo OBJ final, para que você possa ver o poder da torção em extrusão linear em ação.

## Respostas Rápidas
- **Qual é a classe principal para extrusão?** `LinearExtrusion`
- **Qual propriedade adiciona rotação?** `Twist`
- **Quantas fatias dão resultados suaves?** Aproximadamente 100 fatias (ajuste conforme necessário)
- **Posso usar outras formas?** Sim, qualquer `IProfile` como círculos, polígonos ou curvas personalizadas
- **Qual formato de arquivo é usado no exemplo?** Wavefront OBJ (`.obj`)

## Pré-requisitos

Antes de mergulharmos, certifique‑se de que você tem o seguinte:

- Aspose.3D for .NET instalado. Se ainda não o baixou, obtenha **[aqui](https://releases.aspose.com/3d/net/)**.
- Um ambiente de desenvolvimento .NET funcional (Visual Studio, VS Code ou qualquer IDE de sua preferência).
- Familiaridade básica com a sintaxe C# e conceitos orientados a objetos.

## Importar Namespaces

Em qualquer projeto .NET, o uso adequado de namespaces é crucial. Comece importando os namespaces necessários para aproveitar efetivamente as funcionalidades do Aspose.3D. Aqui está um trecho para guiá‑lo:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Guia Passo a Passo

### Etapa 1: Inicializar o Perfil Base

Começamos definindo a forma que será extrudada. Neste exemplo usamos um retângulo com um pequeno raio de arredondamento para dar às bordas uma curva sutil.

```csharp
// Initialize the base profile to be extruded
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

### Etapa 2: Criar uma Cena 3D

Um objeto `Scene` funciona como a tela onde todas as entidades 3‑D vivem. Pense nele como o palco para sua extrusão.

```csharp
// Create a scene 
Scene scene = new Scene();
```

### Etapa 3: Adicionar Nós Esquerdo e Direito

Nós permitem organizar objetos hierarquicamente. Criaremos dois nós irmãos — um para uma extrusão reta e outro para a versão torcida.

```csharp
// Create left node
var left = scene.RootNode.CreateChildNode();
// Create right node
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
```

### Etapa 4: Executar Extrusão Linear com Torção no Nó Esquerdo

A propriedade `Twist` controla quanto o perfil gira enquanto está sendo extrudado. Definir **0** resulta em uma extrusão reta clássica.

```csharp
// Twist property defines the degree of the rotation while extruding the profile
// Perform linear extrusion on the left node using twist and slices property
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 0, Slices = 100 });
```

### Etapa 5: Executar Extrusão Linear com Torção no Nó Direito

Agora aplicamos uma torção de 90 graus ao mesmo perfil. Isso demonstra claramente o efeito de **extrusão linear com torção**.

```csharp
// Perform linear extrusion on the right node using twist and slices property
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 90, Slices = 100 });
```

### Etapa 6: Salvar a Cena 3D

Por fim, exporte a cena para um formato que você possa visualizar em qualquer visualizador 3‑D. O exemplo usa Wavefront OBJ, mas o Aspose.3D suporta muitos outros formatos também.

```csharp
// Save 3D scene
scene.Save("Your Output Directory" + "TwistInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Por que Usar Extrusão Linear com Torção?

- **Prototipagem rápida:** Transforme esboços 2D em peças 3D sem modelagem manual.
- **Flexibilidade de design:** Ajuste o valor `Twist` para criar espirais, nervuras helicoidais ou recursos decorativos.
- **Desempenho amigável:** O parâmetro `Slices` permite equilibrar fidelidade visual e velocidade de execução.

## Problemas Comuns & Dicas

- **Muitas fatias:** Embora 100 fatias pareçam suaves, valores extremamente altos podem desacelerar a renderização. Teste com contagens menores se o desempenho se tornar um problema.
- **Valores de torção negativos:** Um `Twist` negativo gira na direção oposta — útil para designs espelhados.
- **Caminhos de arquivo:** Certifique‑se de que o diretório de saída exista e que você tenha permissão de escrita; caso contrário, `scene.Save` lançará uma exceção.

## Conclusão

Neste tutorial demonstramos **como criar extrusão** com torção usando Aspose.3D for .NET. Ajustando as propriedades `Twist` e `Slices`, você pode gerar uma ampla variedade de formas, desde barras torcidas simples até estruturas helicoidais complexas, tudo com apenas algumas linhas de código.

## Perguntas Frequentes

**Q: Posso aplicar extrusão linear com torção a outras formas?**  
A: Absolutamente! Qualquer classe que implemente `IProfile` — como `CircleShape`, `PolygonShape` ou uma spline personalizada — pode ser extrudada com torção.

**Q: O que a propriedade `Twist` realmente representa?**  
A: Ela especifica o ângulo total de rotação (em graus) aplicado ao perfil ao longo do comprimento da extrusão.

**Q: Aumentar o número de fatias afetará o uso de memória?**  
A: Sim, mais fatias geram mais vértices e faces, o que consome memória adicional e pode impactar o desempenho em dispositivos de baixo custo.

**Q: Posso combinar extrusão linear com outros recursos do Aspose.3D?**  
A: Definitivamente. Você pode aplicar materiais, texturas ou até operações booleanas após a extrusão para criar modelos ainda mais ricos.

**Q: Onde posso obter ajuda ou discutir ideias com outros desenvolvedores?**  
A: Junte‑se à comunidade Aspose.3D no **[Aspose Forum](https://forum.aspose.com/c/3d/18)** para suporte, exemplos e discussões.

---

**Última atualização:** 2026-03-23  
**Testado com:** Aspose.3D 24.11 for .NET  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}