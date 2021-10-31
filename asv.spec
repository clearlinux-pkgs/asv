#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : asv
Version  : 0.4.2
Release  : 32
URL      : https://github.com/airspeed-velocity/asv/archive/v0.4.2/asv-0.4.2.tar.gz
Source0  : https://github.com/airspeed-velocity/asv/archive/v0.4.2/asv-0.4.2.tar.gz
Summary  : Airspeed Velocity: A simple Python history benchmarking tool
Group    : Development/Tools
License  : BSD-3-Clause
Requires: asv-bin = %{version}-%{release}
Requires: asv-license = %{version}-%{release}
Requires: asv-python = %{version}-%{release}
Requires: asv-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pip
BuildRequires : pytest
BuildRequires : pytest-python
BuildRequires : virtualenv

%description
airspeed velocity
=================
**airspeed velocity** (``asv``) is a tool for benchmarking Python
packages over their lifetime.

%package bin
Summary: bin components for the asv package.
Group: Binaries
Requires: asv-license = %{version}-%{release}

%description bin
bin components for the asv package.


%package license
Summary: license components for the asv package.
Group: Default

%description license
license components for the asv package.


%package python
Summary: python components for the asv package.
Group: Default
Requires: asv-python3 = %{version}-%{release}

%description python
python components for the asv package.


%package python3
Summary: python3 components for the asv package.
Group: Default
Requires: python3-core
Provides: pypi(asv)
Requires: pypi(six)

%description python3
python3 components for the asv package.


%prep
%setup -q -n asv-0.4.2
cd %{_builddir}/asv-0.4.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635704596
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/asv
cp %{_builddir}/asv-0.4.2/LICENSE.rst %{buildroot}/usr/share/package-licenses/asv/8565420f58601d5de7f1124e5e20c2f6ab1a6a6b
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/asv

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/asv/8565420f58601d5de7f1124e5e20c2f6ab1a6a6b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
