#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-dotenv
Version  : 0.15.0
Release  : 4
URL      : https://files.pythonhosted.org/packages/53/04/1a8126516c8febfeb2015844edee977c9b783bdff9b3bcd89b1cc2e1f372/python-dotenv-0.15.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/53/04/1a8126516c8febfeb2015844edee977c9b783bdff9b3bcd89b1cc2e1f372/python-dotenv-0.15.0.tar.gz
Summary  : Add .env support to your django/flask apps in development and deployments
Group    : Development/Tools
License  : BSD-3-Clause
Requires: python-dotenv-bin = %{version}-%{release}
Requires: python-dotenv-license = %{version}-%{release}
Requires: python-dotenv-python = %{version}-%{release}
Requires: python-dotenv-python3 = %{version}-%{release}
Requires: click
Requires: flake8
Requires: ipython
Requires: python-mock
Requires: tox
Requires: twine
Requires: wheel
BuildRequires : buildreq-distutils3
BuildRequires : click
BuildRequires : flake8
BuildRequires : ipython
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-mock
BuildRequires : tox
BuildRequires : twine
BuildRequires : virtualenv
BuildRequires : wheel

%description
_______ .__   __. ____    ____
               |   ____||  \ |  | \   \  /   /
               |  |__   |   \|  |  \   \/   /
               |   __|  |  . `  |   \      /
            __ |  |____ |  |\   |    \    /
           (__)|_______||__| \__|     \__/
        ```

%package bin
Summary: bin components for the python-dotenv package.
Group: Binaries
Requires: python-dotenv-license = %{version}-%{release}

%description bin
bin components for the python-dotenv package.


%package license
Summary: license components for the python-dotenv package.
Group: Default

%description license
license components for the python-dotenv package.


%package python
Summary: python components for the python-dotenv package.
Group: Default
Requires: python-dotenv-python3 = %{version}-%{release}

%description python
python components for the python-dotenv package.


%package python3
Summary: python3 components for the python-dotenv package.
Group: Default
Requires: python3-core
Provides: pypi(python_dotenv)

%description python3
python3 components for the python-dotenv package.


%prep
%setup -q -n python-dotenv-0.15.0
cd %{_builddir}/python-dotenv-0.15.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1605751585
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-dotenv
cp %{_builddir}/python-dotenv-0.15.0/LICENSE %{buildroot}/usr/share/package-licenses/python-dotenv/36fe354f4526001c781c4c99847c059ebc00878c
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/dotenv

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-dotenv/36fe354f4526001c781c4c99847c059ebc00878c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
