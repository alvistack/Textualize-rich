# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
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

%global source_date_epoch_from_changelog 0

Name: python-rich
Epoch: 100
Version: 13.9.2
Release: 1%{?dist}
BuildArch: noarch
Summary: Python library for rich text and beautiful formatting in the terminal
License: MIT
URL: https://github.com/Textualize/rich/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Rich is a Python library for rich text and beautiful formatting in the
terminal. The Rich API makes it easy to add color and style to terminal
output. Rich can also render pretty tables, progress bars, markdown,
syntax highlighted source code, tracebacks, and more — out of the box.

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

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-rich
Summary: Python library for rich text and beautiful formatting in the terminal
Requires: python3
Requires: python3-markdown-it-py >= 2.2.0
Requires: python3-Pygments >= 2.13.0
Requires: python3-typing-extensions >= 4.0.0
Provides: python3-rich = %{epoch}:%{version}-%{release}
Provides: python3dist(rich) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-rich = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(rich) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-rich = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(rich) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-rich
Rich is a Python library for rich text and beautiful formatting in the
terminal. The Rich API makes it easy to add color and style to terminal
output. Rich can also render pretty tables, progress bars, markdown,
syntax highlighted source code, tracebacks, and more — out of the box.

%files -n python%{python3_version_nodots}-rich
%license LICENSE
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-rich
Summary: Python library for rich text and beautiful formatting in the terminal
Requires: python3
Requires: python3-markdown-it-py >= 2.2.0
Requires: python3-Pygments >= 2.13.0
Requires: python3-typing-extensions >= 4.0.0
Provides: python3-rich = %{epoch}:%{version}-%{release}
Provides: python3dist(rich) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-rich = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(rich) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-rich = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(rich) = %{epoch}:%{version}-%{release}

%description -n python3-rich
Rich is a Python library for rich text and beautiful formatting in the
terminal. The Rich API makes it easy to add color and style to terminal
output. Rich can also render pretty tables, progress bars, markdown,
syntax highlighted source code, tracebacks, and more — out of the box.

%files -n python3-rich
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-rich
Summary: Python library for rich text and beautiful formatting in the terminal
Requires: python3
Requires: python3-markdown-it-py >= 2.2.0
Requires: python3-pygments >= 2.13.0
Requires: python3-typing-extensions >= 4.0.0
Provides: python3-rich = %{epoch}:%{version}-%{release}
Provides: python3dist(rich) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-rich = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(rich) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-rich = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(rich) = %{epoch}:%{version}-%{release}

%description -n python3-rich
Rich is a Python library for rich text and beautiful formatting in the
terminal. The Rich API makes it easy to add color and style to terminal
output. Rich can also render pretty tables, progress bars, markdown,
syntax highlighted source code, tracebacks, and more — out of the box.

%files -n python3-rich
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
