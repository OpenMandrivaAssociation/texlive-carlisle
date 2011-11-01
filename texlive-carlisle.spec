Name:		texlive-carlisle
Version:	20100218
Release:	1
Summary:	David Carlisle's small packages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/carlisle
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/carlisle.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/carlisle.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/carlisle.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Many of David Carlisle's more substantial packages stand on
their own, or as part of the LaTeX tools set; this set
contains: - Making dotless 'j' characters for fonts that don't
have them; - Fix marks in 2-column output; - A method for
combining the capabilities of longtable and tabularx; - A
proforma for building personalised LaTeX formats; - A jiffy to
suppress page numbers; - An environment for including Plain TeX
in LaTeX documents; - A jiffy to remove counters from other
counters' reset lists; - A package to rescale fonts to
arbitrary sizes; - A jiffy to create 'slashed' for physicists;
and - An environment for including HTML in LaTeX documents.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/carlisle/dotlessj.sty
%{_texmfdistdir}/tex/latex/carlisle/ltxtable.sty
%{_texmfdistdir}/tex/latex/carlisle/mylatex.ltx
%{_texmfdistdir}/tex/latex/carlisle/plain.sty
%{_texmfdistdir}/tex/latex/carlisle/remreset.sty
%{_texmfdistdir}/tex/latex/carlisle/scalefnt.sty
%{_texmfdistdir}/tex/latex/carlisle/slashed.sty
%doc %{_texmfdistdir}/doc/latex/carlisle/README
%doc %{_texmfdistdir}/doc/latex/carlisle/ltx1.tex
%doc %{_texmfdistdir}/doc/latex/carlisle/ltxtable.pdf
#- source
%doc %{_texmfdistdir}/source/latex/carlisle/ltxtable.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
