---
date: 2026-01-17
description: Aprenda a listar propriedades de material, alterar a cor difusa e modificar
  atributos de material 3D usando Aspose.3D para .NET. Exemplos de código passo a
  passo incluídos.
linktitle: List Material Properties in 3D Scenes with Aspose.3D
second_title: Aspose.3D .NET API
title: Listar propriedades de material em cenas 3D com Aspose.3D
url: /pt/net/3d-scene/set-3d-properties/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Listar Propriedades de Material em Cenas 3D com Aspose.3D

## Introdução

Se você precisa **listar propriedades de material** de um modelo 3D e então ajustar coisas como a cor difusa, está no lugar certo. Aspose.3D para .NET oferece uma API limpa, orientada a objetos, que permite inspecionar, recuperar e modificar atributos de material sem sair do seu código C#. Neste tutorial vamos percorrer o carregamento de uma cena, enumerar suas propriedades de material e alterar valores como o componente difuso — para que você possa dar aos seus modelos a aparência exata que deseja.

## Respostas Rápidas
- **Qual é o objetivo principal?** Listar propriedades de material e modificá‑las (por exemplo, cor difusa).  
- **Qual biblioteca é necessária?** Aspose.3D para .NET.  
- **Preciso de licença?** Uma licença temporária ou completa é necessária para uso em produção.  
- **Formatos de arquivo suportados?** FBX, OBJ, STL, STL‑ASCII, 3MF e mais.  
- **Tempo típico de implementação?** Cerca de 10‑15 minutos para um script básico de listagem de propriedades.

## O que é **list material properties**?
Listar propriedades de material significa iterar sobre a `PropertyCollection` de um material para ler cada nome de propriedade e seu valor atual. Isso é útil para depuração, inspeção visual ou construção de controles de UI que permitem aos usuários ajustar configurações de material em tempo de execução.

## Por que usar Aspose.3D para **access material properties**?
- **Sem conversores externos** – trabalhe diretamente com objetos nativos .NET.  
- **Modelo de propriedades rico** – suporta atributos específicos de FBX além dos valores padrão PBR.  
- **Multiplataforma** – funciona no .NET Framework, .NET Core e .NET 5/6+.  

## Pré‑requisitos

