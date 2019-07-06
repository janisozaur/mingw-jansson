%{?mingw_package_header}

%global pkgname jansson

Name:           mingw-%{pkgname}
Version:        2.12
Release:        1%{?dist}
Summary:        C library for encoding, decoding and manipulating JSON data
Group:          Development/Libraries
License:        MIT 
URL:            http://www.digip.org/jansson/
Source0:        https://github.com/akheron/jansson/archive/v%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  cmake

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-dlfcn

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-dlfcn


%description
Small library for parsing and writing JSON documents.

%package -n mingw32-%{pkgname}
Summary:        C library for encoding, decoding and manipulating JSON data

%description -n mingw32-%{pkgname}
Small library for parsing and writing JSON documents.

%package -n mingw64-%{pkgname}
Summary:        C library for encoding, decoding and manipulating JSON data

%description -n mingw64-%{pkgname}
Small library for parsing and writing JSON documents.

%{?mingw_debug_package}


%prep
ls -l
%autosetup -p1 -n %{pkgname}-%{version}


%build
%mingw_cmake -DJANSSON_BUILD_SHARED_LIBS=ON -DJANSSON_EXAMPLES=OFF -DJANSSON_WITHOUT_TESTS=ON -DJANSSON_BUILD_DOCS=OFF -DCMAKE_BUILD_TYPE=RelWithDebInfo
%mingw_make %{?_smp_mflags}


%install
%mingw_make install DESTDIR=%{buildroot}


%files -n mingw32-%{pkgname}
%license LICENSE
%{mingw32_bindir}/libjansson.dll
%{mingw32_libdir}/libjansson.dll.a
%{mingw32_libdir}/pkgconfig/jansson.pc
%{mingw32_includedir}/jansson.h
%{mingw32_includedir}/jansson_config.h
%{mingw32_prefix}/cmake/janssonConfig.cmake
%{mingw32_prefix}/cmake/janssonConfigVersion.cmake
%{mingw32_prefix}/cmake/janssonTargets-relwithdebinfo.cmake
%{mingw32_prefix}/cmake/janssonTargets.cmake

%files -n mingw64-%{pkgname}
%license LICENSE
%{mingw64_bindir}/libjansson.dll
%{mingw64_libdir}/libjansson.dll.a
%{mingw64_libdir}/pkgconfig/jansson.pc
%{mingw64_includedir}/jansson.h
%{mingw64_includedir}/jansson_config.h
%{mingw64_prefix}/cmake/janssonConfig.cmake
%{mingw64_prefix}/cmake/janssonConfigVersion.cmake
%{mingw64_prefix}/cmake/janssonTargets-relwithdebinfo.cmake
%{mingw64_prefix}/cmake/janssonTargets.cmake

# See https://fedoraproject.org/wiki/Packaging:MinGW

%changelog
* Wed Jul 03 2019 Michał Janiszewski <janisozaur+janssonfedoramingw@gmail.com> - 2.12-1
- Initial MinGW packaging
