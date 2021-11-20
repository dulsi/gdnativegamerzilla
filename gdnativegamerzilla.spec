Name:           gdnativegamerzilla
Version:        0.1
Release:        2%{?dist}
Summary:        Godot native interface to gamerzilla
License:        zlib
URL:            http://identicalsoftware.com/gamerzilla/

Source0:        %{url}/%{name}-%{version}.tgz
Source1: https://github.com/godotengine/godot-cpp/archive/refs/tags/godot-3.3.4-stable.tar.gz#/godot-cpp-godot-3.3.4-stable.tar.gz
Source2: https://github.com/godotengine/godot-headers/archive/refs/tags/godot-3.3.4-stable.tar.gz#/godot-headers-godot-3.3.4-stable.tar.gz
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: libgamerzilla-devel
BuildRequires: scons


%description
Godot native interface to award game achievements. The libgamerzilla is
used to communicate with the gamerzilla server.


%prep
%setup -q -T -c -a0
tar -x -v -f %{SOURCE1} --transform='s,^godot-cpp-godot-3.3.4-stable,godot-cpp,'
tar -x -v -f %{SOURCE2} --transform='s,^godot-headers-godot-3.3.4-stable,godot-cpp/godot-headers,'

%build
cd godot-cpp
scons platform=linux generate_bindings=yes -j4
cd ../%{name}-%{version}
mkdir bin
scons platform=linux

%install
mkdir -p %{buildroot}%{_libdir}
cp %{name}-%{version}/bin/x11/libgdgamerzilla.so %{buildroot}%{_libdir}/libgdgamerzilla.so

%files
%doc %{name}-%{version}/README
%license %{name}-%{version}/LICENSE
%{_libdir}/libgdgamerzilla.so


%changelog
* Sun Oct 03 2021 Dennis Payne <dulsi@identicalsoftware.com> - 0.1-2
- Simplify the setup and build

* Sun Oct 03 2021 Dennis Payne <dulsi@identicalsoftware.com> - 0.1-1
- Initial build
