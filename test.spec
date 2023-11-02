Name:           test
Version:        0.1.0
Release:        1%{?dist}
Summary:        test

License:        test
URL:            github.com
Source0:        test.tar


#禁止打包debug
%define debug_package %{nil}

#禁止生成build-id
%define _build_id_links none
%undefine _missing_build_ids_terminate_build




BuildRequires:  make
Requires:       make





%description

    test rpm build procedure

%prep
    echo prep
    pwd


# %autosetup
%setup -c
# %setup -q



    echo setup
    pwd
    ls -al


%build

    echo build
    pwd

    
    ls -al

    



    cp test-0.1.0/* ./
    rm -rf test-0.1.0
    ls -al
    bash hello.sh

    # rm -rf %{buildroot}


    make 


    echo %{buildroot}


%configure

    echo configure
    pwd


# %make_build

#    echo make_build
#     pwd


%install
    # rm -rf $RPM_BUILD_ROOT

    echo install
    pwd

    ls -al 



    DEST_DIR=%{buildroot}/usr/local/test
    mkdir -p $DEST_DIR


    # cp pre_install.sh $DEST_DIR
    cp post_install.sh $DEST_DIR
    cp pre_uninstall.sh $DEST_DIR
    # cp post_uninstall.sh $DEST_DIR


    echo %{buildroot}

    ls -al %{buildroot}


    



# %make_install



#包安装前执行
%pre

    echo pre install
    pwd
    ls -al


#包安装后执行
%post

    echo post install
    pwd
    ls -al

    /usr/local/test/post_install.sh

#包卸载前执行
%preun
    
    echo pre uninstall
    pwd
    ls -al

    /usr/local/test/pre_uninstall.sh

#包卸载后执行
%postun

    echo post uninstall
    pwd
    ls -al

    




%files

    # /usr/local/test/pre_install.sh
    /usr/local/test/post_install.sh
    /usr/local/test/pre_uninstall.sh
    # /usr/local/test/post_uninstall.sh









# %license add-license-file-here
# %doc add-docs-here



%changelog
* Wed Nov  1 2023 zhangqy <zhangqy@yusur.tech>
- 
