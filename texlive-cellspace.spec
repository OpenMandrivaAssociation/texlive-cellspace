Name:		texlive-cellspace
Version:	61501
Release:	2
Summary:	Ensure minimal spacing of table cells
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cellspace
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cellspace.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cellspace.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
It is well known that high or deep cells tend to touch the
\hlines of a tabular. This package provides a modifier S acting
on usual column types so that to ensure a minimal distance that
can be controlled through two parameters \cellspacetoplimit and
\cellspacebottomlimit. The approach employed by this package is
noticeably simpler than that of tabls, which considers the
dimensions of each entire row; whereas you can ask the
cellspace only to look at the cells of potentially difficult
columns.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/cellspace/cellspace.sty
%doc %{_texmfdistdir}/doc/latex/cellspace/README
%doc %{_texmfdistdir}/doc/latex/cellspace/cellspace.pdf
%doc %{_texmfdistdir}/doc/latex/cellspace/cellspace.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
