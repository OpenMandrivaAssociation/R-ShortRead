%global packname  ShortRead
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.12.4
Release:          1
Summary:          Classes and methods for high-throughput short-read sequencing data
Group:            Sciences/Mathematics
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
Requires:         R-methods R-IRanges R-GenomicRanges R-Biostrings R-lattice R-Rsamtools R-latticeExtra 
Requires:         R-IRanges R-GenomicRanges R-Biostrings R-Biobase R-hwriter R-Rsamtools R-zlibbioc R-lattice 
Requires:         R-biomaRt R-RUnit R-GenomicFeatures R-yeastNagalakshmi 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-methods R-IRanges R-GenomicRanges R-Biostrings R-lattice R-Rsamtools R-latticeExtra
BuildRequires:    R-IRanges R-GenomicRanges R-Biostrings R-Biobase R-hwriter R-Rsamtools R-zlibbioc R-lattice 
BuildRequires:    R-biomaRt R-RUnit R-GenomicFeatures R-yeastNagalakshmi 

%description
Base classes, functions, and methods for representation of
high-throughput, short-read sequencing data.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/script
%{rlibdir}/%{packname}/template
%{rlibdir}/%{packname}/unitTests
