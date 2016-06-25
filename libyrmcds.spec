Name:          libyrmcds
Version:       1.3.0
Release:       1%{?dist}
Summary:       A memcached client library for C/C++. Best suited to yrmcds.
Group:         Development/Libraries
License:       BSD-2-Clause
URL:           http://cybozu.github.io/libyrmcds/
Source0:       https://github.com/cybozu/%{name}/archive/v%{version}.tar.gz
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-tmp
BuildRequires: gcc-c++
BuildRequires: make

%description
libyrmcds is a memcached client library written in C.
This is a companion to yrmcds, a memcached compatible KVS.
In addition to the library itself, a client program called yc is included.

%package devel
Summary: Development library for libyrmcds
Requires: %{name} = %{version}-%{release}
Provides: yrmcds-devel = %{version}-%{release}

%description devel
libyrmcds is a memcached client library written in C.
This is a companion to yrmcds, a memcached compatible KVS.
In addition to the library itself, a client program called yc is included

%prep
%setup -q -n %{name}-%{version}

%build
make PREFIX=%{_prefix} 

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_includedir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_libdir}/%{name}


install -d %{buildroot}%{_bindir}
install -m0755 yc %{buildroot}%{_bindir}/
install -m0755 yc-cnt %{buildroot}%{_bindir}/

install -m0644 *.h %{buildroot}%{_includedir}/%{name}/
install -m0644 *.o %{buildroot}%{_libdir}/%{name}/
install -m0644 *.c %{buildroot}%{_libdir}/%{name}/
install -m0644 *.a %{buildroot}%{_libdir}/%{name}/

%clean
rm -rf $RPM_BUILD_ROOT


%files
%{_bindir}/yc
%{_bindir}/yc-cnt
%doc COPYING README* USAGE*

%files devel
%{_includedir}/%{name}
%{_libdir}/%{name}


%changelog
* Sat Jun 25 2016 Kazuhisa Hara <kazuhisya@gmail.com> - 1.3.0-1
- init
