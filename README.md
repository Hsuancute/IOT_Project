<h1 dir="auto"><span style="color:null">🔥早期火源智能偵測滅火風扇<br />
Intelligent Early Fire Terminator</span></h1>

<h2 dir="auto"><span style="color:null">💡 1. 關於專案</span></h2>

<ul dir="ltr">
	<li><span style="color:null">火災可以在極短的時間摧毀人事物，而每場火災皆從星星之火開始燃燒，盡早發現火源，即是避免擴大災害的關鍵。</span></li>
	<li><span style="color:null">風可以助長火勢亦能用來滅火，主要取決於風的大小和可燃物的溫度，當風無法使可燃物溫度降至著火點以下時，風便助火，例如：用扇子往木炭搧風生火；當風使可燃物降溫到著火點以下時，風便滅火，例如：用扇子將燭火搧熄。</span></li>
	<li><span style="color:null">本專案鏡頭會持續間隔幾秒照相，並且回傳照片給Rasberry Pi ，做影像辨識是否有火源，當偵測到火源時，LED即亮燈，並打開風扇滅火，滅完火後，偵測無火源，LED即會熄滅，並關閉風扇。</span></li>
</ul>

<h2 dir="auto"><span style="color:null">🎥 2. Demo影片連結</span></h2>

<ul>
	<li><span style="color:null">https://youtu.be/6x3yZjtfDS4</span></li>
</ul>

<h2 dir="auto"><span style="color:null">🛒 3. 所需材料</span></h2>

<p dir="auto"><span style="color:null"><input alt="" src="https://github.com/Hsuancute/IOT_Project/blob/ea4d3096191871d8650291a8689edc471c0e33a9/pic/Circuit%20Diagram.JPG" type="image" /><img alt="" src="https://github.com/Hsuancute/IOT_Project/blob/main/pic/Required%20Components.JPG?raw=true" /></span></p>

<ul>
	<li><span style="color:null">Raspberry Pi 4 Model B *1</span></li>
	<li><span style="color:null">SD Card 32GB *1</span></li>
	<li><span style="color:null">鏡頭 *1</span></li>
	<li><span style="color:null">杜邦線&nbsp;*N條</span></li>
	<li><span style="color:null">LED *1</span></li>
	<li><span style="color:null">電阻 *1</span></li>
	<li><span style="color:null">USB風扇 5V</span></li>
	<li><span style="color:null">泡棉膠　(最好用！黏力強，可搭配紙膠帶或無痕膠帶，輕鬆撕除不傷元件)</span></li>
	<li><span style="color:null">紙膠帶</span></li>
	<li><span style="color:null">剪刀</span></li>
	<li><span style="color:null">螺絲起子</span></li>
	<li><span style="color:null">紙板</span></li>
	<li><span style="color:null">蠟燭 *N根</span></li>
	<li><span style="color:null">水 (怕蠟燭被弄倒，滅火備用)</span></li>
</ul>

<h2 dir="auto"><span style="color:null">📸 4. 外觀</span></h2>

<ul dir="ltr">
	<li><span style="color:null">風扇背面<img alt="" src="https://github.com/Hsuancute/IOT_Project/blob/main/pic/detail%20(2).JPG?raw=true" /></span></li>
	<li><span style="color:null">風扇側面<img alt="" src="https://github.com/Hsuancute/IOT_Project/blob/main/pic/detail%20(1).JPG?raw=true" /></span></li>
	<li><span style="color:null">麵包版細節<img alt="" src="https://github.com/Hsuancute/IOT_Project/blob/main/pic/detail%20(3).JPG?raw=true" /></span></li>
	<li><span style="color:null">樹莓派細節<img alt="" src="https://github.com/Hsuancute/IOT_Project/blob/main/pic/detail%20(4).JPG?raw=true" /></span></li>
	<li><span style="color:null">鏡頭正面視角<img alt="" src="https://github.com/Hsuancute/IOT_Project/blob/main/pic/detail%20(5).JPG?raw=true" /></span></li>
	<li><span style="color:null">底部伺服馬達細節<img alt="" src="https://github.com/Hsuancute/IOT_Project/blob/main/pic/detail%20(6).JPG?raw=true" /></span></li>
</ul>

<h2 dir="auto"><span style="color:null">🔗 5. 實驗步驟</span></h2>

<ul dir="ltr">
	<li><span style="color:null">電路板連接方式</span></li>
</ul>

<p dir="auto" style="margin-left:40px"><span style="color:null"><img alt="" src="https://github.com/Hsuancute/IOT_Project/blob/main/pic/Circuit%20Diagram.JPG?raw=true" /></span></p>

