#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-robCompositions
Version  : 2.3.0
Release  : 46
URL      : https://cran.r-project.org/src/contrib/robCompositions_2.3.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/robCompositions_2.3.0.tar.gz
Summary  : Compositional Data Analysis
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-robCompositions-lib = %{version}-%{release}
Requires: R-GGally
Requires: R-Rcpp
Requires: R-RcppEigen
Requires: R-VIM
Requires: R-car
Requires: R-cvTools
Requires: R-data.table
Requires: R-e1071
Requires: R-fda
Requires: R-fpc
Requires: R-ggplot2
Requires: R-kernlab
Requires: R-mclust
Requires: R-pls
Requires: R-reshape2
Requires: R-robustbase
Requires: R-rrcov
Requires: R-sROC
Requires: R-tidyr
Requires: R-zCompositions
BuildRequires : R-GGally
BuildRequires : R-Rcpp
BuildRequires : R-RcppEigen
BuildRequires : R-VIM
BuildRequires : R-car
BuildRequires : R-cvTools
BuildRequires : R-data.table
BuildRequires : R-e1071
BuildRequires : R-fda
BuildRequires : R-fpc
BuildRequires : R-ggplot2
BuildRequires : R-kernlab
BuildRequires : R-mclust
BuildRequires : R-pls
BuildRequires : R-reshape2
BuildRequires : R-robustbase
BuildRequires : R-rrcov
BuildRequires : R-sROC
BuildRequires : R-tidyr
BuildRequires : R-zCompositions
BuildRequires : buildreq-R

%description
{robCompositions}
=======================================
Robust Methods for Compositional Data

%package lib
Summary: lib components for the R-robCompositions package.
Group: Libraries

%description lib
lib components for the R-robCompositions package.


%prep
%setup -q -c -n robCompositions
cd %{_builddir}/robCompositions

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1605802458

%install
export SOURCE_DATE_EPOCH=1605802458
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library robCompositions
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library robCompositions
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library robCompositions
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc robCompositions || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/robCompositions/CITATION
/usr/lib64/R/library/robCompositions/DESCRIPTION
/usr/lib64/R/library/robCompositions/INDEX
/usr/lib64/R/library/robCompositions/Meta/Rd.rds
/usr/lib64/R/library/robCompositions/Meta/data.rds
/usr/lib64/R/library/robCompositions/Meta/features.rds
/usr/lib64/R/library/robCompositions/Meta/hsearch.rds
/usr/lib64/R/library/robCompositions/Meta/links.rds
/usr/lib64/R/library/robCompositions/Meta/nsInfo.rds
/usr/lib64/R/library/robCompositions/Meta/package.rds
/usr/lib64/R/library/robCompositions/Meta/vignette.rds
/usr/lib64/R/library/robCompositions/NAMESPACE
/usr/lib64/R/library/robCompositions/NEWS
/usr/lib64/R/library/robCompositions/R/robCompositions
/usr/lib64/R/library/robCompositions/R/robCompositions.rdb
/usr/lib64/R/library/robCompositions/R/robCompositions.rdx
/usr/lib64/R/library/robCompositions/data/Rdata.rdb
/usr/lib64/R/library/robCompositions/data/Rdata.rds
/usr/lib64/R/library/robCompositions/data/Rdata.rdx
/usr/lib64/R/library/robCompositions/doc/imputation.R
/usr/lib64/R/library/robCompositions/doc/imputation.Rnw
/usr/lib64/R/library/robCompositions/doc/imputation.pdf
/usr/lib64/R/library/robCompositions/doc/index.html
/usr/lib64/R/library/robCompositions/doc/robCompositions-overview.Rnw
/usr/lib64/R/library/robCompositions/doc/robCompositions-overview.pdf
/usr/lib64/R/library/robCompositions/help/AnIndex
/usr/lib64/R/library/robCompositions/help/aliases.rds
/usr/lib64/R/library/robCompositions/help/paths.rds
/usr/lib64/R/library/robCompositions/help/robCompositions.rdb
/usr/lib64/R/library/robCompositions/help/robCompositions.rdx
/usr/lib64/R/library/robCompositions/html/00Index.html
/usr/lib64/R/library/robCompositions/html/R.css
/usr/lib64/R/library/robCompositions/tests/testthat.R
/usr/lib64/R/library/robCompositions/tests/testthat/imp_test.R
/usr/lib64/R/library/robCompositions/tests/testthat/importFood.R
/usr/lib64/R/library/robCompositions/tests/testthat/rz.R
/usr/lib64/R/library/robCompositions/tests/testthat/test_iris.r

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/robCompositions/libs/robCompositions.so
