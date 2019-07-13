#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : asv
Version  : 0.3.1
Release  : 11
URL      : https://github.com/airspeed-velocity/asv/archive/v0.3.1.tar.gz
Source0  : https://github.com/airspeed-velocity/asv/archive/v0.3.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: asv-bin = %{version}-%{release}
Requires: asv-license = %{version}-%{release}
Requires: asv-python = %{version}-%{release}
Requires: asv-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : six
BuildRequires : virtualenv

%description
This is the asv_test_repo project, version {version}.

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

%description python3
python3 components for the asv package.


%prep
%setup -q -n asv-0.3.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1540259898
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test || :
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/asv
cp LICENSE.rst %{buildroot}/usr/share/package-licenses/asv/LICENSE.rst
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
/usr/share/package-licenses/asv/LICENSE.rst

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
