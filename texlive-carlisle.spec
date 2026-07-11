%global tl_name carlisle
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	David Carlisles small packages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/carlisle
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/carlisle.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/carlisle.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/carlisle.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Many of David Carlisle's more substantial packages stand on their own,
or as part of the LaTeX latex-tools set; this set contains: Making
dotless 'j' characters for fonts that don't have them; A method for
combining the capabilities of longtable and tabularx; An environment for
including Plain TeX in LaTeX documents; A jiffy to remove counters from
other counters' reset lists (now obsolete as it has been incorporated
into the LaTeX format); A jiffy to create 'slashed' characters for
physicists.

