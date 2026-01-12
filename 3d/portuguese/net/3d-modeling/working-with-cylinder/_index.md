---
date: 2026-01-12
description: Aprenda como criar um cilindro de base de cisalhamento e como exportar
  o modelo 3D em OBJ usando Aspose.3D para .NET. Siga este guia passo a passo para
  dominar a modelagem 3D.
linktitle: Customized Shear Bottom Cylinder
second_title: Aspose.3D .NET API
title: Como criar um cilindro de base cônica com Aspose.3D para .NET
url: /pt/net/3d-modeling/working-with-cylinder/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Cilindro com Base Cisalhada Personalizada

## Introdução
Bem‑vindo ao nosso guia abrangente onde **você aprenderá a criar modelos de cilindro com base cisalhada** com Aspose.3D for .NET. Seja construindo um ativo de jogo, uma peça mecânica ou uma demonstração visual, este tutorial mostra exatamente como modelar a base de um cilindro, aplicar um cisalhamento e, finalmente, **exportar o arquivo OBJ do modelo 3D** para uso em qualquer pipeline subsequente. Vamos percorrer cada passo juntos, para que você possa começar a produzir geometria personalizada em minutos.

## Respostas Rápidas
- **O que é um cilindro com base cisalhada?** Um cilindro cuja face inferior está inclinada (cisalhada) ao invés de plana.  
- **Qual biblioteca é usada?** Aspose.3D for .NET.  
- **Como exportar o modelo?** Use `scene.Save(..., FileFormat.WavefrontOBJ)`.  
- **Preciso de uma licença?** Uma versão de avaliação está disponível; uma licença comercial é necessária para produção.  
- **Quais pré‑requisitos são necessários?** Ambiente de desenvolvimento .NET e o pacote NuGet Aspose.3D.

## O que é um cilindro com base cisalhada?
Um cilindro com base cisalhada é uma malha cilíndrica padrão cuja face inferior foi transformada por uma operação de cisalhamento. Isso permite criar bases anguladas, rampas ou conectores personalizados sem editar manualmente os vértices.

## Por que usar Aspose.3D para esta tarefa?
- **Full control** sobre os parâmetros de geometria (raio, altura, segmentos).  
- **Built‑in shear support** via a propriedade `ShearBottom`, economizando a manipulação de malha de baixo nível.  
- **One‑click export** para formatos populares como OBJ, FBX e STL, facilitando a integração com outras ferramentas.

## Pré‑requisitos
Antes de começarmos, certifique‑se de que você tem:

- Conhecimento básico de C# e .NET.  
- Aspose.3D for .NET instalado. Você pode baixá‑lo **[aqui](https://releases.aspose.com/3d/net/)**.  
- Uma IDE compatível com .NET (Visual Studio, Rider ou VS Code).

## Importar Namespaces
No seu arquivo C#, comece importando os namespaces necessários:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```

## Etapa 1: Criar uma Cena
Primeiro, instancie uma nova cena 3‑D que conterá todos os nossos objetos.

```csharp
Scene scene = new Scene();
```

## Etapa 2: Criar o Cilindro 1
Crie o cilindro principal que personalizaremos com uma base cisalhada.

```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```

## Etapa 3: Personalizar a Base Cisalhada para o Cilindro 1
Aplique o cisalhamento, habilite a geração de fan e ajuste outras propriedades para alcançar a forma desejada.

```csharp
// Shear 47.5deg in the xy plane (z‑axis)
cylinder1.ShearBottom = new Vector2(0, 0.83); 

// Set GenerateFanCylinder to true
cylinder1.GenerateFanCylinder = true;
// Set ThetaLength
cylinder1.ThetaLength = MathUtils.ToRadian(270);

// Set OffsetTop
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```

## Etapa 4: Adicionar o Cilindro 1 à Cena
Coloque o cilindro personalizado na cena e mova‑lo um pouco para a direita para que possamos ver ambos os objetos lado a lado.

```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```

## Etapa 5: Criar o Cilindro 2
Crie um segundo cilindro simples para comparação.

```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```

## Etapa 6: Adicionar o Cilindro 2 à Cena
Adicione o segundo cilindro sem nenhum cisalhamento personalizado — isso ajuda a ilustrar o efeito das etapas anteriores.

```csharp
scene.RootNode.CreateChildNode(cylinder2);
```

## Etapa 7: Salvar a Cena
Finalmente, exporte toda a cena como um arquivo OBJ para que você possa abri‑lo no Blender, Maya ou qualquer outro visualizador 3‑D.

```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```

## Problemas Comuns & Dicas
- **Shear values**: O `Vector2` recebe fatores de cisalhamento X e Y. Um valor de `0.83` corresponde a aproximadamente 47,5°, mas você pode ajustá‑lo para diferentes ângulos.  
- **Export path**: Certifique‑se de que a pasta especificada exista e que você tenha permissões de gravação; caso contrário, `scene.Save` lançará uma exceção.  
- **Performance**: Para cilindros com muitos segmentos, considere reduzir a contagem de segmentos (`20` no exemplo) para manter o tamanho do arquivo OBJ manejável.

## Perguntas Frequentes

### O Aspose.3D for .NET é adequado para iniciantes?
Absolutamente! Aspose.3D for .NET oferece uma API amigável, tornando‑a acessível tanto para iniciantes quanto para desenvolvedores experientes.

### Posso aplicar diferentes ângulos de cisalhamento aos cilindros?
Sim, você pode personalizar o `ShearBottom` de cada cilindro individualmente, permitindo alcançar efeitos únicos.

### Existe uma versão de avaliação disponível?
Sim, você pode explorar a versão de avaliação gratuita **[aqui](https://releases.aspose.com/)**.

### Onde posso encontrar suporte adicional?
Visite o **[forum Aspose.3D](https://forum.aspose.com/c/3d/18)** para suporte da comunidade e discussões.

### Como posso obter uma licença temporária?
Obtenha sua licença temporária **[aqui](https://purchase.aspose.com/temporary-license/)**.

**Additional Q&A**

**Q: Como mudar o formato de exportação para FBX?**  
A: Substitua `FileFormat.WavefrontOBJ` por `FileFormat.FBX` na chamada `scene.Save`.

**Q: Posso animar o cilindro após a exportação?**  
A: OBJ não suporta animação; use FBX ou GLTF se precisar de dados animados.

**Q: E se eu precisar de um raio de cilindro maior?**  
A: Ajuste os dois primeiros parâmetros do construtor `Cylinder` (por exemplo, `new Cylinder(4, 4, …)`).

## Conclusão
Agora você dominou como **criar cilindros com base cisalhada** e exportá‑los como arquivos OBJ usando Aspose.3D for .NET. Experimente diferentes valores de cisalhamento, contagens de segmentos e formatos de exportação para atender às necessidades do seu projeto. Boa modelagem!

---

**Last Updated:** 2026-01-12  
**Tested With:** Aspose.3D for .NET 24.11 (latest at time of writing)  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}