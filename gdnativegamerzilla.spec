Name:           gdnativegamerzilla
Version:        0.2
Release:        1%{?dist}
Summary:        Godot native interface to gamerzilla
License:        zlib
URL:            http://identicalsoftware.com/gamerzilla/

Source0:        %{url}/%{name}-%{version}.tgz
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: godot-cpp-devel
BuildRequires: libgamerzilla-devel
BuildRequires: scons


%description
Godot native interface to award game achievements. The libgamerzilla is
used to communicate with the gamerzilla server.


%prep
%setup -q

%build
mkdir bin
scons platform=linux target=release godot_headers_path=%{_includedir}/godot-cpp/godot-headers/  cpp_bindings_path=%{_includedir}/godot-cpp/ cpp_libs_path=%{_libdir}

%install
install -Dpm 0755 bin/x11/libgdgamerzilla.so %{buildroot}%{_libdir}/libgdgamerzilla.so

%files
%doc README
%license LICENSE
%{_libdir}/libgdgamerzilla.so


%changelog
* Sun Nov 21 2021 Dennis Payne <dulsi@identicalsoftware.com> - 0.2-1
- Move godot-cpp into a separate package.

* Sat Nov 20 2021 Dennis Payne <dulsi@identicalsoftware.com> - 0.1-2
- Simplify the setup and build

* Sun Oct 03 2021 Dennis Payne <dulsi@identicalsoftware.com> - 0.1-1
- Initial build
