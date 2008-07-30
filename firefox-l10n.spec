%define _enable_debug_packages %{nil}
%define debug_package %{nil}

%define prel 0
%define oname firefox
%define name %{oname}-l10n
%define version 3.0.1
%define release %mkrel 2
%define mozillalibdir %{_libdir}/%{oname}-%{version}

%if %{prel}
%define xpidir http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}%{prel}/linux-i686/xpi/
%else
%define xpidir http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/
%endif

# Supported l10n language lists
%define langlist	ar af be ca cs da de el en_GB es_ES es_AR eu fi fr fy ga_IE gu_IN he hu id it ja ka ko ku lt mn mk nb_NO nn_NO nl pa_IN pl pt_PT pt_BR ro ru si sk sl sq sr sv_SE tr uk zh_CN zh_TW

# Disabled l10n languages, for any reason
%define disabled_langlist	uu br_FR et_EE bg

# Disabled myspell dicts, for any reason
%define disabled_dict_langlist	ar be br_FR es_AR eu fi fy gu_IN he id ja ka ko ku mk mn pa_IN tr zh_CN zh_TW

# Language descriptions
%define language_ar ar
%define langname_ar Arabic
%define language_af af
%define langname_af Afrikaans
%define language_be be
%define langname_be Belarusian
%define language_bg bg
%define langname_bg Bulgarian
%define language_br_FR br-FR
%define langname_br_FR Breton
%define language_ca ca
%define langname_ca Catalan
%define language_cs cs
%define langname_cs Czech
%define language_da da
%define langname_da Dansk
%define language_de de
%define langname_de German
%define language_el el
%define langname_el Greek
%define language_en_GB en-GB
%define langname_en_GB British English
%define language_es_AR es-AR
%define langname_es_AR Spanish (Argentina)
%define language_es_ES es-ES
%define langname_es_ES Spanish
%define language_et_EE et-EE
%define langname_et_EE Estonian
%define language_eu eu
%define langname_eu Basque
%define language_fi fi
%define langname_fi Finnish
%define language_fr fr
%define langname_fr French
%define language_fy fy-NL
%define langname_fy Frisian
%define language_ga_IE ga-IE
%define langname_ga_IE Irish
%define language_gu_IN gu-IN
%define langname_gu_IN Gujarati
%define language_he he
%define langname_he Hebrew
%define language_hu hu
%define langname_hu Hungarian
%define language_id id
%define langname_id Indonesian
%define language_it it
%define langname_it Italian
%define language_ja ja
%define langname_ja Japanese
%define language_ka ka
%define langname_ka Georgian
%define language_ko ko
%define langname_ko Korean
%define language_ku ku
%define langname_ku Kurdish
%define language_lt lt
%define langname_lt Lithuanian
%define language_mk mk
%define langname_mk Macedonian
%define language_mn mn
%define langname_mn Mongolian
%define language_nb_NO nb-NO
%define langname_nb_NO Norwegian Bokmaal
%define language_nn_NO nn-NO
%define langname_nn_NO Norwegian Nynorsk
%define language_nl nl
%define langname_nl Dutch
%define language_pa_IN pa-IN
%define langname_pa_IN Punjabi (gurmukhi)
%define language_pl pl
%define langname_pl Polish
%define language_pt_BR pt-BR
%define langname_pt_BR Brazilian portuguese
%define language_pt_PT pt-PT
%define langname_pt_PT Portuguese
%define language_ro ro
%define langname_ro Romanian
%define language_ru ru
%define langname_ru Russian
%define language_si si
%define langname_si Sinhala
%define language_sk sk
%define langname_sk Slovak
%define language_sl sl
%define langname_sl Slovenian
%define language_sq sq
%define langname_sq Shqipe
%define language_sr sr
%define langname_sr Serbian
%define language_sv_SE sv-SE
%define langname_sv_SE Swedish
%define language_tr tr
%define langname_tr Turkish
%define language_uk uk
%define langname_uk Ukrainian
%define language_uk_UA uk-UA
%define langname_uk_UA Ukrainian
%define language_zh_CN zh-CN
%define langname_zh_CN Simplified Chinese
%define language_zh_TW zh-TW
%define langname_zh_TW Traditional Chinese

# --- Danger line ---

# Defaults (all languages enabled by default)
# l10n
%{expand:%(for lang in %langlist; do echo "%%define with_$lang 1"; done)}
%{expand:%(for lang in %disabled_langlist; do echo "%%define with_$lang 0"; done)}
# dicts
%{expand:%(for lang in %langlist; do echo "%%define with_dict_$lang 0"; done)}
%{expand:%(for lang in %disabled_dict_langlist; do echo "%%define with_dict_$lang 0"; done)}

