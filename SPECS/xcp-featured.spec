Name:           xcp-featured
Version:        1.1.6
Release:        1%{?dist}
Summary:        XCP-ng feature daemon
Group:          System/Hypervisor
License:        ISC
URL:            https://github.com/xcp-ng/xcp-featured
Source0:        https://github.com/xcp-ng/xcp-featured/archive/v%{version}/xcp-featured-%{version}.tar.gz
Source1:        v6d.service
BuildRequires:  systemd-devel
BuildRequires:  xs-opam-repo
BuildRequires:  xapi-idl-devel
BuildRequires:  xapi-client-devel

%{?systemd_requires}

%description
This package contains an RPC serving daemon, which reports the features
available on an xcp-ng host.

%prep
%autosetup -p1

%build
DESTDIR=%{buildroot} %{__make}

%install
DESTDIR=%{buildroot} LIBEXECDIR=/opt/xensource/libexec %{__make} install
ln -s /opt/xensource/libexec/xcp-featured %{buildroot}/opt/xensource/libexec/v6d
%{__install} -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/v6d.service

%post
%systemd_post v6d.service

%preun
%systemd_preun v6d.service

%postun
%systemd_postun v6d.service

%files
/opt/xensource/libexec/v6d
/opt/xensource/libexec/xcp-featured
%{_unitdir}/v6d.service

%changelog
* Fri Sep 22 2023 Benjamin Reis <benjamin.reis@vates.fr> - 1.1.6-1
- Update to 1.1.6

* Fri Mar 03 2023 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.1.5-3
- Rebuild for xapi-23.3.0-1.1.xcpng8.3

* Wed Jan 18 2023 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.1.5-2
- Rebuild for updated XAPI

* Fri Jan 13 2023 Benjamin Reis <benjamin.reis@vates.fr> - 1.1.5-1
- Update to 1.1.5

* Tue Dec 20 2022 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.1.4-2
- Rebuild for updated XAPI

* Thu Oct 27 2022 Benjamin Reis <benjamin.reis@vates.fr> - 1.1.4-1
- Update to 1.1.4

* Fri Sep 16 2022 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.1.3-4
- Rebuild for XCP-ng 8.3 alpha
- Update Buildrequires: ocaml-xcp-idl-devel => xapi-idl-devel

* Tue Jan 11 2022 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.1.3-3
- Rebuild for XCP-ng 8.2.1

* Wed Sep 08 2021 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.1.3-2
- Rebuild to take new(ish) feature from XAPI into account (pool secret rotation)
- Static linking is evil!

* Mon Jul 06 2020 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.1.3-1
- Update to 1.1.3 which @benjamreis ported from jbuilder to dune 2

* Wed Jul 01 2020 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.1.1-4
- Rebuild for XCP-ng 8.2

* Thu May 09 2019 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.1.1-3
- Rebuild for XCP-ng 8.0

* Tue Jan 22 2019 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.1.1-2
- Rebuild for new XAPI with ZSTD support

* Fri Oct 12 2018 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.1.1-1
- New version 1.1.1 that does not report Corosync as available anymore,
  since it is a feature that relies on proprietary packages that we
  don't provide.

* Thu Sep 13 2018 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.1.0-3
- Rebuild for XCP-ng 7.6.0

* Tue Jul 24 2018 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.1.0-2
- Fix upgrade from previous version (no more removed symlink)
- Add systemd requires for scriptlets
- Fix paths

* Mon Jul 02 2018 John Else <john.else@gmail.com> - 1.1.0-1
- Update to build against new RPC library

* Wed Apr 25 2018 John Else <john.else@gmail.com> - 1.0.1-2
- Prevent symlink deletion on upgrade

* Mon Apr 09 2018 John Else <john.else@gmail.com> - 1.0.1-1
- Add additional feature flags

* Sun Mar 25 2018 John Else <john.else@gmail.com> - 1.0.0-1
- Initial package
