langlist="ach af ak ar as ast be bg bn_BD bn_IN br bs ca cs csb cy da de el en_GB en_US en_ZA eo es_AR es_CL es_ES es_MX et eu fa ff fi fr fy ga_IE gd gl gu_IN he hi hr hu hy id is it ja kk km kn ko ku lg lij lt lv mai mk ml mr nb_NO nn_NO nl nso or pa_IN pl pt_PT pt_BR rm ro ru si sk sl son sq sr sv_SE ta ta_LK te th tr uk vi zh_CN zh_TW zu"
fversion=23.0

for i in $langlist;do wget http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/$fversion/linux-i686/xpi/$i.xpi;done
