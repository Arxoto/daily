# MPV

https://mpv.io/manual/master/
https://hooke007.github.io/mpv-lazy/mpv.html

## 基础配置

mpv.exe 旁边新建一个 portable_config 文件夹，该目录具有最高级的优先级，一旦存在此文件夹，其它所有的设置目录都会被忽略。

新建 ./portable_config/mpv.conf 确保文本编码为 UTF-8

```conf
vo=gpu                                  # <gpu|gpu-next> 视频输出驱动 gpu最高普适性和完成度
gpu-context=d3d11                       # <win|d3d11|winvk> 选择图形输出后端 与 --gpu-api=<opengl|d3d11|vulkan> 相对应
hwdec=auto                              # 默认值 no 为软解 值 auto|auto-save 优先尝试原生硬解 但不支持部分设置/滤镜
hwdec-codecs=all                        # 尽可能所有格式先尝试硬解
# 双显卡笔记本配置
d3d11-adapter=NV                        # [当 --gpu-api=d3d11 时] 指定某张显卡作为主渲染输出 值可以前缀匹配
#vulkan-device                           # [当 --gpu-api=vulkan 时] 代替 --d3d11-adapter 执行指定显卡的职能 值必须为完整设备名 见任务管理器

no-input-builtin-bindings               # 屏蔽全部内建的原始快捷键预设
#no-input-default-bindings               # 进一步屏蔽外置脚本内的静态若绑定预设
save-position-on-quit=yes               # 退出时保存当前播放状态
keep-open=yes                           # 播完列表暂停
audio-file-auto=fuzzy                   # 自动加载同名外置音轨
sub-auto=fuzzy                          # 自动加载同名外置字幕
icc-cache-dir="~~/icc_cache"            # 保存缓存加速启动
gpu-shader-cache-dir="~~/shaders_cache" # 保存缓存加速启动
screenshot-directory="~~desktop/"       # 截图输出在桌面
```

新建 ./portable_config/input.conf 确保文本编码为 UTF-8

```conf
MBTN_LEFT      ignore               # <无操作> [左键-单击]
MBTN_LEFT_DBL  cycle fullscreen     # 切换 全屏状态 [左键-双击]
MBTN_RIGHT     cycle pause          # 切换 暂停/播放状态 [右键-单击]
WHEEL_UP       add volume  2        # 音量 +
WHEEL_DOWN     add volume -2        # 音量 -
SPACE          cycle pause          # 切换 暂停/播放状态 [空格键]
ENTER          cycle fullscreen     # 切换 全屏状态 [回车键]
ESC            set fullscreen no    # 退出 全屏状态 [ESC]

UP             add volume  2        # 音量 +
DOWN           add volume -2        # 音量 -
LEFT           seek -5              # 后退 5s
RIGHT          seek  5              # 前进 5s
-              add speed -0.5       # 播放速度 -（最小0.01）
=              add speed  0.5       # 播放速度 +（最大100）
BS             set speed  1.0       # 重置播放速度 [退格键]
[              frame-back-step      # （暂停）帧步退
]              frame-step           # （暂停）帧步进
l              ab-loop              # 设置/清除 A-B循环点

` script-binding console/enable     # 打开控制台 ESC退出
i script-binding stats/display-stats
I script-binding stats/display-stats-toggle
```

## 内置脚本

新建 ./portable_config/script-opts/script_name.conf 为同名脚本的配置

### 控制台 console.lua

- 快捷键 ` 唤起控制台
- 快捷键 ESC 关闭

官方手册定位： https://mpv.io/manual/master/#console

### 数据统计 stats.lua

- 快捷键 i 短暂显示
- 快捷键 I 常态显示

官方手册定位： https://mpv.io/manual/master/#stats

## 脚本插件

新建 ./portable_config/scripts/script_name.lua

对应配置 ./portable_config/script-opts/script_name.conf

https://github.com/mpv-player/mpv/wiki/User-Scripts#lua-scripts

- autoload.lua：自动载入播放列表
- playlistmanager.lua：播放列表显示

