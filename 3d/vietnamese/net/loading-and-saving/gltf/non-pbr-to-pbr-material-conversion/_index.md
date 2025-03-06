---
title: Chuyển đổi vật liệu không PBR sang PBR
linktitle: Chuyển đổi vật liệu không PBR sang PBR
second_title: API Aspose.3D .NET
description: Khám phá Aspose.3D for .NET - Chuyển đổi vật liệu Non-PBR sang PBR một cách dễ dàng. Hướng dẫn toàn diện và API mạnh mẽ.
weight: 16
url: /vi/net/loading-and-saving/gltf/non-pbr-to-pbr-material-conversion/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Chuyển đổi vật liệu không PBR sang PBR

## Giới thiệu

Chào mừng bạn đến với hướng dẫn từng bước này về cách sử dụng Aspose.3D cho .NET để chuyển đổi vật liệu Non-PBR (Kết xuất dựa trên vật lý) sang vật liệu PBR. Aspose.3D là một API mạnh mẽ cho phép các nhà phát triển làm việc liền mạch với các định dạng tệp 3D trong ứng dụng .NET của họ.

## Điều kiện tiên quyết

Trước khi chúng ta đi sâu vào hướng dẫn, hãy đảm bảo bạn có các điều kiện tiên quyết sau:

-  Aspose.3D for .NET: Đảm bảo bạn đã cài đặt thư viện Aspose.3D for .NET. Bạn có thể tìm thấy liên kết tải xuống[đây](https://releases.aspose.com/3d/net/).

- Hiểu biết cơ bản về C#: Hướng dẫn này giả định rằng bạn có hiểu biết cơ bản về lập trình C#.

- IDE (Môi trường phát triển tích hợp): Chọn IDE ưa thích của bạn để phát triển .NET, chẳng hạn như Visual Studio.

## Nhập không gian tên

Trong mã C# của bạn, hãy bắt đầu bằng cách nhập các vùng tên cần thiết:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
```

## Bước 1: Khởi tạo cảnh 3D mới

Bắt đầu bằng cách tạo cảnh 3D mới bằng mã sau:

```csharp
// ExStart:Non_PBRtoPBRMaterial
// khởi tạo cảnh 3D mới
var scene = new Scene();
```

## Bước 2: Tạo đối tượng 3D

Tiếp theo, tạo đối tượng 3D, ví dụ: hộp:

```csharp
var box = new Box();
scene.RootNode.CreateChildNode("box1", box).Material = new PhongMaterial() { DiffuseColor = new Vector3(1, 0, 1) };
```

## Bước 3: Định cấu hình chuyển đổi vật liệu

Thiết lập các tùy chọn chuyển đổi vật liệu để chuyển đổi Non-PBR sang PBR:

```csharp
GltfSaveOptions options = new GltfSaveOptions(FileFormat.GLTF2);
options.MaterialConverter = delegate (Material material)
{
    PhongMaterial phongMaterial = (PhongMaterial)material;
    return new PbrMaterial() { Albedo = new Vector3(phongMaterial.DiffuseColor.x, phongMaterial.DiffuseColor.y, phongMaterial.DiffuseColor.z) };
};
```

## Bước 4: Lưu ở định dạng GLTF 2.0

Lưu cảnh đã chuyển đổi ở định dạng GLTF 2.0:

```csharp
scene.Save("Your Output Directory" + "Non_PBRtoPBRMaterial_Out.gltf", options);
// ExEnd:Non_PBRtoPBRChất liệu
```

Lặp lại các bước này nếu cần cho trường hợp sử dụng cụ thể của bạn, đảm bảo từng chi tiết được đặt cấu hình chính xác.

## Phần kết luận

Chúc mừng! Bạn đã học thành công cách chuyển đổi vật liệu Non-PBR sang PBR bằng Aspose.3D cho .NET. Công cụ mạnh mẽ này mở ra khả năng vô tận cho thao tác đồ họa 3D trong các ứng dụng .NET của bạn.

## Câu hỏi thường gặp

### Câu hỏi 1: Aspose.3D có tương thích với tất cả các định dạng tệp 3D không?

Câu trả lời 1: Có, Aspose.3D hỗ trợ nhiều định dạng tệp 3D, mang lại sự linh hoạt cho các dự án của bạn.

### Câu hỏi 2: Tôi có thể sử dụng Aspose.3D cho các ứng dụng thương mại không?

 A2: Chắc chắn rồi! Aspose.3D là một sản phẩm thương mại và bạn có thể mua nó[đây](https://purchase.aspose.com/buy).

### Câu hỏi 3: Tôi có cần giấy phép tạm thời để thử nghiệm không?

 Câu trả lời 3: Có, bạn có thể xin giấy phép tạm thời cho mục đích thử nghiệm[đây](https://purchase.aspose.com/temporary-license/).

### Câu hỏi 4: Tôi có thể tìm hỗ trợ cho Aspose.3D ở đâu?

 A4: Tham quan[Diễn đàn Aspose.3D](https://forum.aspose.com/c/3d/18) để được cộng đồng hỗ trợ và thảo luận.

### Câu 5: Có bản dùng thử miễn phí không?

 Câu trả lời 5: Có, bạn có thể khám phá phiên bản dùng thử miễn phí[đây](https://releases.aspose.com/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
