Name:		encfs
Version:	1.9
Release:	0
Summary:	Encrypted pass-thru filesystem in userspace
License:	GPLv3+
Group:		System Environment/Kernel

Url:		https://vgough.github.io/encfs/
Source0:	https://github.com/vgough/encfs/tarball/master
Source1:	https://github.com/vgough/encfs/zipball/master

BuildRoot:	%{_tmppath}/%{name}-%{version}%{release}

Requires:	fuse >= 2.6
Requires:	openssl openssl-libs
Requires:	gettext
Requires:	intltool

Provides:	encfs = %{version}.%{release}

BuildRequires:	fuse-devel >= 2.6
BuildRequires:	openssl-devel
BuildRequires:	gettext
BuildRequires:	intltool


%description
EncFS provides an encrypted filesystem in user-space. It runs in userspace,
using the FUSE library for the filesystem interface. EncFS is open source
software, licensed under the LGPL.

EncFS is now over 10 years old (first release in 2003).  It was written because
older NFS and kernel-based encrypted filesystems such as CFS had not kept pace with Linux
development.  When FUSE became available, I wrote a CFS replacement for my own
use and released the first version to Open Source in 2003.

EncFS encrypts individual files, by translating all requests for the virtual
EncFS filesystem into the equivalent encrypted operations on the raw
filesystem.

%prep

%build

##some debug info
echo ===== build ============
##echo %{_bindir}
##echo %{_includedir}
##echo %{_mandir}
##echo %{_libdir}
##echo ========================

%install
echo ===== install ==========
mkdir %{buildroot}%{_usr}
tar -xf ./INSTALL/%{name}-%{version}.%{release}.tar -C %{buildroot}%{_usr}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/encfs
%{_bindir}/encfsctl
%{_bindir}/encfssh

## library not needed
##%{_includedir}/tinyxml2.h
##%{_libdir}/libencfs.a
##%{_libdir}/libtinyxml2.a
##%{_libdir}/pkgconfig/tinyxml2.pc

%doc
%defattr(-,root,root,-)
%{_mandir}/man1/encfs.1.gz
%{_mandir}/man1/encfsctl.1.gz
