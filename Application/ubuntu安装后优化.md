# 卸载

```
# 卸载不需要的软件
sudo apt-get remove  unity-webapps-common  totem  rhythmbox simple-scan gnome-mahjongg aisleriot gnome-mines  transmission-common gnome-orca webbrowser-app gnome-sudoku onboard deja-dup firefox libreoffice-style-galaxy thunderbird
# 清理缓存
sudo apt-get autoremove
sudo apt-get autoclean 
```
# 更换源
- 方法一：

图形化界面中，更改设置中的软件与更新，选择中国阿里云

- 方法二：

命令行修改

```
# 打开配置文件
sudo cp /etc/apt/sources.list /etc/apt/sources.list.backup
sudo vi /etc/apt/sources.list
# 添加如下163 ubuntu16.04源
deb http://mirrors.163.com/ubuntu/ xenial main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ xenial-security main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ xenial-updates main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ xenial-proposed main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ xenial-backports main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ xenial main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ xenial-security main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ xenial-updates main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ xenial-proposed main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ xenial-backports main restricted universe multiverse
# 添加优麒麟的源
echo deb http://archive.ubuntukylin.com:10006/ubuntukylin trusty main | sudo tee /etc/apt/sources.list.d/ubuntukylin.list 
# 更新源
sudo apt-get update 
# 注:如果提示没有公钥,无法验证下列数字签名 xxx
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-　keys xxxx
sudo apt-get update
```
# 常用软件安装

## 常规安装
```
sudo apt-get install git vlc unrar gparted nginx bleachbit htop
```

## vim
```
sudo add-apt-repository ppa:jonathonf/vim
sudo apt update
sudo apt install vim ctags vim-doc
```

## typora
```
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys BA300B7755AFCFAE
sudo add-apt-repository 'deb http://typora.io linux/'
sudo apt-get update
sudo apt-get install typora
```
## R
```
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9
sudo sh -c "echo deb http://mirror.bjtu.edu.cn/cran/bin/linux/ubuntu precise/ >>/etc/apt/sources.list"
sudo apt-get install r-base
sudo apt-get install r-base-dev
sudo apt-get update
```
## wine-de
```
sudo add-apt-repository ppa:wine/wine-builds
sudo apt-get update
sudo apt-get install wine-devel
sudo apt install winehq-devel
```
## Thunderbird
```
sudo add-apt-repository ppa:ubuntu-mozilla-security/ppa
sudo apt-get update
sudo apt-get install thunderbird
```
## gimp
```
# 安装
sudo add-apt-repository ppa:otto-kesselgulasch/gimp
sudo apt-get update
sudo apt-get install gimp
# 卸载(可选)
sudo apt-get install ppa-purge
sudo ppa-purge ppa:otto-kesselgulasch/gimp
```
## chrome
```
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb 
sudo apt-get install libappindicator1 libindicator7 
sudo dpkg -i google-chrome-stable_current_amd64.deb 
# 自动安装依赖
$ sudo apt-get -f install 
```

## indicator-sysmonitor

```
sudo add-apt-repository ppa:fossfreedom/indicator-sysmonitor 
sudo apt-get update 
sudo apt-get install indicator-sysmonitor
```
## wps

```
sudo apt-get install wps-office 
# 1. 下载缺失的字体文件
# 国外下载地址：https://www.dropbox.com/s/lfy4hvq95ilwyw5/wps_symbol_fonts.zip
# 国内下载地址：https://pan.baidu.com/s/1eS6xIzo
# 解压并进入目录中，继续执行：
sudo cp * /usr/share/fonts
# 2. 执行以下命令,生成字体的索引信息：
sudo mkfontscale
sudo mkfontdir
# 3. 运行fc-cache命令更新字体缓存。
sudo fc-cache
# 4. 重启wps即可，字体缺失的提示不再出现。
```

