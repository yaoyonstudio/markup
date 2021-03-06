# mac

## brew

>类似ubuntu中的apt-get包管理器，主要装非图形化界面，需下载源码，编译，安装

命令行安装

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

使用

```
$brew search name       	# 搜索brew 支持的软件（支持模糊搜索）
$brew info svn			   # 显示软件的各种信息（包括版本、源码地址、依赖等等）
$brew install name          # 安装源码
$brew uninstall name	    # 卸载软件
$brew upgrade name    		#更新安装过的软件(如果不加软件名，就更新所有可以更新的软件)
$brew list                  # 列出本机通过brew安装的所有软件
$brew update                # brew自身更新
$brew cleanup             	#清除下载的缓存
(PS:详见man brew)
```

## brew cask

> 对于图形化界面程序的安装管理，补充了appstore，需下载编译好的文件，安装

安装

```
安装完brew时，brew-cask已经安装好了，无需额外安装
```

使用

```
$brew cask search               # 列出所有可以被安装的软件
$brew cask search name     	    # 查找所有和 name相关的应用
$brew cask info app             # 列出应用的信息
$brew cask install name         # 下载安装软件
$brew cask uninstall name       # 卸载软件
$brew cask upgrade name    		#更新安装过的软件(如果不加软件名，就更新所有可以更新的软件)
$brew cask list                 # 列出本机安装过的软件列表
$brew cask cleanup              # 清除下载的缓存以及各种链接信息
(PS:详见man brew cask)
```

## 系统文件

```
# 显示
defaults write com.apple.finder AppleShowAllFiles TRUE
killall Finder
# 关闭
defaults write com.apple.finder AppleShowAllFiles FALSE
killall Finder
```

