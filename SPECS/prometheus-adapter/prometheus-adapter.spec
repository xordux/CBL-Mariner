Summary:        Kubernetes Custom, Resource, and External Metric APIs implemented to work with Prometheus.
Name:           prometheus-adapter
Version:        0.10.0
Release:        1%{?dist}
License:        Apache-2.0
Vendor:         Microsoft Corporation
Distribution:   Mariner
URL:            https://github.com/kubernetes-sigs/prometheus-adapter
Source0:        https://github.com/kubernetes-sigs/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Source1:        prometheus.service
# Source2:        prometheus.sysconfig
# Source3:        prometheus.yml
# Source4:        prometheus.conf
# Source5:        prometheus.logrotate
# Source6:        promu-%{promu_version}.tar.gz
# Debian patch for default settings
# Patch0:         02-Default_settings.patch
BuildRequires:  golang
BuildRequires:  prometheus
#BuildRequires:  nodejs
#BuildRequires:  systemd-rpm-macros
#Requires(pre):  %{_bindir}/systemd-sysusers

%description
Implementation of Prometheus via Kubernetes Custom, Resource, and External Metric API.

%prep
%autosetup -p1

%build
make prometheus-adapter

%install
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp adapter             %{buildroot}%{_bindir}/

%check
make test

%files
%license LICENSE NOTICE
%doc docs CONTRIBUTING.md OWNERS SECURITY.md SECURITY_CONTACTS VERSION code-of-conduct.md 
%doc README.md RELEASE.md
%{_bindir}/*

%changelog
* Wed Feb 15 2023 Osama Esmail <osamaesmail@microsoft.com> - 0.10.0-1
- Creating initial spec file.
- License verified.