## pycharm
```
sudo snap install [pycharm-professional|pycharm-community] --classic
```
## mysql
```
sudo apt-get install mysql-server
sudo apt-get install libmysqld-dev 
sudo apt-get install libmysqlclient-dev 
```
## redis
```
sudo apt-get install software-properties-common
sudo apt-add-repository ppa:chris-lea/redis-server
sudo apt-get update
sudo apt-get install redis-server
```
## remarkable
```
wget https://remarkableapp.github.io/files/remarkable_1.87_all.deb
sudo dpkg -i remarkable_1.87_all.deb
sudo apt-get -f install 
```
## Nodepadqq
```
sudo add-apt-repository ppa:notepadqq-team/notepadqq
sudo apt-get update
sudo apt-get install notepadqq
```

## polipo

socket5代理转换为http

```
sudo apt-get install polipo
# 停止服务
sudo service polipo stop
# 修改配置文件
sudo vi /etc/polipo/config
# 新增如下两个配置
socksParentProxy = localhost:1080
proxyPort = 8787
# 启动服务
$ sudo service polipo start
# 添加命令代理别名
$ cd
$ vi .bashrc
# 添加配置如下
 alias http_proxy='export http_proxy=http://127.0.0.1:8787/'
alias https_proxy='export https_proxy=http://127.0.0.1:8787/'
# 生效配置
$ source .bashrc 
```
## ss-qt5
```
# 安装curl
$ sudo apt install curl
# 安装ss-qt5
# github地址：https://github.com/shadowsocks/shadowsocks-qt5/releases
# 使用命令下载
$ wget https://github-production-release-asset-2e65be.s3.amazonaws.com/18427187/04086db8-f3cd-11e7-9c68-2b0d4b4dbe5b?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20180112%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20180112T150901Z&X-Amz-Expires=300&X-Amz-Signature=73c91b88196b277e49f46a9d0874d4d76384c6b35d33861b3c9b55a4396b03f7&X-Amz-SignedHeaders=host&actor_id=0&response-content-disposition=attachment%3B%20filename%3DShadowsocks-Qt5-3.0.0-x86_64.AppImage&response-content-type=application%2Foctet-stream

# 启动ss-qt5客户端，添加配置，启动服务
# 测试代理
$ http_proxy
$ https_proxy
$ curl http://ip.cn
```
## pac manager（xshell替代）
```
$ wget https://astuteinternet.dl.sourceforge.net/project/pacmanager/pac-4.0/pac-4.5.5.7-all.deb
$ sudo dpkg -i pac-4.5.5.7-all.deb 
$ sudo apt-get install -f
$ sudo apt-get install libgtk2-appindicator-perl
```
## vpnc
```
sudo apt-get install git vpnc
```
## openssh-server
```
sudo apt-get install openssh-server
```
## gdb-dashboard
```
wget -P ~ git.io/.gdbinit
mv ~/.gdbinit ~/.gdb-dashboard
# 然后在使用gdb调试的时候可以在gdb界面调用gdb-dashboard
(gdb) source ~/.gdb-dashboard
# 也可以直接修改~/.gdbinit,加入source ~/.gdb-dashboard使gdb在载入时自动加载gdb-dashboard
```
## VMWare
```
# 永久许可证秘钥： 
VMware Workstation v12 for Windows 
5A02H-AU243-TZJ49-GTC7K-3C61
VMware Workstation v11 for Windows 
1F04Z-6D111-7Z029-AV0Q4-3AEH8
VMware Workstation v10 for Windows 
1Z0G9-67285-FZG78-ZL3Q2-234JG 
4C4EK-89KDL-5ZFP9-1LA5P-2A0J0 
HY086-4T01N-CZ3U0-CV0QM-13DNU 
```
## 设置开启小键盘

```
sudo apt-get install numlockx
sudo gedit /usr/share/lightdm/lightdm.conf.d/50-unity-greeter.conf

# 在配置文件最后添加：
greeter-setup-script=/usr/bin/numlockx on
```
## 同步windows时间

```
sudo timedatectl set-local-rtc 1  
sudo apt-get install ntpdate
sudo ntpdate time.windows.com
sudo hwclock --localtime --systohc
```