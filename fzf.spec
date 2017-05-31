%global debug_package %{nil}

Name:           fzf
Version:        0.16.7
Release:        1%{?dist}
Summary:        A command-line fuzzy finder written in Go

License:        MIT
URL:            https://github.com/junegunn/fzf/
Source0:        https://github.com/junegunn/fzf/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  golang
BuildRequires:  git
Requires:       tmux

%description
fzf is a general-purpose command-line fuzzy finder.

%prep
%setup -q

%build
pushd src
  make
popd

%install
mkdir -p %{buildroot}/%{_bindir}
cp src/fzf/fzf* %{buildroot}/%{_bindir}/fzf
cp bin/fzf-tmux %{buildroot}/%{_bindir}/fzf-tmux

mkdir -p %{buildroot}/%{_datadir}/%{name}
cp -r shell %{buildroot}/%{_datadir}/%{name}/shell

%files
%{_bindir}/*
%{_datadir}/*

%changelog
* Tue May 30 2017 Viet Nguyen <vietjtnguyen@gmail.com> - 1:0.16.7-1
- Initial packaging