<ul dir="ltr">
	<li>
	<h2><span style="color:null">程式碼主要引用&nbsp;</span><a href="https://chtseng.wordpress.com/2016/10/19/%E4%BD%BF%E7%94%A8%E8%88%B5%E6%A9%9F%E9%9B%B2%E5%8F%B0%E8%BF%BD%E8%B9%A4%E8%87%89%E5%AD%94/"><span style="color:null">使用舵機雲台追蹤臉孔/CH.Tseng</span></a><br />
	<span style="color:null">【Github】</span><a href="https://github.com/ch-tseng/PanTilt"><span style="color:null">ch-tseng/PanTilt</span></a></h2>
	</li>
	<li><span style="color:null">樹莓派GPIO參考：</span><a href="https://pinout.xyz/" rel="nofollow"><span style="color:null">https://pinout.xyz/</span></a></li>
	<li><span style="color:null">SG90 初步測試參考</span>
	<ul>
		<li><a href="http://RASPBERRY PI LESSON 28: CONTROLLING A SERVO ON RASPBERRY PI WITH PYTHON"><span style="color:null">RASPBERRY PI LESSON 28: CONTROLLING A SERVO ON RASPBERRY PI WITH PYTHON</span></a></li>
		<li><span style="color:null">【Youtube】</span><a href="https://www.youtube.com/watch?v=mv9G561xDFY&amp;ab_channel=%E8%89%BE%E9%8D%97"><span style="color:null">[Raspberry Pi ] PWM (SG90伺服馬達控制)/艾鍗</span></a></li>
		<li><a href="https://blog.everlearn.tw/%E7%95%B6-python-%E9%81%87%E4%B8%8A-raspberry-pi/raspberry-pi-3-mobel-3-%E5%88%A9%E7%94%A8-pwm-%E6%8E%A7%E5%88%B6%E4%BC%BA%E6%9C%8D%E9%A6%AC%E9%81%94"><span style="color:null">RASPBERRY PI 3 MOBEL B 利用 PWM 控制伺服馬達</span></a></li>
	</ul>
	</li>
</ul>

<div>
<ul>
	<li><span style="color:null">安裝函示庫</span><br />
	<span style="color:null">pip3 install imutils</span><br />
	<span style="color:null">pip3 install opencv-python </span></li>
</ul>
</div>

<ul dir="ltr">
	<li><a href="https://chtseng.wordpress.com/2016/10/19/%E4%BD%BF%E7%94%A8%E8%88%B5%E6%A9%9F%E9%9B%B2%E5%8F%B0%E8%BF%BD%E8%B9%A4%E8%87%89%E5%AD%94/"><span style="color:null">使用舵機雲台追蹤臉孔/CH.Tseng</span></a></li>
</ul>

<blockquote>
<p>一）匯入</p>

<p>from&nbsp;libCH.pantilt&nbsp;import&nbsp;PanTilt</p>

<p>二）建立物件，參數：PAN的pin腳12，TILT的pin腳11</p>

<p>motorPT&nbsp;=&nbsp;PanTilt(12,11)</p>

<p>三）啟動Pan/Tilt運作（開始傳入PWM，您會聽到servo轉動的聲音）</p>

<p>motorPT.start()</p>

<p>四）往右或左移動X距離（1相當於18度，例如要右移動90度，傳入參數X為5，往左移動90度則為-5）</p>

<p>motorPT.movePAN(X)</p>

<p>五）往上或下移動Y距離（（1相當於18度，例如要上移動10度，傳入參數Y為-0.56，往下移動10度則為0.56）</p>

<p>motorPT.moveTILT(Y)</p>

<p>六）往右或往左移動到xDegree的位置（xDegree的範圍為2.5~12.5，對應於0~180度，因此若傳入xDegree=7.5，會轉到中間90度的位置）</p>

<p>motorPT.movePAN(xDegree)</p>

<p>七）往上或往下移動到yDegree的位置（yDegree的範圍為2.5~12.5，對應於0~180度，因此若傳入yDegree=7.5，會轉到中間90度的位置）</p>

<p>motorPT.moveTILT(yDegree)</p>

<p>八）停止Pan/Tilt運作（停止傳入PWM，servo會停止轉動）</p>

<p>motorPT.stop()</p>
</blockquote>

<ul>
	<li>火的影像辨識資料集</li>
</ul>

<blockquote>
<p>【Github】<a href="https://github.com/gagan1411/Fire-Detection-using-HAAR-Cascade-Classifier-in-OpenCV">Fire-Detection-using-HAAR-Cascade-Classifier-in-OpenCV</a></p>
</blockquote>

<h2 dir="auto"><span style="color:null">⚠ 6. 可改進或其他發想</span></h2>

