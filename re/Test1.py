import re

html = """
<!DOCTYPE html><html><head><meta charset=utf-8><title>赵露思机场街拍，长的好看的人笑起来果然都很甜</title><meta http-equiv=x-dns-prefetch-control content=on><link rel=dns-prefetch href=//s3.pstatp.com/ ><link rel=dns-prefetch href=//s3a.pstatp.com/ ><link rel=dns-prefetch href=//s3b.pstatp.com><link rel=dns-prefetch href=//p1.pstatp.com/ ><link rel=dns-prefetch href=//p3.pstatp.com/ ><meta http-equiv=Content-Type content="text/html; charset=utf-8"><meta http-equiv=X-UA-Compatible content="IE=edge,chrome=1"><meta name=viewport content="width=device-width,initial-scale=1,maximum-scale=1,minimum-scale=1,user-scalable=no,minimal-ui"><meta name=360-site-verification content=b96e1758dfc9156a410a4fb9520c5956><meta name=360_ssp_verify content=2ae4ad39552c45425bddb738efda3dbb><meta name=google-site-verification content=3PYTTW0s7IAfkReV8wAECfjIdKY-bQeSkVTyJNZpBKE><meta name=shenma-site-verification content=34c05607e2a9430ad4249ed48faaf7cb_1432711730><meta name=baidu_union_verify content=b88dd3920f970845bad8ad9f90d687f7><meta name=domain_verify content=pmrgi33nmfuw4ir2ej2g65lunfqw6ltdn5wselbcm52wszbchirdqyztge3tenrsgq3dknjume2tayrvmqytemlfmiydimddgu4gcnzcfqrhi2lnmvjwc5tfei5dcnbwhazdcobuhe2dqobrpu><link rel="shortcut icon" href=//s3a.pstatp.com/toutiao/resource/ntoutiao_web/static/image/favicon_5995b44.ico type=image/x-icon><!--[if lt IE 9]>
  <p>您的浏览器版本过低，请<a href="http://browsehappy.com/">升级浏览器</a></p>
<![endif]--><script src="//s3.pstatp.com/toutiao/monitor/sdk/slardar.js?ver=20171221_1" crossorigin=anonymous></script><script>window.Slardar && window.Slardar.install({
    sampleRate: 1,
    bid: 'toutiao_pc',
    pid: 'image_detail_new',
    ignoreAjax: [/\/action_log\//],
    ignoreStatic: [/\.tanx\.com\//, /\.alicdn\.com\//, /\.mediav\.com/]
  });</script><meta name=pathname content=toutiao_pc_image_detail_new><meta name=keywords content=今日头条，头条，头条网，头条新闻，今日头条官网><meta name=description content=《今日头条》(www.toutiao.com)是一款基于数据挖掘的推荐引擎产品，它为用户推荐有价值的、个性化的信息，提供连接人与信息的新型服务，是国内移动互联网领域成长最快的产品服务之一。><link rel=stylesheet href=//s3b.pstatp.com/toutiao/static/css/page/index_node/index.8b48d1a4c3755dc87013acbbf1b28182.css><script>!function(e){function t(a){if(o[a])return o[a].exports;var r=o[a]={exports:{},id:a,loaded:!1};return e[a].call(r.exports,r,r.exports,t),r.loaded=!0,r.exports}var a=window.webpackJsonp;window.webpackJsonp=function(n,p){for(var c,s,l=0,i=[];l<n.length;l++)s=n[l],r[s]&&i.push.apply(i,r[s]),r[s]=0;for(c in p)Object.prototype.hasOwnProperty.call(p,c)&&(e[c]=p[c]);for(a&&a(n,p);i.length;)i.shift().call(null,t);if(p[0])return o[0]=0,t(0)};var o={},r={0:0};t.e=function(e,a){if(0===r[e])return a.call(null,t);if(void 0!==r[e])r[e].push(a);else{r[e]=[a];var o=document.getElementsByTagName("head")[0],n=document.createElement("script");n.type="text/javascript",n.charset="utf-8",n.async=!0,n.src=t.p+"static/js/"+e+"."+{1:"134e79204c8c9a21bd21",2:"8a6e6ade8a4b1796823d",3:"0b96e5779e3f1eefe13c",4:"80a93b04852050a9996f"}[e]+".js",o.appendChild(n)}},t.m=e,t.c=o,t.p="/toutiao/",t.p="//s3.pstatp.com/toutiao/"}([]);</script></head><body><div id=app></div><script src=//s3.pstatp.com/inapp/lib/raven.js crossorigin=anonymous></script><script>;(function(window) {
    // sentry
    window.Raven && Raven.config('//key@m.toutiao.com/log/sentry/v2/96', {
      whitelistUrls: [/pstatp\.com/],
      sampleRate: 1,
      shouldSendCallback: function(data) {
        var ua = navigator && navigator.userAgent;
        var isDeviceOK = !/Mobile|Linux/i.test(navigator.userAgent);
        if (data.message && data.message.indexOf('p.tanx.com') !== -1) {
          return false;
        }
        return isDeviceOK;
      },
      tags: {
        bid: 'toutiao_pc',
        pid: 'image_detail_new'
      },
      autoBreadcrumbs: {
        'xhr': false,
        'console': true,
        'dom': true,
        'location': true
      }
    }).install();
  })(window);</script><script>var PAGE_SWITCH = {"adScriptQihu":true,"adScriptTB":true,"anti_spam":false,"migScriptUrl":"//s3a.pstatp.com/toutiao/picc_mig/dist/img.min.js","nineteen":"","picVersion":"20180412_01","qihuAdShow":true,"taVersion":"20171221_1","ttAdShow":true};</script><script>var BASE_DATA = {
    headerInfo: {
      id: 0,
      isPgc: false,
      userName: '',
      avatarUrl: '',
      isHomePage: false,
      chineseTag: '图片',
      crumbTag: 'ch/news_image/',
      hasBar: true
    },
    mediaInfo: {
      name: '美搭刊',
      avatarUrl: '//p3.pstatp.com/large/135300132f188efeb9ff',
      openUrl: '/c/user/3880121671/',
      user_id: '3880121671',
      like: false
    },
    userInfo: {
      id: 0,
      name: '',
      avatarUrl: '',
      isPgc: false,
      isOwner: false
    },
    commentInfo: {
      group_id: '6646919257013617166',
      item_id: '6646919257013617166',
      comments_count: 30,
      ban_comment: 0
    }
  }

  BASE_DATA.galleryInfo = {
    title: '赵露思机场街拍，长的好看的人笑起来果然都很甜',
    isOriginal: true,
    mediaInfo: BASE_DATA.mediaInfo,
    
    gallery: JSON.parse("{\"count\":9,\"sub_images\":[{\"url\":\"http:\\/\\/p1.pstatp.com
    \\/origin\\/pgc-image\\/001aebfe528a457e96342d3589bc641f\",\"width\":800,\"url_list\":
    [{\"url\":\"http:\\/\\/p1.pstatp.com\\/origin\\/pgc-image\\/001aebfe528a457e96342d3589bc641f\"},
    {\"url\":\"http:\\/\\/pb3.pstatp.com\\/origin\\/pgc-image\\/001aebfe528a457e96342d3589bc641f\"},
    {\"url\":\"http:\\/\\/pb9.pstatp.com\\/origin\\/pgc-image\\/001aebfe528a457e96342d3589bc641f\"}]
    u4eba\\u7b11\\u8d77\\u6765\\u679c\\u7136\\u90fd\\u5f88\\u751c\"]}"),
    
    
    
"""

