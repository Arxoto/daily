# build workspace in new personal computer

## climb wall
```
OVO
https://ovofast.com/#/dashboard
```

## [download]

- pwsh
- VSCode
- OfficeTool
- ~~HoneyView + Bandizip -> 【在压缩包里连续看图】~~
- ~~MouseWithoutBordersSetup~~


## [store]

- powertoys
- terminal
- notepads
- nanazip
- NeeView
- quicklook
- starrea


## [chrome edge]

> C:\Users\xxx\AppData\Local\Microsoft\Edge\User Data\Default\Extensions

- Proxy SwitchyOmega - AutoProxy: https://raw.githubusercontent.com/gfwlist/gfwlist/master/gfwlist.txt
- uBlock Origin
- Tampermonkey
- Markdown Viewer
- SuperCopy
- DeepL translate
- Octotree - GitHub code tree
- Listen 1

## [scoop]

```pwsh
scoop export > .\plaintext\workspace.json
```

### choose dir (admin)
```
$env:SCOOP='D:\develop\scoop'
$env:SCOOP_GLOBAL='D:\develop\scoop\GlobalScoopApps'
$env:SCOOP='C:\develop\Scoop'
$env:SCOOP_GLOBAL='C:\develop\Scoop\GlobalScoopApps'
[Environment]::SetEnvironmentVariable('SCOOP', $env:SCOOP, 'User')
[Environment]::SetEnvironmentVariable('SCOOP_GLOBAL', $env:SCOOP_GLOBAL, 'Machine')
mkdir $env:SCOOP_GLOBAL
```

### normal
```
# (maybe) Set-ExecutionPolicy RemoteSigned -scope CurrentUser
iwr -useb get.scoop.sh | iex
# (or) Invoke-Expression (New-Object System.Net.WebClient).DownloadString('https://get.scoop.sh')
```

```
shutdown -r -t 0
```

```
scoop config proxy localhost:7898
git config --global https.proxy 'socks5://localhost:7898'
git config --global http.proxy 'socks5://localhost:7898'

scoop install git
scoop bucket add extras
scoop bucket add java
scoop bucket add versions
scoop bucket add nerd-fonts
scoop bucket add nonportable
scoop bucket add dorado https://github.com/chawyehsu/dorado

# environment
# main/
scoop install cmake curl ffmpeg sudo gsudo lessmsi
scoop install gcc mingw rustup-msvc python go nodejs pnpm # 由 rustup 管理 rust & cargo
# java/
scoop install openjdk17
scoop install openjdk8-redhat
# versions/
scoop install python27

# environment
# extras/
sudo scoop install vcredist2005 vcredist2008 vcredist2010 vcredist2012 vcredist2013 vcredist2022
# scoop install main/dotnet-sdk
# scoop install dorado/dotnet-desktop-runtime

# system clean program +runner
# extras/
scoop install dismplusplus driverstoreexplorer geekuninstaller
scoop install freemove wiztree # spacesniffer
scoop install memreduct hasher

# video picture +runner
# main/
scoop install youtube-dl yt-dlp
# extras/
scoop install vlc mpv mpv.net youtube-dl-gui
scoop install screentogif sharex
# scoop install potplayer madvr
# # nonportable/
# scoop install lav-filters-megamix-np

# builder +runner
# extras/
# 绘图 矢量 位图
scoop install inkscape krita
# 视频音频
scoop install shotcut audacity
# 3D建模
scoop install blender
# 2D动画
scoop install opentoonz # enve找不到
# 游戏引擎
scoop install godot
# 串流
scoop install moonlight sunshine
# 按键显示
scoop install keyviz

# Android +runner
# main/
scoop install adb scrcpy
# extras/
scoop install qtscrcpy

# download +runner
# main/
scoop install n-m3u8dl-cli
# extras/
scoop install qbittorrent-enhanced aria-ng-gui neatdownloadmanager
# emule motrix

# 或者直接 https://discord.com/app
# proxy +runner
# main
scoop install sing-box v2ray xray
# extras/
scoop install clash-verge-rev v2rayn telegram discord

# program recommend +runner
# nerd-fonts/
sudo scoop install -g SarasaGothic-SC
# extras/
scoop install sumatrapdf cheat-engine
# dorado/
scoop install steampp

# program start_with_os
# extras/
scoop install everything translucenttb # eartrumpet quicklook
# dorado/
scoop install trafficmonitor snipaste-beta

# *hold*
scoop hold nodejs pnpm
# scoop hold gcc mingw rustup-msvc go # dotnet-sdk dotnet-desktop-runtime
scoop hold vcredist2005 vcredist2008 vcredist2010 vcredist2012 vcredist2013 vcredist2022
# scoop hold lav-filters-megamix-np madvr
sudo scoop hold -g SarasaGothic-SC

# check
scoop checkup
scoop status
```

