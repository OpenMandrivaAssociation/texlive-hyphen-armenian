%global tl_name hyphen-armenian
%global tl_revision 78069

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Armenian hyphenation patterns.
Group:		Publishing
URL:		https://www.ctan.org/pkg/hyphen-armenian
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-armenian.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-armenian.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Hyphenation patterns for Armenian for Unicode engines. Auto-generated
from a script included in hyph-utf8.


%install -a
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-armenian:
armenian loadhyph-hy.tex
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-armenian:
\addlanguage{armenian}{loadhyph-hy.tex}{}{1}{2}
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/%{tl_name} <<'TL_HYPHEN_EOF'
-- from hyphen-armenian:
['armenian'] = {
	loader = 'loadhyph-hy.tex',
	lefthyphenmin = 1,
	righthyphenmin = 2,
	synonyms = {  },
	patterns = 'hyph-hy.pat.txt',
},
TL_HYPHEN_EOF
