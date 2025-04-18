%global debug_package %{nil}
Name: oaknut
Version: 1.2.2
Release: 0
Summary: C++ implementation of a fast hash map and hash set using robin hood hashing
URL: https://github.com/azahar-emu/mcl
License: MIT
BuildRequires: cmake
BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: cmake(fmt)
BuildRequires: rpm_macro(cmake)
BuildRequires: rpm_macro(cmake_build)
BuildRequires: rpm_macro(cmake_install)
BuildRequires: cmake

Source: https://github.com/huakim/%{name}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

%package devel
Summary: %{summary}.

%description devel
%{summary}.

%description
%{summary}.


%prep
%autosetup

%build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_libdir} -DCMAKE_INSTALL_INCLUDEDIR=%{_includedir} -DBUILD_TESTING=OFF
%cmake_build

%install
%cmake_install
#mv -Tv %{buildroot}/%{_libdir}/lib%{name}.so{,.0}
#ln -sTfv lib%{name}.so.0 %{buildroot}/%{_libdir}/lib%{name}.so

#%files
#%_libdir/lib%{name}.so.0

%files devel
%_includedir/%{name}
%_libdir/cmake/%{name}
#%_libdir/lib%{name}.so
