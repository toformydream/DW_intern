for i in range(85,343):

    seg_number=i/3
    if i<3:
        seg_number=0


    #original_img = cv2.imread('venv/crop_art_knife_2/'+ str(j) + '.png')

    img = cv2.imread('venv/crop_art_knife_2/' + str(i) + '.png')
    q,e,r = original_img.shape
    h, w, c = img.shape
    new_h = q/h
    new_w = e/w
    boundbox = [0, 0, w, h]
    json_new_annotation = []
    area=h*w
    og_segmentation_x = augm_json_train['annotations'][j]['segmentation'][0][0][0::2]
    og_segmentation_y = augm_json_train['annotations'][j]['segmentation'][0][0][1::2]
    print(og_segmentation_x)
    print(og_segmentation_y)
    opop=np.multiply(og_segmentation_x,new_h) #new segmentation X
    jpjp= np.multiply(og_segmentation_y,new_w) #new segmentation Y
    for way in range(0:17):
        if way%2==0:
            continue
        else:
            opop.insert(way,jpjp[way/2])
    j = j + 1