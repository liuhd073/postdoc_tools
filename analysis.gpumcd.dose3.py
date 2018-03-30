#!/usr/bin/env python3
import plot,os,image,numpy as np,random

#rundir = os.path.join(r"Z:\brent\dosia_dump",'8903804','20Gy.trialname.1.beam')
rundir = r"Z:\brent\dosia_validatiedump\F180220C\6MV_COM.trialname.1.beam"
#rundir = r"Z:\brent\dosia_validatiedump\AA171214\Epid_6MV_COM.trialname.1.beam"

images = [image.image(os.path.join(rundir,'dose.mhd')),
image.image(os.path.join(rundir,'gpumcd_dose_water.mhd')), #dose to water, propagate water
image.image(os.path.join(rundir,'gpumcd_dose_inaqua.mhd')), #dose to water, propagate medium
image.image(os.path.join(rundir,'gpumcd_dose.mhd'))
]

names = ['TPS',
       'GPUMCD_water_water',
       'GPUMCD_in_aqua',
       'GPUMCD_medium_medium'
       ]

xsize1 = np.linspace( 0, int( images[0].header['ElementSpacing'][0]*images[0].header['DimSize'][0] ), images[0].header['DimSize'][0] )
xsize2 = np.linspace( 0, int( images[2].header['ElementSpacing'][2]*images[2].header['DimSize'][2] ), images[2].header['DimSize'][2] )

f, (row1,row2,row3,row4) = plot.subplots(nrows=4, ncols=3, sharex=False, sharey=False)

for im,leg in zip( [images[0],images[3]], [names[0],names[3]] ):
    col=random.choice(plot.colors*3)
    row1[0].plot(xsize1,im.getline('y'),alpha=0.5,color=col,label=leg)
    row1[1].plot(xsize1,im.getline('z'),alpha=0.5,color=col,label=leg)
    row1[2].plot(xsize2,im.getline('x'),alpha=0.5,color=col,label=leg)
for im,leg in zip( [images[0],images[2]], [names[0],names[2]] ):
    col=random.choice(plot.colors)
    row2[0].plot(xsize1,im.getline('y'),alpha=0.5,color=col,label=leg)
    row2[1].plot(xsize1,im.getline('z'),alpha=0.5,color=col,label=leg)
    row2[2].plot(xsize2,im.getline('x'),alpha=0.5,color=col,label=leg)
for im,leg in zip( [images[0],images[1]], [names[0],names[1]] ):
    col=random.choice(plot.colors)
    row3[0].plot(xsize1,im.getline('y'),alpha=0.5,color=col,label=leg)
    row3[1].plot(xsize1,im.getline('z'),alpha=0.5,color=col,label=leg)
    row3[2].plot(xsize2,im.getline('x'),alpha=0.5,color=col,label=leg)
for im,leg in zip( images[1:], names[1:] ):
    col=random.choice(plot.colors)
    row4[0].plot(xsize1,im.getline('y'),alpha=0.5,color=col,label=leg)
    row4[1].plot(xsize1,im.getline('z'),alpha=0.5,color=col,label=leg)
    row4[2].plot(xsize2,im.getline('x'),alpha=0.5,color=col,label=leg)

row1[0].set_title('PDD')
row1[1].set_title('Profile')
row4[0].set_xlabel('Axis [mm]')
row4[1].set_xlabel('Axis [mm]')
for row in (row1,row2,row3,row4):
    row[0].set_ylabel('Dose [cGy]')
    row[1].set_ylabel('Dose [cGy]')
    row[0].set_xlabel('Axis [mm]')
    row[1].set_xlabel('Axis [mm]')
    row[1].legend(loc='upper right', bbox_to_anchor=(1.2, 1.),frameon=False)

f.savefig(os.path.join(rundir,'dose_prof_pdd.pdf'), bbox_inches='tight')
f.savefig(os.path.join(rundir,'dose_prof_pdd.png'), bbox_inches='tight',dpi=300)

plot.close('all')