```
shutdown -r -t 0
```

## down_xz_N_m3u8DL-setting.html
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>m3u8</title>
</head>

<style type="text/css">
    table tr td:first-child {
        text-align: right;
    }

    textarea {
        resize: none;
        border-style: none;
    }

    textarea::-webkit-scrollbar {
        display: none;
    }
</style>

<body onload="init()">
    <table id="table">
        <tr>
            <td colspan="2">
                <h1>click below to copy |</h1>
            </td>
            <td>
                <h1><a href="https://nilaoda.github.io/N_m3u8DL-CLI/Advanced.html">m3u8 home</a></h1>
            </td>
        </tr>
        <tr>
            <td colspan="2">
                <p>delete the log in_</p>
            </td>
            <td><textarea style="width: 25em; height: 1em;"
                    onfocus="this.select();document.execCommand('copy');">C:\develop\Scoop\apps\n-m3u8dl-cli\current</textarea>
            </td>
        </tr>
        <tr>
            <td colspan="2"><textarea id="result" style="width: 30em; text-align: right;"></textarea></td>
        </tr>
        <tr>
            <td>URL|File|JSON 下载链接</td>
            <td><input type="text" id="UrlFileJson" onchange="flush()" onfocus="this.select();" /></td>
        </tr>
    </table>
</body>

<script>
    const settings = {
        workDir: 'D:\\Downloads',
        proxyAddress: 'http://127.0.0.1:10809'
    }
    const params = {
        workDir: ['', 'Directory 设定程序工作目录'],
        saveName: ['', 'Filename 设定存储文件名(不包括后缀)'],
        proxyAddress: ['', 'http://ip:port 设置HTTP代理'],
        stopSpeed: [0, 'Number 当速度低于此值时，重试(单位为KB/s)'],
        maxSpeed: [0, 'Number 设置下载速度上限(单位为KB/s)'],
        baseUrl: ['', 'BaseUrl 设定Baseurl'],
        headers: ['', 'headers 设定请求头，格式 key:value 使用|分割不同的key&value'],
        downloadRange: ['', 'Range 仅下载视频的一部分分片或长度'],
        liveRecDur: ['', 'HH:MM:SS 直播录制时，达到此长度自动退出软件'],
        maxThreads: [32, 'Thread 设定程序的最大线程数(默认为32)'],
        minThreads: [16, 'Thread 设定程序的最小线程数(默认为16)'],
        retryCount: [15, 'Count 设定程序的重试次数(默认为15)'],
        timeOut: [10, 'Sec 设定程序网络请求的超时时间(单位为秒，默认为10秒)'],
        muxSetJson: ['', 'File 使用外部json文件定义混流选项'],
        useKeyFile: ['', 'File 使用外部16字节文件定义AES-128解密KEY'],
        useKeyBase64: ['', 'Base64String 使用Base64字符串定义AES-128解密KEY'],
        useKeyIV: ['', 'HEXString 使用HEX字符串定义AES-128解密IV'],
        enableDelAfterDone: [false, '开启下载后删除临时文件夹的功能'],
        enableMuxFastStart: [false, '开启混流mp4的FastStart特性'],
        enableBinaryMerge: [false, '开启二进制合并分片'],
        enableParseOnly: [false, '开启仅解析模式(程序只进行到meta.json)'],
        enableAudioOnly: [false, '合并时仅封装音频轨道'],
        disableDateInfo: [false, '关闭混流中的日期写入'],
        noMerge: [false, '禁用自动合并'],
        noProxy: [false, '不自动使用系统代理'],
        disableIntegrityCheck: [false, '不检测分片数量是否完整']
    }
    function init() {
        const table = document.getElementById('table');
        for (const key in params) {
            if (Object.hasOwnProperty.call(params, key)) {
                const value = params[key][0];
                const describe = params[key][1];
                let tr = document.createElement('tr');
                tr.appendChild(document.createElement('td')).append(describe);
                let input = document.createElement('input');
                input.id = key;
                if (typeof value === "string") {
                    input.type = 'text';
                    input.value = value;
                } else if (typeof value === "number") {
                    input.type = 'number';
                    input.value = value;
                } else if (typeof value === "boolean") {
                    input.type = 'checkbox';
                    input.checked = value;
                }
                input.onchange = flush;
                tr.appendChild(document.createElement('td')).appendChild(input);
                table.appendChild(tr);
            }
        }
        for (const key in settings) {
            if (Object.hasOwnProperty.call(settings, key)) {
                const value = settings[key];
                document.getElementById(key).value = value;
            }
        }
        document.getElementById('UrlFileJson').focus();
    }
    function flush() {
        const result = document.getElementById('result');
        const UFJ = document.getElementById('UrlFileJson').value;
        if (!UFJ) {
            result.value = 'no Url File Json';
            result.onfocus = () => { };
            return;
        }
        let resultVlaue = `"${UFJ}"`;
        for (const key in params) {
            if (Object.hasOwnProperty.call(params, key)) {
                const defaultValue = params[key][0];
                if (typeof defaultValue === "boolean") {
                    const value = document.getElementById(key).checked;
                    if (value !== defaultValue) {
                        resultVlaue += ` --${key}`;
                    }
                } else {
                    const value = document.getElementById(key).value;
                    if (value != defaultValue) {
                        resultVlaue += ` --${key} ${value}`;
                    }
                }
            }
        }
        result.value = resultVlaue;
        result.onfocus = copy;
    }
    function copy() {
        const result = document.getElementById('result');
        result.select();
        document.execCommand('copy');
    }
