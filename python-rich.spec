%global debug_package %{nil}

Name: python-rich
Epoch: 100
Version: 12.3.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Python library for rich text and beautiful formatting in the terminal
License: MIT
URL: https://github.com/Textualize/rich/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-dataclasses >= 0.7
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
%fdupes -s %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-rich
Summary: Python library for rich text and beautiful formatting in the terminal
Requires: python3
Requires: python3-commonmark >= 0.9.0
Requires: python3-dataclasses >= 0.7
Requires: python3-Pygments >= 2.6.0
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
Requires: python3-commonmark >= 0.9.0
Requires: python3-dataclasses >= 0.7
Requires: python3-Pygments >= 2.6.0
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
Requires: python3-commonmark >= 0.9.0
Requires: python3-dataclasses >= 0.7
Requires: python3-pygments >= 2.6.0
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
