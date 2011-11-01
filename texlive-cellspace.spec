Name:		texlive-cellspace
Version:	1.6
Release:	1
Summary:	Ensure minimal spacing of table cells
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cellspace
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cellspace.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cellspace.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

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

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/cellspace/cellspace.sty
%doc %{_texmfdistdir}/doc/latex/cellspace/README
%doc %{_texmfdistdir}/doc/latex/cellspace/cellspace.pdf
%doc %{_texmfdistdir}/doc/latex/cellspace/cellspace.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
