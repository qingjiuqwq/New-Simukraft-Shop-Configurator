# New-Simukraft Shop Configurator

![Powered By Gemini](https://img.shields.io/badge/Powered%20By-Gemini-blue?style=for-the-badge&logo=google)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![Three.js](https://img.shields.io/badge/Three.js-000000?style=for-the-badge&logo=threedotjs&logoColor=white)

这是一个专为 **[New:Sim-U-Kraft](https://github.com/New-Sim-U-Kraft/New-Simukraft-1.21.1)** 及其扩展模组 **[SimCity Expansion](https://modrinth.com/mod/simcityexpansion)** 打造的纯前端商店配置生成工具。由大语言模型 Gemini 强势驱动开发。

本工具旨在解决手动配置 JSON、SK 文件以及打包结构时繁琐的命名与对齐问题，通过直观的卡片化 Web 界面，让玩家和服主可以轻松地可视化配置专属商店！

---

## 核心功能特色

- **多商店卡片流**：支持在一个页面内同时创建、展开和配置多个不同的商店，再也不怕文件混乱。
- **一键打包 ZIP**：配置完成后，勾选需要的建筑，点击打包按钮，即可自动生成完全符合 SimCity Expansion 导入格式（严格校验 SHA256）的压缩包。
- **智能中文搜索**：导入一次 All_Languages 汉化包后，即可在输入框内支持原版物品的中文搜索与自动补全。
- **动态图标渲染**：配合本地 ./icons/ 与云端原版材质库，实时显示你配置的商品图标。
- **内置 3D NBT 预览**：将 .nbt 结构文件直接拖入浏览器，即可在专属卡片内利用 Three.js 实现高性能的全 3D 材质渲染，并自动读取长宽高写入配置中！
- **自动云存档 (Auto-Save)**：所有填写的配置、中文词库，甚至是 NBT 3D 模型缓存，都会在本地浏览器中每 5 秒自动保存。关闭网页再次打开，数据瞬间无缝恢复！

---

## 使用方法

本工具是**完全纯前端**的应用，不需要任何服务器、Node.js 或是复杂的环境安装，即开即用！

1. 将本仓库克隆或下载到本地，解压。
2. 双击打开文件夹中的 自定义商店.html（建议使用现代浏览器，如 Chrome, Edge 等）。
3. (可选) 点击右上角 "导入语言包"，选中包含游戏 zh_cn.json 的 All_Languages 文件夹，即可激活强大的中文智能搜索。
4. 在卡片中修改配置信息，拖拽 .nbt 模型进行长宽高自动识别与预览。
5. 点击右上方的 "打包已选的建筑 (.zip)"，即可获得完美符合模组导入标准的压缩包。

---

## 生成的模组包结构规范

工具一键导出的 .zip 文件将直接兼容模组所需的包结构：
```text
shop_pack.zip
 ┣ buildings
 ┃ ┗ commercial
 ┃   ┣ [文件名].nbt   (包含你拖入的结构文件)
 ┃   ┣ [文件名].sk    (自动生成的元数据)
 ┃   ┗ [文件名].json  (自动生成的交易配置)
 ┣ icon.png           
 ┣ pack.json          
 ┗ index.json         (包含精确计算的文件 SHA256 哈希值)
```

## 相关链接与致谢

- **基础模组 (New:Sim-U-Kraft)**: [GitHub Repository](https://github.com/New-Sim-U-Kraft/New-Simukraft-1.21.1)
- **扩展模组 (SimCity Expansion)**: [Modrinth Page](https://modrinth.com/mod/simcityexpansion)
- **核心开发驱动**: Google Gemini
