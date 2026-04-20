---
date: 2026-03-23
description: Aprenda como adicionar torção na extrusão linear com Aspose.3D para .NET
  e descubra como usar a extrusão em projetos de modelagem 3D em ASP.NET.
linktitle: Twist Offset in Linear Extrusion
second_title: Aspose.3D .NET API
title: Como adicionar torção em extrusão linear usando Aspose.3D para .NET
url: /pt/net/3d-modeling/linear-extrusion/twist-offset-in-linear-extrusion/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Como Adicionar Torção em Extrusão Linear usando Aspose.3D para .NET

## Introdução

Se você está procurando um guia claro, passo a passo sobre **como adicionar torção** a uma extrusão linear, está no lugar certo. Neste tutorial percorreremos todo o processo com Aspose.3D para .NET, mostrando **como usar extrusão** para criar formas 3D dinâmicas que são perfeitas para *asp.net 3d modeling* cenários. Ao final, você terá um exemplo pronto‑para‑executar que demonstra o deslocamento da torção, fatias e a gravação do resultado como um arquivo OBJ.

## Respostas Rápidas
- **O que o “twist offset” faz?** Ele desloca o ponto inicial da torção ao longo do eixo da extrusão.  
- **Preciso de uma licença para executar o exemplo?** Uma licença temporária funciona para testes; uma licença completa é necessária para produção.  
- **Quais versões do .NET são suportadas?** .NET Framework 4.5+, .NET Core 3.1+, .NET 5/6+.  
- **Posso alterar o número de fatias?** Sim—ajuste a propriedade `Slices` para controlar a suavidade da malha.  
- **O formato de saída está limitado a OBJ?** Não, o Aspose.3D suporta muitos formatos; OBJ é usado aqui por simplicidade.

## O que é Twist Offset em Extrusão Linear?

Um twist offset define um deslocamento translacional aplicado à operação de torção. Em vez de girar ao redor do início exato da extrusão, a geometria começa a girar a partir do vetor de offset especificado, proporcionando maior controle artístico sobre a forma final.

## Por que Usar Aspose.3D para .NET?

- **API completa** – Lida com perfis, transformações e uma ampla variedade de formatos de arquivo.  
- **Multiplataforma** – Funciona no Windows, Linux e macOS com .NET Core.  
- **Desempenho otimizado** – Gera malhas limpas sem cálculos manuais.  
- **Documentação excelente** – Muitos exemplos para acelerar o desenvolvimento.

## Pré‑requisitos

Antes de começarmos, certifique‑se de que você tem:

- Biblioteca Aspose.3D para .NET: Baixe e instale a biblioteca a partir da [página de lançamento](https://releases.aspose.com/3d/net/).  
- Seu ambiente de desenvolvimento: Visual Studio, Rider ou qualquer IDE que suporte C#.

## Importar Namespaces

Primeiro, importe os namespaces que dão acesso às classes principais 3D.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

Essas instruções tornam as classes `Scene`, `LinearExtrusion`, `Vector3` e outros tipos essenciais disponíveis no seu código.

## Guia Passo a Passo

### Etapa 1: Inicializar o Perfil Base

Começamos com um perfil retangular simples e damos a ele um pequeno raio de arredondamento para que as bordas não fiquem perfeitamente afiadas.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

### Etapa 2: Criar uma Cena

Um `Scene` funciona como um contêiner para todos os nós, luzes, câmeras e geometria.

```csharp
Scene scene = new Scene();
```

### Etapa 3: Criar Nós

Dois nós filhos são adicionados à raiz da cena—um para a extrusão simples e outro para a versão torcida. O nó da esquerda é deslocado no eixo X para separação visual.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(18, 0, 0);
```

### Etapa 4: Extrusão Linear no Nó da Esquerda (Sem Twist Offset)

Aqui demonstramos uma extrusão básica com uma torção completa de 360° e 100 fatias para suavidade.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100 });
```

### Etapa 5: Extrusão Linear no Nó da Direita com Twist Offset

Agora aplicamos um twist offset de `(3, 0, 0)`. Isso move o início da torção três unidades ao longo do eixo X, criando uma hélice visivelmente deslocada.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100, TwistOffset = new Vector3(3, 0, 0) });
```

### Etapa 6: Salvar a Cena 3D

Finalmente, gravamos a cena em um arquivo OBJ. Altere o caminho de saída conforme necessário para o seu ambiente.

```csharp
scene.Save("Your Output Directory" + "TwistOffsetInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Problemas Comuns e Soluções

| Problema | Por que acontece | Solução |
|----------|------------------|---------|
| **A torção parece plana** | `Slices` está definido muito baixo, resultando em uma malha grosseira. | Aumente `Slices` (por exemplo, 200) para uma rotação mais suave. |
| **Objeto está fora do centro** | `TwistOffset` usa coordenadas globais; o nó pode já estar transladado. | Aplique o offset relativo à transformação local do nó ou ajuste a translação do nó conforme necessário. |
| **Arquivo não salvo** | Caminho de saída incorreto ou permissões de gravação ausentes. | Verifique se o diretório existe e se a aplicação tem permissão de gravação. |
| **Exceção de licença** | Executando sem uma licença válida em uma compilação não‑de teste. | Carregue uma licença temporária ou permanente antes de criar a cena. |

## Perguntas Frequentes

### Q1: Posso usar Aspose.3D para .NET com outras linguagens de programação?

**A1:** O Aspose.3D suporta principalmente linguagens .NET, mas a Aspose fornece bibliotecas semelhantes para Java e outras plataformas.

### Q2: Como obtenho uma licença temporária para Aspose.3D para .NET?

**A2:** Visite [este link](https://purchase.aspose.com/temporary-license/) para adquirir uma licença temporária para fins de teste.

### Q3: Existe um fórum da comunidade para Aspose.3D para .NET?

**A3:** Claro! Junte‑se à comunidade em [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) para interagir com outros desenvolvedores e buscar assistência.

### Q4: Existem exemplos e documentação adicionais disponíveis?

**A4:** Explore a [documentação](https://reference.aspose.com/3d/net/) para guias e exemplos extensos.

### Q5: Onde posso comprar Aspose.3D para .NET?

**A5:** Acesse [este link](https://purchase.aspose.com/buy) para efetuar a compra e desbloquear todo o potencial do Aspose.3D.

### Q6: Posso exportar o modelo para formatos além de OBJ?

**A6:** Sim—o Aspose.3D suporta FBX, STL, 3MF e muitos outros. Basta alterar o valor do enum `FileFormat` na chamada `Save`.

### Q7: Como “como adicionar torção” difere de uma rotação regular?

**A7:** Uma torção gira gradualmente o perfil ao longo do comprimento da extrusão, enquanto uma rotação regular aplica um único ângulo estático. O offset adiciona um deslocamento translacional antes que a rotação comece.

**Última atualização:** 2026-03-23  
**Testado com:** Aspose.3D para .NET (última versão)  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}