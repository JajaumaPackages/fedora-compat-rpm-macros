%global __rpmmacrodir %{_rpmconfigdir}/macros.d

Name:           fedora-compat-rpm-macros
Version:        1.0.0
Release:        1%{?dist}
Summary:        RPM macros for compatibility with Fedora

License:        MIT
Source0:        macros.fedora-compat

BuildArch: noarch


%description
This package provides some RPM macros for compatibility with Fedora.


%prep


%build


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{__rpmmacrodir}
install -m 644 %{SOURCE0} %{buildroot}/%{__rpmmacrodir}


%files
%{__rpmmacrodir}/macros.fedora-compat


%changelog
* Thu Sep 07 2017 Jajauma's Packages <jajauma@yandex.ru> - 1.0.0-1
- Initial release
