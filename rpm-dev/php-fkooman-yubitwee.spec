%global commit0 af5b10dd4834993bc92b296da348e6c763f9df6e

Name:           php-fkooman-yubitwee
Version:        1.1.4
Release:        1%{?dist}
Summary:        YubiKey OTP Validator library

License:        MIT
URL:            https://git.tuxed.net/fkooman/php-yubitwee
Source0:        https://git.tuxed.net/fkooman/php-yubitwee/snapshot/php-yubitwee-%{commit0}.tar.xz

BuildArch:      noarch

#        "php": ">=5.4",
BuildRequires:  php(language) >= 5.4.0
#        "ext-curl": "*",
#        "ext-date": "*",
#        "ext-hash": "*",
#        "ext-pcre": "*",
#        "ext-spl": "*",
BuildRequires:  php-curl
BuildRequires:  php-date
BuildRequires:  php-hash
BuildRequires:  php-pcre
BuildRequires:  php-spl
#        "paragonie/constant_time_encoding": "^1|^2",
#        "paragonie/random_compat": ">=1",
#        "symfony/polyfill-php56": "^1"
BuildRequires:  php-composer(paragonie/constant_time_encoding)
BuildRequires:  php-composer(paragonie/random_compat) >= 1
BuildRequires:  php-composer(symfony/polyfill-php56)
BuildRequires:  %{_bindir}/phpunit
BuildRequires:  %{_bindir}/phpab

#        "php": ">=5.4",
Requires:       php(language) >= 5.4.0
#        "ext-curl": "*",
#        "ext-date": "*",
#        "ext-hash": "*",
#        "ext-pcre": "*",
#        "ext-spl": "*",
Requires:       php-curl
Requires:       php-date
Requires:       php-hash
Requires:       php-pcre
Requires:       php-spl
#        "paragonie/constant_time_encoding": "^1|^2",
#        "paragonie/random_compat": ">=1",
#        "symfony/polyfill-php56": "^1"
Requires:       php-composer(paragonie/constant_time_encoding)
Requires:       php-composer(paragonie/random_compat) >= 1
Requires:       php-composer(symfony/polyfill-php56)

Provides:       php-composer(fkooman/yubitwee) = %{version}

%description
A very simple, secure YubiKey OTP Validator with pluggable HTTP client.

%prep
%autosetup -n php-yubitwee-%{commit0}

%build
%{_bindir}/phpab -o src/autoload.php src
cat <<'AUTOLOAD' | tee -a src/autoload.php
require_once '%{_datadir}/php/ParagonIE/ConstantTime/autoload.php';
require_once '%{_datadir}/php/random_compat/autoload.php';
require_once '%{_datadir}/php/Symfony/Polyfill/autoload.php';
AUTOLOAD

%install
mkdir -p %{buildroot}%{_datadir}/php/fkooman/YubiTwee
cp -pr src/* %{buildroot}%{_datadir}/php/fkooman/YubiTwee

%check
%{_bindir}/phpab -o tests/autoload.php tests
cat <<'AUTOLOAD' | tee -a tests/autoload.php
require_once 'src/autoload.php';
AUTOLOAD

%{_bindir}/phpunit tests --verbose --bootstrap=tests/autoload.php

%files
%license LICENSE
%doc composer.json CHANGES.md README.md
%dir %{_datadir}/php/fkooman
%{_datadir}/php/fkooman/YubiTwee

%changelog
* Fri Jun 08 2018 François Kooman <fkooman@tuxed.net> - 1.1.4-1
- update to 1.1.4

* Sat Jun 02 2018 François Kooman <fkooman@tuxed.net> - 1.1.3-1
- update to 1.1.3

* Fri Jun 01 2018 François Kooman <fkooman@tuxed.net> - 1.1.2-2
- update upstream URL to git.tuxed.net

* Thu Mar 22 2018 François Kooman <fkooman@tuxed.net> - 1.1.2-1
- update to 1.1.2

* Thu Dec 07 2017 François Kooman <fkooman@tuxed.net> - 1.1.1-2
- use phpab to generate the classloader

* Mon Oct 30 2017 François Kooman <fkooman@tuxed.net> - 1.1.1-1
- update to 1.1.1
- spec file cleanup

* Sat Oct 28 2017 François Kooman <fkooman@tuxed.net> - 1.1.0-2
- update spec file according to practices

* Tue Sep 12 2017 François Kooman <fkooman@tuxed.net> - 1.1.0-1
- update to 1.1.0

* Wed Aug 30 2017 François Kooman <fkooman@tuxed.net> - 1.0.1-2
- rework spec, to align it with practices document

* Thu Jun 01 2017 François Kooman <fkooman@tuxed.net> - 1.0.1-1
- update to 1.0.1
- license changed to MIT

* Tue Apr 11 2017 François Kooman <fkooman@tuxed.net> - 1.0.0-1
- initial package