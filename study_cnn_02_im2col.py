import numpy as np

def im2col(input_data, filter_h, filter_w, stride=1, pad=0):
    N, C, H, W = input_data.shape
    print("N:",N)
    print("C:", C)
    print("H:", H)
    print("W:", W)

    out_h = (H + 2 * pad-filter_h) // stride + 1
    out_w = (W + 2 * pad-filter_w) // stride + 1
    print("out (HxW) : (",out_h,"x",out_w,")")

    img=np.pad(input_data, [(0,0),(0,0),(pad,pad),(pad,pad)],'constant')
    # (0,0) : 1st, padding around N
    # (0,0) : 2nd, padding around Channel
    # (pad,pad) ; 3rd, padding around H, (upper pad cnt, lower pad cnt)
    # (pad,pad) : 4th, padding arounf W, (left pad cnt, right pad cnt)
    print("pad img:", img)

    col = np.zeros((N, C, filter_h, filter_w, out_h, out_w))
    print("col.shape:",col.shape)

    for y in range(filter_h):
        y_max = y+stride*out_h
        for x in range(filter_w):
            x_max = x + stride * out_w
            col[:,:,y,x,:,:]=img[:,:,y:y_max:stride,x:x_max:stride]
            print("col:",col)

    col = col.transpose(0,4,5,1,2,3).reshape(N*out_h,out_w,-1)
    return col



d = np.array(range(16)).reshape(1,1,4,4)
f = np.array(range(4)).reshape(2,2)

print(d)
print("result:",im2col(d,3,3))

