%global debug_package %{nil}

Name: python-virtualenv
Epoch: 100
Version: 20.11.2
Release: 1%{?dist}
BuildArch: noarch
Summary: Tool to create isolated Python environments
License: MIT
URL: https://github.com/pypa/virtualenv/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
virtualenv is a tool to create isolated Python environments. virtualenv
is a successor to workingenv, and an extension of virtual-python. It is
written by Ian Bicking, and sponsored by the Open Planning Project.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
%fdupes -s %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500 || 0%{?centos_version} == 700
%package -n python%{python3_version_nodots}-virtualenv
Summary: Tool to create isolated Python environments
Requires: python3
Requires: python3-distlib >= 0.3.1
Requires: python3-filelock >= 3.2
Requires: python3-importlib-metadata >= 0.12
Requires: python3-importlib-resources >= 1.0
Requires: python3-platformdirs >= 2
Requires: python3-six >= 1.9.0
Provides: python3-virtualenv = %{epoch}:%{version}-%{release}
Provides: python3dist(virtualenv) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-virtualenv = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(virtualenv) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-virtualenv = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(virtualenv) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-virtualenv
virtualenv is a tool to create isolated Python environments. virtualenv
is a successor to workingenv, and an extension of virtual-python. It is
written by Ian Bicking, and sponsored by the Open Planning Project.

%files -n python%{python3_version_nodots}-virtualenv
%license LICENSE
%{_bindir}/virtualenv
%{python3_sitelib}/virtualenv*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?centos_version} == 700)
%package -n python3-virtualenv
Summary: Tool to create isolated Python environments
Requires: python3
Requires: python3-distlib >= 0.3.1
Requires: python3-filelock >= 3.2
Requires: python3-importlib-metadata >= 0.12
Requires: python3-importlib-resources >= 1.0
Requires: python3-platformdirs >= 2
Requires: python3-six >= 1.9.0
Provides: python3-virtualenv = %{epoch}:%{version}-%{release}
Provides: python3dist(virtualenv) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-virtualenv = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(virtualenv) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-virtualenv = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(virtualenv) = %{epoch}:%{version}-%{release}

%description -n python3-virtualenv
virtualenv is a tool to create isolated Python environments. virtualenv
is a successor to workingenv, and an extension of virtual-python. It is
written by Ian Bicking, and sponsored by the Open Planning Project.

%files -n python3-virtualenv
%license LICENSE
%{_bindir}/virtualenv
%{python3_sitelib}/virtualenv*
%endif

%changelog
