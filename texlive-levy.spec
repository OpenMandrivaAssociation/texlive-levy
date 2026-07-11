%global tl_name levy
%global tl_revision 76924

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Fonts for typesetting classical greek
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/greek/levy
License:	gpl2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/levy.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/levy.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
These fonts are derivatives of Knuth's CM fonts. Macros for use with
Plain TeX are included in the package; for use with LaTeX, see lgreek
(with English documentation) or levy (with German documentation).

