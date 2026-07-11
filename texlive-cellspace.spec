%global tl_name cellspace
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.9.1a
Release:	%{tl_revision}.1
Summary:	Ensure minimal spacing of table cells
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/cellspace
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cellspace.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cellspace.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
It is well known that high or deep cells tend to touch the \hlines of a
tabular. This package provides a modifier S acting on usual column types
so that to ensure a minimal distance that can be controlled through two
parameters \cellspacetoplimit and \cellspacebottomlimit. The approach
employed by this package is noticeably simpler than that of tabls, which
considers the dimensions of each entire row; whereas you can ask the
cellspace only to look at the cells of potentially difficult columns.
The package depends on ifthen, array, calc, and xkeyval.

