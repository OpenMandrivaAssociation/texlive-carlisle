# revision 18258
# category Package
# catalog-ctan /macros/latex/contrib/carlisle
# catalog-date 2010-02-18 13:36:42 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-carlisle
Version:	20100218
Release:	9
Summary:	David Carlisle's small packages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/carlisle
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/carlisle.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/carlisle.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/carlisle.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

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

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20100218-2
+ Revision: 749975
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20100218-1
+ Revision: 718007
- texlive-carlisle
- texlive-carlisle
- texlive-carlisle
- texlive-carlisle
- texlive-carlisle

