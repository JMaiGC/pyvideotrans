# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'info.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore,  QtWidgets
from PySide6.QtGui import  QDesktopServices


class Ui_articleform(object):
    def setupUi(self, articleform):
        articleform.setObjectName("articleform")
        articleform.setWindowModality(QtCore.Qt.NonModal)
        articleform.resize(900, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(articleform.sizePolicy().hasHeightForWidth())
        articleform.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(articleform)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser = QtWidgets.QTextBrowser(articleform)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.anchorClicked.connect(self.openExternalLink)
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)

        self.retranslateUi(articleform)
        QtCore.QMetaObject.connectSlotsByName(articleform)
    def openExternalLink(self, url):
        # Open the link in the system browser
        QDesktopServices.openUrl(url)

    def retranslateUi(self, articleform):
        _translate = QtCore.QCoreApplication.translate
        articleform.setWindowTitle(_translate("articleform", "帮助教程文章"))
        self.textBrowser.setHtml(_translate("articleform", """
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" />
<style type="text/css">
ul{margin-bottom:30px}
p, li { white-space: pre-wrap; margin-bottom:10px}
a{text-decoration:none;color:#fff;font-size:14px}
a:hover{color:#ff0}
</style></head>
<body style="font-size:9pt; font-weight:400; font-style:normal;">
<div>
<a  href="https://www.pyvideotrans.com" style="font-size:18px"> 
最新教程请查看文档网站 pyvideotrans.com
</a>
<br>
<a  href="https://tool.pyvideotrans.com/trans.html" style="font-size:14px;color:#aaa;display:block;margin-top:12px"> 
在线免费视频翻译:使用更简单，无需注册无需登录，点击打开
</a>
</div>



<ul>

<li><a href="https://pyvideotrans.com/guide">使用方法</a></li>
<li><a href="https://pyvideotrans.com/01">新手快速入门</a></li>
<li><a href="https://pyvideotrans.com/02">模型使用与说明</a></li>
<li><a href="https://pyvideotrans.com/setting">界面选项与相关设置</a></li>
<li><a href="https://pyvideotrans.com/duojuese">多角色配音</a></li>
<li><a href="https://pyvideotrans.com/shiting">试听配音</a></li>         
<li><a href="https://pyvideotrans.com/model">模型下载</a></li>
<li><a href="https://pyvideotrans.com/faq">常见问题</a></li>

<li><a href="https://pyvideotrans.com/vocal">人声和背景音乐分离</a></li>   
<li><a href="https://pyvideotrans.com/gpu">CUDA安装配置</a></li>
<li><a href="https://pyvideotrans.com/cache">如何彻底删除缓存</a></li>
<li><a href="https://pyvideotrans.com/chongshi">频繁出现重试5次失败</a></li>
<li><a href="https://pyvideotrans.com/10">百度翻译/腾讯翻译/Gemini等API申请</a></li>
<li><a href="https://pyvideotrans.com/openai">ChatGPT接口使用</a></li>          
<li><a href="https://pyvideotrans.com/deeplx">部署DeepLX</a></li>
<li><a href="https://pyvideotrans.com/06">在cloudflare上创建免费翻译API</a></li>
<li><a href="https://pyvideotrans.com/13">FreeGoogle翻译使用</a></li>
<li><a href="https://pyvideotrans.com/15">无需代理使用Google翻译的方法</a></li>
<li><a href="https://pyvideotrans.com/ott">部署OTT文字翻译</a></li>

<li><a href="https://pyvideotrans.com/adv">高级设置参数说明</a></li>
<li><a href="https://pyvideotrans.com/09">声音字幕画面对齐方法</a></li>
<li><a href="https://pyvideotrans.com/03">faster模式与openai模式的区别</a></li>
<li><a href="https://pyvideotrans.com/04">提高翻译质量的技巧</a></li>
<li><a href="https://pyvideotrans.com/cli">CLI命令行使用</a></li>
<li><a href="https://pyvideotrans.com/12">在软件中使用GPT-SoVITS配音</a></li>
<li><a href="https://pyvideotrans.com/14">本地部署Qwen通义千问大模型</a></li>

</ul>

<p style="padding:8px;margin-top:15px;margin-bottom:20px">
<a style="color:#ff0;" href="https://github.com/jianchang512/pyvideotrans/blob/main/about.md">开源不易，在免费的情况下保持维护和优化更难，若有可能请小额赞助，帮助项目持续更新。点击软件底部右下角“小额捐赠”字样可查看捐助方式和信息</a></p>

<hr style="color:#161E26;background-color:#161E26">
<hr style="color:#161E26;background-color:#161E26">
</body></html>
"""))