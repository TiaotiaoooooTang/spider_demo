import requests
# 只有https协议才会有ssl认证错误
url = 'https://www.12306.cn/mormhweb/'
# response = requests.get(url)
response = requests.get(url,verify=False) # 关闭ssl认证

# print(response.content.decode())
print(response.status_code)  # ssl.CertificateError: hostname 'www.12306.cn' doesn't match either of 'webssl.chinanetcenter.com', 'i.l.inmobicdn.net', '*.fn-mart.com', 'www.1zhe.com', '*.pinganfang.com', '*.anhouse.com', 'dl.jphbpk.gxpan.cn', 'dl.givingtales.gxpan.cn', 'dl.toyblast.gxpan.cn', 'dl.sds.gxpan.cn', 'download.ctrip.com', 'mh.tiancity.com', 'cdn.hxjyios.iwan4399.com', 'ios.hxjy.iwan4399.com', 'gjzx.gjzq.com.cn', 'f.3000test.com', 'tj.img4399.com', '*.zhe800.com', '*.qiyipic.com', '*.vxinyou.com', '*.gdjh.vxinyou.com', '*.3000.com', 'pay.game2.cn', 'static1.j.cn', 'static2.j.cn', 'static3.j.cn', 'static4.j.cn', 'video1.j.cn', 'video2.j.cn', 'video3.j.cn', 'online.j.cn', 'playback.live.j.cn', 'audio1.guang.j.cn', 'audio2.guang.j.cn', 'audio3.guang.j.cn', 'img1.guang.j.cn', 'img2.guang.j.cn', 'img3.guang.j.cn', 'img4.guang.j.cn', 'img5.guang.j.cn', 'img6.guang.j.cn', '*.4399youpai.com', 'w.tancdn.com', '*.3000api.com', 'static11.j.cn', '*.kuyinyun.com', '*.kuyin123.com', '*.diyring.cc', '3000test.com', '*.3000test.com', 'www.3387.com', '*.cankaoxiaoxi.com', '*.service.kugou.com', 'xiuxiu.huodong.meitu.com', '*.meitu.com', '*.meitudata.com', '*.wheetalk.com', '*.shanliaoapp.com', 'xiuxiu.web.meitu.com', 'api.account.meitu.com', 'open.web.meitu.com', 'id.api.meitu.com', 'api.makeup.meitu.com', 'im.live.meipai.com', '*.meipai.com', 'img1.homekoocdn.com', 'cdn.homekoocdn.com', 'cdn1.homekoocdn.com', 'cdn2.homekoocdn.com', 'cdn3.homekoocdn.com', 'cdn4.homekoocdn.com', 'img.homekoocdn.com', 'img2.homekoocdn.com', 'img3.homekoocdn.com', 'img4.homekoocdn.com', '*.macauslot.com', '*.samsungapps.com', 'auto.tancdn.com', '*.winbo.top', 'static.bst.meitu.com', 'api.xiuxiu.meitu.com', 'api.photo.meituyun.com', 'h5.selfiecity.meitu.com', 'api.selfiecity.meitu.com', 'h5.beautymaster.meiyan.com', 'api.beautymaster.meiyan.com', 'www.yawenb.com', 'm.yawenb.com', 'www.biqugg.com', 'www.dawenxue.net', 'cpg.meitubase.com', 'www.qushuba.com', 'www.ranwena.com', '*.4399sy.com', 'ms.awqsaged.cn', 'fanxing2.kugou.com', 'fanxing.kugou.com', 'sso.56.com', 'upload.qf.56.com', 'sso.qianfan.tv', 'cdn.danmu.56.com', 'www-ppd.hermes.cn', 'www-uat.hermes.cn', 'www-ts2.hermes.cn', 'www-tst.hermes.cn', '*.syyx.com', 'img.09mk.cn', 'img.85nh.cn', '*.zhuoquapp.com', '*.5054399.com', '*.aiwan4399.com', 'user.beevideo.bestv.com.cn', '*.3839.com', '*.actdelivery.net', '*.4399.cn', '*.yx3.com', '*.163.com', 'm.kf.cn', 'cmscn.bmwgroup.com', 'secure-int-web-tic-cn.bmwgroup.com', 'pvmessage.cn.bmwgroup.com', 'secure-infonet3.bmwgroup.com', 'secure-infonet3-int.bmwgroup.com', 'secure-web-tic-mini-cn.bmwgroup.com', 'secure-int-web-tic-mini-cn.bmwgroup.com', 'secure-infonet2-int.bmwgroup.com', 'secure-web-tic-cn.bmwgroup.com', 'yjzhres.bnngame.com', '*.account.meitu.com', 'cdn.ssjj.iwan4399.com', '*.iwan4399.com', 'm.kyxnz.cn', 'wheetalk.com'
