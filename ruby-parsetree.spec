Summary:	Access to Ruby's internal parse tree
Name:		ruby-parsetree
Version:	1.7.1
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/21469/ParseTree-%{version}.gem
# Source0-md5:	b516a478ac1fe6ae35d0c23eaca24c3e
URL:		http://parsetree.rubyforge.org
BuildRequires:	rake
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	setup.rb = 3.3.1
Requires:	ruby-inline
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ParseTree is a C extension (using RubyInline) that extracts the parse
tree for an entire class or a specific method and returns it as a
s-expression (aka sexp) using ruby's arrays, strings, symbols, and
integers.

%prep
%setup -q -c
tar xf %{SOURCE0} -O data.tar.gz | tar xzv-
cp %{_datadir}/setup.rb .

%build
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc --op rdoc lib
rdoc --ri --op ri lib
rm ri/created.rid

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc
%attr(755,root,root) /usr/bin/*
%{ruby_rubylibdir}/*.rb
%{ruby_ridir}/*