</script>

</html>
```

## qbittorrent tracker
https://trackerslist.com/all.txt


## [setting.terminal]

<https://wallpaperhub.app/wallpapers/6277>

background60 acrylic80

pwshElevated sudo pwsh


## [setting]

7zip

everything.server

eartrumpet.start_with_os_reg

snipaste.shortcut


## VLC 关联文件
```reg
Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\vlc\shell\open\command]
@="\"D:\\develop\\scoop\\apps\\vlc\\current\\vlc.exe\" \"%1\""

[HKEY_CLASSES_ROOT\.aac]
@="vlc"

[HKEY_CLASSES_ROOT\.ac3]
@="vlc"

[HKEY_CLASSES_ROOT\.flac]
@="vlc"

[HKEY_CLASSES_ROOT\.m4a]
@="vlc"

[HKEY_CLASSES_ROOT\.m4p]
@="vlc"

[HKEY_CLASSES_ROOT\.mp1]
@="vlc"

[HKEY_CLASSES_ROOT\.mp2]
@="vlc"

[HKEY_CLASSES_ROOT\.mp3]
@="vlc"

[HKEY_CLASSES_ROOT\.wav]
@="vlc"

[HKEY_CLASSES_ROOT\.wma]
@="vlc"

[HKEY_CLASSES_ROOT\.f4v]
@="vlc"

[HKEY_CLASSES_ROOT\.flv]
@="vlc"

[HKEY_CLASSES_ROOT\.mkv]
@="vlc"

[HKEY_CLASSES_ROOT\.mov]
@="vlc"

[HKEY_CLASSES_ROOT\.mp2v]
@="vlc"

[HKEY_CLASSES_ROOT\.mp4]
@="vlc"

[HKEY_CLASSES_ROOT\.mp4v]
@="vlc"

[HKEY_CLASSES_ROOT\.rmvb]
@="vlc"

[HKEY_CLASSES_ROOT\.wmv]
@="vlc"

[HKEY_CLASSES_ROOT\.m3u]
@="vlc"

[HKEY_CLASSES_ROOT\.m3u8]
@="vlc"

[HKEY_CLASSES_ROOT\.vlc]
@="vlc"

[HKEY_CLASSES_ROOT\Applications\vlc\shell\open\command]
@="\"D:\\develop\\scoop\\apps\\vlc\\current\\vlc.exe\" \"%1\""

[HKEY_CLASSES_ROOT\Applications\vlc\SupportedTypes]
".aac"=""
".ac3"=""
".flac"=""
".m4a"=""
".m4p"=""
".mp1"=""
".mp2"=""
".mp3"=""
".wav"=""
".wma"=""
".f4v"=""
".flv"=""
".mkv"=""
".mov"=""
".mp2v"=""
".mp4"=""
".mp4v"=""
".rmvb"=""
".wmv"=""
".m3u"=""
".m3u8"=""
".vlc"=""

```

## PotPlayerMini64.ini 滤镜 关联

- 关闭内置滤镜（图像滤镜关闭、内置编解码滤镜支持视频流切换）
- 全局滤镜强制使用
- madvr驱动类型选择 digital monitor

```
[MainShortCutList]
0=9,0,10351,0
1=13,0,10013,0
2=27,0,10013,0
3=8,0,10230,0
4=32,0,10014,0
5=68,0,10292,0
6=65,0,10291,0
7=87,0,10248,0
8=83,0,10247,0
9=81,0,10249,0
10=90,0,10251,0
11=69,0,10250,0
12=67,0,10252,0
13=39,0,10060,0
14=37,0,10059,0
15=38,0,10035,0
16=40,0,10036,0
17=116,0,10010,0
18=117,0,10228,0
19=119,0,10011,0
20=
```
