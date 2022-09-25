import numpy as np
from mpi4py import MPI

# import hd5py_parallel as hp
import h5py as hp

communicator = MPI.COMM_WORLD
rank = communicator.Get_rank()
procs = communicator.Get_size()


Nx = Ny = Nz = 4
Nx_d = Ny_d = Nx//procs

fName = "Soln_.hdf5"
# creates the file
f = hp.File(fName, 'w',driver='mpio',comm=communicator) 
dShape = [Nx, Ny, Nz]

if(rank == 1):
    Vx = np.ones([Nx_d,Ny,Nz])
    Vy = np.ones([Nx_d,Ny,Nz])
    Vz = np.ones([Nx_d,Ny,Nz])

if(rank == 0):
    Vx = np.zeros([Nx_d,Ny,Nz])
    Vy = np.zeros([Nx_d,Ny,Nz])
    Vz = np.zeros([Nx_d,Ny,Nz])

if(rank == 2):
    Vx = np.zeros([Nx_d,Ny,Nz]) +2
    Vy = np.zeros([Nx_d,Ny,Nz])+2
    Vz = np.zeros([Nx_d,Ny,Nz])+2

if(rank == 3):
    Vx = np.zeros([Nx_d,Ny,Nz])+3
    Vy = np.zeros([Nx_d,Ny,Nz])+3
    Vz = np.zeros([Nx_d,Ny,Nz])+3
    
uDset= f.create_dataset("Vx", dShape, dtype = 'f')
vDset = f.create_dataset("Vy", dShape, dtype = 'f')
wDset = f.create_dataset("Vz", dShape, dtype = 'f')
# tDset = f.create_dataset("T", dShape, dtype = 'f')
# pDset = f.create_dataset("P", dShape, dtype = 'f')

uDset[(rank*Nx_d):((rank+1)*Nx_d),:,:] = Vx[:,:,:]
vDset[(rank*Nx_d):((rank+1)*Nx_d),:,:] = Vy[:,:,:]    
wDset[(rank*Nx_d):((rank+1)*Nx_d),:,:] = Vz[:,:,:]
f.close()

fr = hp.File(fName, 'r',driver='mpio',comm=communicator)
# a = np.array(fr["Vx"])[:,:,:]
a = np.array(fr["Vx"])[(rank*Nx_d):((rank+1)*Nx_d),:,:]

if(rank == 0):
    print(a)

fr.close()


# print(list(f.keys()))