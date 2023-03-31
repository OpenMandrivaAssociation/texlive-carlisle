Name:		texlive-carlisle
Version:	59577
Release:	2
Summary:	David Carlisle's small packages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/carlisle
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/carlisle.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/carlisle.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/carlisle.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/carlisle
%doc %{_texmfdistdir}/doc/latex/carlisle
#- source
%doc %{_texmfdistdir}/source/latex/carlisle

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
