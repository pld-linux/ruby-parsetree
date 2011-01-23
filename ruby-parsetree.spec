# Todo: degemify
Summary:	Access to Ruby's internal parse tree
Summary(pl.UTF-8):	Dostęp do wewnętrznego drzewa analizy interpretera Ruby
Name:		ruby-parsetree
Version:	2.0.2
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	http://gems.rubyforge.org/gems/ParseTree-%{version}.gem
# Source0-md5:	137bb2b6275d29f37964d0acd32ccfaa
URL:		http://parsetree.rubyforge.org
BuildRequires:	rake
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	setup.rb >= 3.3.1
Requires:	ruby-inline
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ParseTree is a C extension (using RubyInline) that extracts the parse
tree for an entire class or a specific method and returns it as a
s-expression (aka sexp) using Ruby's arrays, strings, symbols, and
integers.

%description -l pl.UTF-8
ParseTree to rozszerzenie C (używające RubyInline) wydobywające drzewo
analizy dla całej klasy lub określonej metody i zwracające je jako
s-wyrażenie (sexp) przy użyciu tablic, łańcuchów, symboli i liczb
całkowitych języka Ruby.

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
rm ri/Module/cdesc-Module.yaml
rm ri/Class/cdesc-Class.yaml

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
%attr(755,root,root) %{_bindir}/*
%{ruby_rubylibdir}/*.rb
%{ruby_ridir}/*
