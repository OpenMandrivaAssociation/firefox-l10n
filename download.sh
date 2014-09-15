langlist="af ar ak as ast be bg bn-IN bn-BD br bs ca cs cy da de el en-GB en-ZA eo es-AR es-CL es-ES es-MX et eu fa fi fr fy-NL ga-IE gd gl gu-IN he hi-IN hr hu hy-AM id is it ja kk ko km kn ku lg lt lv mai mk ml mr nb-NO nl nn-NO nso or pa-IN pl pt-BR pt-PT ro ru si sk sl sq sr sv-SE ta ta-LK te th tr uk vi zh-CN zh-TW zu"

fversion=32.0.1

for i in $langlist;do wget http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/$fversion/linux-i686/xpi/$i.xpi;done
