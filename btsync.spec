Summary:	BitTorrent Sync
Name:		btsync
Version:	1.3.67
Release:	0.2
# TODO: figure out what's the licensing and redistribution
License:	?
Group:		Applications
Source0:	http://download-lb.utorrent.com/endpoint/btsync/os/linux-i386/track/stable/%{name}_i386-%{version}.tar.gz
# NoSource0-md5:	b18f350098b74b3d98c3eca9f0afd80b
NoSource:	0
Source1:	http://download-lb.utorrent.com/endpoint/btsync/os/linux-x64/track/stable/%{name}_x64-%{version}.tar.gz
# NoSource1-md5:	88cfb037c0189c895c8df3b524e32dd9
NoSource:	1
URL:		http://www.bittorrent.com/sync/
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# Filter GLIBC_PRIVATE Requires
%define		_noautoreq	(GLIBC_PRIVATE)

%description
Secure, unlimited file-syncing. No cloud required.

- Sync never stores your files on servers, so they stay safe from data
  breaches and prying eyes.
- Create a Sync folder for your stuff. Open it on any computer, phone,
  or tablet. Access docs, share photos, and start working from anywhere.
- BitTorrent Sync skips the cloud to deliver your files at lightning
  speed. No matter where you are.
- Sync, send and share as much as you want. There are no file size
  limits, or caps on creativity. It’s as simple as that.

%prep
%ifarch %{ix86}
%setup -qcT -b 0
%endif
%ifarch %{x8664}
%setup -qcT -b 1
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -p btsync $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.TXT
%attr(755,root,root) %{_bindir}/btsync
