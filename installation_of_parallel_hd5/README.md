Download tar file of hd5 from :

    https://www.hdfgroup.org/downloads/hdf5/source-code/

Install this tar file for c++ by command :

    ./configure --enable-parallel --enable-shared --prefix=/path/to/install/directory

    make

    make check

    make install



After this install h5py with mpi for python 

    CC="mpicc" HDF5_MPI="ON" HDF5_DIR=path_to_h5_parallel_for_c++ pip install --no-binary=h5py h5py
