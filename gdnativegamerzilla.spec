Name:           gdnativegamerzilla
Version:        0.1
Release:        1%{?dist}
Summary:        Godot native interface to gamerzilla
License:        zlib
URL:            http://identicalsoftware.com/gamerzilla/

Source0:        %{url}/%{name}-%{version}.tgz
# https://github.com/godotengine/godot-cpp/archive/refs/tags/godot-3.3.4-stable.tar.gz
Source1:        godot-cpp-godot-3.3.4-stable.tar.gz
# https://github.com/godotengine/godot-headers/archive/refs/tags/godot-3.3.4-stable.tar.gz
Source2:        godot-headers-godot-3.3.4-stable.tar.gz
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: libgamerzilla-devel
BuildRequires: scons


%description
Godot native interface to award game achievements. The libgamerzilla is
used to communicate with the gamerzilla server.


%prep
%setup -q
cd ..
rm -rf godot-cpp
rm -rf godot-cpp-godot-3.3.4-stable
%setup -T -D -b 1
cd ..
rm -rf godot-headers-godot-3.3.4-stable
%setup -T -D -b 2

%build
cd ..
mv godot-cpp-godot-3.3.4-stable godot-cpp
rmdir godot-cpp/godot-headers
mv godot-headers-godot-3.3.4-stable godot-cpp/godot-headers
cd godot-cpp
scons platform=linux generate_bindings=yes -j4
cd ../%{name}-%{version}
mkdir bin
scons platform=linux

%install
mkdir -p $RPM_BUILD_ROOT/%{_libdir}
cp bin/x11/libgdgamerzilla.so %{buildroot}%{_libdir}/libgdgamerzilla.so

%files
%doc README
%license LICENSE
%{_libdir}/libgdgamerzilla.so


%changelog
* Sun Oct 03 2021 Dennis Payne <dulsi@identicalsoftware.com> - 0.1-1
- Initial build
