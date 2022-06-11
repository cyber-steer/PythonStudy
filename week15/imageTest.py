import cv2

image= cv2.imread('tmp.png')
#make mask of where the transparent bits are
transp_mask= image[:,:,:3]== 0
transp_mask= image[:,:,:3]== 1 # swap
#replace areas of transparency with white and not transparent
image[transp_mask]= [100]
#new image without alpha channel...
new_img= cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
cv2.imwrite('testingnew.jpg',new_img)
print(new_img.shape)