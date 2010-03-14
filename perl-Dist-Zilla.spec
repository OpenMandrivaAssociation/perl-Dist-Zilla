%define upstream_name    Dist-Zilla
%define upstream_version 1.100711

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Something that provides a version number for the dist
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://search.cpan.org/CPAN/authors/id/R/RJ/RJBS/%{upstream_name}-%{upstream_version}.tar.gz

Buildrequires: perl(App::Cmd)
Buildrequires: perl(Archive::Tar)
Buildrequires: perl(CPAN::Uploader)
Buildrequires: perl(Config::INI::MVP::Reader)
Buildrequires: perl(Data::Section)
Buildrequires: perl(DateTime)
Buildrequires: perl-ExtUtils-Manifest
Buildrequires: perl(File::Copy::Recursive)
Buildrequires: perl(File::Find::Rule)
Buildrequires: perl(File::HomeDir)
Buildrequires: perl(File::ShareDir::Install)
Buildrequires: perl(File::chdir)
Buildrequires: perl(Hash::Merge::Simple)
Buildrequires: perl(List::MoreUtils)
Buildrequires: perl(Log::Dispatchouli)
Buildrequires: perl(Mixin::ExtraFields::Param)
Buildrequires: perl(Moose)
Buildrequires: perl(Moose::Autobox)
Buildrequires: perl(MooseX::Singleton)
Buildrequires: perl(MooseX::Types::Path::Class)
Buildrequires: perl(PPI)
Buildrequires: perl(Path::Class)
Buildrequires: perl(Perl::Version)
Buildrequires: perl(Pod::Eventual)
Buildrequires: perl(Software::License)
Buildrequires: perl(String::Flogger)
Buildrequires: perl(String::Format)
Buildrequires: perl(String::Formatter)
Buildrequires: perl(String::RewritePrefix)
Buildrequires: perl(Text::Template)
Buildrequires: perl(Version::Requirements)
Buildrequires: perl(YAML::Tiny)
Buildrequires: perl(autobox)
Buildrequires: perl(namespace::autoclean)
Buildrequires: perl(version) >= 1:0.790.0

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

Requires: perl(Archive::Tar)
Requires: perl(Config::INI::MVP::Reader)
Requires: perl(Pod::Eventual)
Requires: perl(namespace::autoclean)
Requires: perl(version) >= 1:0.790.0

Suggests: perl(Dist::Zilla::Plugin::AutoPrereq)
Suggests: perl(Dist::Zilla::Plugin::AutoVersion::Relative)
Suggests: perl(Dist::Zilla::Plugin::CheckChangeLog)
Suggests: perl(Dist::Zilla::Plugin::CompileTests)
Suggests: perl(Dist::Zilla::Plugin::CopyTo)
Suggests: perl(Dist::Zilla::Plugin::CriticTests)
Suggests: perl(Dist::Zilla::Plugin::Git)
Suggests: perl(Dist::Zilla::Plugin::MakeMaker::SkipInstall)
Suggests: perl(Dist::Zilla::Plugin::MatchManifest)
Suggests: perl(Dist::Zilla::Plugin::MetaNoIndex)
Suggests: perl(Dist::Zilla::Plugin::MetaProvides)
Suggests: perl(Dist::Zilla::Plugin::MetaRecommends)
Suggests: perl(Dist::Zilla::Plugin::ModuleInstall)
Suggests: perl(Dist::Zilla::Plugin::PodPurler)
Suggests: perl(Dist::Zilla::Plugin::PodWeaver)
Suggests: perl(Dist::Zilla::Plugin::PerlTidy)
Suggests: perl(Dist::Zilla::Plugin::PodLoom)
Suggests: perl(Dist::Zilla::Plugin::Prepender)
Suggests: perl(Dist::Zilla::Plugin::ReadmeFromPod)
Suggests: perl(Dist::Zilla::Plugin::Repository)
Suggests: perl(Dist::Zilla::Plugin::Signature)
Suggests: perl(Dist::Zilla::Plugin::TemplateCJM)
Suggests: perl(Dist::Zilla::Plugin::VersionFromModule)
Suggests: perl(Dist::Zilla::PluginBundle::CJM)
Suggests: perl(Dist::Zilla::PluginBundle::FAYLAND)
Suggests: perl(Dist::Zilla::PluginBundle::JQUELIN)
Suggests: perl(Dist::Zilla::PluginBundle::RJBS)


%description
Dist::Zilla builds distributions of code to be uploaded to the CPAN. In
this respect, it is like the ExtUtils::MakeMaker manpage, the Module::Build
manpage, or the Module::Install manpage. Unlike those tools, however, it is
not also a system for installing code that has been downloaded from the
CPAN. Since it's only run by authors, and is meant to be run on a
repository checkout rather than on published, released code, it can do much
more than those tools, and is free to make much more ludicrous demands in
terms of prerequisites.

For more information, see the Dist::Zilla::Tutorial manpage.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std
install -d %{buildroot}/etc/bash_completion.d/
install -m 644 misc/dzil-bash_completion %{buildroot}/etc/bash_completion.d/dzil

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README META.yml META.json
%{_mandir}/man3/*
%perl_vendorlib/*
/usr/bin/dzil
/etc/bash_completion.d/dzil
