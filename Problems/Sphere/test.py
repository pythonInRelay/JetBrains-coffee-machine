i = cv2.imread('aaa.png')
    im_gray = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)

    template = cv2.imread('Official_assets/binance.png')
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    if im_gray.shape != template_gray.shape:
        # w = 138
        # h = 135
        wi, hi = template_gray.shape
        dim = (wi, hi)
        resize = cv2.resize(im_gray, dim, interpolation = cv2.INTER_AREA)
    res = cv2.matchTemplate(resize, template_gray, cv2.TM_CCOEFF_NORMED)