<ul dir="auto">
	<li dir="ltr"><span style="color:null">因鏡頭排線較短，限制了移動範圍，可更換排線或用其他鏡頭設備做靈活多角度的移動</span></li>
	<li dir="ltr">因僅使用泡棉膠固定風扇和鏡頭，較為不穩，不易靈活轉動，可使用專用的雲台</li>
	<li dir="ltr">散熱風扇多為12V，但以目前現有材料僅能使用5V的風扇</li>
	<li dir="ltr"><span style="color:null">可優化影像辨識速度</span></li>
	<li dir="ltr"><span style="color:null">可加裝輪子四處移動偵測環境，或是搭配掃地機器人</span></li>
	<li dir="ltr"><span style="color:null">偵測到火源即自動通報失火地點</span></li>
	<li dir="ltr"><span style="color:null">改用其他滅火方式，如滅火器、水霧加風扇</span></li>
</ul>

<h2 dir="auto"><span style="color:null">📚 7. 參考資料</span></h2>

<ul dir="auto">
	<li><a href="https://github.com/kaiokan/IOT_Project#iot_project-%E4%BA%BA%E9%AB%94%E7%9B%A3%E6%B8%AC%E7%B3%BB%E7%B5%B1"><span style="color:null">IOT_Project: 人體監測系統</span></a></li>
	<li><a href="https://www.hackster.io/mjrobot/real-time-face-recognition-an-end-to-end-project-a10826"><span style="color:null">Real-Time Face Recognition: An End-to-End Project</span></a><br />
	<span style="color:null">【Github】</span><a href="https://github.com/Mjrovai" rel="author"><span style="color:null">Mjrovai</span></a><span style="color:null">/</span><a href="https://github.com/Mjrovai/OpenCV-Face-Recognition"><span style="color:null">OpenCV-Face-Recognition</span></a></li>
	<li><a href="https://webb0219.pixnet.net/blog/post/337206877"><span style="color:null">[Raspberry Pi] 人臉追蹤相機 之 相機雲台/我的Maker之路</span></a></li>
	<li><a href="https://toptechboy.com/raspberry-pi-lesson-28-controlling-a-servo-on-raspberry-pi-with-python/"><span style="color:null">RASPBERRY PI LESSON 28: CONTROLLING A SERVO ON RASPBERRY PI WITH PYTHON</span></a></li>
	<li><a href="https://chtseng.wordpress.com/2016/10/19/%E4%BD%BF%E7%94%A8%E8%88%B5%E6%A9%9F%E9%9B%B2%E5%8F%B0%E8%BF%BD%E8%B9%A4%E8%87%89%E5%AD%94/"><span style="color:null">使用舵機雲台追蹤臉孔/CH.Tseng</span></a><br />
	<span style="color:null">【Github】</span><a href="https://github.com/ch-tseng/PanTilt"><span style="color:null">ch-tseng/PanTilt</span></a></li>
	<li><a href="https://towardsdatascience.com/early-fire-detection-system-using-deep-learning-and-opencv-6cb60260d54a"><span style="color:null">Early Fire detection system using deep learning and OpenCV</span></a></li>
	<li><span style="color:null">【Youtube】</span><a href="https://www.youtube.com/watch?v=mv9G561xDFY&amp;ab_channel=%E8%89%BE%E9%8D%97"><span style="color:null">[Raspberry Pi ] PWM (SG90伺服馬達控制)/艾鍗</span></a></li>
	<li><a href="https://blog.everlearn.tw/%E7%95%B6-python-%E9%81%87%E4%B8%8A-raspberry-pi/raspberry-pi-3-mobel-3-%E5%88%A9%E7%94%A8-pwm-%E6%8E%A7%E5%88%B6%E4%BC%BA%E6%9C%8D%E9%A6%AC%E9%81%94"><span style="color:null">RASPBERRY PI 3 MOBEL B 利用 PWM 控制伺服馬達</span></a></li>
	<li><a href="https://www.hackster.io/mjrobot/pan-tilt-multi-servo-control-b67791"><span style="color:null">Pan-Tilt Multi Servo Control</span></a></li>
	<li><a href="http://akizukidenshi.com/download/ds/towerpro/SG90.pdf"><span style="color:null">SG90 Micro Servo</span></a></li>
	<li><a href="https://stackoverflow.com/questions/15014310/why-is-there-no-xrange-function-in-python3"><span style="color:null">Why is there no xrange function in Python3?</span></a></li>
	<li><span style="color:null">【Github】</span><a href="https://github.com/gagan1411/Fire-Detection-using-HAAR-Cascade-Classifier-in-OpenCV"><span style="color:null">Fire-Detection-using-HAAR-Cascade-Classifier-in-OpenCV</span></a></li>
	<li><span style="color:null">【Github】</span><a href="https://github.com/opencv/opencv/tree/master"><span style="color:null">opencv</span></a><a href="https://github.com/opencv/opencv/tree/master/data/haarcascades"><span style="color:null">/data/<strong>haarcascades</strong>/</span></a></li>
	<li><a href="https://baijiahao.baidu.com/s?id=1645816207288345157&amp;wfr=spider&amp;for=pc"><span style="color:null">风是助火，还是灭火呢？它主要取决于两点！</span></a></li>
</ul>
