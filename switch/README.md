# switch emulator

- Yuzu 柚子（被正义制裁）
  - from the creators of Citra and written in C++
  - https://github.com/yuzu-emu/
  - https://yuzu-mirror.github.io/
- Suyu 柚子（秽土转生版）
  - https://suyu.dev/
  - https://github.com/suyu-emu/suyu/releases
- Ryujinx 龙神
  - created by gdkchan and written in C#
  - https://ryujinx.org/
  - https://github.com/Ryujinx/Ryujinx

## Firmware and Prod Keys

固件和key从这个网站上下载 
- https://prodkeys.net/dl/
- key: 文件 - 打开suyu文件夹 - keys - prod.keys & title.keys
- firmware: 工具 - 安装固件 - Firmware-Unzipped-Folder

P.S. 固件也可以从这里获取 https://github.com/THZoria/NX_Firmware/releases

## Game

download from
- https://www.gamer520.com/

包处理工具
- https://github.com/julesontheroad/NSC_BUILDER
- fill prod.keys in NSCB\ztools\keys.txt
- 如果不需要每次自动更新 NUT DB 可以解压 NSCB\zconfig\zconfig_no_update.7z 文件到当前目录，覆盖文件
- 如果想手动更新 NUT DB 可以打开 NSCB\zconfig\NUT_DB_URL.txt 下载 https://**.json 然后修改对应后缀放入 NSCB\zconfig\DB\
- 上一条实测原址已经下不到了 从镜像下载 备份见本项目的 NSCB_DB\
- 执行 NSCB.exe 输出文件在 NSCB\NSCB_output\

```
输入 "1"  单文件处理   （ XCI/NSP互转 【常用功能】 ）
输入 "2"  多文件处理   （ XCI整合用 【常用功能】 ）
输入 "3"  文件拆分     （ XCI/NSP拆包 【常用功能】 ）
输入 "4"  文件信息查询 （ 游戏版本信息等 【常用功能】 ）
输入 "5"  数据库构建   （ 重建游戏文件数据库 ）
输入 "6"  高级选项     （ 修补链接账户要求等 【常用功能】 ）
输入 "7"  合并模式     （ 文件合并 ）
输入 "8"  压缩/解压    （ XCI转XCZ/NSP转NSZ 【常用功能】 ）
输入 "9"  文件还原     （ 从备份文件恢复原始包 ）
输入 "10" 文件管理     （ 暂无功能 ）
输入 "0"  配置选项     （ 设置程序配置 ）
```
