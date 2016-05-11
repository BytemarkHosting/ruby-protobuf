%if 0%{?rhel} < 7
%global ruby_vendorlibdir  %(ruby -rrbconfig -e 'puts Config::CONFIG["sitelibdir"]')
%endif

Name:           ruby-protobuf
Version:        0.4.11
Release:        1%{?dist}
Summary:        Protocol Buffers for Ruby

Group:          Development/Languages
License:        MIT
URL:            https://github.com/ruby-protobuf/protobuf
Source0:        %{name}_%{version}.orig.tar.gz

BuildArch:      noarch
BuildRequires:  ruby
BuildRequires:  ruby-devel
Requires:       ruby


%description
%{summary}.


%prep
%setup -q -c %{name}-%{version}


%build


%install
mkdir -p %{buildroot}%{_bindir}
cp -a bin/* %{buildroot}%{_bindir}/

mkdir -p %{buildroot}%{ruby_vendorlibdir}
cp -a lib/protobuf %{buildroot}%{ruby_vendorlibdir}/

%files
%{_bindir}/*
%{ruby_vendorlibdir}/protobuf