pattern = re.compile('BASE_DATA.galleryInfo.*?title:.*?\'(.*?)\',.*?gallery: JSON.parse\("(.*?)"\),', re.S)
result = re.search(pattern, html)
if result:
    print(result.group(1))

html = """
{\"count\":7,\"sub_images\":[{\"url\":\"http:\\/\\/p1.pstatp.com\\/origin\\/pgc-image\\/91b25b33ce3d46719f7e990993557e8e\",\"width\":600,\"url_list\":[{\"url\":\"http:\\/\\/p1.pstatp.com\\/origin\\/pgc-image\\/91b25b33ce3d46719f7e990993557e8e\"},{\"url\":\"http:\\/\\/pb3.pstatp.com\\/origin\\/pgc-image\\/91b25b33ce3d46719f7e990993557e8e\"},{\"url\":\"http:\\/\\/pb9.pstatp.com\\/origin\\/pgc-image\\/91b25b33ce3d46719f7e990993557e8e\"}],\"uri\":\"origin\\/pgc-image\\/91b25b33ce3d46719f7e990993557e8e\",\"height\":900},{\"url\":\"http:\\/\\/p1.pstatp.com\\/origin\\/pgc-image\\/ff8c1c600c43462c95b5159b4f514758\",\"width\":600,\"url_list\":[{\"url\":\"http:\\/\\/p1.pstatp.com\\/origin\\/pgc-image\\/ff8c1c600c43462c95b5159b4f514758\"},{\"url\":\"http:\\/\\/pb3.pstatp.com\\/origin\\/pgc-image\\/ff8c1c600c43462c95b5159b4f514758\"},{\"url\":\"http:\\/\\/pb9.pstatp.com\\/origin\\/pgc-image\\/ff8c1c600c43462c95b5159b4f514758\"}],\"uri\":\"origin\\/pgc-image\\/ff8c1c600c43462c95b5159b4f514758\",\"height\":900},{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/pgc-image\\/65600a49dc954d8ea0bd5f173fecc8b7\",\"width\":594,\"url_list\":[{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/pgc-image\\/65600a49dc954d8ea0bd5f173fecc8b7\"},{\"url\":\"http:\\/\\/pb9.pstatp.com\\/origin\\/pgc-image\\/65600a49dc954d8ea0bd5f173fecc8b7\"},{\"url\":\"http:\\/\\/pb1.pstatp.com\\/origin\\/pgc-image\\/65600a49dc954d8ea0bd5f173fecc8b7\"}],\"uri\":\"origin\\/pgc-image\\/65600a49dc954d8ea0bd5f173fecc8b7\",\"height\":756},{\"url\":\"http:\\/\\/p9.pstatp.com\\/origin\\/pgc-image\\/18b60abed26d459ab381d822f0f7dec9\",\"width\":600,\"url_list\":[{\"url\":\"http:\\/\\/p9.pstatp.com\\/origin\\/pgc-image\\/18b60abed26d459ab381d822f0f7dec9\"},{\"url\":\"http:\\/\\/pb1.pstatp.com\\/origin\\/pgc-image\\/18b60abed26d459ab381d822f0f7dec9\"},{\"url\":\"http:\\/\\/pb3.pstatp.com\\/origin\\/pgc-image\\/18b60abed26d459ab381d822f0f7dec9\"}],\"uri\":\"origin\\/pgc-image\\/18b60abed26d459ab381d822f0f7dec9\",\"height\":900},{\"url\":\"http:\\/\\/p1.pstatp.com\\/origin\\/pgc-image\\/a89983baaa7a45108f10debb8a4256e8\",\"width\":600,\"url_list\":[{\"url\":\"http:\\/\\/p1.pstatp.com\\/origin\\/pgc-image\\/a89983baaa7a45108f10debb8a4256e8\"},{\"url\":\"http:\\/\\/pb3.pstatp.com\\/origin\\/pgc-image\\/a89983baaa7a45108f10debb8a4256e8\"},{\"url\":\"http:\\/\\/pb9.pstatp.com\\/origin\\/pgc-image\\/a89983baaa7a45108f10debb8a4256e8\"}],\"uri\":\"origin\\/pgc-image\\/a89983baaa7a45108f10debb8a4256e8\",\"height\":847},{\"url\":\"http:\\/\\/p1.pstatp.com\\/origin\\/pgc-image\\/52c3b962b663453b97abbff0b5e5f949\",\"width\":679,\"url_list\":[{\"url\":\"http:\\/\\/p1.pstatp.com\\/origin\\/pgc-image\\/52c3b962b663453b97abbff0b5e5f949\"},{\"url\":\"http:\\/\\/pb3.pstatp.com\\/origin\\/pgc-image\\/52c3b962b663453b97abbff0b5e5f949\"},{\"url\":\"http:\\/\\/pb9.pstatp.com\\/origin\\/pgc-image\\/52c3b962b663453b97abbff0b5e5f949\"}],\"uri\":\"origin\\/pgc-image\\/52c3b962b663453b97abbff0b5e5f949\",\"height\":1024},{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/pgc-image\\/6e379fc6c3134dc99681249830a44693\",\"width\":479,\"url_list\":[{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/pgc-image\\/6e379fc6c3134dc99681249830a44693\"},{\"url\":\"http:\\/\\/pb9.pstatp.com\\/origin\\/pgc-image\\/6e379fc6c3134dc99681249830a44693\"},{\"url\":\"http:\\/\\/pb1.pstatp.com\\/origin\\/pgc-image\\/6e379fc6c3134dc99681249830a44693\"}],\"uri\":\"origin\\/pgc-image\\/6e379fc6c3134dc99681249830a44693\",\"height\":766}],\"max_img_width\":679,\"labels\":[\"\\u65f6\\u5c1a\",\"\\u7fbd\\u7ed2\\u670d\",\"\\u53e4\\u529b\\u5a1c\\u624e\",\"\\u65f6\\u88c5\\u642d\\u914d\"],\"sub_abstracts\":[\"\\u59dc\\u9ec4\\u8272\\u7f8a\\u7f94\\u7ed2\\u5c0f\\u5916\\u5957\\u5185\\u642d\\u6d45\\u84dd\\u8272\\u886c\\u8863\\u663e\\u5f97\\u4eba\\u7279\\u522b\\u5229\\u7d22\\uff0c\\u7c73\\u8272\\u5927\\u56f4\\u5dfe\\u597d\\u6e29\\u6696\\u3002\\u8fd9\\u4e00\\u8eab\\u642d\\u914d\\u6ca1\\u6bdb\\u75c5\\uff0c\\u552f\\u4e00\\u7684\\u7f3a\\u9677\\u5c31\\u662f\\u59b9\\u5b50\\u7684\\u817f\\u592a\\u7626\\u4e86\\uff0c\\u53cd\\u800c\\u5931\\u53bb\\u4e86\\u7f8e\\u611f\\u3002\\n\",\"\\u8fd9\\u6b3e\\u7fbd\\u7ed2\\u670d\\u5b9d\\u5b9d\\u4eec\\u53ef\\u4ee5\\u5165\\u624b\\u4e00\\u4ef6\\u4e86\\uff0c\\u76f4\\u7b52\\u5bbd\\u677e\\u7248\\u578b\\uff0c\\u7b80\\u7ea6\\u53c8\\u5927\\u65b9\\u3002\\u9ed1\\u767d\\u62fc\\u63a5\\uff0c\\u589e\\u52a0\\u65f6\\u5c1a\\u611f\\u3002\\u9ed1\\u8272\\u6bdb\\u9886\\u63d0\\u5347\\u6c14\\u573a\\uff0c\\u8d8a\\u7b80\\u5355\\uff0c\\u8d8a\\u8010\\u770b\\u3002\",\"\\u9ed1\\u8272\\u4e1d\\u7ed2\\u68c9\\u670d\\uff0c\\u4fdd\\u6696\\u53c8\\u767e\\u642d\\uff0c\\u642d\\u914d\\u6d45\\u8272\\u76f4\\u7b52\\u725b\\u4ed4\\u88e4\\u6700\\u5408\\u9002\\u4e0d\\u8fc7\\u4e86\\u3002\\u7c89\\u8272\\u6bdb\\u8863\\uff0c\\u7126\\u7cd6\\u8272\\u9774\\u5b50\\uff0c\\u7b80\\u5355\\u5229\\u7d22\\uff0c\\u7279\\u522b\\u8010\\u770b\\u3002\",\"\\u519b\\u7eff\\u8272\\u77ed\\u6b3e\\u9762\\u5305\\u670d\\u914d\\u5c0f\\u811a\\u88e4\\uff0c\\u8fd9\\u4e00\\u8eab\\u642d\\u914d\\u6211\\u633a\\u559c\\u6b22\\uff0c\\u7b80\\u5355\\u8010\\u770b\\u3002\\u51ac\\u5b63\\u7a7f\\u5728\\u8eab\\u4e0a\\u7684\\u8863\\u670d\\u6bd4\\u8f83\\u591a\\uff0c\\u4e0d\\u9700\\u8981\\u7e41\\u7410\\u7684\\u642d\\u914d\\u589e\\u52a0\\u7d2f\\u8d58\\uff0c\\u5c31\\u8fd9\\u6837\\u7b80\\u7b80\\u5355\\u5355\\u7684\\u642d\\u914d\\uff0c\\u518d\\u914d\\u4e00\\u4e2a\\u51fa\\u5f69\\u7684\\u5355\\u54c1\\u6765\\u70b9\\u775b\\u5c31\\u53ef\\u4ee5\\u4e86\\u3002\",\"\\u5728\\u51ac\\u5929\\u4f30\\u8ba1\\u8c01\\u90fd\\u4e0d\\u4f1a\\u62d2\\u7edd\\u6e29\\u6696\\u53ef\\u7231\\u7684\\u7f8a\\u7f94\\u7ed2\\u5916\\u5957\\u4e86\\uff0c\\u4e0a\\u8eab\\u6548\\u679c\\u7279\\u522b\\u68d2\\uff0c\\u65f6\\u9ae6\\u4fdd\\u6696\\u53c8\\u4e0d\\u81c3\\u80bf\\u3002\\u9e82\\u76ae\\u7684\\u9762\\u6599\\u548c\\u67d4\\u8f6f\\u7684\\u6bdb\\u9886\\u8bbe\\u8ba1\\uff0c\\u6e05\\u65b0\\u7684\\u7070\\u8272\\u8c03\\u53ef\\u7231\\u53c8\\u6709\\u578b\\uff0c\\u662f\\u4e00\\u4ef6\\u4e0d\\u53ef\\u591a\\u5f97\\u7684\\u51ac\\u5b63\\u5355\\u54c1\\u3002\",\"\\u53e4\\u529b\\u5a1c\\u624e\\u8eab\\u7a7fSMFK\\u9ed1\\u8272\\u76ae\\u8349\\u62fc\\u63a5\\u9576\\u8fb9\\u5b57\\u6bcd\\u5370\\u82b1\\u5939\\u514b\\uff0c\\u7c89\\u8272\\u9489\\u73e0\\u86c7\\u5934\\u5305\\u4ee4\\u6574\\u4e2aLook\\u589e\\u6dfb\\u5c11\\u5973\\u6c14\\u606f\\uff0c\\u84dd\\u8272\\u7684\\u6bdb\\u8fb9\\u62fc\\u63a5\\u9ad8\\u8170\\u4e5d\\u5206\\u4ed4\\u88e4\\u5c3d\\u663e\\u4f11\\u95f2\\u968f\\u6027\\u3002\",\"\\u8fd9\\u59d1\\u5a18\\u7684\\u8eab\\u6750\\u7b80\\u76f4\\u592a\\u5b8c\\u7f8e\\u4e86!\\u77ed\\u6b3e\\u6536\\u8170\\u5c0f\\u68c9\\u8863\\uff0c\\u5e3d\\u5b50\\u6234\\u5934\\u4e0a\\uff0c\\u7b80\\u76f4\\u5c31\\u662f\\u4e00\\u4e2a\\u9b3c\\u9a6c\\u5c0f\\u7cbe\\u7075\\u3002\\u9ed1\\u8272\\u7d27\\u8eab\\u5c0f\\u811a\\u88e4\\u914d\\u9a6c\\u4e01\\u9774\\uff0c\\u5c0f\\u9e1f\\u5927\\u957f\\u817f\\uff0c\\u770b\\u8d77\\u6765\\u7279\\u522b\\u7f8e\\u3002\"],\"sub_titles\":[\"\\u8857\\u62cd\\uff1a\\u8fd9\\u4e9b\\u6df1\\u51ac\\u642d\\u914d\\u53ef\\u4ee5\\u6253100\\u5206\\u4e86 \\u6700\\u540e\\u4e00\\u4e2a\\u59b9\\u5b50\\u5927\\u957f\\u817f\\u592a\\u52fe\\u4eba\",\"\\u8857\\u62cd\\uff1a\\u8fd9\\u4e9b\\u6df1\\u51ac\\u642d\\u914d\\u53ef\\u4ee5\\u6253100\\u5206\\u4e86 \\u6700\\u540e\\u4e00\\u4e2a\\u59b9\\u5b50\\u5927\\u957f\\u817f\\u592a\\u52fe\\u4eba\",\"\\u8857\\u62cd\\uff1a\\u8fd9\\u4e9b\\u6df1\\u51ac\\u642d\\u914d\\u53ef\\u4ee5\\u6253100\\u5206\\u4e86 \\u6700\\u540e\\u4e00\\u4e2a\\u59b9\\u5b50\\u5927\\u957f\\u817f\\u592a\\u52fe\\u4eba\",\"\\u8857\\u62cd\\uff1a\\u8fd9\\u4e9b\\u6df1\\u51ac\\u642d\\u914d\\u53ef\\u4ee5\\u6253100\\u5206\\u4e86 \\u6700\\u540e\\u4e00\\u4e2a\\u59b9\\u5b50\\u5927\\u957f\\u817f\\u592a\\u52fe\\u4eba\",\"\\u8857\\u62cd\\uff1a\\u8fd9\\u4e9b\\u6df1\\u51ac\\u642d\\u914d\\u53ef\\u4ee5\\u6253100\\u5206\\u4e86 \\u6700\\u540e\\u4e00\\u4e2a\\u59b9\\u5b50\\u5927\\u957f\\u817f\\u592a\\u52fe\\u4eba\",\"\\u8857\\u62cd\\uff1a\\u8fd9\\u4e9b\\u6df1\\u51ac\\u642d\\u914d\\u53ef\\u4ee5\\u6253100\\u5206\\u4e86 \\u6700\\u540e\\u4e00\\u4e2a\\u59b9\\u5b50\\u5927\\u957f\\u817f\\u592a\\u52fe\\u4eba\",\"\\u8857\\u62cd\\uff1a\\u8fd9\\u4e9b\\u6df1\\u51ac\\u642d\\u914d\\u53ef\\u4ee5\\u6253100\\u5206\\u4e86 \\u6700\\u540e\\u4e00\\u4e2a\\u59b9\\u5b50\\u5927\\u957f\\u817f\\u592a\\u52fe\\u4eba\"]}

"""
r = html.replace('\\', '')
print(r)
