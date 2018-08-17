%global sum()   A simple %* wrapper around inotify
%global desc \
inotify_simple is a simple Python wrapper around inotify. No fancy bells and \
whistles, just a literal wrapper with ctypes. Only 122 lines of code!

%if 0%{?fedora}
  %bcond_without python2
  %bcond_without python3
%else
  %if 0%{?rhel} > 7
    %bcond_with    python2
    %bcond_without python3
  %else
    %bcond_without python2
    %bcond_with    python3
  %endif
%endif

%global sname inotify_simple

Name:           python-%sname
Version:        1.1.8
Release:        1%{?dist}
Summary:        %{sum Python}
BuildArch:      noarch

License:        BSD
URL:            https://github.com/chrisjbillington/%sname
Source0:        https://pypi.org/packages/source/i/%sname/%sname-%version.tar.gz

%if %{with python2}
BuildRequires: python2-devel
%endif
%if %{with python3}
BuildRequires: python3-devel
%endif


%description
%desc


%if %{with python2}
%package -n     python2-%sname
Summary:        %{sum Python 2}
Requires:       python2-enum34

%description -n python2-%sname
%{desc}
%endif


%if %{with python3}
%package -n     python3-%sname
Summary:        %{sum Python 3}

%description -n python3-%sname
%{desc}
%endif


%prep
%autosetup -n %sname-%version -p1


%build
%{?with_python2:%py2_build}
%{?with_python3:%py3_build}


%install
%{?with_python2:%py2_install}
%{?with_python3:%py3_install}


%if %{with python2}
%files -n python2-%sname
%license LICENSE
%python2_sitelib/%sname
%python2_sitelib/%sname-%{version}*.egg-info
%endif


%if %{with python3}
%files -n python3-%sname
%license LICENSE
%python3_sitelib/%sname
%python3_sitelib/%sname-%{version}*.egg-info
%endif


%changelog
* Fri Aug 17 2018 Pavel Raiskup <praiskup@redhat.com> - 1.1.8-1
- initial RPM packaging
