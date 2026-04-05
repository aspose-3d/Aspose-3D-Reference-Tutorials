---
date: 2026-03-26
description: Aprenda a criar um cilindro e exportar um arquivo OBJ usando Aspose.3D
  para .NET. Este guia para iniciantes cobre a configuração da cena 3D e a exportação
  do OBJ.
linktitle: Customized Shear Bottom Cylinder
second_title: Aspose.3D .NET API
title: Como criar um cilindro com base de cisalhamento – Aspose.3D para .NET
url: /pt/net/3d-modeling/working-with-cylinder/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Como Criar um Cilindro com Base Cisalhante – Aspose.3D para .NET

## Introdução
Se você está se perguntando **como criar cilindro** objetos com uma base cisalhante personalizada em um ambiente .NET, você chegou ao lugar certo. Neste tutorial, percorreremos cada passo — desde a configuração de uma cena 3‑D até a exportação do modelo final como um arquivo OBJ — para que você possa aprimorar suas habilidades de *modelagem 3D para iniciantes* usando **Aspose.3D para .NET**.

## Respostas Rápidas
- **Qual é a classe principal para iniciar um modelo 3D?** `Scene` cria o contêiner raiz para toda a geometria.  
- **Qual método exporta o modelo para OBJ?** `scene.Save(..., FileFormat.WavefrontOBJ)`.  
- **Preciso de uma licença para testes?** Uma avaliação gratuita está disponível — veja o link de avaliação nas Perguntas Frequentes.  
- **Posso mudar o ângulo de cisalhamento?** Sim, modifique `ShearBottom` com um valor `Vector2`.  
- **Isso é adequado para iniciantes?** Absolutamente; a API abstrai o manuseio de malha de baixo nível.

## O que é uma Cena 3D?
Uma *cena 3D* é um contêiner hierárquico que contém todas as entidades geométricas, luzes, câmeras e transformações. No Aspose.3D, a classe `Scene` fornece uma maneira limpa de organizar e posteriormente exportar seus modelos.

## Por que Exportar OBJ?
OBJ é um formato baseado em texto, amplamente suportado, que muitas aplicações 3‑D (Blender, Maya, Unity) podem importar. Exportar para OBJ permite que você compartilhe ou edite ainda mais seus modelos de cilindro fora do .NET.

## Pré‑requisitos
- Conhecimento básico de C# e desenvolvimento .NET.  
- **Aspose.3D for .NET** instalado – você pode baixá-lo **[aqui](https://releases.aspose.com/3d/net/)**.  
- Uma IDE .NET (Visual Studio, Rider ou VS Code) pronta para codificar.

## Importar Namespaces
Primeiro, traga os namespaces necessários para o escopo para que os tipos da API sejam reconhecidos.

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

## Etapa 1: Criar uma Cena 3D
O objeto `Scene` atua como a raiz da hierarquia do seu modelo.

```csharp
Scene scene = new Scene();
```

## Etapa 2: Criar o Cilindro 1
Geramos o primeiro cilindro com raio 2, altura 10 e 20 segmentos radiais.

```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```

## Etapa 3: Personalizar a Base Cisalhante para o Cilindro 1
Aplique uma transformação de cisalhamento, habilite a geração de cilindro em fan‑cylinder e ajuste outras propriedades para alcançar a forma desejada.

```csharp
// Shear 47.5deg in the xy plane (z-axis)
cylinder1.ShearBottom = new Vector2(0, 0.83); 

// Set GenerateFanCylinder to true
cylinder1.GenerateFanCylinder = true;
// Set ThetaLength
cylinder1.ThetaLength = MathUtils.ToRadian(270);

// Set OffsetTop
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```

## Etapa 4: Adicionar o Cilindro 1 à Cena
Posicione o primeiro cilindro em um local conveniente usando uma transformação de translação.

```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```

## Etapa 5: Criar o Cilindro 2
Um segundo cilindro é criado com as mesmas dimensões base, mas sem cisalhamento personalizado — perfeito para comparação lado a lado.

```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```

## Etapa 6: Adicionar o Cilindro 2 à Cena
Simplesmente anexamos o segundo cilindro ao grafo da cena.

```csharp
scene.RootNode.CreateChildNode(cylinder2);
```

## Etapa 7: Exportar a Cena como um Arquivo OBJ
Finalmente, salvamos toda a cena em um arquivo OBJ para que ele possa ser aberto em qualquer visualizador 3‑D padrão.

```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```

## Problemas Comuns e Soluções
| Problema | Por que acontece | Correção |
|----------|------------------|----------|
| **O arquivo OBJ está vazio** | A cena não tem geometria anexada. | Certifique-se de que ambos os cilindros foram adicionados a `scene.RootNode`. |
| **Cisalhamento parece errado** | `ShearBottom` espera a tangente do ângulo. | Use `Math.Tan(angleInRadians)` ou o valor `0.83` fornecido para ~47,5°. |
| **Erros de caminho de arquivo** | Diretório inválido ou ausente. | Use `Path.Combine(Environment.CurrentDirectory, "CustomizedShearBottomCylinder.obj")`. |

## Perguntas Frequentes
### O Aspose.3D para .NET é adequado para iniciantes?
Absolutamente! Aspose.3D para .NET oferece uma API de alto nível que abstrai as partes matemáticas complexas da modelagem 3‑D, tornando-a acessível para desenvolvedores de qualquer nível de habilidade.

### Posso aplicar diferentes ângulos de cisalhamento aos cilindros?
Sim, cada instância de `Cylinder` possui sua própria propriedade `ShearBottom`, portanto você pode atribuir um ângulo único a cada objeto.

### Existe uma versão de avaliação disponível?
Sim, você pode explorar a versão de avaliação gratuita **[aqui](https://releases.aspose.com/)**.

### Onde posso encontrar suporte adicional?
Visite o **[fórum Aspose.3D](https://forum.aspose.com/c/3d/18)** para ajuda da comunidade, exemplos de código e discussões.

### Como posso obter uma licença temporária?
Obtenha sua licença temporária **[aqui](https://purchase.aspose.com/temporary-license/)**.

**Q&A Adicionais**

**Q: Como exporto o modelo em um formato diferente, como STL?**  
A: Substitua `FileFormat.WavefrontOBJ` por `FileFormat.STL` na chamada `scene.Save`.

**Q: Posso animar os cilindros após a criação?**  
A: Sim, você pode adicionar animações de quadros‑chave às transformações dos nós usando as classes `Animation` fornecidas pelo Aspose.3D.

**Q: A API suporta .NET Core?**  
A: A biblioteca é totalmente compatível com .NET Core, .NET 5+ e .NET 6+.

---

**Última atualização:** 2026-03-26  
**Testado com:** Aspose.3D for .NET (última versão)  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}