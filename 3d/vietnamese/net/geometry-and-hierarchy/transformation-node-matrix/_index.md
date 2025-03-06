---
title: Nút chuyển đổi bằng ma trận chuyển đổi
linktitle: Nút chuyển đổi bằng ma trận chuyển đổi
second_title: API Aspose.3D .NET
description: Chuyển đổi các nút dễ dàng trong cảnh 3D bằng Aspose.3D cho .NET. Tìm hiểu các chuyển đổi nút từng bước với hướng dẫn.
weight: 21
url: /vi/net/geometry-and-hierarchy/transformation-node-matrix/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Nút chuyển đổi bằng ma trận chuyển đổi

## Giới thiệu

Trong lĩnh vực động của đồ họa và trực quan hóa 3D, khả năng điều khiển các vật thể trong một cảnh là một khía cạnh quan trọng. Aspose.3D for .NET trao quyền cho các nhà phát triển chuyển đổi liền mạch các nút bằng cách sử dụng ma trận chuyển đổi, thêm một lớp sáng tạo và khả năng kiểm soát vào cảnh 3D. Hướng dẫn này sẽ hướng dẫn bạn từng bước trong quá trình chuyển đổi nút trong cảnh 3D.

## Điều kiện tiên quyết

Trước khi đi sâu vào hướng dẫn, hãy đảm bảo bạn có sẵn các điều kiện tiên quyết sau:

1.  Aspose.3D for .NET Library: Đảm bảo bạn đã cài đặt thư viện Aspose.3D trong dự án .NET của mình. Bạn có thể tải nó xuống[đây](https://releases.aspose.com/3d/net/).

2. Môi trường phát triển: Thiết lập một môi trường phát triển .NET đang hoạt động và nếu bạn chưa có, hãy tạo một dự án mới nơi bạn sẽ triển khai các chuyển đổi.

## Nhập không gian tên

Bắt đầu bằng cách nhập các vùng tên cần thiết vào dự án .NET của bạn. Các không gian tên này cung cấp các lớp và phương thức cần thiết để thao tác với cảnh 3D.

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

Bây giờ chúng ta đã đề cập đến những điều cơ bản, hãy chia quá trình chuyển đổi thành hướng dẫn từng bước.

## Bước 1: Khởi tạo cảnh

```csharp
// ExStart:AddTransformationToNodeByTransformationMatrix
// Khởi tạo đối tượng cảnh
Scene scene = new Scene();

```

Trong bước này, chúng ta tạo cảnh 3D trống mới.

## Bước 2: Tạo lưới và đính kèm vào cảnh

```csharp
// Gọi Lớp chung tạo lưới bằng phương pháp xây dựng đa giác để đặt phiên bản lưới
Mesh mesh = (new Box()).ToMesh();

// Tạo một nút chứa cho lưới.
Node cubeNode = scene.RootNode.CreateChildNode(mesh);
```

Ở đây, chúng ta tạo lưới bằng phương pháp xây dựng đa giác và gán nó cho nút, thiết lập hình dạng cho khối lập phương của chúng ta.

## Bước 3: Đặt ma trận dịch tùy chỉnh

```csharp
// Đặt ma trận dịch tùy chỉnh
cubeNode.Transform.TransformMatrix = new Matrix4(
    1, -0.3, 0, 0,
    0.4, 1, 0.3, 0,
    0, 0, 1, 0,
    0, 20, 0, 1
);        
```

Xác định ma trận dịch tùy chỉnh để xác định phép biến đổi cụ thể được áp dụng cho nút. Điều chỉnh các giá trị ma trận nếu cần cho phép chuyển đổi mong muốn của bạn.

Bao gồm nút khối trong cảnh, biến nó thành một phần của môi trường 3D tổng thể.

## Bước 4: Lưu cảnh

```csharp
// Đường dẫn đến thư mục tài liệu.
var output = "TransformationToNode.fbx";

// Lưu cảnh 3D ở các định dạng tệp được hỗ trợ
scene.Save(output);
// ExEnd:AddTransformationToNodeByTransformationMatrix
Console.WriteLine("\nTransformation added successfully to node.\nFile saved at " + output);
```

Chỉ định thư mục đầu ra và tên tệp, sau đó lưu cảnh 3D ở định dạng tệp mong muốn. Trong ví dụ này, chúng tôi lưu nó ở định dạng FBX7500ASCII.

## Phần kết luận

Chúc mừng! Bạn đã chuyển đổi thành công một nút bằng cách sử dụng ma trận chuyển đổi trong cảnh 3D với Aspose.3D cho .NET. Khả năng này mở ra cánh cửa cho các ứng dụng 3D đa dạng và hấp dẫn về mặt hình ảnh.

## Câu hỏi thường gặp

### Câu hỏi 1: Ma trận biến đổi trong đồ họa 3D là gì?

Câu trả lời 1: Ma trận biến đổi là một biểu diễn toán học được sử dụng để áp dụng các phép biến đổi khác nhau (dịch chuyển, xoay, chia tỷ lệ) cho các đối tượng trong không gian 3D.

### Câu hỏi 2: Tôi có thể áp dụng nhiều phép biến đổi cho một nút không?

Câu trả lời 2: Có, bạn có thể kết hợp nhiều phép biến đổi bằng cách nhân các ma trận tương ứng của chúng và áp dụng kết quả cho nút.

### Câu hỏi 3: Có định dạng tệp nào khác được hỗ trợ để lưu cảnh 3D không?

 Câu trả lời 3: Aspose.3D cho .NET hỗ trợ nhiều định dạng tệp khác nhau, bao gồm STL, GLTF, OBJ, v.v. Tham khảo đến[tài liệu](https://reference.aspose.com/3d/net/) để có danh sách đầy đủ.

### Câu hỏi 4: Làm cách nào tôi có thể nhận được giấy phép tạm thời cho Aspose.3D cho .NET?

 A4: Tham quan[trang giấy phép tạm thời](https://purchase.aspose.com/temporary-license/)trên trang web Aspose để lấy giấy phép tạm thời cho mục đích đánh giá.

### Câu hỏi 5: Tôi có thể tìm kiếm hỗ trợ hoặc kết nối với cộng đồng Aspose.3D ở đâu?

 A5: Tham quan[Diễn đàn Aspose.3D](https://forum.aspose.com/c/3d/18) để đặt câu hỏi, chia sẻ kinh nghiệm và kết nối với các nhà phát triển khác bằng Aspose.3D.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
