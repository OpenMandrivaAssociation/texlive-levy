Name:		texlive-levy
Version:	21750
Release:	2
Summary:	Fonts for typesetting classical greek
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/greek/levy
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/levy.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/levy.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
These fonts are derivatives of Kunth's CM fonts. Macros for use
with Plain TeX are included in the package; for use with LaTeX,
see lgreek (with English documentation) or levy (with German
documentation).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/levy/a.mf
%{_texmfdistdir}/fonts/source/public/levy/b.mf
%{_texmfdistdir}/fonts/source/public/levy/d.mf
%{_texmfdistdir}/fonts/source/public/levy/digits.mf
%{_texmfdistdir}/fonts/source/public/levy/e.mf
%{_texmfdistdir}/fonts/source/public/levy/f.mf
%{_texmfdistdir}/fonts/source/public/levy/g.mf
%{_texmfdistdir}/fonts/source/public/levy/gen_acc.mf
%{_texmfdistdir}/fonts/source/public/levy/gen_sigma.mf
%{_texmfdistdir}/fonts/source/public/levy/graccent.mf
%{_texmfdistdir}/fonts/source/public/levy/grbase.mf
%{_texmfdistdir}/fonts/source/public/levy/grbld10.mf
%{_texmfdistdir}/fonts/source/public/levy/grbld8.mf
%{_texmfdistdir}/fonts/source/public/levy/grbld9.mf
%{_texmfdistdir}/fonts/source/public/levy/greek.mf
%{_texmfdistdir}/fonts/source/public/levy/grpunct.mf
%{_texmfdistdir}/fonts/source/public/levy/grreg10.mf
%{_texmfdistdir}/fonts/source/public/levy/grreg8.mf
%{_texmfdistdir}/fonts/source/public/levy/grreg9.mf
%{_texmfdistdir}/fonts/source/public/levy/grtt10.mf
%{_texmfdistdir}/fonts/source/public/levy/h.mf
%{_texmfdistdir}/fonts/source/public/levy/i.mf
%{_texmfdistdir}/fonts/source/public/levy/j.mf
%{_texmfdistdir}/fonts/source/public/levy/k.mf
%{_texmfdistdir}/fonts/source/public/levy/l.mf
%{_texmfdistdir}/fonts/source/public/levy/lig.mf
%{_texmfdistdir}/fonts/source/public/levy/lower.mf
%{_texmfdistdir}/fonts/source/public/levy/m.mf
%{_texmfdistdir}/fonts/source/public/levy/n.mf
%{_texmfdistdir}/fonts/source/public/levy/o.mf
%{_texmfdistdir}/fonts/source/public/levy/p.mf
%{_texmfdistdir}/fonts/source/public/levy/q.mf
%{_texmfdistdir}/fonts/source/public/levy/r.mf
%{_texmfdistdir}/fonts/source/public/levy/s.mf
%{_texmfdistdir}/fonts/source/public/levy/t.mf
%{_texmfdistdir}/fonts/source/public/levy/u.mf
%{_texmfdistdir}/fonts/source/public/levy/upper.mf
%{_texmfdistdir}/fonts/source/public/levy/w.mf
%{_texmfdistdir}/fonts/source/public/levy/x.mf
%{_texmfdistdir}/fonts/source/public/levy/y.mf
%{_texmfdistdir}/fonts/source/public/levy/z.mf
%{_texmfdistdir}/fonts/tfm/public/levy/grbld10.tfm
%{_texmfdistdir}/fonts/tfm/public/levy/grbld8.tfm
%{_texmfdistdir}/fonts/tfm/public/levy/grbld9.tfm
%{_texmfdistdir}/fonts/tfm/public/levy/grreg10.tfm
%{_texmfdistdir}/fonts/tfm/public/levy/grreg8.tfm
%{_texmfdistdir}/fonts/tfm/public/levy/grreg9.tfm
%{_texmfdistdir}/tex/generic/levy/greekmacros.tex
%{_texmfdistdir}/tex/generic/levy/slgreek.sty
%doc %{_texmfdistdir}/doc/fonts/levy/README
%doc %{_texmfdistdir}/doc/fonts/levy/digits.mf-old
%doc %{_texmfdistdir}/doc/fonts/levy/g.mf-old
%doc %{_texmfdistdir}/doc/fonts/levy/greekhist.tex
%doc %{_texmfdistdir}/doc/fonts/levy/greekuse.tex
%doc %{_texmfdistdir}/doc/fonts/levy/grinstall.tex
%doc %{_texmfdistdir}/doc/fonts/levy/grtestfont.tex
%doc %{_texmfdistdir}/doc/fonts/levy/makeall
%doc %{_texmfdistdir}/doc/fonts/levy/makefont
%doc %{_texmfdistdir}/doc/fonts/levy/testfont

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
