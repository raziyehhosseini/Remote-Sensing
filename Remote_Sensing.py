From google.colab import drive
Drive.mount(“/content/Drive”)
#***********************************
Pip install rasterio 
Import rasterio as rio
From osgeo import gdal
Import numpy
Import matplotlib.pyplot as plt
#***********************************
Dataset = rio.open(“/content/Drive/MyDrive/Satellite Imagey/sis_sentinel.tif”)
arrayImg = dataset.read()

arrayImg.shape # output: (number of bands, Number of rows, Number of columns)

Bands = arrayImg[0]
nRows = arrayImg[1]
nCols = arrayImg[2]
Plt. Figure(fixsize = (10,10))
Plt.imshow(arrayImg[8, :,  :], cmap = “gray”)
Plt.show()
#************************************
Plt.figure(figsize = (10,7))
Plt. Grid(axis = “y” ,  alpha=0.75)
Plt.xlabel(“value”)
Plt.ylabel(“Frequency”)
Plt.title(“sentinel 2 Imagery”)
N, bins, patches = plt.hist(x=arrayImg.flatten(), bins=100 , color=”#0504aa” , alpha=0.7 , rwidth=0.85)
Plt.plot(arrayImg[:,200,400])
minValue= np.min(arrayImg)
maxValue= np.max(arrayImg)

normalizedImg = (arrayImg-minValue)/(maxValue-minValue)*255
normalizedImg = normalizedImg.astype(np.uint8)

minValue1= np.min(normalizedImg)
maxValue1= np.max(normalizedImg)
rgbImg = np.zeros((nrows, nCols, 3) , dtype=np.uint8)

rgbImg[:,:,0] = normalizedImg[8,:,:]
rgbImg[:,:,1] = normalizedImg[4,:,:]
rgbImg[:,:,1] = normalizedImg[3,:,:]

Plt.figure(figsize=(10,10))
Plt.imshow(rgbImg)
Plt.title(“sentinel_2 RGB Imagery”)
Plt.axis(“off”)
Plt.show()