- Aspose.3D para .NET instalado no seu projeto. Baixe-o [aqui](https://releases.aspose.com/3d/net/).
- Uma pasta no disco para armazenar seus arquivos fonte 3‑D (por exemplo, um arquivo FBX com texturas incorporadas).

Agora que você tem o básico pronto, vamos mergulhar no código.

## Importar Namespaces

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```

## Etapa 1: Carregar Cena 3D

```csharp
//ExStart: Load3DScene
string dataDir = "Your Document Directory";
Scene scene = new Scene(dataDir + "EmbeddedTexture.fbx");
//ExEnd: Load3DScene
```

## Etapa 2: **Access material properties** do primeiro nó

```csharp
//ExStart: AccessMaterialProperties
Material material = scene.RootNode.ChildNodes[0].Material;
PropertyCollection props = material.Properties;
//ExEnd: AccessMaterialProperties
```

## Etapa 3: **List material properties** – veja cada par nome/valor

```csharp
//ExStart: ListAllProperties
foreach (var prop in props)
{
    Console.WriteLine("{0} = {1}", prop.Name, prop.Value);
}

//or using ordinal for loop
for (int i = 0; i < props.Count; i++)
{
    var prop = props[i];
    Console.WriteLine("{0} = {1}", prop.Name, prop.Value);
}
//ExEnd: ListAllProperties
```

## Etapa 4: **How to change diffuse** – modificar a propriedade Diffuse

```csharp
//ExStart: GetModifyPropertyByName
var diffuse = props["Diffuse"];
Console.WriteLine(diffuse);

//modify property value by name
props["Diffuse"] = new Vector3(1, 0, 1); // sets a magenta diffuse color
//ExEnd: GetModifyPropertyByName
```

## Etapa 5: **Retrieve property by name** – obter uma instância fortemente tipada

```csharp
//ExStart: GetPropertyInstanceByName
Property pdiffuse = props.FindProperty("Diffuse");
Console.WriteLine(pdiffuse);
//ExEnd: GetPropertyInstanceByName
```

## Etapa 6: Percorrer as próprias propriedades de uma propriedade (avançado)

```csharp
//ExStart: TraversePropertyProperties
Console.WriteLine("Property flags = {0}", pdiffuse.GetProperty("flags"));

//and some properties that only defined in FBX file:
Console.WriteLine("Label = {0}", pdiffuse.GetProperty("label"));
Console.WriteLine("Type Name = {0}", pdiffuse.GetProperty("typeName"));

//traversal on property's property is possible
foreach (var pp in pdiffuse.Properties)
{
    Console.WriteLine("Diffuse.{0} = {1}", pp.Name, pp.Value);
}
//ExEnd: TraversePropertyProperties
```

## Como **change 3d material color** além do difuso
Se precisar afetar cores especular, ambiente ou emissiva, basta substituir `"Diffuse"` por `"Specular"` ou `"Ambient"` na atribuição `props["..."]` acima. As mesmas estruturas `Vector3` ou `Vector4` se aplicam.

## Armadilhas Comuns & Dicas
- **Sensibilidade a maiúsculas/minúsculas nos nomes de propriedade** – as chaves de propriedade do Aspose.3D diferenciam maiúsculas de minúsculas; use exatamente o nome exibido na listagem.  
- **Propriedade ausente** – nem todos os materiais expõem cada atributo PBR. Verifique `props.ContainsKey("Specular")` antes de acessar.  
- **Salvar alterações** – após modificar propriedades, chame `scene.Save("output.fbx");` para persistir as mudanças.

## Conclusão

Agora você aprendeu a **listar propriedades de material**, **recuperar uma propriedade pelo nome** e **alterar a cor difusa** (ou qualquer outro atributo de material) usando Aspose.3D para .NET. Experimente diferentes tipos de propriedade para ajustar finamente a aparência dos seus ativos 3‑D.

## Perguntas Frequentes

### Q1: Posso usar Aspose.3D para .NET com outros formatos de arquivo 3D?

A1: Sim, o Aspose.3D suporta vários formatos de arquivo 3D, incluindo FBX, STL e muitos outros.

### Q2: Como posso obter uma licença temporária para Aspose.3D para .NET?

A2: Visite [aqui](https://purchase.aspose.com/temporary-license/) para obter uma licença temporária.

### Q3: Existe um fórum da comunidade para usuários do Aspose.3D?

A3: Sim, você pode encontrar suporte e discussões no [fórum Aspose.3D](https://forum.aspose.com/c/3d/18).

### Q4: Onde encontro documentação detalhada para Aspose.3D para .NET?

A4: Consulte a [documentação](https://reference.aspose.com/3d/net/) para orientação completa.

### Q5: Posso experimentar o Aspose.3D para .NET gratuitamente antes de comprar?

A5: Claro! Baixe a [versão de avaliação gratuita](https://releases.aspose.com/) para explorar seus recursos.

## Perguntas Frequentes

**Q: O que representa o `Vector3(1, 0, 1)`?**  
A: Define a cor difusa como magenta (vermelho = 1, verde = 0, azul = 1) no espaço de cor linear.

**Q: Preciso chamar `scene.Save` após mudar propriedades?**  
A: Sim, persistir a cena grava suas modificações no disco; caso contrário, as alterações permanecem apenas na memória.

**Q: Posso enumerar atributos FBX personalizados?**  
A: Absolutamente. A `PropertyCollection` incluirá quaisquer atributos personalizados, que podem ser acessados via `GetProperty("customName")`.

**Q: Existe uma forma de atualizar em lote vários materiais?**  
A: Percorra `scene.RootNode.ChildNodes` e repita as etapas de modificação de propriedade para cada material.

**Q: O Aspose.3D suporta .NET 6?**  
A: Sim, a biblioteca é totalmente compatível com .NET 6 e versões posteriores.

---

**Última atualização:** 2026-01-17  
**Testado com:** Aspose.3D 24.11 para .NET  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}