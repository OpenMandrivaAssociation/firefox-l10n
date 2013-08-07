langlist="af ar as ast be bg bn_IN bn_BD br bs ca cs cy da de el en_GB en_ZA eo es_AR es_CL es_ES es_MX et eu fa fi fr fy ga_IE gd gl gu_IN he hi hr hu hy id is it ja kk ko km kn ku lg lt lv mai mk ml mr nb_NO nl nn_NO nso or pa_IN pl pt_BR pt_PT ro ru si sk sl sq sr sv_SE ta ta_LK te th tr uk vi zh_CN zh_TW zu"

fversion=23.0

for i in $langlist;do wget http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/$fversion/linux-i686/xpi/$i.xpi;done
