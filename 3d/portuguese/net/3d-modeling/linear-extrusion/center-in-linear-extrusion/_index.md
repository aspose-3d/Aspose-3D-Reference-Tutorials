---
date: 2026-01-07
description: Aprenda a adicionar um plano de base ao realizar extrusão linear com
  Aspose.3D para .NET e exportar arquivos Wavefront OBJ. Domine técnicas de centralização
  e posicionamento da base em modelagem 3‑D.
linktitle: Add Ground Plane and Center in Linear Extrusion
second_title: Aspose.3D .NET API
title: Adicionar Plano de Base e Centro na Extrusão Linear
url: /pt/net/3d-modeling/linear-extrusion/center-in-linear-extrusion/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Adicionar Plano de Base e Centralizar na Extrusão Linear

## Introdução

Bem‑vindo a este guia completo sobre como dominar a extrusão linear usando Aspose.3D para .NET. Se você deseja **adicionar um plano de base** aos seus modelos e **exportar arquivos Wavefront OBJ** mantendo a extrusão centralizada, está no lugar certo. Neste tutorial, vamos explorar a técnica de extrusão linear, focando especificamente no aspecto de centralização e em como um plano de base ajuda a visualizar o resultado de forma mais clara.

## Respostas Rápidas
- **O que “adicionar plano de base” realiza?** Ele fornece uma referência visual que facilita ver onde a extrusão se posiciona no plano X‑Z.  
- **Qual formato é usado para exportar o modelo?** A cena é salva como um arquivo Wavefront OBJ (`FileFormat.WavefrontOBJ`).  
- **Preciso de licença para executar o código?** Uma avaliação gratuita funciona para desenvolvimento; uma licença permanente é necessária para produção.  
- **Posso alterar o comprimento da extrusão?** Sim – modifique o segundo parâmetro de `LinearExtrusion`.  
- **A centralização é opcional?** Definir `Center = true` centraliza a extrusão em torno do perfil; `false` alinha-a a um lado.

## Pré‑requisitos

Antes de embarcarmos nesta jornada empolgante, certifique‑se de que você possui os seguintes pré‑requisitos:

- Compreensão básica da linguagem de programação C#.  
- Visual Studio instalado em sua máquina.  
- Biblioteca Aspose.3D para .NET, que pode ser baixada na [Aspose.3D .NET Documentation](https://reference.aspose.com/3d/net/).  
- Garanta acesso à [Aspose.3D .NET Documentation](https://reference.aspose.com/3d/net/) para consulta ao longo do tutorial.

## Importar Namespaces

Para começar, vamos importar os namespaces necessários. Eles servirão de base para nossa obra‑prima de modelagem 3D.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Etapa 1: Inicializar o Perfil Base

Começamos definindo um perfil retangular que será extrudado. O `RoundingRadius` adiciona um leve arredondamento aos cantos.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## Etapa 2: Criar uma Cena 3D

Um objeto `Scene` atua como contêiner para toda a geometria, luzes e câmeras.

```csharp
Scene scene = new Scene();
```

## Etapa 3: Criar Nós Esquerdo e Direito

Dois nós irmãos são criados sob a raiz. Um demonstrará a extrusão **sem** centralização, o outro **com** centralização. Também translacionamos o nó esquerdo para que os dois exemplos não se sobreponham.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(5, 0, 0);
```

## Etapa 4: Executar Extrusão Linear no Nó Esquerdo (Sem Central)

Aqui extrudamos o perfil sem centralização. Observe a flag `Center = false`.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 2) { Center = false, Slices = 3 });
```

## Etapa 5: Adicionar Plano de Base para Referência (Nó Esquerdo)

Adicionar uma caixa fina funciona como um **plano de base** para que você possa ver claramente como a extrusão se posiciona na base.

```csharp
left.CreateChildNode(new Box(0.01, 3, 3));
```

## Etapa 6: Executar Extrusão Linear no Nó Direito (Com Central)

Agora extrudamos o mesmo perfil, mas habilitando a centralização. A geometria será posicionada de forma simétrica ao redor da origem do perfil.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 2) { Center = true, Slices = 3 });
```

## Etapa 7: Adicionar Plano de Base para Referência (Nó Direito)

Um segundo plano de base é adicionado ao nó direito para manter a comparação visual consistente.

```csharp
right.CreateChildNode(new Box(0.01, 3, 3));
```

## Etapa 8: Exportar Arquivo Wavefront OBJ

Por fim, **exportamos o Wavefront OBJ** para que o resultado possa ser aberto em qualquer visualizador 3‑D padrão.

```csharp
scene.Save("Your Output Directory" + "CenterInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Por que Adicionar um Plano de Base?

Adicionar um plano de base fornece uma pista visual imediata sobre a altura e o alinhamento da extrusão. Isso é especialmente útil quando você precisa comparar resultados centralizados versus não centralizados, como demonstrado neste tutorial.

## Problemas Comuns & Dicas

- **Plano de base não visível:** Certifique‑se de que a espessura do plano (`0.01` no construtor `Box`) seja pequena o suficiente para não obscurecer a extrusão, mas grande o bastante para ser renderizada.  
- **Falha na exportação:** Verifique se o diretório de saída existe e se você tem permissões de gravação.  
- **Extrusão centralizada aparece deslocada:** Verifique a propriedade `Center`; `true` centraliza o perfil, `false` alinha‑o a um lado.

## Perguntas Frequentes

### Q1: Posso usar Aspose.3D para .NET com outras linguagens de programação?

A1: Aspose.3D suporta principalmente linguagens .NET como C# e VB.NET.

### Q2: Onde posso encontrar suporte para dúvidas relacionadas ao Aspose.3D?

A2: Visite o [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) para suporte dedicado e discussões.

### Q3: Existe uma avaliação gratuita disponível para Aspose.3D para .NET?

A3: Sim, você pode acessar a avaliação gratuita [aqui](https://releases.aspose.com/).

### Q4: Como posso obter uma licença temporária para Aspose.3D para .NET?

A4: Você pode adquirir uma licença temporária [aqui](https://purchase.aspose.com/temporary-license/).

### Q5: Onde posso comprar a licença do Aspose.3D para .NET?

A5: Adquira sua licença [aqui](https://purchase.aspose.com/buy).

### Q6: Posso exportar a cena para outros formatos além de OBJ?

A6: Sim, Aspose.3D suporta vários formatos como STL, FBX e GLTF. Basta alterar o valor do enum `FileFormat` no método `Save`.

### Q7: Como altero o número de fatias da extrusão?

A7: Ajuste a propriedade `Slices` no construtor `LinearExtrusion` para controlar a densidade da malha.

---

**Última atualização:** 2026-01-07  
**Testado com:** Aspose.3D para .NET versão mais recente  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}