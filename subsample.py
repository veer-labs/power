#!/usr/bin/python 

# subsamples a target image a given pixel size and number of times
# runs our blob detection algorithm to count hits per fov in each subimage
# returns a distribution of hits per fov and average hits per fov
# this information is output to R for further information processing

import sys,os,cv,random
ucsf = r"/home/egbutter/ghoulish/malariaRADAR/malaria_images/2010-12-21/ucsf-pics/"
bf = cv.LoadImageM(ucsf+r"BF_10x_1.tif")
xp = cv.LoadImageM(ucsf+r"Polarized_10x_1.tif")

# hackish bootstrap: resampling from image (assume independent subsamples > this is 
# scientifically arguable!) to estimate hemozoin distribution
ssr = 60  # lets take subsample rows of len ssr px
ssc = 60 # subsample cols of len ssc px
subro = round(random.uniform(1,bf.rows-ssr))
subco = round(random.uniform(1,bf.cols-ssc))
sub = cv.GetSubRect(img, (60, 70, ssr, ssc))  # sub is ssrxssc px patch within imgi

cv.SetZero(sub)                             # clear sub to zero, which also clears 32x32 pixels in img
