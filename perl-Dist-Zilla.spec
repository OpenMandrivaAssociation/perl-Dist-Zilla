%define upstream_name    Dist-Zilla
%define upstream_version 4.300029
Name:		perl-%{upstream_name}
Version:	%perl_convert_version 4.300029
Release:	3

Summary:	Something that provides a version number for the dist
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/R/RJ/RJBS/Dist-Zilla-4.300029.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(App::Cmd)
BuildRequires:	perl(Archive::Tar)
BuildRequires:	perl(CPAN::Meta::Converter)
BuildRequires:	perl(CPAN::Meta::Prereqs)
BuildRequires:	perl(CPAN::Meta::Validator)
BuildRequires:	perl(CPAN::Uploader)
BuildRequires:	perl(Config::MVP::Reader::INI) >= 2.0.0
BuildRequires:	perl(Data::Section)
BuildRequires:	perl(DateTime)
BuildRequires:	perl-ExtUtils-Manifest
BuildRequires:	perl(File::Copy::Recursive)
BuildRequires:	perl(File::Find::Rule)
BuildRequires:	perl(File::HomeDir)
BuildRequires:	perl(File::ShareDir)
BuildRequires:	perl(File::ShareDir::Install)
BuildRequires:	perl(File::chdir)
BuildRequires:	perl(File::pushd)
BuildRequires:	perl(Hash::Merge::Simple)
BuildRequires:	perl(IO::TieCombine)
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(Log::Dispatchouli)
BuildRequires:	perl(Mixin::ExtraFields::Param)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Moose::Autobox)
BuildRequires:	perl(MooseX::LazyRequire)
BuildRequires:	perl(MooseX::Role::Parameterized)
BuildRequires:	perl(MooseX::SetOnce)
BuildRequires:	perl(MooseX::Singleton)
BuildRequires:	perl(MooseX::Types::Path::Class)
BuildRequires:	perl(MooseX::Types::Perl)
BuildRequires:	perl(PPI)
BuildRequires:	perl(Path::Class)
BuildRequires:	perl(Perl::PrereqScanner)
BuildRequires:	perl(Perl::Version)
BuildRequires:	perl(Pod::Eventual)
BuildRequires:	perl(Software::License)
BuildRequires:	perl(String::Flogger)
BuildRequires:	perl(String::Format)
BuildRequires:	perl(String::Formatter)
BuildRequires:	perl(String::RewritePrefix)
BuildRequires:	perl(Term::ReadKey)
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Text::Template)
BuildRequires:	perl(Version::Requirements)
BuildRequires:	perl(YAML::Tiny)
BuildRequires:	perl(autobox)
BuildRequires:	perl(namespace::autoclean)
BuildRequires:	perl(version) >= 1:0.790.0

BuildArch:	noarch
Requires:	perl(aliased)
Requires:	perl(namespace::autoclean)
Requires:	perl(version)
Suggests:	perl(Task::Dist::Zilla)


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
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std
install -d %{buildroot}%{_sysconfdir}/bash_completion.d/
install -m 644 misc/dzil-bash_completion %{buildroot}/etc/bash_completion.d/dzil

%files
%doc Changes LICENSE README META.yml
%{_mandir}/man1/*
%{_mandir}/man3/*
%{perl_vendorlib}/*
%{_bindir}/dzil
%{_sysconfdir}/bash_completion.d/dzil


