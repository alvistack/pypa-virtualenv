# Copyright 2023 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: python-virtualenv
Epoch: 100
Version: 20.24.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Tool to create isolated Python environments
License: MIT
URL: https://github.com/pypa/virtualenv/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools >= 59.6

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
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500 || 0%{?centos_version} == 700
%package -n python%{python3_version_nodots}-virtualenv
Summary: Tool to create isolated Python environments
Requires: python3
Requires: python3-distlib >= 0.3.6
Requires: python3-filelock >= 3.12
Requires: python3-importlib-metadata >= 6.6
Requires: python3-platformdirs >= 3.5.1
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
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?centos_version} == 700)
%package -n python3-virtualenv
Summary: Tool to create isolated Python environments
Requires: python3
Requires: python3-distlib >= 0.3.6
Requires: python3-filelock >= 3.12
Requires: python3-importlib-metadata >= 6.6
Requires: python3-platformdirs >= 3.5.1
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
%{_bindir}/*
%{python3_sitelib}/*
%endif

%changelog