# Locales
%{expand:%(for lang in %langlist; do echo "%%define locale_$lang `echo $lang | cut -d _ -f 1` "; done)}

# Macro for easy adding i18n sources
# auto-increment as called.
%define src 1

%define l10nsrc() Source%src: %{xpidir}/%{1}.xpi\
%define src2 %(echo $((%src+1)))\
%define src %{src2}

Summary:	Localizations for Firefox (virtual package)
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Networking/WWW
Url:		http://www.mozilla.org/
# Language package template
Source0:	%{name}-template.spec
# l10n sources
%{expand:%(\
	for lang in %langlist; do\
		echo "%%{expand:%%l10nsrc %%{language_$lang}}";\
	done\
	)
}
Patch0:		fix-sq-invalid-rdf.patch
BuildRequires:	libxml2-utils
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Localizations for Firefox web browser.

# Expand all languages packages.
%{expand:%(\
	for lang in %langlist; do\
		echo "%%{expand:%%(sed "s!__LANG__!$lang!g" %{_sourcedir}/%{name}-template.spec 2> /dev/null)}";\
	done\
	)
}

%prep
%setup -q -c -T

# Convert rpm macros to bash variables
%{expand:%(for lang in %langlist; do echo "language_$lang=%%{language_$lang}"; done)}
%{expand:%(for lang in %langlist; do echo "locale_$lang=%%{locale_$lang}"; done)}
%{expand:%(for lang in %langlist; do echo "with_$lang=%%{with_$lang}"; done)}
%{expand:%(for lang in %langlist; do echo "dict_$lang=%%{with_dict_$lang}"; done)}

# Unpack all languages
for lang in %langlist; do
	with="with_$lang"
	with=${!with}
	[ $with -eq 0 ] && continue

	language="language_$lang"
	language=${!language}

	locale="locale_$lang"
	locale=${!locale}

	# l10n
	mkdir ${language}
	cd ${language}
	unzip %{_sourcedir}/${language}.xpi
	cd ..

	# dict
	dict="dict_$lang"
	dict=${!dict}
	[ $dict -eq 0 ] && continue

	mkdir -p ${language}-dict/dictionaries
	cd ${language}-dict
	if [ -e %{_datadir}/dict/ooo/$lang.aff ]; then
		ln -s %{_datadir}/dict/ooo/$lang.aff ./dictionaries/$language.aff
		ln -s %{_datadir}/dict/ooo/$lang.dic ./dictionaries/$language.dic
	elif [ -e %{_datadir}/dict/ooo/$locale.aff ]; then
		ln -s %{_datadir}/dict/ooo/$locale.aff ./dictionaries/$language.aff
		ln -s %{_datadir}/dict/ooo/$locale.dic ./dictionaries/$language.dic
	else
		ln -s %{_datadir}/dict/ooo/${locale}_*.aff ./dictionaries/$language.aff
		ln -s %{_datadir}/dict/ooo/${locale}_*.dic ./dictionaries/$language.dic
	fi
	cd ..
done

# Patches
cd ${language_fy}
sed -i 's/\x0D//g;/^$/d' install.rdf
cd ..

cd sq
%patch0 -p0
cd ..

%build
# All install.rdf files must validate
xmllint --noout */install.rdf

%install
rm -rf %{buildroot}

# Convert rpm macros to bash variables
%{expand:%(for lang in %langlist; do echo "language_$lang=%%{language_$lang}"; done)}
%{expand:%(for lang in %langlist; do echo "with_$lang=%%{with_$lang}"; done)}
%{expand:%(for lang in %langlist; do echo "dict_$lang=%%{with_dict_$lang}"; done)}

# Install all languages
for lang in %langlist; do
	with="with_$lang"
	with=${!with}
	[ $with -eq 0 ] && continue

	language="language_$lang"
	language=${!language}

	# l10n
	cd $language
	mkdir -p %buildroot%{mozillalibdir}/extensions/langpack-${language}@firefox.mozilla.org/
	cp -f -r * %buildroot%{mozillalibdir}/extensions/langpack-${language}@firefox.mozilla.org/
	cd ..

	# Dicts
	dict="dict_$lang"
	dict=${!dict}
	[ $dict -eq 0 ] && continue

	cp -af $language-dict/dictionaries/*.{aff,dic} \
		%buildroot%{mozillalibdir}/dictionaries/
done

%clean
rm -rf %buildroot
