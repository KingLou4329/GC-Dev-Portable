# Google Chrome Dev Portable Enhanced

[![LICENSE](https://img.shields.io/badge/License-GPL--3.0--only-blue.svg?style=for-the-badge&logo=github "LICENSE")](https://github.com/KingLou4329/GC-Dev-Portable/blob/main/LICENSE)

使用了新[Bush2021/chrome_plus](https://github.com/Bush2021/chrome_plus)补丁, 由此遵循 GPL-3.0 许可证

~~自用Dev版~~

## 功能

- ~~双击关闭标签页~~
- ~~右键关闭标签页（按住 Shift 弹出原有菜单）~~
- ~~保留最后标签页（防止关闭最后一个标签页时关闭浏览器, 点关闭按钮不行）~~
- 根据个人习惯取消了双击关闭, 避免误触带来的麻烦
- 鼠标悬停标签栏时使用滚轮切换标签页
- 按住右键时使用滚轮切换标签页
- ~~新建标签页打开地址栏输入的内容（可配置前台或后台打开）~~
- ~~新建标签页打开书签（可配置前台或后台打开）~~
- ~~当前为新标签页时, 可以禁用上面两个功能~~
- ~~自定义快捷键快速隐藏浏览器窗口（老板键）~~
- ~~自定义快捷键进行网页翻译~~
- ~~便携化（不兼容原版数据, 可以重装系统换电脑不丢数据）~~
- 便携设计, 程序放在Chrome目录, 数据和缓存放在同级目录Data\Cache下, 不会在%User%/AppData中建立目录（不兼容原版数据, 可以重装系统换电脑不丢数据）
- 可以自定义 Chromium 命令行开关
- 移除更新错误警告, 移除不必要的显示（因为是绿色版没有自动更新功能）
- 更多功能参见 [INI 配置文件](https://github.com/Bush2021/chrome_plus/blob/main/src/chrome%2B%2B.ini)

以上配置都可以在chrome++.ini中进行修改

## 获取

全自动无人管理项目, 每周定时拉取最新Chrome离线包, 并封装为便携版

采用GitHub Actions自动编译发布, 下载地址: [Google-Chrome-Dev-Portable](https://nightly.link/KingLou4329/GC-Dev-Portable/workflows/build/main)

状态: [![build status](https://github.com/KingLou4329/GC-Dev-Portable/actions/workflows/build.yml/badge.svg)](https://github.com/KingLou4329/GC-Dev-Portable/actions/workflows/build.yml)

## 安装

**解压Chrome.zip, 然后启动Chrome.exe即可建立桌面快捷方式**

## 更新

~~无法自动更新, 未来可以建立独立的绿色升级软件~~

Chrome dev每周发布一次新版本, 定时为每周 周三早八拉取构建新版本

**保留Chrome文件夹中的Data和Cache, 其他文件删除后解压新版压缩包, 然后进行简单地文件替换即可**

## 卸载

删除Chrome文件夹, 删除快捷方式即可, 无残留

**注意提前保存Data, 避免自己的个人浏览数据清空（可谷歌账号同步, 但不如Data全面）**
