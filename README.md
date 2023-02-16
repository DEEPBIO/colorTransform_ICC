# colorTransform_ICC
how to simply apply ICC color profile transform on slides

방법은 간단합니다
slide 가 저장된 path = wsipath

getColorTransform(wsipath) 를 이용해 transform 정보를 받고
이를 applyTransform 함수를 통해 patch-wise 하게 적용하면 됩니다
